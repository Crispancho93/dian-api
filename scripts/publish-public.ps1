<#
.SYNOPSIS
    Publica el código actual en el repo público (dian-api), sin k8s/ ni .env.

.DESCRIPTION
    Un remote no filtra contenido: recibe lo que le pushees. Para que "public"
    reciba menos archivos que "origin", este script mantiene una rama local
    "public-main" cuyo contenido es siempre "todo lo de tu rama actual, menos
    k8s/ y .env", y la pushea a public/main.

    Es seguro correrlo varias veces: si no hay cambios que publicar, no crea
    commits vacíos. La primera vez crea "public-main" como rama huérfana (sin
    el historial de origin, que sí tiene .env y k8s/ en commits viejos).

.USAGE
    .\scripts\publish-public.ps1
#>

# OJO con "2>&1" o "2>$null" sobre comandos externos como git: en Windows
# PowerShell, redirigir el stderr de un ejecutable nativo lo envuelve en un
# NativeCommandError y pone $? en $false aunque el comando haya salido con
# código 0 (git usa stderr para mensajes informativos, no solo errores). Por
# eso acá nunca se toca el stream de error: se deja que git imprima lo suyo, y
# el chequeo real de fallos es siempre por $LASTEXITCODE.
$ErrorActionPreference = "Stop"

function Assert-LastExitCode([string]$step) {
    if ($LASTEXITCODE -ne 0) {
        throw "Fallo en: $step (exit code $LASTEXITCODE)"
    }
}

# Rutas que NUNCA deben llegar al repo público.
$ExcludedPaths = @("k8s", ".env")

$repoRoot = git rev-parse --show-toplevel
if (-not $repoRoot) {
    Write-Error "No estás dentro de un repositorio git."
    exit 1
}
Set-Location $repoRoot

if (-not (git remote | Select-String -SimpleMatch "public")) {
    Write-Error "No existe el remote 'public'. Agregalo con:`n  git remote add public https://github.com/Crispancho93/dian-api.git"
    exit 1
}

$sourceBranch = git branch --show-current
if (-not $sourceBranch) {
    Write-Error "No se pudo determinar la rama actual (¿HEAD detached?)."
    exit 1
}
if ($sourceBranch -eq "public-main") {
    Write-Error "Estás parado en 'public-main'. Cambiá a tu rama de trabajo antes de publicar."
    exit 1
}
if (git status --porcelain) {
    Write-Error "Hay cambios sin commitear en '$sourceBranch'. Commiteá o hacé stash antes de publicar."
    exit 1
}

Write-Host "Rama de origen : $sourceBranch" -ForegroundColor Cyan
Write-Host "Remote publico  : public -> $(git remote get-url public)" -ForegroundColor Cyan

$publicBranchExists = [bool](git branch --list "public-main")

try {
    if ($publicBranchExists) {
        Write-Host "`nActualizando la rama 'public-main'..." -ForegroundColor Yellow
        git checkout public-main | Out-Null
        Assert-LastExitCode "git checkout public-main"
    } else {
        Write-Host "`nPrimera vez: creando la rama 'public-main' (sin historial de origin)..." -ForegroundColor Yellow
        git checkout --orphan public-main | Out-Null
        Assert-LastExitCode "git checkout --orphan public-main"
    }

    # Se vacía el índice y se reconstruye completo desde la rama de origen, así
    # los archivos borrados en origin también desaparecen del lado público
    # (no solo se pisan los que cambiaron). --ignore-unmatch: en la primera
    # corrida (rama huérfana) el índice ya está vacío y no hay nada que sacar;
    # eso no es un error.
    git rm -r --cached --ignore-unmatch . | Out-Null
    Assert-LastExitCode "git rm -r --cached ."

    git checkout $sourceBranch -- . | Out-Null
    Assert-LastExitCode "git checkout $sourceBranch -- ."

    foreach ($path in $ExcludedPaths) {
        git rm -r --cached --ignore-unmatch -- $path | Out-Null
        Assert-LastExitCode "git rm -r --cached -- $path"
        if (Test-Path $path) {
            Remove-Item -Recurse -Force $path
        }
    }

    # .gitignore propio del repo público: se reescribe siempre, para no
    # depender de si el .gitignore de origin cambia con el tiempo.
    $publicGitignore = @("venv/", "__pycache__", "") + $ExcludedPaths
    Set-Content -Path .gitignore -Value $publicGitignore -Encoding utf8

    git add -A
    Assert-LastExitCode "git add -A"

    # git diff, NO git status, para chequear si hay algo staged: funciona por
    # exit code (0 = sin cambios, 1 = hay cambios) incluso sin ningún commit
    # previo en la rama (git status --porcelain --cached ni siquiera es una
    # combinación válida de flags).
    git diff --cached --quiet
    $hasChanges = ($LASTEXITCODE -ne 0)

    if (-not $hasChanges) {
        Write-Host "`nNo hay cambios para publicar: 'public-main' ya está al día." -ForegroundColor Green
    } else {
        $message = if ($publicBranchExists) {
            "sync $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
        } else {
            "Initial public release"
        }
        git commit -m $message | Out-Null
        Assert-LastExitCode "git commit"

        git push public public-main:main
        Assert-LastExitCode "git push public public-main:main"

        Write-Host "`nPublicado en dian-api (rama main)." -ForegroundColor Green
    }
} finally {
    git checkout $sourceBranch | Out-Null
    $backOk = ($LASTEXITCODE -eq 0) -and ((git branch --show-current) -eq $sourceBranch)

    if ($backOk) {
        Write-Host "De vuelta en '$sourceBranch'." -ForegroundColor Cyan

        # La propia rama de trabajo puede tener commiteada una versión vieja
        # de este script (de antes de un fix). Si "public-main" tiene una
        # versión más nueva, se trae para que no se pierda en el próximo
        # checkout. No se commitea sola: te avisa para que lo revises vos.
        $scriptPath = "scripts/publish-public.ps1"
        if ((git diff --name-only public-main -- $scriptPath)) {
            Write-Host "`nAVISO: '$scriptPath' en '$sourceBranch' difiere del que quedó en 'public-main'." -ForegroundColor Yellow
            Write-Host "Si esta rama tiene la versión vieja, traé la nueva con:" -ForegroundColor Yellow
            Write-Host "  git checkout public-main -- $scriptPath" -ForegroundColor Yellow
            Write-Host "  git add $scriptPath" -ForegroundColor Yellow
            Write-Host "  git commit -m `"fix: $scriptPath`"" -ForegroundColor Yellow
        }
    } else {
        Write-Warning "No se pudo volver automáticamente a '$sourceBranch'. Estás en: $(git branch --show-current)`nRevisá 'git status' antes de seguir trabajando."
    }
}

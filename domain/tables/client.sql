CREATE TABLE client (
    id SERIAL PRIMARY KEY,
    nit VARCHAR(50) NOT NULL,
    digito VARCHAR(2) NOT NULL,
    resolucion VARCHAR(50) NOT NULL,
    full_name VARCHAR(500) NOT NULL,
    pfx_password VARCHAR(500) NOT NULL,
    pfx_path VARCHAR(500) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_client_nit ON client (nit);
CREATE UNIQUE INDEX idx_client_resolucion ON client (resolucion);
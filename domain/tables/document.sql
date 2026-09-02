CREATE TABLE document (
    id SERIAL PRIMARY KEY,
    tipo VARCHAR(10) NOT NULL,
    numero VARCHAR(100) NOT NULL,
    cliente_nit VARCHAR(50) NOT NULL,
    resolucion VARCHAR(50),
    identificador VARCHAR(200),
    ambiente VARCHAR(1) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    mensajes TEXT,
    respuesta_dian TEXT,
    zip_path VARCHAR(500),
    zip_key VARCHAR(200),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_document_nit ON document (cliente_nit);
CREATE INDEX idx_document_created ON document (created_at DESC);
CREATE INDEX idx_document_tipo_estado ON document (tipo, estado);

BEGIN;

CREATE UNIQUE INDEX IF NOT EXISTS ux_client_nit
ON client (nit);

ALTER TABLE document
  ADD CONSTRAINT fk_document_cliente
  FOREIGN KEY (cliente_nit)
  REFERENCES client (nit)
  ON UPDATE CASCADE
  ON DELETE RESTRICT;

CREATE INDEX IF NOT EXISTS idx_document_cliente_nit
ON document (cliente_nit);

COMMIT;
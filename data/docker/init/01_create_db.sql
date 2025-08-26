-- Cria schema e configura search_path para o DB inicial (maturidade)
CREATE SCHEMA IF NOT EXISTS bronze AUTHORIZATION postgres;

-- Opcional: garante que quando conectar nesse DB, bronze venha primeiro
ALTER DATABASE maturidade SET search_path TO bronze, public;

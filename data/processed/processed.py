# pip install pandas sqlalchemy psycopg2-binary python-dotenv

import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(__file__)          
env_path = os.path.join(BASE_DIR, ".env")
load_dotenv(env_path)

USER   = os.getenv("POSTGRES_USER")
PWD    = os.getenv("POSTGRES_PASSWORD")
DB     = os.getenv("POSTGRES_DB")
HOST   = os.getenv("POSTGRES_HOST")
PORT   = os.getenv("POSTGRES_PORT")
SCHEMA = os.getenv("POSTGRES_SCHEMA")
TABLE  = os.getenv("POSTGRES_TABLE")

# string de conexão
url = f"postgresql+psycopg2://{USER}:{PWD}@{HOST}:{PORT}/{DB}"
engine = create_engine(url)

# puxar o DataFrame
with engine.begin() as conn:
    df = pd.read_sql(text(f"SELECT * FROM {SCHEMA}.{TABLE}"), conn)

print(df.head())

import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
host = os.getenv("REDSHIFT_HOST")
port = os.getenv("REDSHIFT_PORT")
dbname = os.getenv("REDSHIFT_DB")
user = os.getenv("REDSHIFT_USER")
password = os.getenv("REDSHIFT_PASSWORD")


conn_str = (
    f"redshift+redshift_connector://{user}:{password}@{host}:{port}/{dbname}"
)


engine = create_engine(conn_str)


with engine.connect() as connection:
    query = "SELECT nombre FROM ricardobal_coderhouse.prueba LIMIT 10"  # Ajusta la consulta según tus necesidades
    df = pd.read_sql(query, connection)
    print(df)


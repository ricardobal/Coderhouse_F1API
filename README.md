# Coderhouse_F1API

# Proyecto: Integración de Datos de OpenF1 con Redshift

## Descripción

Este proyecto tiene como objetivo integrar datos de la API pública de OpenF1 (https://api.openf1.org/) y almacenarlos en una base de datos Amazon Redshift. La API de OpenF1 proporciona información sobre sesiones de Fórmula 1, como tiempos de vuelta, velocidades en puntos intermedios, y otros detalles relevantes.

### Funcionalidades

- **Extracción de Datos**: Conexión a la API de OpenF1 para extraer datos de sesiones y vueltas.
- **Transformación de Datos**: Procesamiento y transformación de los datos extraídos para que sean compatibles con la estructura de la base de datos.
- **Carga de Datos**: Inserción de los datos procesados en una tabla en Amazon Redshift.

## Requisitos

- **Python 3.8+**
- **Bibliotecas de Python**:
  - `requests`: Para realizar solicitudes HTTP a la API.
  - `pandas`: Para manipulación y análisis de datos.
  - `sqlalchemy`: Para la conexión a la base de datos.
  - `redshift_connector`: Para conectarse a Amazon Redshift.
  - `python-dotenv`: Para gestionar variables de entorno.

Instala las dependencias usando pip:

```bash
pip install requests pandas sqlalchemy redshift_connector python-dotenv
Configuración
Archivo .env: Crea un archivo llamado .env en el directorio raíz del proyecto para almacenar tus credenciales y parámetros de conexión a Redshift.

env
Copiar código
REDSHIFT_HOST=your-redshift-cluster.us-west-2.redshift.amazonaws.com
REDSHIFT_PORT=5439
REDSHIFT_DB=your_database
REDSHIFT_USER=your_username
REDSHIFT_PASSWORD=your_password
Archivo de Configuración: Asegúrate de que tu archivo de configuración en Python (config.py) o el script principal (main.py) lea estas variables de entorno.

Uso
Extracción de Datos: Ejecuta el script __main__.py para extraer datos de la API de OpenF1.

bash
Copiar código
python __main__.py
Transformación de Datos: Los datos extraídos serán procesados y transformados en un formato adecuado para la base de datos.

Carga de Datos: Ejecuta el script load_data.py para cargar los datos transformados en tu base de datos Amazon Redshift.

bash
Copiar código
python load_data.py
Estructura del Proyecto
bash
Copiar código
project/
│
├── __main__.py           # Script para extraer datos de la API de OpenF1
├── load_data.py          # Script para cargar datos en Amazon Redshift
├── config.py             # Archivo de configuración para la conexión a Redshift
├── .env                  # Archivo con las variables de entorno
├── requirements.txt      # Lista de dependencias del proyecto
└── README.md             # Este archivo
Ejemplo de Código
__main__.py
python
Copiar código
import requests
import pandas as pd
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Parámetros de la API
API_URL = "https://api.openf1.org/v1/laps"
SESSION_KEY = "latest"
LAP_NUMBER = 8

# Solicitar datos a la API
response = requests.get(API_URL, params={"session_key": SESSION_KEY, "lap_number": LAP_NUMBER})
data = response.json()

# Convertir a DataFrame
df = pd.DataFrame(data['laps'])

# Guardar datos en CSV
df.to_csv("laps_data.csv", index=False)
load_data.py
python
Copiar código
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

Contacto
Para preguntas o soporte, contacta a ricardobal@gmail.com.

markdown
Copiar código

### Instrucciones para el uso

1. **Configura las variables de entorno**: Crea un archivo `.env` en la raíz del proyecto con tus credenciales de Redshift.
2. **Instala las dependencias**: Usa `pip` para instalar las bibliotecas necesarias.
3. **Ejecuta los scripts**: Usa los comandos proporcionados para extraer y cargar los datos.

import requests
import pandas as pd

def store_data_from_api(data: pd.DataFrame):
    data.to_parquet('f1laps.parquet')

def get_data_from_api(url: str, session: str):
    data = None
    try:
        params = {
            "session_key": session
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            data = pd.DataFrame(data)
            store_data_from_api(data)
        else:
            print(f"Error: {response.status_code}")
            data = pd.DataFrame()  

        return data
    except Exception as e:
        print({"error": e})
        return pd.DataFrame()  
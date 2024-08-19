import requests
import pandas as pd

def store_data_from_api(data: pd.DataFrame):
    data.to_parquet('f1laps.parquet')


def get_data_from_api():

    try:
        url = "https://api.openf1.org/v1/laps"
        params = {
                    "session_key": 9161,  
                    "lap_number": 8      
                }
        response = requests.get(url, params=params)

        if response.status_code == 200:
                data = response.json()
                data = pd.DataFrame(data)
                store_data_from_api(data)
        else:
            print(f"Error: {response.status_code}")
        
        return data
    except Exception  as e:
        print({"error":e})
       

data = get_data_from_api()
print(data)
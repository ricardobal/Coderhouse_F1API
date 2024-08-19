from modules.api import get_data_from_api
from modules.sqldata import grabar_archivo



def main():
    ## Obtengo la ultima session
    url = "https://api.openf1.org/v1/sessions"
    data = get_data_from_api(url, 'latest')
    last_session = data["session_key"]
    print(last_session)

    ## Descargo los tiempos de la ultima session
    url = "https://api.openf1.org/v1/laps"
    data = get_data_from_api(url, last_session)
    print(data)

    ## Defino las variables de DB
    file_path = 'f1laps.parquet'
    table_name = 'laps'

    ## grabo 
    grabar_archivo(file_path, table_name)




if __name__ == "__main__":
    main()

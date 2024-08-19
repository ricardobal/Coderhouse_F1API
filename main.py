from modules.api import get_data_from_api



def main():
    ## Obtengo la ultima session
    url = "https://api.openf1.org/v1/sessions"
    data = get_data_from_api(url, 'latest')
    last_session = data["session_key"]
    ## print(last_session)


    url = "https://api.openf1.org/v1/laps"
    data = get_data_from_api(url, last_session)
    print(data)


if __name__ == "__main__":
    main()
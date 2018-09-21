import requests


def main():
    print(getData())


def getData():
    API_KEY = "117144.6TRIzMhji4Kxw"
    NAME = "CW5773"

    PARAMS = {"name": NAME, "apikey": API_KEY, "what": "loc", "format": "json"}
    URL = "https://api.aprs.fi/api/get"

    response = requests.get(URL, params=PARAMS)

    return response.content


if __name__ == '__main__':
    main()

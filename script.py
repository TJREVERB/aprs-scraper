import requests


def main():
    CALL_SIGN = "ARISS"  # APRS call sign for the ISS

    response = getData(CALL_SIGN)
    responseJSON = response.json()

    if int(responseJSON["found"]) > 0:  # Ensure valid response that has at least 1 entry
        print(responseJSON["entries"])
        writeDataToFile(responseJSON)
    else:
        print("No entries found")


def getData(CALL_SIGN):
    API_KEY = "117144.6TRIzMhji4Kxw"  # API key used to connect to aprs.fi

    PARAMS = {"name": CALL_SIGN, "apikey": API_KEY, "what": "loc", "format": "json"}
    URL = "https://api.aprs.fi/api/get"

    response = requests.get(URL, params=PARAMS)

    return response


def writeDataToFile(responseJSON):
    file = open("data.txt", "a")
    file.write(str(responseJSON["entries"]))
    file.write("\n")
    file.close()

if __name__ == '__main__':
    main()

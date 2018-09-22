# APRS Scraper

Retrieves data about a given vehicle using the [aprs.fi](http://aprs.fi) API. 

**APRS**, or **A**utomatic **P**acket **R**eporting **S**ystem, is a two-way real-time digital communications system between all vehicles in a network.

The script (_script.py_) will retrieve JSON data for a given call sign, and will store the JSON data into a text file (_data.txt_).


## Functions
 - `getData(CALL_SIGN)`: Reads the given call sign (such as "ARISS" for the ISS), and returns a `requests` response.
 - `writeDataToFile(responseJSON)`: Takes in a `requests` JSON object, and writes the JSON data to a file.
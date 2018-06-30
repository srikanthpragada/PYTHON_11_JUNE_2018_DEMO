import requests
import sys

resp = requests.get("https://restcountries.eu/rest/v2/all")

if resp.status_code != 200:
    print("Sorry! Could not get details of countries!")
    sys.exit(0)

for country in resp.json():
    print( "%-30s  %s"  % (country['name'], country['capital']))

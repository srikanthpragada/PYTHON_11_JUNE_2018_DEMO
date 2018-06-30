import requests
import sys

resp = requests.get("https://api.github.com/users/srikanthpragada/repos")

if resp.status_code != 200:
    print("Sorry! Could not get details of repos")
    sys.exit(0)

for repo in resp.json():
    print(repo["name"], ':', repo["description"])

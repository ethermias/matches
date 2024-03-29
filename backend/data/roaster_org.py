import requests
from util import read_json_file, write_json_file

url1 = "https://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/teams/"

def main():
    teams = read_json_file('teams.json')
    for i in teams:
        url = url1 + str(i["id"]) + "/roster"
        file_path = "roaster_org/" + i["abbr"] + ".json"
        print(url)
        response = requests.get(url)
        if response.status_code == 200:
            write_json_file(file_path, response.json())
        else:
            print(f"Failed to fetch data from {url}")


if  __name__ == "__main__":
    main()
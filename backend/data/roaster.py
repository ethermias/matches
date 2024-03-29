from util import read_json_file, write_json_file
 
def main():
    teams = read_json_file('teams/teams.json')
    
    for i in teams:
        read_file_path = "roaster_org/" + i["abbr"]+ ".json"
        file = read_json_file(read_file_path)
        players = []
        for p in file["athletes"]:
            player = { 
                "id": p["id"],
                'name' : p["shortName"], 
                'position' : p["position"]["abbreviation"],
                'displayName': p["displayName"]
            }
          
            if p.get("jersey") is not None:
                player.update({ 'jersey' : p["jersey"] })
            if p.get("citizenshipCountry") is not None:
                player.update({'citizen': p["citizenshipCountry"]["abbreviation"]})
     
            if p.get("statistics") is not None:
                playerStats = { 
                    'stats': {
                        "general": {  j["name"]: j["value"]  for j in p["statistics"]["splits"]["categories"][0]["stats"] },
                        "offensive": {  j["name"]: j["value"]  for j in p["statistics"]["splits"]["categories"][1]["stats"] }
                    }
                }
                player.update(playerStats)
            players.append(player)
        file_path = "roasters/" + i["abbr"]+ ".json"
        write_json_file(file_path, players)

if  __name__ == "__main__":
    main()


from util import read_json_file, write_json_file

def main():
    teams_org = read_json_file('teams_org.json')
    teams_long = teams_org['sports'][0]['leagues'][0]['teams']
    temp = [  x['team'] for x in teams_long ]
    teams = [  { 'id': t['id'], 'name': t['shortDisplayName'], 'nick': t['nickname'], 'abbr': t['abbreviation'] } for t in temp ]
    write_json_file("teams.json", teams)

if __name__ == "__main__":
    main()
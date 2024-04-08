bottomTeamArr = ["LTN","NFO","SHU","BUR"]
highTeamArr = [ "ARS", "CHE", "LIV", "MNC", "MAN", "TOT"]

def salaryMetrix(abbr, player):
    position = player['position']
    positionSalary = 0
    if position == 'G':
        positionSalary = -700
    elif position == 'D':
        positionSalary = -300
    elif position == 'F':
        positionSalary = 200
    else:
        positionSalary = 0
    
    appearances = player['stats']['general']['appearances']
    appearanceSalary = 0
    if appearances > 20: 
        appearanceSalary = 500
    elif appearances < 5: 
        appearanceSalary = -500


    subIns = player['stats']['general']['subIns']
    subInsSalary = 0
    if subIns > 5: 
        subInsSalary = -200

    if abbr in highTeamArr:
        return 6000 + positionSalary + appearanceSalary + subInsSalary
    elif abbr in bottomTeamArr:
        return 3000 + positionSalary + appearanceSalary + subInsSalary
    else:
        return 4000 + positionSalary + appearanceSalary + subInsSalary
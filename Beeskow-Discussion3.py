# Bryce Beeskow
# Discussion 3
# CSC115
# I certify, that this computer program submitted by me is all of my own work. Signed: Bryce Beeskow

#function of favorite sports teams
def favorite_teams():
    teams_list = ['Vikings', 'Twins', 'Timberwolves', 'Wild', 'Gophers']
    league = ['NFL', 'MLB', 'NBA', 'NHL', 'NCAA Football'] 
   
    for i in range(min(len(teams_list), len(league))):
        print(f'My favorite {league[i]} team is the {teams_list[i]}')    
          
          
print(favorite_teams())
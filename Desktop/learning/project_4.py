from random import choice

players = []
file = open('players.txt', 'r')
players = file.read().splitlines()

file = open('team_name.txt', 'r')
team_name = file.read().splitlines()

print(players)

teamA = []
teamB = []

while len(players) > 0:
    playerA = choice(players) 
    teamA.append(playerA)
    players.remove(playerA)

    if players == []:
        break

    playerB = choice(players) 
    teamB.append(playerB)
    players.remove(playerB)



print(choice(team_name), teamA)
print(choice(team_name), teamB)
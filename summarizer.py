### 
### Author: Faye Bandet
### Course: CSC 110
### Description: This is a program that reads a game log file. It processes the information, and prints out a summary.
###
def main():
    file = input('enter gamelog file name: \n')
    f = open(file)
    lines = f.readlines()
    outer_list = []
    for line in lines:
        line = line.strip().split()
        outer_list.append(line)
    winning_points(outer_list)
    scoring_players(outer_list)
    goals(outer_list)
    
def winning_points(outer_list):
### This function keeps track of the points, and which team won.
    team1 = outer_list[0][0]
    team2 = ''
    team1_points = 0
    team2_points = 0
    for i in range(len(outer_list)):
        if outer_list[i][0] != team1:
            team2 = outer_list[i][0]
        if team1 == outer_list[i][0]:
            if int(outer_list[i][2]) > 0:
                outer_list[i][2].strip('\n')
                team1_points += int(outer_list[i][2])
        if team2 == outer_list[i][0]:
            if int(outer_list[i][2]) > 0:
                outer_list[i][2].strip('\n')
                team2_points += int(outer_list[i][2])
                   
    if team1_points > team2_points:
        print(team1, 'won!')
    else:
        print(team2, 'won!')
    print(team1, 'scored', team1_points, 'points.')
    print(team2, 'scored', team2_points, 'points.')
    
def scoring_players(outer_list):
### This function keeps track of the ammount of scoring players.
    sum = 0
    player_names = []
    for line in outer_list:
        if line[1] not in player_names:
            sum += 1
        player_names.append(line[1])
    print(sum, 'players scored.')
    
def goals(outer_list):
### This function keeps track of who scored the first and last goals of the game.
    for line in outer_list:
        first_scorer = outer_list[0][1]
        last_scorer = outer_list[-1][1]
    print(first_scorer, 'scored first.')
    print(last_scorer, 'scored last.')
    
main()
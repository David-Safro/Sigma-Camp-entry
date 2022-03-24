'''
In the first few lines I set up the variables that I will use to moderate the gameplay. The first for loop is used to take the input from input.txt and reformat it into a 2 dimensional list. 
'''

scores = open("input.txt", "r")
all_games = []
game_count = 0
checker = True
for score in scores:
	score = score.split()
	for x in range(len(score)):
		score[x] = int(score[x])
	all_games.append(score)


for game in range(len(all_games)):
	current = all_games[game]
	if game_count >= 5:
		print(f'error line {game+1}')
		checker = False
		break
	if max(current) < 11:
		continue
	elif abs(current[1] - current[0]) >= 2:
		game_count += 1
		
	else:
		if max(all_games[game+1]) < max(current):
			print(f'error line {game+2}')
			checker = False
			break
# it is +2 because python counts from 0 but the lines start at 1 so I add one more to compensate

if game_count != 5:
	print('incomplete')
elif checker == True:
	print('Complete')
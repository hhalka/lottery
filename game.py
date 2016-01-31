#!/usr/bin/env python
from random import choice
import sys

class GameSettingInputError(ValueError):
	pass
	
class PlayerPreferencesInputError(ValueError):
	pass

if __name__ == "__main__":
	try:
		if len (sys.argv) != 3 or not all([item.isdigit() for item in sys.argv[1:]]):
			raise GameSettingInputError
	except GameSettingInputError:
		massage = 'Usage: game.py n m (n - number of games to play, m - number of players)'
		print massage
	
	else:
		game_n, player_n = int(sys.argv[1]), int(sys.argv[2])
		
		winners_dict = {}
		for _ in range(game_n):
			player_dict = {}
			n = 1
			while n <= player_n:
				while True:
					inputs = raw_input('Please, enter your name and preferred number: ').split()
					try:
						if len(inputs) != 2 or not inputs[1].isdigit():
							raise PlayerPreferencesInputError
						break
					except PlayerPreferencesInputError:
						massage = 'Error. Enter  your name first and than some number'
						print massage
				name_p, number_p = inputs
				player_dict[name_p] = number_p
				n += 1
				
			
			players_number_list = player_dict.values()
			selected_number = choice(players_number_list)
			local_winner = ', '.join([x for x,y in player_dict.items() if y == selected_number])
			print  '%s wins' %(local_winner)
		
			if local_winner not in winners_dict.keys():
				winners_dict[local_winner] = 1
			else:
				winners_dict[local_winner] += 1
				
		max_number_game_won = int(max(winners_dict.values()))
		winner_name = ', '.join([x for x, y in winners_dict.items() if y == max(winners_dict.values())])
		print 'Game winner is %s with number of games won %d' % (winner_name, max_number_game_won)
		

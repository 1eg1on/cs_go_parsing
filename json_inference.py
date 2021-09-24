# necessary imports
import json

# reading the pre-saved parces demo and printing out the keys
with open('first_parsed.json') as f:
	data = json.load(f)


# now that we have our dictionary as a variable, let's pull some info out

for k in data.keys():
	print('-'*40)
	print(k)
	print(type(data[k]))
	try:
		print(len(data[k]))
	except:
		pass
	#print(data[k])


# we are interested mainly in the GameRounds key

print(data.keys())
'''
Keys of data object 

dict_keys(['MatchId', 'ClientName', 'MapName', 'TickRate', 'PlaybackTicks', 'ParseRate', 'ServerVars', 'GameRounds'])
'''

KEY = 'GameRounds'
ROUND = 0

'''
keys of GameRounds dict

dict_keys(['RoundNum', 'StartTick', 'FreezeTimeEnd', 'EndTick', 'EndOfficialTick', 'TScore', 
'CTScore', 'EndTScore', 'EndCTScore', 'CTTeam', 'TTeam', 'WinningSide', 'WinningTeam', 'LosingTeam',
 'RoundEndReason', 'CTStartEqVal', 'CTRoundStartEqVal', 'CTRoundStartMoney', 'CTBuyType', 'CTSpend', 
 'TStartEqVal', 'TRoundStartEqVal', 'TRoundStartMoney', 'TBuyType', 'TSpend', 'Kills', 'Damages', 'Grenades',
  'BombEvents', 'WeaponFires', 'Flashes', 'Frames'])
'''

print(data[KEY][0].keys())


table_cards = ["A_S", "J_H", "7_D", "8_D", "10_D"]
hand_cards = ["J_D", "3_D"]
all_cards = table_cards + hand_cards
new_cards = []
S, H, D, C = 0, 0, 0, 0

for value in all_cards:
	new_cards.append(value[-1])

#print(new_cards)

for card in new_cards:
	if 	card ==  'D':
		D = D+1
	elif card == 'S':
		S = S+1
	elif card == 'H':
		H = H+1
	elif card == 'C':
		C = C+1

if D >= 5:
	print("D:", D, 'flush')
else:
	print('NO FLUSH')
if S >= 5:
	print("S:", S, 'flush')
else:
	print('NO FLUSH')
if H >= 5:
	print("H:", H, 'flush')
else:
	print('NO FLUSH')
if C >= 5:
	print("C:", C,'flush')
else:
	print('NO FLUSH')
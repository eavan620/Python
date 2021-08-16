import time, random

player_victory = 0
enemy_victory = 0

for i in range(1,4):
	time.sleep(2)
	print(f"\n------Round{i}------")
	player_life = random.randint(100,150)
	player_attack = random.randint(30, 50)
	enemy_life = random.randint(100,150)
	enemy_attack = random.randint(30,50)
	print(f"Player\nBlood: {player_life}\nAttack: {player_attack}")
	print("------")
	time.sleep(1)
	print(f"Enemy\nBlood: {enemy_life}\nAttack: {enemy_attack}")
	print('------')
	time.sleep(1)

	while player_life > 0 and enemy_life >0:
		player_life = player_life - enemy_attack
		enemy_life = enemy_life - player_attack
		print(f"You attacked the enemy and now the enemy's blood is {enemy_life}")
		print(f"The enemy attacked you and now your blood is {player_life}")

	if player_life >0 and enemy_life <= 0:
		player_victory +=1
		print("This round you won the game.")
	elif player_life <= 0 and enemy_life >0:
		enemy_victory +=1
		print("This round the enemy won the game.")
	else:
		print("This round has no winner.")
	print("------")

if player_victory > enemy_victory:
	time.sleep(1)
	print("You won the game!")
elif enemy_victory > player_victory:
	print("The enemy won the game!")
else:
	print('No winner!')

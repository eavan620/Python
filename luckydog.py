/*
 * Create a function to find a lucky dog from a list
 */


import random, time 

def luckydog(a,b,c):
	luckylists = [a, b, c]
	a = random.choice(luckylists)
	print("Who is the lucky dog?")
	time.sleep(1)
	print("Countdown: 3")
	time.sleep(1)
	print("Countdown: 2")
	time.sleep(1)
	print("Countdown: 1")
	time.sleep(1)
	image = '''
	 /\_)o<
	|      \\
	| O . O|
	 \_____/
	'''
	print(image)
	print(f"Congrats {a} got the prize!")

luckydog("benben","boniu","niuniu")


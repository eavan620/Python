/*
 * Create two functions to get a person's bonus which depends on the working time.
 */

def bonus(time):

	if time < 6:
		money = 500
	elif 6 < time <= 12:
		money = 120 * time 
	else:
		money = 180 * time 
	return money

def decison(name, time):
	gain = bonus(time)
	print(f"{name} worked {time} months here and the bonus is {gain} dollor.")

decison("Yiyuan",24)


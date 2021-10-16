import time 
for i in range(5,0,-1):
	print(f"\rCountdown: {i} Second", end=' ',flush=True)
	time.sleep(1)
print('Countdown over')
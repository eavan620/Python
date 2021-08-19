scores1 = [91,95,97,99,92,93,96,98]
sum = 0
scores2 = []
for score in scores1:
	sum = sum + score
average = sum / len(scores1)
print(f"The mean number is: {average}")

for score in scores1:
	if score < average:
		scores2.append(score)
print(f"Below the average scores are: {scores2}")
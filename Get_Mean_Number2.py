/ *
  * Get the mean number from a list and show the numbers below the average.
  * /

import numpy as np

scores1 = [91,95,97,99,92,93,96,98]
scores2 = []

average = np.mean(scores1)
print(f"The mean number is: {average}")

for score in scores1:
	if score < average:
		scores2.append(score)
print(f"Below the average scores are: {scores2}")

scores3 = np.array(scores1)
print(f"Below the average are: {scores3[scores3 < average]}")

class Chinese:

	def __init__(self,hometown,region):
		self.hometown = hometown
		self.region = region
	
	def born(self):
		print(f"I was born in {self.hometown}.")

	def live(self):
		print(f"Currently I am living in {self.region}.")
		
	def greeting(self):
		print('Nice to meet you!')
		self.born()
		self.live()

person = Chinese('Ningxia','Germany')
person.greeting()
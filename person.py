

class Person:
	def __init__(self,data):
		self.name = data[0]	
		self.githubname = data[1]
		self.semestercount = data[2]
		self.githubcommits = data[3] #This should come from github api
		self.attendcount = data[4]
		self.wincount = data[5]

	def str(self):
		return self.name + " " + self.githubname
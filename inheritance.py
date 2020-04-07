class Car():
	def __init__(self,model,year):
		self.model=model
		self.year=year
	def gearchange(self):
		print("gear of your car has been changed")
	def info(self):
		print("car  model{} and car top speed{}".format(self.model,self.year))
	def __str__ (self):
		return '{}{}'.format(self.model,self.year)
	def __len__(self):
		return self.year
	def __del__(self):
		print("object deleetd")
class Sportscar(Car):
	def __init__(self,model,year,accel,color):
		super().__init__(model,year)
		self.accel=accel
		self.color=color
	def info(self):
		print("information")
	def __str__(self):
		return '{}{}{}{}'.format(self.model,self.year,self.accel,self.color)

#l=['1','2','3']
#print(l)
alto=Sportscar('alto',2015,123,"red")
print(len(alto) )
del alto
print(alto)
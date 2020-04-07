class Mobile():
	def __init__(self,brand_name,model_name,price):
		self.brandname=brand_name
		self.modelname=model_name
		self.pricew=price
	def welcome(self):
		print("welcome")
	def is_eligible(self):
		if self.age>18:
			return True
		else:
			return False
motox=Mobile("moto","sdfg",24110)
iphone=Mobile("Apple","iphone3",234456)
iphone.price=609999
iphone.welcome()
iphone.is_eligible()
print("modelname {}".format(iphone.price))
def hcf(x,y):
	while(x!=y):
		if(x>y):
			x=x-y
		else:
			y=y-x
	return x


x=int(input("enetre number"))
y=int(input("eneter number"))
print("the hcf of two numbrt",hcf(x,y))
print("enetr two numbre")
x=(input("1"))
y=(input("2"))

while True:

	try:
		if(int(x)>int(y)):
			print(x,"greater")
		else:
			print("lesser")

	except:
		print("you did not add numeric value ")
		print("again")
		x=input("1")
		y=input("2")
		continue
	else:
		print("lol doine")
		break
	finally:

		print("two number compared successful")
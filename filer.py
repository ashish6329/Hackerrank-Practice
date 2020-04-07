file =open(r"/home/lol/Desktop/python prograame/rea.txt",'r')
content=file.readlines()
for line in content[0:5]:
	print(line)

print(content)
file.close()
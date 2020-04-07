

import os
b=(r"/media/lol/ashish/lab programme")
best=os.listdir(b)
b2=(r"/media/lol/ashish/lab programme2")
bestt=os.listdir(b2)
for song in best:
	if song in bestt:
		commonsong=os.path.join(b2,song)
		os.remove(commonsong)
'''names=os.listdir(r"/media/lol/ashish/lab programme")
print(names)'''
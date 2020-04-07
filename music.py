import time,sys
from pygame import mixer #load required library
sys.argv #["alarm","10","5"]
bplay=int(sys.argv[1])
aplay=int(sys.argv[2])
mixer.init()
mixer.music.load(r"music address")
time.sleep(bplay)
mixer.music.play()
time.sleep(aplay)
mixer.music.stop()
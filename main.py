# nerd
from random import seed
from random import randint
import time
# clown
seed(1)
# script kiddy
for i in range(1000000):
	value = randint(100000, 999999)
	time.sleep(0.0001)
	print(value,"\n", end='', flush=True)

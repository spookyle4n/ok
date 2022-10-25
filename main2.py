from random import seed
from random import randint
import time
import random
import string

randomnumber = chr(random.randint(ord('0'), ord('9')))
randomnumber2 = chr(random.randint(ord('0'), ord('9')))
randomnumber3 = chr(random.randint(ord('0'), ord('9')))
randomnumber4 = chr(random.randint(ord('0'), ord('9')))
randomnumber5 = chr(random.randint(ord('0'), ord('9')))
randomnumber6 = chr(random.randint(ord('0'), ord('9')))
randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
randomLowerLetter = chr(random.randint(ord('a'), ord('z')))

for i in range(10):
    print(randomnumber + randomnumber2 + randomnumber3 + randomnumber4 + randomnumber5 + randomnumber6 + randomUpperLetter + randomLowerLetter)

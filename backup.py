from random import seed
from random import randint
import time
import random
import string
for i in range(1000000):
    randomnumber = chr(random.randint(ord('0'), ord('9')))
    randomnumber2 = chr(random.randint(ord('0'), ord('9')))
    randomnumber3 = chr(random.randint(ord('0'), ord('9')))
    randomnumber4 = chr(random.randint(ord('0'), ord('9')))
    randomnumber5 = chr(random.randint(ord('0'), ord('9')))
    randomnumber6 = chr(random.randint(ord('0'), ord('9')))
    randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
    randomLowerLetter = chr(random.randint(ord('a'), ord('z')))

    print(randomnumber + randomnumber2 + randomnumber3 + randomnumber4 + randomnumber5 + randomnumber6 + randomUpperLetter + randomLowerLetter, flush=True)
    time.sleep(0.00001)

from random import seed
from random import randint
import random
import string

print('''
   ____      ____
  |    |    |    |_______________________________
  |    |    |    |         |           |         \
  |    |    |    |   __    |     __    |    ___   \
  |    | /\ |    |  |  |   |    |  \___|   |   |  |
  |    |/  \|    |  |__|   |    |     |    |___|  |
  \             /          |    |     |           /
   \___________/___________|____|     |__________/
   
              tiktok jahsehrare
              insta: spookyle4n

''')
for i in range(1000000):
    randomnumber = chr(random.randint(ord('0'), ord('9')))
    randomnumber2 = chr(random.randint(ord('0'), ord('9')))
    randomnumber3 = chr(random.randint(ord('0'), ord('9')))
    randomnumber4 = chr(random.randint(ord('0'), ord('9')))
    randomnumber5 = chr(random.randint(ord('0'), ord('9')))
    randomnumber6 = chr(random.randint(ord('0'), ord('9')))
    randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
    randomLowerLetter = chr(random.randint(ord('a'), ord('z')))
    
hi = input("[?] Generate wordlist? [y/n]: ")
if hi == 'y':
    for i in range(1000000):
        print(randomnumber + randomnumber2 + randomnumber3 + randomnumber4 + randomnumber5 + randomnumber6 + randomUpperLetter + randomLowerLetter)

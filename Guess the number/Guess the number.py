'''THIS PROGRAM WILL GUESS YOU NUMBER'''

import random
import time

MIN = 1
MAX = 1000
B = '>'
S = '<'
E = '='

numb = random.randrange(1,1000)
print(numb)

while True:
    user_choice = input()
    if user_choice == S:
        MAX = numb
        numb = int((numb + MIN) / 2)
        print(int(numb))

    if user_choice == B:
        MIN = numb
        numb = int((numb + MAX) / 2)
        print(int(numb))

    elif user_choice == E:
        print(int(numb), 'VICTORY!')

        break
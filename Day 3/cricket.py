# cricket problem

import random

runs = int(input("enter your expected runs: "))
if runs < 1 or runs > 250:
    print("Reduce your expectation for 20-20 Cricket")
randomno = random.choice(range(1, 251))
value = abs(randomno - runs)

if value == 0:
    print("you perfectly guess score")
elif value <= 10:
    print("close by! you are true indian fans")
else:
    print("you dont watch that much!")



# using while loop
while 251 > runs > 0:
    print("computer genrated runs " + str(randomno))
    if runs == randomno:
        print("you perfectly guess score")
    elif (randomno - 11) < runs < (randomno + 11):
        print("close by! you are true indian fans")
    else:
        print("you dont watch that much!")
    break


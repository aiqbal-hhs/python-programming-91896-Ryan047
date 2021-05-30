import random
import time



flips = 0
heads = "Heads"
tails = "Tails"

heads_and_tails = [(heads),
                   (tails)]
while input("Do you want to coin flip? [y|n]") == 'y':
    print(random.choice(heads_and_tails))
    time.sleep(.5)
    flips += 1


else:
    print("You flipped the coin",flips,"times")
    print("Good bye")




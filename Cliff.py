import time

answer = ["yes","y"]

person = input("Would Falling for 4 minutes be Fun? \n").lower()

if person in answer:
    print("Correct!")

else:
    time.sleep(240)
    print("Wrong!")


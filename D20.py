from random import randint, seed
die = input("How many sides does your die have?")
repeat = True
roll = randint(1, int(die))
while repeat:
    roll = randint(1, int(die))
    if roll == 1:
        print("Your roll is:",roll,"Critical Fail!")
        print("Roll again?")
        repeat = ("y" or "yes") in input().lower()
    elif roll == int(die):
        print("Your roll is:",roll,"Critical Success!")
        print("Roll again?")
        repeat = ("y" or "yes") in input().lower()
    else:
        print("Your roll is:",roll)
        print("Roll again?")
        repeat = ("y" or "yes") in input().lower()
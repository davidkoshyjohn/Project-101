import random

def dice():
    def roll():
        value = random.randint(1,6)

        if value == 1:
            print("[-----]")
            print("[     ]")
            print("[  *  ]")
            print("[     ]")
            print("[-----]")

        if value == 2:
            print("[-----]")
            print("[     ]")
            print("[ * * ]")
            print("[     ]")
            print("[-----]")

        if value == 3:
            print("[-----]")
            print("[     ]")
            print("[* * *]")
            print("[     ]")
            print("[-----]")

        if value == 4:
            print("[-----]")
            print("[*   *]")
            print("[     ]")
            print("[*   *]")
            print("[-----]")

        if value == 5:
            print("[-----]")
            print("[*   *]")
            print("[  *  ]")
            print("[*   *]")
            print("[-----]")

        if value == 6:
            print("[-----]")
            print("[* * *]")
            print("[     ]")
            print("[* * *]")
            print("[-----]")

    ans = input("press y to roll again and n to exit: ")

    if ans == "y" or ans == "Y":
        roll()
        dice()
    elif ans == "n" or ans == "N":
        quit()
    else:
        print("Sorry, Please enter a valid response")
        dice()

dice()
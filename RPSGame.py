import random
import RPSmodule as RPS

def OutcomeOne():
    print(Player1, "Wins!, ","(",Weapon1,")", "vs", "(",Weapon2,")")

def OutcomeTwo():
    print(Player2, "Wins!, ","(",Weapon2,")", "vs", "(",Weapon1,")")


Rounds = int(input("How many rounds would you like to play? :"))
Player1 = RPS.PlayerOne()
Player2 = RPS.PlayerTwo()
StartPLayer = bool(random.getrandbits(1))

for i in range(1, Rounds + 1):
    print("\r\n** Round ", i)
    if StartPLayer == 0:
        print(Player1, "has been randomly chosen to start the game")
        print(Player1, "please choose your weapon:")
        print("1 = Rock", "\n2 = Paper", "\n3 = Scissors")
        Weapon1 = RPS.WeaponOne()

        print(Player2, "please choose your weapon:")
        print("1 = Rock", "\n2 = Paper", "\n3 = Scissors")
        Weapon2 = RPS.WeaponTwo()
    else:
        print(Player2, "has been randomly chosen to start the game")
        print(Player2, ", please choose your weapon:")
        print("1 = Rock", "\n2 = Paper", "\n3 = Scissors")
        Weapon1 = RPS.WeaponOne()


        print(Player1, "please choose your weapon:")
        print("1 = Rock", "\n2 = Paper", "\n3 = Scissors")
        Weapon2 = RPS.WeaponTwo()

    if Weapon1 == Weapon2:
        print("Draw!")
    elif Weapon1 == 1:
        if Weapon2 == 3:
            OutcomeOne()
        else:
            OutcomeTwo()
    elif Weapon1 == 2:
        if Weapon2 == 1:
            OutcomeOne()
        else:
            OutcomeTwo()
    elif Weapon1 == 3:
        if Weapon2 == 2:
            OutcomeOne()
        else:
            OutcomeTwo()



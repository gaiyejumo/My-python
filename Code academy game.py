import random

money = 100

# write your game of chance functions here

num = random.randint(1, 10)

def Guess_Game(Guess, bet):
    if bet > 100 or bet <= 0:
        return "You can only bet between $1 - $100"
    else:
        if Guess == num:
            return "Congratulation, you have won $" + str(money + bet)
        else:
            return "Ayah, you made the wrong guess, hence you have lost $" + str(money - bet)



print(Guess_Game(10, 10))


flip = random.randint(1, 2)

def Coin_flip(coin, bet):
    if bet > 100 or bet <= 0:
        return "You can only bet between 1 & 2"
    else:
        if flip == 1 and coin == flip:
            return "Congratulations, it is Heads and you have won $" + str(money + bet)
        elif flip != 1:
            return "You have lost $" + str(money - bet)
        elif flip == 2 and coin == flip:
            return "Congratulations, it is Tails and you have won $" + str(money-bet)
        elif flip !=2:
            return "You have lost $" + str(money - bet)

print(Coin_flip(1,50))
print(Coin_flip(2,60))

            

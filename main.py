import random
import sys

values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
playerHand = []
dealerHand = []


def dealHand(numOfCards, person):
    global playerHand, dealerHand
    if person == "player":
        for i in range(numOfCards):
            card = values[random.randint(0, values.__len__() - 1)]
            playerHand.append(card)
    elif person == "dealer":
        for j in range(numOfCards):
            card2 = values[random.randint(0, values.__len__() - 1)]
            dealerHand.append(card2)

def total(person):
    sum1 = 0
    sum2 = 0
    if person == "player":
        for i in range(playerHand.__len__()):
            if playerHand[i] == "J" or playerHand[i] == "K" or playerHand[i] == "Q":
                sum1 = sum1 + 10
                sum2 = sum2 + 10
            elif playerHand[i] == "A":
                sum1 = sum1 + 1
                sum2 = sum2 + 11
            else:
                sum1 = sum1 + playerHand[i]
                sum2 = sum2 + playerHand[i]
        if sum2 <= 21:
            return sum2
        else:
            return sum1
    elif person == "dealer":
        for j in range(dealerHand.__len__()):
            if dealerHand[j] == "J" or dealerHand[j] == "K" or dealerHand[j] == "Q":
                sum1 = sum1 + 10
                sum2 = sum2 + 10
            elif dealerHand[j] == "A":
                sum1 = sum1 + 1
                sum2 = sum2 + 11
            else:
                sum1 = sum1 + dealerHand[j]
                sum2 = sum2 + dealerHand[j]
        if sum2 <= 21:
            return sum2
        else:
            return sum1

def hit():
    dealHand(1,"player")


def update():
    global b
    print("Your cards are: " + ", ".join(str(card) for card in playerHand))
    print("Your total is " + str(total("player")))
    print("_____________________________________________________________________")
    b = input("Would you like to hit or stand? ")

def dealerPlay():
    while total("dealer") < 17:
        card = values[random.randint(0, values.__len__() - 1)]
        dealerHand.append(card)


a = input("Hello! Would You Like To Play BlackJack? ")
if a == "yes":
    dealHand(2, "player")
    dealHand(2, "dealer")
    print("The dealer is showing: " + str(dealerHand[0]))
    update()
    dealerPlay()

    while b == "hit":
        hit()
        update()
    if b == "stand":
        print("Your cards are: " + ", ".join(str(card) for card in playerHand))
        print("Your total is " + str(total("player")))
        print("The dealer's cards are: " + ", ".join(str(card) for card in dealerHand))
        print("The dealer's total is " + str(total("dealer")))
        if total("dealer") < total("player") < 21 or total("player") == 21 or total("player") <= 21 < total("dealer"):
            print("YOU WIN!!!!!")
        else:
            print("YOU LOSE!!!!!")

else:
    print("Okay Bye")
    sys.exit()


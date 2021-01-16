#import numpy
import sys
import random
import traceback

import Cards
#import Constants

gLogEnabled = True
gNumPlayers = 3
gPlayers = []
gBoard = []

def Log(someLog):
    if gLogEnabled:
        print(someLog)

def GetPlayingPlayersFromUser():
    global gNumPlayers
    global gPlayers

    '''
    gNumPlayers = int(raw_input("Please enter number of players from 2-23: "))
    if gNumPlayers not in range(2,23+1):
        print("Invalid input")
        sys.exit(0)

    for i in range(1, gNumPlayers+1):
        gPlayers.append(Cards.Player(i, "Player " + str(i), GetNumRandomCardFromCurrentDeck(2)))

    '''

    i=1
    while True:
        pName = input("Please enter player name (empty to continue): ")
        if not pName:
            break
        gPlayers.append(Cards.Player(i, pName, GetNumRandomCardFromCurrentDeck(2)))
        i+=1

    gNumPlayers = i

def GetNumRandomCardFromCurrentDeck(num):
    cards = []
    for i in range(1,num+1):
        cards.append(GetOneCardFromCurrentDeck())
    return cards

def GetOneCardFromCurrentDeck():
    cardsLeft = len(gCurrentDeck)

    idx = random.randint(0,cardsLeft)
    try:
        card = gCurrentDeck[idx]
    except IndexError as e:
        print("Length of deck: " + str(len(gCurrentDeck)))
        #print(e)
        sys.exit(0)
        #for eachCard in gCurrentDeck:
            #print str(eachCard.value) + eachCard.suite

    del gCurrentDeck[idx]
    return card

def Init():
    global gCurrentDeck

    gCurrentDeck = Cards.GetNewDeck()
    GetPlayingPlayersFromUser()
    PrintPlayersWithCards()

def PrintPlayersWithCards():
    for eachPlayer in gPlayers:
        print("{0} has {1}{2} {3}{4}".format(eachPlayer.name,
            Cards.GetCardNameString(eachPlayer.cards[0].value), eachPlayer.cards[0].suite,
            Cards.GetCardNameString(eachPlayer.cards[1].value), eachPlayer.cards[1].suite)
            )

def GetListOfJustCards(someList):
    newList = []
    for eachItem in someList:
        newList.append("{0}{1}".format(Cards.GetCardNameString(eachItem.value), eachItem.suite))
    return newList

def DealFlop():
    global gBoard
    gBoard = GetNumRandomCardFromCurrentDeck(3)

def DealTurn():
    gBoard.append(GetOneCardFromCurrentDeck())

def DealRiver():
    gBoard.append(GetOneCardFromCurrentDeck())

def Play():
    DealFlop()
    DealTurn()
    DealRiver()

    #gBoard = [Cards.Card(2,'S'), Cards.Card(3,'S'), Cards.Card(4,'D'), Cards.Card(5,'S'), Cards.Card(9,'C'), Cards.Card(10,'C')] 

    print("\nBoard is: " + " ".join(GetListOfJustCards(gBoard)))

    print("\nBest Hands:-\n")

    for eachPlayer in gPlayers:
        Cards.PrintBestHandOfPlayer(eachPlayer, gBoard)

def Rank():
    print("----------------------------")
    print("-----------RANKING----------")
    print("----------------------------")

    gPlayers.sort(key=lambda x: x.points, reverse=True)
    i = 1
    for eachPlayer in gPlayers:
        print("{0}. {1}".format(i, eachPlayer.name))
        i+=1

def main():
    Init()
    Play()
    Rank()

if __name__ == '__main__':
    try:
        main()
    except:
        print(traceback.print_exc())

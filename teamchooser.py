#!/bin/python3
from random import choice
def teamChooser(players):

    firstTeam = []
    secondTeam = []

    while len(players) > 0:
        playerA = choice(players)
        firstTeam.append(playerA)
        players.remove(playerA)

        playerB = choice(players)
        secondTeam.append(playerB)
        players.remove(playerB)

        print("First Team:", firstTeam)
        print("Second Team:", secondTeam)


players=["Jack","Jill","Bob","David","Jeff","Brian","Aaron","Jake"]

teamChooser(players)
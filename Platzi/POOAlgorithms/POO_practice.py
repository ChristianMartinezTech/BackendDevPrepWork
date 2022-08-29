#!/usr/bin/env python3
"""Practie file for POO before taking this course"""

class League:
    """League class"""

    def __init__(self, teams, no_teams, country):
        self.teams = teams
        self.no_teams = no_teams
        self.country = country

class SoccerClub(League):
    """Soccer club class"""

    def __init__(self, players, colors, trophies, league):
        self.players = players
        self.colors = colors
        self.trophies = trophies
        self.league = league

la_liga = League(real_madrid.__name__, 16, "spain")
print(la_liga.teams)
print(la_liga.no_teams)
print(la_liga.country)


# Creating the object Real Madrid
real_madrid = SoccerClub("Vini, Benzema, Modric", "White", 150, "Spanish")
print(real_madrid.players)
print(real_madrid.colors)
print(real_madrid.trophies)
print(real_madrid.league)
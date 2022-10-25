import data
from datetime import date


# Sprint 1
# US 35 - List recent births
def getRecentBirths():
    people = data.personData()
    recentBirths = []
    for person in people:
        if isWithin30Days(person.birthday):
            recentBirths.append(person)
    return recentBirths

# End of US 35


# Sprint 2
# US 31 - List living single
def getLivingSingle():
    people = data.personData()
    livingSingle = []
    for person in people:
        if person.age > 30 and len(person.spouse) == 0:
            livingSingle.append(person)
    return livingSingle


# End of US 31

# US 36 - List recent deaths
def getRecentDeaths():
    people = data.personData()
    recentDeaths = []
    for person in people:
        if not person.alive and isWithin30Days(person.death):
            recentDeaths.append(person)
    return recentDeaths


def isWithin30Days(day):
    today = date.today()
    dateDiff = today - day
    if dateDiff.days <= 30 and dateDiff.days >= 0:
        return True
    return False

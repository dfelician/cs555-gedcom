import data
from datetime import date


# Sprint 1
# US 35 - List recent births
def getRecentBirths():
    people = data.personData()
    recentBirths = []
    for person in people:
        if bornWithin30Days(person.birthday):
            recentBirths.append(person)
    return recentBirths


def bornWithin30Days(birthday):
    today = date.today()
    dateDiff = today - birthday
    if dateDiff.days <= 30:
        return True
    return False
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

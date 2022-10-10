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

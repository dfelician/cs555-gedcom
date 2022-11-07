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


# US 07
def lessThen150():
    people = data.personData()
    today = date.today()
    errorStrings = []
    for person in people:
        if person.alive:
            dateDiff = today.year - person.birthday.year
            if dateDiff >= 150:
                output = "Error: INDIVIDUAL: US07: " + person.id + " " + person.name + " birth is 150 years or more before today"
                errorStrings.append(output)
        if not person.alive:
            dateDiff = person.death.year - person.birthday.year
            if dateDiff >= 150:
                output = "Error: INDIVIDUAL: US07: " + person.id + " " + person.name + " death is 150 years or more before birthday"
                errorStrings.append(output)
    return errorStrings


# US 27
def orderSiblingsByAge():
    families = data.familyData()
    people = data.personData()
    familyDict = {}
    for family in families:
        children = []
        key = family.id
        for person in people:
            if len(person.child) != 0 and person.child[0] == key:
                children.append(person)
        children.sort(key=lambda x: x.age, reverse=True)
        familyDict[key] = children
    return familyDict




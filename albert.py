import data
from datetime import date


def isMarriedBeforeDivorce():
    errorStrings = []
    families = data.familyData()

    for fam in families:
        #US04: Divorce can only occur after marriage
        if (fam.married == "NA" and fam.divorced != "NA"):
            output = "Error US04: Family can not divorce without marriage"
            errorStrings.append(output)
        #US04: Marriage should occur before divorce of spouses
        if (fam.divorced != "NA" and fam.married > fam.divorced):
            output = "Error US04: " + fam.id + ": Marriage date " + str(fam.married) + " occurs after divorce date " + str(fam.divorced)
            errorStrings.append(output)

    return errorStrings

def isBirthBeforeMarriage():
    errorStrings = []
    families = data.familyData()
    people = data.personData()

    for fam in families: 
        childrenIds = fam.childrenIds
        marriageDate = fam.married
        divorceDate = fam.divorced
        for person in people: 
            #US08: Children should be born after marriage of parents
            if (person.id in childrenIds and person.birthday < marriageDate):
                #output = "Anomoly US08: " + person.id + ": Child birthdate " + str(person.birthday) + " occurs before marriage date " + str(marriageDate)
                output = "Anomoly US08: Birth date of " + str(person.name) + "(" + str(person.id) + ") occurs before the marriage date of his parents in Family (" + str(fam.id) + ")"
                errorStrings.append(output)
            #US08: Children should not be born after 9 months of divorce
            if (person.id in childrenIds and divorceDate != "NA"):
                if (person.birthday.year == divorceDate.year):
                    if (person.birthday.month - divorceDate.month > 9):
                        #output = "Anomoly US08: " + person.id + ": Child birthdate " + str(person.birthday) + " occurs over 9 months after divorce date " + str(divorceDate)
                        output = "Anomoly US08: Birth date of " + str(person.name) + "(" + str(person.id) + ") occurs over 9 months after the divorce date of his parents in Family (" + str(fam.id) + ")"
                        errorStrings.append(output)
                elif (person.birthday.year > divorceDate.year):
                    if (12 + person.birthday.month - divorceDate.month > 9):
                        #output = "Anomoly US08: " + person.id + ": Child birthdate " + str(person.birthday) + " occurs over 9 months after divorce date " + str(divorceDate)
                        output = "Anomoly US08: Birth date of " + str(person.name) + "(" + str(person.id) + ") occurs over 9 months after the divorce date of his parents in Family (" + str(fam.id) + ")"
                        errorStrings.append(output)
    return errorStrings

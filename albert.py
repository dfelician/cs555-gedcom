import data
from datetime import date


def isMarriedBeforeDivorce():
    errorStrings = []
    families = data.familyData()

    for fam in families:
        if (
                fam.married.year > fam.divorced.year and fam.married.month > fam.divorced.month and fam.married.day > fam.divorced.day):
            output = "Error: Family: US01: " + fam.id + ": Marriage date " + str(fam.married) + " occurs after divorce date"
            errorStrings.append(output)
        if (
                fam.divorced != "NA" and fam.divorced.year > currentDate.year and fam.divorced.month > currentDate.month and fam.divorced.day > currentDate.day):
            output = "Error: Family: US01: " + fam.id + ": Divorce date " + str(fam.divorced) + " occurs in the future"
            errorStrings.append(output)

    return errorStrings

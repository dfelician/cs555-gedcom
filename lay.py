import data
from datetime import date


def isDateValid():
    errorStrings = []
    currentDate = date.today()
    people = data.personData()
    families = data.familyData()

    for individual in people:
        if (
                individual.birthday.year > currentDate.year and individual.birthday.month > currentDate.month and individual.birthday.day > currentDate.day):
            output = "Error: INDIVIDUAL: US01: " + individual.id + ": Birthday " + str(
                individual.birthday) + " occurs in the future"
            errorStrings.append(output)

        if (
                individual.death != "NA" and individual.death.year > currentDate.year and individual.death.month > currentDate.month and individual.death.day > currentDate.day):
            output = "Error: INDIVIDUAL: US01: " + individual.id + ": Death " + str(
                individual.death) + " occurs in the future"
            errorStrings.append(output)

    for fam in families:
        if (
                fam.married.year > currentDate.year and fam.married.month > currentDate.month and fam.married.day > currentDate.day):
            output = "Error: Family: US01: " + fam.id + ": Marriage date " + str(fam.married) + " occurs in the future"
            errorStrings.append(output)
        if (
                fam.divorced != "NA" and fam.divorced.year > currentDate.year and fam.divorced.month > currentDate.month and fam.divorced.day > currentDate.day):
            output = "Error: Family: US01: " + fam.id + ": Divorce date " + str(fam.divorced) + " occurs in the future"
            errorStrings.append(output)

    return errorStrings


def isMarriageAfter14():
    errorStrings = []
    people = data.personData()
    families = data.familyData()

    for fam in families:
        marriageDate = fam.married
        husbandId = fam.husbandId
        wifeId = fam.wifeId

        for individual in people:
            if (individual.id == husbandId and marriageDate.year - individual.birthday.year < 14):
                output = "Error: Family: US10: " + fam.id + ": Husband Birthdate " + str(
                    individual.birthday) + " is less than 14 years of Marriage Date " + str(marriageDate)
                errorStrings.append(output)
            if (individual.id == wifeId and marriageDate.year - individual.birthday.year < 14):
                output = "Error: Family: US10: " + fam.id + ": Wife Birthdate " + str(
                    individual.birthday) + " is less than 14 years of Marriage Date " + str(marriageDate)
                errorStrings.append(output)

    return errorStrings

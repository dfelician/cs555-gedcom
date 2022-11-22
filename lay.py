from tkinter.font import families
import data
import utils
from datetime import date


def isDateValid():
    errorStrings = []
    currentDate = date.today()
    people = data.personData()
    families = data.familyData()

    for individual in people:

        if (individual.birthday > currentDate):
            output = "Error: INDIVIDUAL: US01: " + individual.id + ": Birthday " + str(
                individual.birthday) + " occurs in the future"
            errorStrings.append(output)

        if (individual.death != "NA" and individual.death > currentDate):
            output = "Error: INDIVIDUAL: US01: " + individual.id + ": Death " + str(individual.death) + " occurs in the future"
            errorStrings.append(output)

    for fam in families:
        if (fam.married != "NA" and fam.married > currentDate):
            output = "Error: FAMILY: US01: " + fam.id + ": Marriage date " + str(fam.married) + " occurs in the future"
            errorStrings.append(output)
        if (fam.divorced != "NA" and fam.divorced > currentDate):
            output = "Error: FAMILY: US01: " + fam.id + ": Divorce date " + str(fam.divorced) + " occurs in the future"
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
            if (marriageDate != "NA" and individual.id == husbandId and marriageDate.year - individual.birthday.year < 14):
                output = "Error: FAMILY: US10: " + fam.id + ": Husband Birthdate " + str(
                    individual.birthday) + " is less than 14 years of Marriage Date " + str(marriageDate)
                errorStrings.append(output)
            if (marriageDate != "NA" and individual.id == wifeId and marriageDate.year - individual.birthday.year < 14):
                output = "Error: FAMILY: US10: " + fam.id + ": Wife Birthdate " + str(
                    individual.birthday) + " is less than 14 years of Marriage Date " + str(marriageDate)
                errorStrings.append(output)

    return errorStrings

def multipleBirths():
    errorStrings = []
    families = data.familyData()
    people = data.personData()
    childrenIds = []
    for fam in families:
        if len(fam.childrenIds) > 5:
            childrenIds = fam.childrenIds
    
            childrenBirthdays = []
            for individual in people:
                if individual.id in childrenIds:
                    childrenBirthdays.append(individual.birthday)
    
            dateDic = {}

            for birthday in childrenBirthdays:

                if birthday not in dateDic:
                    dateDic[birthday] = 1
                else:
                    dateDic[birthday] += 1
            
            for key in dateDic:
                if dateDic[key] > 5:
                    output = "Error: FAMILY: US14: " + fam.id + " More than 5 siblings are born at the same time"
                    errorStrings.append(output)
    
    return errorStrings
    
def isParentsOld():
    errorStrings = []
    families = data.familyData()
    people = data.personData()
    childrenIds = []

    for fam in families:
        husbandId = fam.husbandId
        wifeId = fam.wifeId
        childrenIds = fam.childrenIds
        husband = None
        wife = None
        childrenBirthdays = []


        for person in people:
            if husbandId == person.id:
                husband = person
            if wifeId == person.id:
                wife = person

        for person in people:
            if person.id in childrenIds:
                    childrenBirthdays.append(person.birthday)

        for childBirth in childrenBirthdays:
            # may need to relook into calculating age differences
            if utils.getTimeDifference(childBirth, wife.birthday) > 60:
                output = "Error: FAMILY: US12: " + fam.id + " Mother is greater than 60 years old, Mother id: " + wife.id
                errorStrings.append(output)

            if utils.getTimeDifference(childBirth, husband.birthday) > 80:
                output = "Error: FAMILY: US12: " + fam.id + " Father is greater than 80 years old, Father id: " + husband.id
                errorStrings.append(output)
            break

    return errorStrings

def sameLastNameMale():
    errorStrings = []
    families = data.familyData()
    people = data.personData()

    for fam in families:
        husbandId = fam.husbandId
        husbandLastName = None
        childrenIds = []
        childrenIds = fam.childrenIds

        for person in people:
            if person.id == husbandId:
                husbandLastName = person.name.split()[1][1:-1]
        
        for person in people:
            if person.id in childrenIds and person.gender == 'M' and person.name.split()[1][1:-1] != husbandLastName:
                output = "Error: FAMILY: US16: " + fam.id + " Not all male members of the family have the same last name of " + husbandLastName
                errorStrings.append(output)
                break

    return errorStrings

def correctGenderRole():
    errorStrings = []
    families = data.familyData()
    people = data.personData()

    for fam in families:
        husbandId = fam.husbandId
        wifeId = fam.wifeId
    
        for person in people:
            if person.id == husbandId and person.gender != 'M':
                output = "Error: FAMILY: US21: " + fam.id + " Family Husband is not gender Male, Husband id: " + husbandId
                errorStrings.append(output)
            if person.id == wifeId and person.gender != 'F':
                output = "Error: FAMILY: US21: " + fam.id + " Family Wife is not gender Female, Wife id: " + wifeId
                errorStrings.append(output)
        
    return errorStrings

def uniqueNameBirth():
    errorStrings = []
    people = data.personData()

    uniquePeopleDict = {}

    for person in people:
        key = person.name + str(person.birthday)
        if key not in uniquePeopleDict:
            uniquePeopleDict[key] = 1
        else:
            uniquePeopleDict[key] += 1
    
    for key in uniquePeopleDict:
        #print(key)
        #print(uniquePeopleDict[key])
        if uniquePeopleDict[key] > 1:
            output = 'Error: INDIVIDUAL: US23: More than 1 individuals with same name and birthdays ' + key
            errorStrings.append(output) 

    return errorStrings
 
def uniqueFirstNameInFamily():
    errorStrings = []
    families = data.familyData()
    people = data.personData()

    for fam in families:
        childrenIds = fam.childrenIds
        uniqueChildrenDict = {}

        for person in people:
            if person.id in childrenIds:
                key = person.name + str(person.birthday)
                if key not in uniqueChildrenDict:
                    uniqueChildrenDict[key] = 1
                else:
                    uniqueChildrenDict[key] += 1
        
        for key in uniqueChildrenDict:
            #print(key)
            #print(uniqueChildrenDict[key])
            if uniqueChildrenDict[key] > 1:
                output = 'Error: FAMILY: US25: More than 1 children with same name and birthday, family id ' + fam.id + ' with children ' +  key
                errorStrings.append(output)



    return errorStrings
from pyexpat import ErrorString
from tkinter.font import families
import data

def isIdUnique():
    errorStrings = []
    # peopleDuplicateId = []
    # familyDuplicateId = []

    people = data.personData()
    families = data.familyData()

    uniqueIdChecker(people, "INDIVIDUAL", errorStrings)
    uniqueIdChecker(families, "FAMILY", errorStrings)

    # created a method to check the ID of both Individuals and familiy records, refactoring code below for US22
    # 
    # for i in range(1, len(people)):
    #     id = people[i-1].id
    #     if people[i].id == id:
    #         peopleDuplicateId.append(people[i].id)
    #         errorId = str(people[i].id)
    #         errorId = errorId.replace("\n", "")
    #         output = "Error: INDIVIDUAL: US22: " + errorId + " is not a unique ID"
    #         errorStrings.append(output)

    # for i in range(1, len(families)):
    #     id = families[i-1].id
    #     if families[i].id == id:
    #         familyDuplicateId.append(families[i].id)
    #         errorId = str(people[i].id)
    #         errorId = errorId.replace("\n", "")
    #         output = "Error: FAMILY: US22: " + errorId + " is not a unique ID"
    #         errorStrings.append(output)

    return errorStrings

def uniqueIdChecker(dataset, datasetType, errorStrings):
    duplicateIdList = []
    output = ""
    for i in range(1, len(dataset)):
        id = dataset[i-1].id
        if dataset[i].id == id:
            duplicateIdList.append(dataset[i].id)
            errorId = str(dataset[i].id)
            errorId = errorId.replace("\n", "")
            output = "Error: " + datasetType + ": US22: " + errorId + " is not a unique ID"
            errorStrings.append(output)
            
    return 

def getDeaths():
    people = data.personData()
    death = []

    for person in people:
        if person.alive != True:
            death.append(person)

    
    return death

#US 05 Marriage should occur before death of either spouse

def marriageBeforeDeath():
    people = data.personData()
    families = data.familyData()
    errorStrings = []

    for fam in families:
        wifeId = fam.wifeId
        husbandId = fam.husbandId
        marriedDate = fam.married
        
        for person in people:
            if person.id == wifeId or person.id == husbandId:
                if not person.alive and marriedDate > person.death:
                    output = "Error: FAMILY: US05: Marriage occurs after death of spouse " + person.id +" Death Date " + str(person.death) + " Marriage Date: " + str(marriedDate)
                    errorStrings.append(output)

    return errorStrings

#US 06 Divorce should occur before the death of either spouse

def divorceBeforeDeath():
    people = data.personData()
    families = data.familyData()
    errorStrings = []

    for fam in families:
        wifeId = fam.wifeId
        husbandId = fam.husbandId
        if fam.divorced != "NA":
            divorceDate = fam.divorced
            for person in people:
                if person.id == wifeId or person.id == husbandId:
                    if not person.alive and person.death < divorceDate:
                        output = "Error: FAMILY: US06: Divorce occurs after death of spouse " + person.id +" Death Date " + str(person.death) + " Divorce Date: " + str(divorceDate)
                        errorStrings.append(output)

    return errorStrings

#End of US 06

#US 15 There should be fewer than 15 siblings in a family

def lessThan15Siblings():
    families = data.familyData()
    errorStrings = []

    for fam in families:
        numOfChildren = len(fam.childrenIds)
        if numOfChildren >= 15:
            output = "Error: FAMILY: US15: There are 15 or more siblings in family " + str(fam.id)
            errorStrings.append(output)
 
    return errorStrings


#End of US 15 

#US 18 Siblings should not marry one another

def siblingsShouldNotMarry():
    families = data.familyData()
    errorStrings = []

    marriageDict = {}

    for fam in families:
        husbandId = fam.husbandId
        wifeId = fam.wifeId
        marriageDict[husbandId] = wifeId

    for fam in families:
        for key in marriageDict:
            if key in fam.childrenIds and marriageDict[key] in fam.childrenIds:
                output = "Error: FAMILY: US18: Siblings should not marry each other " + str(fam.id)
                errorStrings.append(output)
    return errorStrings

#US 18 

#US 30 List living married

def livingMarriedCouples():
    people = data.personData()
    families = data.familyData()

    couplesDict = {}
    livingMarried = []

    for fam in families:
        if fam.divorced is "NA":
            couplesDict[fam.husbandId] = fam.wifeId

    for person in people:
        if person.id in couplesDict.keys():
            if person.alive is not True:
                couplesDict.pop(person.id)

    for person in people:
        for key in couplesDict:
            if person.id is couplesDict[key]:
                if person.alive is not True:
                    couplesDict.pop(person.id)

    for person in people:
        if person.id in couplesDict.keys():
            livingMarried.append(person)
        if person.id in couplesDict.values():
            livingMarried.append(person)

    return livingMarried



#End of US 30



#US 33 List orphans

#End of US 33
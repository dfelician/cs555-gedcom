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

def isBirthBeforeParentsDeath():
    errorStrings = []
    families = data.familyData()
    people = data.personData()

    personDict = {}
    for person in people:
        personDict[person.id] = person

    for fam in families: 
        childrenIds = fam.childrenIds
        childrenProfiles = []
        husband = "NA"
        wife = "NA"
        for id in childrenIds:
            childrenProfiles.append(personDict[id])
        husband = personDict[fam.husbandId]
        wife = personDict[fam.wifeId]
        for child in childrenProfiles:
            if wife.death != "NA" and child.birthday > wife.death:
                output = "Error: FAMILY: US09: Birth date of " + str(child.name) + "(" + str(child.id) + ") occurs before the death date of mother (" + str(wife.id) + ")"
                errorStrings.append(output)
            if husband.death != "NA":
                num_months = (child.birthday.year - husband.death.year) * 12 + (child.birthday.month - husband.death.month)
                if num_months > 9:
                    output = "Error: FAMILY: US09: Birth date of " + str(child.name) + "(" + str(child.id) + ") occurs more than 9 months after the death date of father (" + str(husband.id) + ")"
                    errorStrings.append(output)
    return errorStrings

def isSibilingSpacing():
    errorStrings = []
    families = data.familyData()
    people = data.personData()
    personDict = {}

    for person in people:
        personDict[person.id] = person
    for fam in families:
        childrenIds = fam.childrenIds
        childrenProfiles = []

        for id in childrenIds:
            childrenProfiles.append(personDict[id])
        if len(childrenProfiles) > 1:
            childrenProfiles.sort(key=lambda x: x.birthday)
            for index in range(1, len(childrenProfiles)):
                if childrenProfiles[index-1].birthday.year == childrenProfiles[index].birthday.year:
                    if abs(childrenProfiles[index-1].birthday.month - childrenProfiles[index].birthday.month) < 8 and abs((childrenProfiles[index-1].birthday - childrenProfiles[index].birthday).days) > 2:
                        output = "Error: FAMILY: US13: Birth date of " + str(childrenProfiles[index-1].name) + "(" + str(childrenProfiles[index-1].id) + ") is less than 8 months and more than 2 days apart from " + str(childrenProfiles[index].name) + "(" + str(childrenProfiles[index].name) + ")"
                        errorStrings.append(output)

                else:
                    if (12 * abs(childrenProfiles[index-1].birthday.year - childrenProfiles[index].birthday.year)) + childrenProfiles[index-1].birthday.month - childrenProfiles[index].birthday.month < 8 and abs((childrenProfiles[index-1].birthday - childrenProfiles[index].birthday).days) > 2:
                        output = "Error: FAMILY: US13: Birth date of " + str(childrenProfiles[index-1].name) + "(" + str(childrenProfiles[index-1].id) + ") is less than 8 months and more than 2 days apart from " + str(childrenProfiles[index].name) + "(" + str(childrenProfiles[index].name) + ")"
                        errorStrings.append(output)

    return errorStrings

def nonDescendentMarriage():
    errorStrings = []
    families = data.familyData()
    childDict = {}

    for fam in families:
        childrenIds = fam.childrenIds
        husbandId = fam.husbandId
        wifeId = fam.wifeId
        if husbandId in childDict:
            for childId in childrenIds:
                if childId not in childDict[husbandId]:
                    childDict[husbandId].append(childId)
        else:
            childDict[husbandId] = childrenIds

        if wifeId in childDict:
            for childId in childrenIds:
                if childId not in childDict[wifeId]:
                    childDict[wifeId].append(childId)
        else:
            childDict[wifeId] = childrenIds
    
    for fam in families:
        husbandId = fam.husbandId
        wifeId = fam.wifeId
        if husbandId in childDict[husbandId] or husbandId in childDict[wifeId] or wifeId in childDict[wifeId] or wifeId in childDict[husbandId]:
            output = "Error: FAMILY: US17: Spouse cannot be a descendent of the family."
            errorStrings.append(output)
        
    return errorStrings

def isUniqueFamilyBySpouse():
    errorStrings = []
    families = data.familyData()
    marriageDict = {}
    for fam in families:
        husbandId = fam.husbandId
        wifeId = fam.wifeId
        if fam.married in marriageDict:
            if wifeId in marriageDict[fam.married]:
                output = "Error: FAMILY: US24: Spouse " + str(wifeId) + " can not be in multiple families with the same marriage date."
                errorStrings.append(output)
            if husbandId in marriageDict[fam.married]:
                output = "Error: FAMILY: US24: Spouse " + str(husbandId) + " can not be in multiple families with the same marriage date."
                errorStrings.append(output)
        else:
            marriageDict[fam.married] = []
        marriageDict[fam.married].append(husbandId)
        marriageDict[fam.married].append(wifeId)
        
    return errorStrings

def isMultipleBirth():
    families = data.familyData()
    people = data.personData()
    personDict = {}
    birthdayDict = {}
    multipleBirthList = []

    for person in people:
        personDict[person.id] = person
    for fam in families:
        childrenIds = fam.childrenIds
        for id in childrenIds:
            if personDict[id].birthday not in birthdayDict:
                birthdayDict[personDict[id].birthday] = []
                
            birthdayDict[personDict[id].birthday].append(personDict[id])

    for key in birthdayDict:
        if len(birthdayDict[key]) > 1:
            multipleBirthList.extend(birthdayDict[key])

    return multipleBirthList

def isLargeAgeDiff():
    families = data.familyData()
    people = data.personData()
    personDict = {}
    couplesList = []

    for person in people:
        personDict[person.id] = person
    for fam in families:
        husbandId = fam.husbandId
        wifeId = fam.wifeId
        ageGap = personDict[husbandId].birthday - personDict[wifeId].birthday
        if ageGap.days > 730:
            couplesList.append((personDict[husbandId], personDict[wifeId]))
            
    return couplesList
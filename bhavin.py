import data

def isIdUnique():
    errorStrings = []
    peopleDuplicateId = []
    familyDuplicateId = []

    people = data.personData()
    families = data.familyData()

    for i in range(1, len(people)):
        id = people[i-1].id
        if people[i].id == id:
            peopleDuplicateId.append(people[i].id)
            errorId = str(people[i].id)
            errorId = errorId.replace("\n", "")
            output = "Error: INDIVIDUAL: US22: " + errorId + " is not a unique ID"
            errorStrings.append(output)
            print("Not unique")

    for i in range(1, len(families)):
        id = families[i-1].id
        if families[i].id == id:
            familyDuplicateId.append(families[i].id)
            errorId = str(people[i].id)
            errorId = errorId.replace("\n", "")
            output = "Error: FAMILY: US22: " + errorId + " is not a unique ID"
            errorStrings.append(output)

    return errorStrings

def getDeaths():
    people = data.personData()
    death = []

    for person in people:
        if person.alive != True:
            death.append(person)

    
    return death


#US 06

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

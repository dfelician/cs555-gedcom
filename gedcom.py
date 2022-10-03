#CSS-555 Group 2
#GEDCOM data
from prettytable import PrettyTable
from datetime import date, datetime


def gedcomData():
    inputFile = open("gedcom-test.ged", "r")
    gedcom = inputFile.readlines()
    inputFile.close()
    out = open("output.txt", "w")
    validTags = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]

    for line in gedcom:
        x = line.split()
        if len(x) == 2:
            isValid = x[1] in validTags
            if isValid == True:
                out.write(x[0] + "|" + x[1] + "|" + "Y" + "\n")
            else:
                out.write(x[0] + "|" + x[1] + "|" + "N" + "\n")
        elif "@" in x[1]:
            isValid = x[2] in validTags
            if isValid == True:
                out.write(x[0] + "|" + x[2] + "|" + "Y" + "|" + x[1] + "\n")
            else:
                out.write(x[0] + "|" + x[2] + "|" + "N" + "|" + x[1] + "\n")
        else:
            isValid = x[1] in validTags
            if isValid == True:
                out.write(x[0] + "|" + x[1] + "|" + "Y" + "|" + ' '.join(x[2:]) + "\n")
            else:
                out.write(x[0] + "|" + x[1] + "|" + "N" + "|" + ' '.join(x[2:]) + "\n")
    out.close()


class Person:
    def __init__(self, id, name, gender, birthday, age, alive, death, child, spouse):
        self.id = id
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.age = age
        self.alive = alive
        self.death = death
        self.child = child
        self.spouse = spouse

class Family:
    def __init__(self, id, married, divorced, husbandId, husband, wifeId, wife, childrenIds):
        self.id = id
        self.married = married
        self.divorced = divorced
        self.husbandId = husbandId
        self.husband = husband
        self.wifeId = wifeId
        self.wife = wife
        self.childrenIds = childrenIds


def personData():
    inputFile = open("output.txt", "r")
    gedcom = inputFile.readlines()
    inputFile.close()
    people = []
    lineNum = 0
    for line in gedcom:
        x = line.split("|")
        if x[1] == "INDI":
            people.append(Person(x[3], "", "", "", 0, True, "NA", [], []))
        elif x[1] == "NAME" and x[0] == "1":
            people[-1].name = x[3]
        elif x[1] == "BIRT":
            birthdate = gedcom[lineNum + 1].split("|")[3].strip()
            toDate = datetime.strptime(birthdate, "%d %b %Y").date()
            people[-1].birthday = toDate
            people[-1].age = getAge(people[-1].birthday)
        elif x[1] == "DEAT":
            people[-1].alive = False
            deathDate = gedcom[lineNum + 1].split("|")[3].strip()
            toDate = datetime.strptime(deathDate, "%d %b %Y").date()
            people[-1].death = toDate
        elif x[1] == "SEX":
            people[-1].gender = x[3]
        lineNum += 1
    return people

def getAge(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def familyData():
    inputFile = open("output.txt", "r")
    gedcom = inputFile.readlines()
    inputFile.close()
    family = []
    lineNum = 0
    for line in gedcom:
        x = line.split("|")
        if x[1] == "FAM":
            family.append(Family(x[3], "NA", "NA", "", "", "", "", []))

    return family

gedcomData()
people = personData()

x = PrettyTable()
x.field_names=["ID", "NAME", "GENDER", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
for person in people:
    x.add_row([person.id, person.name, person.gender, person.birthday, person.age, person.alive, person.death, person.child, person.spouse])
print("Individuals")
print(x)

y = PrettyTable()
y.field_names["ID", "MARRIED", "DIVORCED", "HUSBAND-ID", "WIFE-ID", "WIFE-NAME", "CHILDREN"]
print("familIES")
print(y)
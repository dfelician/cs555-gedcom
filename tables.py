from prettytable import PrettyTable
import data
import david
import bhavin


def individualsTable():
    people = data.personData()
    x = PrettyTable()
    x.title = "Individuals"
    x.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for person in people:
        if len(person.spouse) == 0:
            person.spouse = "NA"
        if len(person.child) == 0:
            person.child = "NA"
        x.add_row([person.id, person.name, person.gender, person.birthday, person.age, person.alive, person.death,
                   person.child, person.spouse])
    return x


def familiesTable():
    families = data.familyData()
    people = data.personData()
    y = PrettyTable()
    y.title = "Families"
    y.field_names = ["ID", "MARRIED", "DIVORCED", "HUSBAND ID", "HUSBAND NAME", "WIFE ID", "WIFE NAME", "CHILDREN"]
    for family in families:
        if len(family.childrenIds) == 0:
            family.childrenIds = "NA"
        for person in people:
            if family.husbandId == person.id:
                family.husband = person.name
            if family.wifeId == person.id:
                family.wife = person.name

        y.add_row(
            [family.id, family.married, family.divorced, family.husbandId, family.husband, family.wifeId, family.wife,
             family.childrenIds])

    return y


# US 35
def recentBirthsTable():
    recentBirths = david.getRecentBirths()
    z = PrettyTable()
    z.title = "Recent Births"
    z.field_names = ["ID", "Name", "Birthday"]
    for person in recentBirths:
        z.add_row([person.id, person.name, person.birthday])
    return z
# End of US 35


def deathTable():
    # people = data.personData()
    deaths = bhavin.getDeaths()
    deathTable = PrettyTable()
    deathTable.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for person in deaths:
        if len(person.spouse) == 0:
            person.spouse = "NA"
        if len(person.child) == 0:
            person.child = "NA"
        deathTable.add_row([person.id, person.name, person.gender, person.birthday, person.age, person.alive, person.death, person.child, person.spouse])
    return deathTable

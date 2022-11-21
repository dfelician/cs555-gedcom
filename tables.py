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
    recentBirthsPTable = PrettyTable()
    recentBirthsPTable.title = "Recent Births - US 35"
    recentBirthsPTable.field_names = ["ID", "Name", "Birthday"]
    for person in recentBirths:
        recentBirthsPTable.add_row([person.id, person.name, person.birthday])
    return recentBirthsPTable
# End of US 35


def deathTable():
    # people = data.personData()
    deaths = bhavin.getDeaths()
    deathPrettyTable = PrettyTable()
    deathPrettyTable.title = "Deceased - US29"
    deathPrettyTable.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for person in deaths:
        if len(person.spouse) == 0:
            person.spouse = "NA"
        if len(person.child) == 0:
            person.child = "NA"
        deathPrettyTable.add_row([person.id, person.name, person.gender, person.birthday, person.age, person.alive, person.death, person.child, person.spouse])
    return deathPrettyTable


def livingSingleTable():
    livingSingle = david.getLivingSingle()
    singleTable = PrettyTable()
    singleTable.title = "Living Single - US 31"
    singleTable.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for person in livingSingle:
        if len(person.spouse) == 0:
            person.spouse = "NA"
        if len(person.child) == 0:
            person.child = "NA"
        singleTable.add_row([person.id, person.name, person.gender, person.birthday, person.age, person.alive, person.death, person.child, person.spouse])
    return singleTable


def recentDeathsTable():
    recentDeaths = david.getRecentDeaths()
    recentDeathsTble = PrettyTable()
    recentDeathsTble.title = "Recent Deaths - US 36"
    recentDeathsTble.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for person in recentDeaths:
        if len(person.spouse) == 0:
            person.spouse = "NA"
        if len(person.child) == 0:
            person.child = "NA"
        recentDeathsTble.add_row([person.id, person.name, person.gender, person.birthday, person.age, person.alive, person.death, person.child, person.spouse])
    return recentDeathsTble


def orderedSiblingsTable():
    siblings = david.orderSiblingsByAge()
    siblingsTables = []
    for key, value in siblings.items():
        table = PrettyTable()
        table.title = key + " - Ordered Siblings"
        table.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
        if value:
            for person in value:
                if len(person.spouse) == 0:
                    person.spouse = "NA"
                if len(person.child) == 0:
                    person.child = "NA"
                table.add_row(
                    [person.id, person.name, person.gender, person.birthday, person.age, person.alive, person.death,
                     person.child, person.spouse])
            siblingsTables.append(table)
    return siblingsTables


def listLivingMarriedCouples():
    livingMarriedCouples = bhavin.livingMarriedCouples()
    livingMarriedCouplesTable = PrettyTable()
    livingMarriedCouplesTable.title = "Living Married Couples - US30"
    livingMarriedCouplesTable.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]

    for person in livingMarriedCouples:
        if len(person.spouse) == 0:
            person.spouse = "NA"
        if len(person.child) == 0:
            person.child = "NA"
        livingMarriedCouplesTable.add_row([person.id, person.name, person.gender, person.birthday, person.age, person.alive, person.death, person.child, person.spouse])
    return livingMarriedCouplesTable


def listOrphans():
    orphans = bhavin.orphans()
    orphansTable = PrettyTable()
    orphansTable.title = "Orphans - US 33"
    orphansTable.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for person in orphans:
        if len(person.spouse) == 0:
            person.spouse = "NA"
        if len(person.child) == 0:
            person.child = "NA"
        orphansTable.add_row([person.id, person.name, person.gender, person.birthday, person.age, person.alive, person.death, person.child, person.spouse])
    return orphansTable
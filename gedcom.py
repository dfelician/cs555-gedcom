# CSS-555 Group 2
# GEDCOM data
import data
import errorData
import tables


def main():
    data.gedcomData()
    print(tables.individualsTable())
    print(tables.familiesTable())
    print(tables.deathTable())
#    print(tables.recentBirthsTable())

    errors = errorData.errorData()
    # output the list of error strings below here
    for error in errors:
        print(error)

    x = tables.individualsTable()
    y = tables.familiesTable()
    out = open("tables.txt", "w")
    out.write(str(x) + "\n" + str(y))
    out.close()

    z = tables.recentBirthsTable()
    out = open("recentBirths.txt", "w")
    out.write(str(z))
    out.close()

    deathTable = tables.deathTable()
    out = open("deathsTable.txt", "w")
    out.write(str(deathTable))
    out.close()

    singlesTable = tables.livingSingleTable()
    out = open("livingSingleTable.txt", "w")
    out.write(str(singlesTable))
    out.close()

    recentDeathsTable = tables.recentDeathsTable()
    out = open("recentDeaths.txt", "w")
    out.write(str(recentDeathsTable))
    out.close()

    siblingsTable = tables.orderedSiblingsTable()
    out = open("orderedSiblingsTable.txt", "w")
    for table in siblingsTable:
        out.write(str(table) + "\n")
    out.close()

    multiBirthTable = tables.listMultipleBirth()
    out = open("multipleBirthsTable.txt", "w")
    out.write(str(multiBirthTable))
    out.close()

    largeAgeGapTable = tables.listLargeAgeGap()
    out = open("largeAgeGapTable.txt", "w")
    out.write(str(largeAgeGapTable))
    out.close()


if __name__ == "__main__":
    main()


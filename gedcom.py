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

    errors = errorData.errorData()
    # output the list of error strings below here
    for error in errors:
        print(error)

    x = tables.individualsTable()
    y = tables.familiesTable()
    deathTable = tables.deathTable()
    out = open("tables.txt", "w")
    out.write("Individuals\n" + str(x) + "\nFamilies\n" + str(y) + "\nDeaths - US 29\n" + str(deathTable))
    out.close()


if __name__ == "__main__":
    main()


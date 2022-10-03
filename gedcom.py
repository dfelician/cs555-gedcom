#CSS-555 Group 2
#GEDCOM data
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

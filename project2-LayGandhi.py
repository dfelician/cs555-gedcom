#hardcoded set of valid tags from project instuctions
validTags = [
    'INDI',
    'NAME',
    'SEX',
    'BIRT',
    'DEAT',
    'FAMC',
    'FAM',
    'MARR',
    'HUSB',
    'WIFE',
    'CHIL',
    'DIV',
    'DATE',
    'HEAD',
    'TRLE',
    'NOTE'
    ]

def isTagValid(tag): #check if tag is valid based on project instuctions
    if tag in validTags:
        return 'Y'
    return 'N'

def formatOutputLine(line): #method to format the output of each line
    
    parameterList = line.split()
    #print(parameterList)
    level = parameterList[0]
    if len(parameterList) > 2: #for lines greater then 2
        if parameterList[2] == 'INDI' or parameterList[2] == 'FAM': #special condition for INDI and FAM
            tag = parameterList[2]
            arguments = parameterList[1]
        else: #set tag and arguments
            tag = parameterList[1]
            arguments = parameterList[2:]
    else: #when line length is only 2
        tag = parameterList[1]
        arguments = []

    valid = isTagValid(tag)

    #grab all arguments that are not level and tag to display
    information = ""
    for args in arguments:
        information += args + ' '

    print('<- ' + level + '|' + tag + '|' + valid + '|' + information)
    print()



with open('Lay Gandhi Family.ged') as fp:
    for line in fp:
        print('-> ' + line, end='')
        formatOutputLine(line)
from datetime import date


# US27
def getAge(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def getDeathAge(deathdate, birthdate):
    age = deathdate.year - birthdate.year - ((deathdate.month, deathdate.day) < (birthdate.month, birthdate.day))
    return age

# End of US27

def getTimeDifference(endDate, startDate):
    diff = endDate.year - startDate.year - ((endDate.month, endDate.day) < (startDate.month, startDate.day))
    return diff
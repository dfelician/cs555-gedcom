import lay
import bhavin
import albert


def errorData():
    # create a list of errored strings
    allErrors = []

    # use methods to add onto the list of error strings
    # US01
    allErrors.extend(lay.isDateValid())
    # US10
    allErrors.extend(lay.isMarriageAfter14())

    allErrors.extend(bhavin.isIdUnique())

    allErrors.extend(albert.isMarriedBeforeDivorce())

    allErrors.extend(albert.isBirthBeforeMarriage())
    #US09
    allErrors.extend(albert.isBirthBeforeParentsDeath())
    #US13
    allErrors.extend(albert.isSibilingSpacing())
    #US06
    allErrors.extend(bhavin.divorceBeforeDeath())
    #US14
    allErrors.extend(lay.multipleBirths())
    #US05
    allErrors.extend(bhavin.marriageBeforeDeath())
    
    #US12
    allErrors.extend(lay.isParentsOld())

    return allErrors

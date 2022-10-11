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

    return allErrors

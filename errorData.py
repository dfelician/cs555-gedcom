import lay
import bhavin
import albert
import david


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
    #US17
    allErrors.extend(albert.nonDescendentMarriage())
    #US24
    allErrors.extend(albert.isUniqueFamilyBySpouse())
    #US06
    allErrors.extend(bhavin.divorceBeforeDeath())
    #US14
    allErrors.extend(lay.multipleBirths())
    #US05
    allErrors.extend(bhavin.marriageBeforeDeath())
    
    #US12
    allErrors.extend(lay.isParentsOld())
    #US16
    allErrors.extend(lay.sameLastNameMale())
    #US21
    allErrors.extend(lay.correctGenderRole())

    #US15
    allErrors.extend(bhavin.lessThan15Siblings())
    #US18
    allErrors.extend(bhavin.siblingsShouldNotMarry())

    #US07
    allErrors.extend(david.lessThen150())

    #US23
    allErrors.extend(lay.uniqueNameBirth())
    #US25
    allErrors.extend(lay.uniqueFirstNameInFamily())

    return allErrors

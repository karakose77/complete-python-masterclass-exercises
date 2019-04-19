def clean_number(numberString):
    """
    Cleans non-numeric characters from entered string and converts and returns the new number.
    """
    cleanedNumberString = ''

    for char in numberString:
        if char in '0123456789':
            cleanedNumberString = cleanedNumberString + char

    return int(cleanedNumberString)


print(clean_number("9,223,372,036,854,775,807"))

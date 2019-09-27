def clean_number(number_string):
    """
    Cleans non-numeric characters from entered string and converts and returns the new number.
    """
    cleaned_number_string = ''

    for char in number_string:
        if char in '0123456789':
            cleaned_number_string = cleaned_number_string + char

    return int(cleaned_number_string)


print(clean_number("9,223,372,036,854,775,807"))

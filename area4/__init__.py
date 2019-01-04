def initLib():
    dividers = []
    with open("dividers.txt", "r") as fh:
        lines = fh.readlines()
    dividers = "", lines

initLib()


def divider(number: int):
    """
    Gets you the divider you requested!
    
    :param number: the divider number (NOT 0)
    :raises: ValueError
    :return: requested divider
    :rtype: str
    
    :Example:
    area4.divider(97)
    will return 🏖️🏖️🏖️🏖️🏖️🏖️🏖️🏖️🏖️🏖️🏖️🏖️
    """
    
    if number == 0:
        raise ValueError('Please use a number bigger then 0!')
    else:
        return dividers[number]

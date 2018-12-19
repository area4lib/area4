# Area4 Package by RDIL

def check(__name__):
    """
    Tells you if the module is being run directly or being imported
    
    :return: If __name__ is __main__ is true or false
    :rtype: bool
    """
    if __name__ == "__main__":
        return True
    else:
        return False

"""Utilities module."""
#  Copyright (c) 2018 - present RDIL.
#  You should have received a copy of the
# MIT License with this program/distribution.

# area4 package by RDIL
# Utilities module


def check(internal_name):
    """
    Get if the module is being run directly or being imported.

    :return: If __name__ is '__main__' (boolean)
    :rtype: bool
    """
    return internal_name == "__main__"

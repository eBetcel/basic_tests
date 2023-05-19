"""
Program to convert different measurement sacales
"""

def convert_to_cm(measure_in_inches):
    """
    Testes:

    >>> convert_to_cm(1) 
    2.54
    """
    measure_in_cm = measure_in_inches * 2.54

    return measure_in_cm

def convert_to_inches(measure_in_cm):
    """
    Convert a measurement from centimeters to inches.

    >>> convert_to_inches(10)
    3.937007874015748
    >>> convert_to_inches(20)
    7.874015748031496
    >>> convert_to_inches(0)
    0.0
    >>> convert_to_inches(2.54)
    1.0
    """
    measure_in_inches = measure_in_cm / 2.54

    return measure_in_inches

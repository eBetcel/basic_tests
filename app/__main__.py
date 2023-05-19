from .app import convert_to_cm, convert_to_inches

option = input ('Type C to CM\n Type I to inches')

measure = float(input('Insert the measure: '))

match (option):
    case 'C':
        result = convert_to_cm(measure)
        print('The measure is {result} CMs')
    case 'I':
        result = convert_to_inches(measure)
        print('The measure is {result} inches')
    case _:
        print('Type C or F. The value given was wrong!!!')

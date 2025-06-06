#Make a program that read something by the keyboard and show it primitive type and all information about it

something = input('Type something: ')
print('It primitive type is: {}'.format(type(something)))
print('Is it all blank? {}'.format(something.isspace()))
print('Is it alphabetic? {}'.format(something.isalpha()))
print('Is it alphanumeric? {}'.format(something.isalnum()))
print('Is it upper? {}'.format(something.isupper()))
print('Is it lower? {}'.format(something.islower()))
print('Is it capitalized? {}'.format(something.istitle()))
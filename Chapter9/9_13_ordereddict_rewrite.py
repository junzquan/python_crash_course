from collections import OrderedDict

glossary = {
    'Python': 'A beautiful programming language.',
    'Loop': 'A loop can do something repeatly.',
    'List': 'A list can store a group of data.',
    'If-elif-else': 'If statement can examine the current state of a program and respone to that state.',
    'Data_type': 'Data type means different types of date, such as integer and string.',
    'Dictionary': 'A container that contain key-value pairs.',
    'Set': 'A set is like a list, but a set does not contain duplicate items.',
}

for key, value in glossary.items():
    print(key + ": " + value)


print("\n")
glossary = OrderedDict()
glossary['Python'] = "A beautiful programming language."
glossary['Loop'] = "A loop can do something repeatly."
glossary['List'] = "A list can store a group of data."
glossary['If-elif-else'] = "If statement can examine the current state of a program and respone to that state."
glossary['Data_type'] = "Data type means different types of date, such as integer and string."
glossary['Dictionary'] = "A container that contain key-value pairs."
glossary['Set'] = "A set is like a list, but a set does not contain duplicate items."

for key, value in glossary.items():
    print(key + ": " + value)
    
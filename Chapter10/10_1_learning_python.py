
filename = 'learning_python.txt'
with open(filename) as file_object:
    content = file_object.read()
print(f"This is the entire file:\n{content}\n")

with open(filename) as file_object:
    print("This is looping lines:\n")
    for line in file_object:
        print(line)
    print("\n")

with open(filename) as file_object:
    lines = file_object.readlines()
print("These are lines in a list:\n")
print(lines)

def classify(myclass):
    names = []
    for key, value in myclass.items():
        if value == 'cpeg':
            names.append(key)
            
    return names

myclass = {}


x = input("Enter student's name: ")
y = input("Enter student's major: ")

while x != "end":
    myclass[x]=y
    x = input("Enter student's name: ")
    y = input("Enter student's major: ")

names = classify(myclass)
print("The enrolled students are:")
print(myclass)
print("The CPEG students are:")
print(names)

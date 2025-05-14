name = "Farhan Raditya Al Gazali"
major = "Computer Technology Engineer"
studiProgram = "TRK 2B"
college = "Samarinda State Polytechnique"

print("What do you want to know about me? like name, major, studi program, or my college.")

userChoices = str(input("Write your answer here -> "))

userChoices.lower

if userChoices == 'name':
    print(f"My name is {name}, nice to meet you!.")
elif userChoices == 'major':
    print(f"I'm {major}, it's cool right!.")
elif userChoices == 'studi program' or userChoices == 'prodi':
    print(f"My studi program is {studiProgram}, we learn everything about computer.")
elif userChoices == 'college':
    print(f"I study at {college} it was in Samarinda, it's quite far from my hometown.")
else:
    print(f"I can't answer that question for now, but here's all the information about me...")
    print(f"Name: {name}")
    print(f"Major: {major}")
    print(f"Studi Program: {studiProgram}")
    print(f"College: {college}")
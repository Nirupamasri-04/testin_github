name = input("enter the name")
age = int(input("enter the age"))
height = float(input("enter the height"))
is_student = True
month = age*12
days = age*365
division = age%7
square = age**2
print(name, age, height, is_student)
print("Name: ", name, "Age: ", age, "Height: ", height, "Student: ", is_student)
print("Age in months:", month,"Age in days: ", days, "Remainder when age is divided by 7: ", division,"Age raised to the power of 2: ", square)
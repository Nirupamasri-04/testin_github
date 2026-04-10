#age = int(input("Enter thr age"))
#if age>=60:
#    print("Eligilble for Senior Citizen")
#elif age<12:
#    print("Eligible for Children Qota")
#else:
#    print("Not eligible")
#num = int(input("eneter a number"))
#if num%2==0:
#    print("number is even")
#else:
#    print("number is odd")
#marks = int(input("enter the marks"))
#if marks>=90:
#    print("Grade A")
#elif marks>=75:
#    print("Grade B")
#elif marks>=50:
#    print("Grade C")
#else:
#    print("Fail")
#year = int(input("enter the year"))
#if (year%4 == 0 and year%100 !=0) or (year%400 ==0):
#    print("Leap year")
#else:
#    print("Not leap year")
#
# num =int(input("enter a number"))
# if (num%2 == 0) and (num%3 == 0):
#    print("Two and Three")
#if num%2 == 0:
#    print("Two")
#elif num%3 == 0:
#    print("Three")
#else:
#    print("Not divisible by 2 or 3")
#num = int(input("enter a number"))
#if (num%2 == 0) and (num%3 ==0):
#    print("Divisible by both")
#elif (num%2 == 0) or (num%3 == 0): 
#    print("Divisible by 2 or 3")
#else:
#    print("Not divisible")
#num =int(input("enter a nnumber"))
#if (num%2 == 0) and (num%3 == 0):
#    print("Divisible by both")
#elif num%2 == 0:
#    print("Divisible by 2")
#elif num%3 == 0:
#    print("Divisible by 3")
#else:
#    print("Not divisible")
#num =int(input("enter a number"))
#if (num%7 == 0) and (num%11 == 0):
#    print("Multiple of both")
#elif num%7 == 0:
#    print("Multiple of 7")
#elif num%11 == 0:
#    print("Multiple of 11")
#else:
#    print("Not a multiple of 7 or 11")
#age = int(input("enter the age"))
#salary = int(input("enter the salary"))
#if (age>=21) and (salary>=25000):
#    print("Eligible for loan")
#else:
#    if age<21:  
#        print("Too yooung")
#    if salary<25000:
#        print("Low salary")
#account_balance = int(input("enter the balance"))
#withdrawal_amount = int(input("enter the amount"))
#if withdrawal_amount > account_balance:
#    print("Insufficient balance")
#elif withdrawal_amount%100 != 0:
#    print("enter withdrawal_amount in multiples of 100")
#else:
#    print("Transaction successful")
user_name = input("Enter the username: ")
if user_name != "admin":
    print("Invalid username")
else:
    for i in range(3):
        print("Attempt", i + 1)
        password = input("Enter the password: ")

        if password == "1234":
            print("Login successful")
            break
        else:
            print("Incorrect password")
    else:
        print("Account locked")
'''age = int(input("Enter your age: "))
attendance = float(input("Enter your attendance (percentage): "))
score = float(input("Enter your score: "))

coursework_status = input("Completed required coursework(yes or no): ").lower()
disciplinary_issue = input("Do you have any outstanding disciplinary issue (yes or no): ").lower()

if disciplinary_issue == "yes":
    print("disqualified")
elif age < 16 or attendance < 75 or coursework_status == "no":
    print("Not Eligible!")
elif score >= 70:
    print("Eligible - Distinction")
elif score >= 60:
    print("Eligible - Merit")
elif score >= 50:
    print("Eligible - Pass")
else:
    print("Eligible - Assessment Required")'''

'''number = 1

while number <= 10:
    print(number)
    number = number + 1'''

'''attempts = 0

while attempts < 3:

   password =input("Enter password: ")

   if password == "python123":
       print("Login successful")
       break 
   
   else:
       print("Incorrect password")
       attempts = attempts + 1

if attempts == 3:
    print("Account locked")'''


score = -1

while score < 0 or score > 100:

    score = int(input("Enter your score: "))
    if score < 0 or score > 100:
        print("Invalid score. Try again.")

if score >= 70:
        print("Distinction")
elif score >= 60:
        print("Merit")
elif score >= 50:
        print("Pass")
else:
        print("Fail")




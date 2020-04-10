# name :- vinayak parab

# WAP for taking one number as input and using if else statement assign grade
"""
A grade = 85+
B grade = 70+
C grade = 60+
D grade = 50+
E grade = 40+
fail = below 40
"""
marks = int(input("enter your marks: "))
if 100 >= marks >= 85:
    print("your marks is "+ str(marks) +" you got A grade")
elif 85 > marks >= 70:
    print("your marks is "+ str(marks) +" you got B grade")
elif 70 > marks >= 60:
    print("your marks is "+ str(marks) +" you got C grade")
elif 60 > marks >= 50:
    print("your marks is "+ str(marks) +" you got D grade")
elif 50 > marks >= 40:
    print("your marks is "+ str(marks) +" you got E grade")
else:
    print("your marks is " + str(marks) + "." + "Thats less then expected. Try again later.")



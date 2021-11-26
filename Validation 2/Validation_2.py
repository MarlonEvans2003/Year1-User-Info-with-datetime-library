import re
import datetime 
from datetime import date

def Firstname():
    FirstValidation = True
    while FirstValidation == True:
        First = str(input("Please enter your first name: "))
        if First == "":
            print("Cannot leave blank")
        if len(First) > 2 and len(First) < 20:
            return First
            FirstValidation = False
        else:
            print("please enter a name between 2 and 20 characters long")
    
def Secondname():            
    SecondValidation = True
    while SecondValidation == True:
        Second = str(input("Please enter your second name: "))
        if Second == "":
            print("Cannot leave blank")
        if len(Second) > 2 and len(First) < 20:
            return Second
            SecondValidation = False
        else:
            print("please enter a second name between 2 and 20 characters long")


def ContactNumber():
    FirstValidation = True
    while FirstValidation == True:
        Num = input("Please enter your number: ")
        if Num == "":
            print("Cannot leave blank")
        if Num.isalpha():
            print("please enter only numerical values ")
        elif len(Num) < 1 and len(Num) > 11:
            FirstValidation = True
        else:
            FirstValidation = False
    return Num

def Email():
    FirstValidation = True
    while FirstValidation == True:
        email = input("Please enter your Email: ")
        if email == "":
            print("Cannot leave blank")
        elif "@" not in email or "." not in email:
            print("invalid email, please try again")
        else:
            FirstValidation = False
            return email


def dateofpass():
    theorydate = input("When did you pass your theory test? Please enter date like this DD/MM/YYYY: ")
    invaliddate = True
    while invaliddate == True:
        try:
            formatdate = datetime.datetime.strptime(theorydate, "%d/%m/%Y")
            invaliddate = False
            return formatdate
            break
        except ValueError:
            print("The date needs to be in format like this - DD/MM/YYYY Try Again")
            invaliddate = True
            theorydate = input("When did you pass your Theory Test: ")
        #now we know that the date is valid
        #


def DateofBirth():
    DOB = input("Please enter your date of birth Please enter date like this DD/MM/YYYY: ")
    invaliddate = True
    while invaliddate == True:
        try:
            DOB = datetime.datetime.strptime(DOB, "%d/%m/%Y")
            invaliddate = False
            return DOB
            break
        except ValueError:
            print("The date needs to be in format like this - DD/MM/YYYY Try Again")
            invaliddate = True
            theorydate = input("When did you pass your Theory Test: ")
        #now we know that the date is valid
#
#
# Main Menu
#
#
#

First = Firstname()
Second = Secondname()
Number = ContactNumber()
Mail = Email()
TheoryDate = dateofpass()
while True:
    TheoryDateYear = TheoryDate.year
    TheoryDateMonth = TheoryDate.month
    TheoryDateDay = TheoryDate.day
    TheoryDate1 = date(TheoryDateYear, TheoryDateMonth, TheoryDateDay)
    today = date.today()
    TodayYear = today.year
    TodayMonth = today.month
    TodayDay = today.day
    TodayDate1 = date(TodayYear, TodayMonth, TodayDay)
    delta = TodayDate1 - TheoryDate1
    if delta.days <= (365 * 2):
        break
    else:
        print("Make sure it is within the last 2 years")
        TheoryDate = dateofpass()
                 
DOB = DateofBirth()
while True:
        DateofBirthYear = DOB.year
        DateofBirthMonth = DOB.month
        DateofBirthDay = DOB.day
        DateofBirth1 = date(DateofBirthYear, DateofBirthMonth, DateofBirthDay)
        today = date.today()
        TodayYear = today.year
        TodayMonth = today.month
        TodayDay = today.day
        TodayDate1 = date(TodayYear, TodayMonth, TodayDay)
        delta = TodayDate1 - DateofBirth1
        if delta.days >= (365 * 17):
            break
        else:
            print("You have to be 17 or older to enter in for this. Try again")
            DOB = DateofBirth()
#

print("")
print("")
print("")
print("Users Detail: ")
print(First + " " + Second)
print(Number)
print(Mail)
print(TheoryDate)
print (DOB)
print("All credentials valid. Please proceed to date selection for your practical driving test.")
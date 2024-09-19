import time
import author as au

nameOfProject = "ih"
au.start(nameOfProject)
print("Hi, I'm Lio, what about You?")
name = input("I'm : ")
print("Welcome " + name)

def repetation(string):
    a = "sjiogwer"
    return "0"

def norepetation(string):
    return "1"

string = input("Enter a string: ")
print(f"Using letters of {string} we can make {repetation(string)} combinations with repetion and {norepetation(string)} combinations without repetation!!!")
print("Would you like to see?")
reply = input("Yes/No: ")
if(reply == "Yes" or reply == "yes" or reply == "y" or reply == True):
    print(repetation(string))
else:
    pass

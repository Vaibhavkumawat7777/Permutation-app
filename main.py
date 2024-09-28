from collections import defaultdict
import author as au

nameOfProject = "ih"
au.start(nameOfProject)
print("Hi, I'm Lio, what about You?")
name = input("I'm : ")
print("Welcome " + name)

def factorial(fac):
    if fac == 0 or fac == 1:
        return 1
    elif fac < 0:
        return "not define"
    else:
        product = 1
        while fac > 0:
            product = product*fac
            fac -= 1
        return product
    
    
def repetation(string):
    listOfString = [i for i in string]
    return len(listOfString)*len(listOfString)

def norepetation(string):
    listOfString = [i for i in string]
    letter_count = defaultdict(int)
    for i in listOfString:
        for char in i:
            letter_count[char] += 1
    result = dict(letter_count)
    product = 1
    print(result.values())
    for key in result.keys():
        product = product*factorial(result[key])
    return (factorial(len(listOfString)))/product        


string = input("Enter a string: ")
print(f"Using letters of {string} \nWe can make {repetation(string)} combinations with repetion \n{norepetation(string)} combinations without repetation!!!")
print("Would you like to see?")
reply = input("Yes/No: ")
if(reply == "Yes" or reply == "yes" or reply == "y" or reply == True):
    print("Programm comming soon")
else:
    au.end()
#Tam Hoang
# July 13 2018
#Having a secure password is a very important practice,when much of our information is stored online.
#Write a program that validates a new password, following these rules:
#• The password must be at least 8 characters long.
#• The password must have at least one upper case and one lowercase letter. 
#• The password must have at least one digit.
#Write a program that asks for a password, then asks again to confirm it. If the passwords don’t match or the rules are not fulfilled,
#prompt again. Your program should include a function that checks whether a password is valid.

from math import*

def inputPassword():
    print("Enter a password with the following rules:\n"
          "The password must be at least 8 characters long.\n"
          "The password must have at least one upper case and one lowercase letter.\n"
          "The password must have at least one digit.")
    
    password = input("Enter a password: ")
    password1 = input("Confirm Password: ")
    return (password, password1)

def checkForValidPassword(pass1, pass2):
    uppercaseCounter = 0
    lowercaseCounter = 0
    digitCounter = 0
    for i in range(len(pass1)):
        if(pass1[i].isupper()):
            uppercaseCounter += 1
        elif(pass1[i].islower()):
            lowercaseCounter += 1
        elif(pass1[i].isdigit()):
            digitCounter += 1
        
    if(pass1 != pass2):
        return 1
    elif(len(pass1) < 8):
        return 2
    elif(uppercaseCounter < 1 or lowercaseCounter < 1):
        return 3
    elif(digitCounter < 1):
        return 4
    return 5


boolval = 1
while(boolval):
    (password,confirmPassword) = inputPassword()   
    result = checkForValidPassword(password, confirmPassword)    
    if(result == 1):
        print("The password doesn't match.\n")
    elif(result == 2):
        print("The password is not 8 character long.\n")
    elif(result == 3):
        print("The password need to be at least 1 uppercase and lower case.\n")
    elif(result == 4):
        print("The password need to have at least 1 digit.\n")
    else:
        print("The password is valid.")
        boolval = 0

import string
from random import randint
import pyperclip



ascii_letters = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation


lengthPassword = int(input("How many characters should the password be?: "))
wantNumbers = input("Would you like to have numbers in the password? (Y/N): ")
wantLetters = input("Would you like to have letters in the password? (Y/N): ")
wantPunctuation = input("Would you like to have punctuation in the password? (Y/N): ")
len_ascii_letters = len(ascii_letters)
len_numbers = len(numbers)
len_punctuation = len(punctuation)

password = ""

def generate_password():
    password = ""

    i = 0
    while i < lengthPassword:
    
        if wantNumbers.lower() == 'y':
            password += numbers[randint(0,len_numbers -1)]
            if len(password) == lengthPassword:
                break

        if wantLetters.lower() == "y":
            password += ascii_letters[randint(0,len_ascii_letters-1)]
            if len(password) == lengthPassword:
                break

        if wantPunctuation.lower() == "y":
            password += punctuation[randint(0,len_punctuation)-1]
            if len(password) == lengthPassword:
                break


        i+=1

    return password

getPassword = generate_password()

print("Password Generated: {}".format(getPassword))

copy_to_clipboard = input("Would you like to copy the password to your clipboard? (Y/N): ")
if copy_to_clipboard.lower() == "y":
    pyperclip.copy(getPassword)
    print("The password has been copied to the clipboard!")







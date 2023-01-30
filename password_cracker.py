from random import *
import os

your_password = input("Enter a password: ")

password = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r", "s", "t", "u", "ü", "v", "w", "x", "y", "z", " ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", ".", "+", "%", "&", "/", "(", ")", "=", "?", "*", "-", "_", ":"]

pw = ""

while(pw != your_password):
    pw = ""
    for letter in range(len(your_password)):
        guess_password = password[randint(0, 17)]
        pw = str(guess_password) + str(pw)
        print(pw)
        print("Cracking the password, please wait ....")
        os.system("cls")

print("Your password is:", your_password)
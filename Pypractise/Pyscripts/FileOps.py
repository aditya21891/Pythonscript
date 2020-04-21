import re
import os
file1 = open("linuxtest.txt","r+")
text = file1.read().strip().split()
print (text)
 #Conditions
while True:
    s = input("Enter a string: ") #Takes input of a string from user
    if s == "": #if no value is entered for the string
        continue
    if s in text: #string in present in the text file
        print("Matched")
        break
    else: #string is absent in the text file
        print("No such string found,try again")
        continue
file1.close()

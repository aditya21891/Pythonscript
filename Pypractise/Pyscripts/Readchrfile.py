# program to read the characters in a file.
from sys import argv
script,filename=argv
txt=open(filename)
print"The name of file is %r:" %filename
print txt.read()
print " Here is the filename %r:" % filename

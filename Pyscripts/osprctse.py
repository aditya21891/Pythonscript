import os
try:
    fd="learnpython.txt"
    file = open(fd, 'w')
    file.write("I enjoy coding Python with a Beer")
    file.write("\n")
    file.write("I love writing python code because it is easy to learn")
    m
    file = open(fd, 'r')
    text = file.read()
    print(text)


except IOError:
    print ('File does not exist' +fname)
    print ('Content does not exist' +fname)

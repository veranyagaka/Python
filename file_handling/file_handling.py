#read from a file in python
file=open('example.txt', 'r')
content=file.read()
print(content)
file.close() #closing the file
#writing to a file
file=open('example.txt','w')
file.write('But vera is sooo cool\n')
file.write('If i had to talk about love, i would tell them about us\n')
#writelines
file.writelines(['Python is kinda cool too\n', 'Allan is a dudu head\n', 'Mommy wants milk'])
file.close()
#name=raw_input('Enter name:')
#open a file syntax: open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None) 
myfile=open('example.txt')
#file objects: in this case file is the file object. Attributes are the name,closed and mode
print(file.name)
print(file.closed)
print(file.mode)
#readlines and readline
file=open('example.txt', 'r')
contents1=file.readline(20)
contents2=file.readlines()
print(contents1)
print(contents2)
file.close()
'''create a file
file=open('example2.txt', 'x')
file.close()
'''
#modify a file: append or write
#writelines

#open file for multiple operations
with open('example2.txt','r+') as file:
    #file.write('Hello Vera') error will occur
    file.write('Hello Vera')
#append
with open('example2.txt','a+') as file:
    #file.write('Hello Vera') error will occur
    file.write('Hello World!!')
#delete files
import os
os.remove()
##context managers syntax with open('path','<mode>') as <var>:  and also automatically closes the file!!!
#example of class and context managers
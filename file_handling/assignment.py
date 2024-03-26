#File Creations
file =open('my_file.txt','w')
file.writelines(['This is the File Handling Assignment\n', 'Week 5\n', 'Check out my GitHub' ])
file.close()
#File Display
file =open('my_file.txt','r')
contents=file.read()
print(contents)
file.close()
#Appending
file =open('my_file.txt','a')
file.writelines(['Python is tight!\n', 'nyagakavera@gmail.com\n', 'Nairobi, Kenya' ])
#Error Handling
try:
    file =open('my_file.txt','r')
    contents=file.read()
    print(contents)
    file.close()
except FileNotFoundError:
    print('File is not Found!!!!')
except PermissionError:
    print('You are denied access to view the file')

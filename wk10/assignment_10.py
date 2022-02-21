'''
This week we will create a program that performs file processing activities.
Your program this week will use the OS library in order to validate that a directory exists before
creating a file in that directory. Your program will prompt the user for the directory they would
like to save the file in as well as the name of the file. The program should then prompt the user
for their name, address, and phone number. Your program will write this data to a comma separated
line in a file and store the file in the directory specified by the user.

Once the data has been written your program should read the file you just wrote to the file system
and display the file contents to the user for validation purposes.

Submit a link to your Github repository.
'''
import csv
import os
FOLDER_PATH = input('please provide folder path: ')
while not os.path.isdir(FOLDER_PATH):
    print(FOLDER_PATH + ' is not a directory.')
    FOLDER_PATH = input('please provide folder path: ')
FILE_NAME = input('please provide file name: ')
USER_NAME = input('please provide your name: ')
USER_ADDRESS = input('please provide your address: ')
USER_PHONE = input('please provide your phone number: ')
with open('/'.join([FOLDER_PATH, FILE_NAME]),
          'w', newline='') as csvfile:
    MY_WRITER = csv.DictWriter(csvfile, fieldnames=['name', 'address', 'phone'])
    MY_WRITER.writeheader()
    MY_WRITER.writerow({'name': USER_NAME, 'address': USER_ADDRESS, 'phone': USER_PHONE})
csvfile.close()
with open('/'.join([FOLDER_PATH, FILE_NAME]), newline='') as f:
    print('')
    for line in f:
        print(line, end='')
f.close()

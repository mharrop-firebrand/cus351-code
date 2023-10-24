""" 
#! What is a file?
A file is a collection of data that is stored on a computer's storage device, such as a hard drive, SSD, or a USB flash drive

Files can contain various types of data, including text, images, videos, audio, program instructions

Files are organized into directories (also known as folders), and each file is identified by its unique name and location within the file system

Files allow us to store and organize data for various purposes, and they form the backbone of data storage and retrieval in modern computing.
"""

#! File Paths:
"""
Absolute File Path: This specifies the complete location of a file from the root directory of the file system """
# C:\Users\username\Documents\example.txt

"""Relative File Path: This specifies the location of a file relative to the current working directory of your program"""
# example.txt

#! Opening a file- open()
# You need to provide the file path and the mode in which you want to open the file (read, write, append, binary, or text mode)

"""
r:	It opens an existing file to read-only mode. The file pointer exists at the beginning.

rb:	It opens the file to read-only in binary format. The file pointer exists at the beginning.

r+: 	It opens the file to read and write both. The file pointer exists at the beginning.

w:	It opens the file to write only. It overwrites the file if previously exists or creates a new: one if no file exists with the same name.

wb:	It opens the file to write only in binary format. It overwrites the file if it exists previously or creates a new one if no file exists.

w+:	It opens the file to write and read data. It will override existing data.

a:	It opens the file in the append mode. It will not override existing data. It creates a new file if no file exists with the same name.

ab:	It opens the file in the append mode in binary format.

"""
#! Read the contents file
#! read()
# Read all the lines
# open('filepath', acessmode(r, w, a, x))
# my_file = open('example.txt', 'r')
# print(my_file.read())
# my_file.close()

#! Closing a file
"""It is important to close a file to save it from being unwarrantedly modified
It ensures better garbage collection
It releases the resources that have been tied up with the file
There may be a limit to the number of open files in an application
"""
#! readlines()
# Read line-by-line
my_file = open('example.txt')
# using the readlines() function we'll look through each line
for line in my_file.readlines():
    print(line)
my_file.close()

#! readline()
# Read each line
# Explicitly open the log file for reading
my_file = open('example.txt')
# my_file.readline()
print(my_file.readline())
my_file.readline()
print(my_file.readline())
my_file.readline()
my_file.close()


# Explicitly open log for reading
log_file = open('sample.log', 'r')

try:
    #process each line in the log file
    for line in log_file:
        #Split the log entry into it's components
        timestamp, level, message = line.split(" -", 2)

        if 'INFO' in level:
            print(f'INFO: {message} - {timestamp}')
        elif 'ERROR' in level:
            print(f'ERROR: {message} - {timestamp}')
        elif 'WARNING' in level:
            print(f'WARNING: {message} - {timestamp}')
finally:
    #explicitly close the log file to release the resources
    log_file.close()
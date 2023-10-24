# Pass in argument 'a' for opening a file in append mode
# ! Appending a file

#! write() append
my_file = open('example2.txt', 'a')
# Updating a file with new content
string_to_write = '\nThis is our new fifth line'
my_file.write(string_to_write)
my_file.close()

my_file = open('example2.txt', 'r')
for line in my_file:
    print(line)
my_file.close()




#! writelines() append
# Add mutiple lines
my_file = open('example2.txt', 'a')
list_of_string = ['\nThis is the new first line in example2', '\nThis is the second line', '\nFinal Line.']
my_file.writelines(list_of_string)
my_file.close()
# Read the file
my_file = open('example2.txt', 'r')
for line in my_file:
    print(line)
my_file.close()
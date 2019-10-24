#to write a file: 

fout= open('output.txt', 'w')

#if file already exists, opening it with write mode clears out the old data
#and starts fresh  

line1= "How many roads must a man walk down\n"
fout.write(line1)

line2= "Before you call him a man?\n"
fout.write(line2)

#dont forget to close the file when done 
#it'll close it for you 

fout.close()


#Exercise 1: 
def sed(str, replacement_str, filename1, filename2):
    pass


#Filenames and Paths

#files are organized into directories: 'folders', and each running prog has 
#a current directory- default directory. 

#OS functions for working with files and directories 

import os
cwd = os.getcwd() #returns name of current directory

print(os.path.abspath('output.txt'))
print(os.path.exists('output.txt'))
print(os.path.isdir('output.txt'))
print(os.path.isdir('/exercises'))
print(os.path.isfile('output.txt'))
print(os.listdir(cwd))

def walk(dirname): 
    """ Prints the name of all files in dirname and its subdirectories.
    dirname: string name of directory
    """

    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        #takes directory file name and joins them into complete path
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


def walk2(dirname):
    """Prints the names of all files in 
    dirname and its subdirectories.

    dirname: string name of directory
    """
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))
    

###############  Catching Exceptions ########################

#opening a file that does not exist creates an error 

# fin = open('bad_file') #won't open, no file exists

#no permission to access file= permission error 
#if you try to open a directory for reading: is directory Error

#To avoid these errors, you could use functions :
#  os.path.exists and os.path.isfile

try: 
    fin = open('bad_file')
except:
    print ('Something went wrong.')

#works as if, else statement- try catches an exception 


########PICKLING###########

#translates any type of object into a strin suitable for storage in
#a database and then translates strings back into objects

import pickle
t = [1, 2, 3]
print(pickle.dumps(t))


t1 = [1, 2, 3]
s = pickle.dumps(t1)
t2 = pickle.loads(s)
print(t2)

t1 == t2
t1 is t2



############ Writing Modules #################

def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

print(linecount('Classwork/Session 13/Exercises/wc.py'))

#any file contains python can be imported as a module 
#this program reads itself and prints the number of lines in a file which is 7

import wc

print(wc)
wc.linecount('Classwork/Session 13/Exercises/wc.py')




if __name__ == '__main__':
    print(linecount('Classwork/Session 13/Exercises/wc.py'))

# __name__ = built in variable that is set when the program starts and has the value
#__main__ ; the test code runs otherwise if module is being imported, the test code
#is skipped. 


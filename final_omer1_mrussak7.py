"""
File:        final_omer1_mrussak7.py

Authors:     Omer Cem Sevim and Michael Russak

Date:        12/05/2020

Description: This Python script is a modification of Project 2. In our proposal, we outlined that we would implement a more 
flexible tree displaying program, with flags that specify what information/files are displayed.
"""
import sys
from subprocess import call
import os

def parse_input(flags):
    l = len(sys.argv)
    i = 1
    while i < l:
        #If the user sends in -d flag, check that the next argument is a valid directory and add it to the list of arguments,
        #If its not a valid directory notify the user and return false.
        if sys.argv[i] == '-d':
            if i+1 < l and os.path.isdir(sys.argv[i+1]): #Check if the directory name exists and is valid.
                flags.append(sys.argv[i+1])
                i += 1 #skip to the next argument.
            elif i+1 == l:
                print('ERROR: -d is used with a directory name. -d [DIRECTORY], --help for usage info.')
                return False
            else:
                print('ERROR: Directory named ' + sys.argv[i+1] + ' does not exist, --help for usage info.')
                return False

        #If the user sends in -f flag, check that the next argument exists.
        elif sys.argv[i] == '-f':
            if i+1 < l:
                s = sys.argv[i+1]

                #Format the input so it can be used with the tree command.
                if sys.argv[i+1][0] == '.':
                    s = '*' + s
                s = '\\' + s

                flags.append('-P ' + s)
                i += 1 #skip to the next argument.
            else:
                print('ERROR: -f flag is used with a file name or file extension. -f [FILENAME | FILEEXTENSION], --help for usage info.')
                return False;
        #Add the help flag to the list.
        elif sys.argv[i] == '--help':
            flags.append('--help')

        #check if all the flags are valid.
        else:
            print('ERROR: ' + sys.argv[i] + ' is not a valid flag options, --help for usage info')
            return False;
        i += 1

    return True


def help_options():
    print('usage: final_omer1_mrussak7.py [OPTIONAL FLAG, ..., OPTIONAL FLAG]')
    print('----------------Flag Options----------------')
    print('-d directory             Start listing from the given directory')
    print('-f filename | extension  Only display files matching the name or with the same extension')
    print('--------------------------------------------')
    
def main():
    if len(sys.argv) == 1:
        call('tree')
        return True
    else:
        flags = []
        check = parse_input(flags)

        if not check:
            return False;

        if '--help' in flags:
            help_options()
            return True;
        s = 'tree'
        for f in flags:
            s+= ' ' + f
            
        call(s, shell=True)




if __name__ == '__main__':
    main()

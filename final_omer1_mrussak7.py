import sys
from subprocess import call

def parse_input(flags):
    for i in sys.argv:
        if(i == '-d'){
            flags.append('d');
        }

def main():
    if len(sys.argv) == 1:
        call('tree')
    else:
        flags = []
        parse_input(flags)






if __name__ == '__main__':
    main()

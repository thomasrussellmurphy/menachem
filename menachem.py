#!/usr/bin/env python

# Modules
import sys
import random

# Constants
MIN_DOORS = 2
MAX_DOORS = 10

# Loop for our interface
def interface_loop():
    depth = 0
    while True:
        n = random.randint(MIN_DOORS, MAX_DOORS)
        print 'You are ' + str(depth) + ' rooms into the maze.'
        print 'You are in a room. There are ' + str(n) + ' doors, zero-indexed.'
        while True:
            instr = raw_input('> ')
            
            if instr == '':
                continue

            elif instr == 'exit' or instr == 'quit':
                print 'Are you sure?'
                noinput = True
                while noinput:
                    response = raw_input('[y/n] ')
                    if response == 'y':
                        return
                    elif response == 'n':
                        noinput = False
            
            elif all([True if i in '1234567890' else False for i in instr]):
                i = int(instr)
                if 0 > i or n <= i:
                    print 'Invalid input. Please enter a valid door number.'
                else:
                    print 'You go through door number ' + instr + '.'
                    depth += 1
                    break
            else:
                print 'Invalid input.'

def main():
    if len(sys.argv) > 1:
        interface_loop()
    else:
        print 'Hello World'

# Call the main() function to begin the program.
main()

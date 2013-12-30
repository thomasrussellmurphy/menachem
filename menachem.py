#!/usr/bin/env python

# Modules
import sys

# Loop for our interface
def inteface_loop():
    print 'Testing Echo'
    while true:
        input = raw_input('> ')
        print input

def main():
    if len(sys.argv) > 1:
        print 'Hello World'
        interface_loop()
    else:
        print 'Hello World'

# Call the main() function to begin the program.
if __name__ == '__main__':
    main()

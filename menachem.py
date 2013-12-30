#!/usr/bin/env python

# Modules
import sys

# Loop for our interface
def interface_loop():
    print 'Testing Echo'
    while True:
        input = raw_input('> ')
        print input

def main():
    if len(sys.argv) > 1:
        print 'Hello World'
        interface_loop()
    else:
        print 'Hello World'

# Call the main() function to begin the program.
main()

#!/usr/bin/env python

# Modules
import sys
from classes.state import State

# Loop for our interface
def interface_loop():
    state = State()
    while True:
        # Notify user of current state
        state.print_state()
        
        # Input parsing block
        while True:
            instr = raw_input('> ')
            
            if instr == '':
                continue
            
            # Exit parsing
            elif instr == 'exit' or instr == 'quit':
                print 'Are you sure?'
                noinput = True
                while noinput:
                    response = raw_input('[y/n] ')
                    if response == 'y':
                        return
                    elif response == 'n':
                        noinput = False
            
            elif instr == 'h' or instr == 'help':
                print 'This can be helpful.'
                print 'help, #, exit, quit, location?'
                continue
            
            elif instr == 'location?':
                state.print_desc()
            
            # Choosing a door
            elif all([i in '1234567890' for i in instr]):
                i = int(instr)
                if 0 > i or state.doors <= i:
                    print 'Invalid input. Please enter a valid door number.'
                else:
                    print 'You go through door number ' + instr + '.'
                    break
            else:
                print 'Invalid input.'
                
        # Get the next state, also sets intital state
        state.next_state()

def main():
    if len(sys.argv) > 1:
        interface_loop() # Start loop until exit `return`
        print 'Exiting, game not saved.'
    else:
        print 'Run with any arguments to start.'

# Call the main() function to begin the program.
main()

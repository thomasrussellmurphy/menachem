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
            data = raw_input('> ').lower()
            split = data.partition(' ')
            instr = split[0]
            args = split[2]
            
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
                print 'General commands: help, exit, quit'
                print 'Status commands: location?'
                print 'Movement commands: enter N, back'
                continue
            
            elif instr == 'location?':
                state.print_desc()
            
            elif instr == 'back':
                print 'There is no door actually behind you. Look forward. It will be better that way.'
            
            # Choosing a door
            elif instr == 'enter':
                if all([i in '1234567890' for i in args]):
                    i = int(args)
                    if 0 > i or state.doors <= i:
                        print 'Invalid input. Please enter a valid door number.'
                    else:
                        print 'You go through door number ' + str(i) + '.'
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

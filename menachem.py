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
                print 'Status commands: look'
                print 'Movement commands: enter N, back, sit, stand'
                continue
            
            elif instr == 'look':
                print 'You look around the room.'
                state.print_desc()
                
            elif instr == 'sit':
                state.sit()
                print 'You sit down in the room. Not much seems to happen.'
            
            elif instr == 'stand':
                state.stand()
                print 'You stand back up. There is forward to consider.'
            
            elif instr == 'back':
                print 'There is no door behind you. Look forward. It will be better that way.'
            
            # Choosing a door
            elif instr == 'enter':
                if state.sitting:
                    print 'Stand up if you actually want to get to a door.'
                elif state.check_valid_door(args):
                    print 'You go through door number ' + args + '.'
                    break # to get to next state
                else:
                    print 'Invalid input. Please enter a valid door number'
            
            else:
                print 'Invalid input.'
                
        # Transition to the next state.
        state.next_state()

def main():
    if len(sys.argv) > 1:
        interface_loop() # Start loop until exit `return`
        print 'Exiting, game not saved.'
    else:
        print 'Run with any arguments to start.'

# Call the main() function to begin the program.
main()

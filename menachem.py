#!/usr/bin/env python

# Modules
import sys
from classes.state import State

# Process input: parse and act according to verb and arguments
def process_input(state, data):
    split = data.partition(' ')
    instr = split[0]
    args = split[2]
    
    if instr == '':
        return
    
    elif instr == 'exit' or instr == 'quit':
        print state.locale.get_string('exit-confirm',[])
        noinput = True
        while noinput:
            response = raw_input(state.locale.get_string('exit-prompt',[]))
            if response == state.locale.get_phrases('exit-responses')[0]:
                print state.locale.get_string('exit-no-save', [])
                exit() # End of program
            elif response == state.locale.get_phrases('exit-responses')[1]:
                noinput = False # Continue execution
                    
    elif instr == 'h' or instr == 'help':
        print state.locale.get_string('help',[])
                
    elif instr == 'look':
        print state.locale.get_string('look',[])
        state.print_desc()
                
    elif instr == 'sit':
        state.sit()
        print state.locale.get_string('sit',[])
                
    elif instr == 'stand':
        state.stand()
        print state.locale.get_string('stand', [])
                
    elif instr == 'back':
        print state.locale.get_string('back', [])
    
    elif instr == 'enter':
        desired_door = ''
        if state.sitting:
            print state.locale.get_string('enter-sitting', [])
        elif args == '':
            desired_door = raw_input(state.locale.get_string('enter-prompt',[]))
        else:
            desired_door = args

        if state.check_valid_door(desired_door):
            print state.locale.get_string('enter-valid', [desired_door])
            state.next_state() # to get to next state
            state.print_state()
        else:
            print state.locale.get_string('enter-invalid', [])
            state.print_desc()
    
    elif instr == 'set-locale':
        desired_locale = ''
        if args == '':
            desired_locale = raw_input(state.locale.get_string('locale-prompt',[]))
        else:
            desired_locale = args
        
        if state.locale.set_locale(desired_locale):
            print state.locale.get_string('locale-set-success',[desired_locale])
        else:
            print state.locale.get_string('locale-set-failure',[desired_locale])
            
        
    elif instr == 'check-locale':
        print state.locale.get_locale()
        
    elif instr == 'list-locales':
        print state.locale.get_localizations()
    
    elif instr == 'save':
        if args == '':
            response = raw_input(state.locale.get_string('save-prompt',[]))
            print state.create_save(response)
        else:
            print state.create_save(args)

    elif instr == 'load':
        if args == '':
            response = raw_input(state.locale.get_string('load-prompt',[]))
            print state.load_save(response)
        else:
            print state.load_save(args)
    
    elif instr == 'list-saves':
        print state.locale.get_string('load-list-saves',[state.get_available_saves()])
    
    elif instr == 'remove-save':
        if args == '':
            response = raw_input(state.locale.get_string('remove-prompt',[]))
            print state.remove_save(response)
        else:
            print state.remove_save(args)
    
    else:
        print state.locale.get_string('invalid-input', [])
    return

# Loop for our interface
def interface_loop():
    state = State()
    state.print_state()
    # Input parsing block
    while True:
        data = raw_input('> ').lower()
        process_input(state, data)


def main():
    if len(sys.argv) > 1:
        interface_loop() # Start loop until exit `return`
    else:
        print 'Run with any arguments to start.' # not localized

# Call the main() function to begin the program.
main()

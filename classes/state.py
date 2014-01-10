import random
from classes.localization import Localization
import glob
import io
import os

# Constants
MIN_DOORS = 2
MAX_DOORS = 10

class State:

    # Initializes the starting values.
    def __init__(self):
        self.name = 'player'
        self.depth = 0
        self.doors = random.randint(MIN_DOORS, MAX_DOORS)
        self.color = None # TODO: implement color.
        self.sitting = False
        self.locale = Localization() # TODO: implement loading localization
    
    def print_depth(self):
        if self.depth == 1:
            print 'You are 1 room into the maze.'
        else:
            print  'You are ' + str(self.depth) + ' rooms into the maze.'
        
    def print_desc(self):
        if self.sitting:
            print 'You are sitting in the room. Stand up and take a look around.'
        else:
            print 'You are in a room. There are ' + str(self.doors) + ' doors, zero-indexed.'
    
    def print_state(self):
        self.print_depth()
        self.print_desc()
    
    def next_state(self):
        self.doors = random.randint(MIN_DOORS, MAX_DOORS)
        self.depth += 1
        self.sitting = False

    def sit(self):
        self.sitting = True

    def stand(self):
        self.sitting = False

    def check_valid_door(self, args):
        if all([i in '1234567890' for i in args]) and args != '':
            i = int(args)
            if 0 <= i and i < self.doors:
                return True
        else:
            return False

    def create_save(self, save_name):
        # Remove leading '.' and whitespace in any number
        save_name = save_name.lstrip().lstrip('.')
        if not save_name.endswith('.json'):
            save_name += '.json'
        save_file = io.open('saves/' + save_name, 'w')
        
        return self.locale.get_string('save-failure',[])

    def load_save(self, save_name):
        return self.locale.get_string('load-failure',[])

    def get_available_saves(self):
        output = ''
        valid_paths = glob.iglob('saves/*.json')
        for path in valid_paths:
            split = path.partition('/')
            output += split[2] + '\n'
        return output[:-1]

    def remove_save(self, save_name):
        # Remove leading '.' and whitespace for some safety of other files
        save_name = save_name.lstrip().lstrip('.')
        save_path = 'saves/' + save_name
        if os.path.isfile(save_path) and save_name.endswith('.json'):
            os.remove(save_path)
            return self.locale.get_string('remove-save-success',[save_name])
        else:
            return self.locale.get_string('remove-save-failure',[save_name])

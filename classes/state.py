import random
from classes.localization import Localization
import glob
import io
import os
import json

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
        self.locale = Localization()
    
    def print_depth(self):
        if self.depth == 1:
            print self.locale.get_string('depth-one',[])
        else:
            print self.locale.get_string('depth-general',[self.depth])
        
    def print_desc(self):
        if self.sitting:
            print self.locale.get_string('desc-sitting',[])
        else:
            print self.locale.get_string('desc-room',[self.doors])
    
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
        save_file = io.open('saves/' + save_name, 'wb')
        
        save_dict = {'name': self.name, 'depth': self.depth, 'doors': self.doors, 'color': self.color, 'sitting': self.sitting, 'locale-name': self.locale.locale_name}
        try:
            json.dump(save_dict, save_file, separators=(',',':'))
            save_file.close()
        except (IOError) as err:
            return self.locale.get_string('save-failure',[save_name])
        return self.locale.get_string('save-success',[save_name])

    def load_save(self, save_name):
        save_name =  save_name.lstrip().lstrip('.')
        if  os.path.isfile('saves/' + save_name):
            save_file = io.open('saves/' + save_name, 'r')
            save_dict = json.load(save_file)
            
            name = depth = doors = color = sitting = locale_name = None
            
            try:
                name = save_dict['name']
                depth = save_dict['depth']
                doors = save_dict['doors']
                color = save_dict['color']
                sitting = save_dict['sitting']
                locale_name = save_dict['locale-name']
                
            except (KeyError):
                return self.locale.get_string('load-bad-save',[save_name])
            
            self.name = name
            self.depth = depth
            self.doors = doors
            self.color = color
            self.sitting = sitting
            self.locale.set_locale(locale_name)
            
            return self.locale.get_string('load-success',[save_name])
            
        else:
            return self.locale.get_string('load-failure',[save_name])

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

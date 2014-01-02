import random

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

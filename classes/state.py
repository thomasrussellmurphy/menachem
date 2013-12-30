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
        self.color = None # TODO: implement color. Also, possibly spell it right.
    
    def print_depth(self):
        if self.depth == 1:
            print 'You are 1 room into the maze.'
        else:
            print  'You are ' + str(self.depth) + ' rooms into the maze.'
        
    def print_desc(self):
        print 'You are in a room. There are ' + str(self.doors) + ' doors, zero-indexed.'
    
    def print_state(self):
        self.print_depth()
        self.print_desc()
    
    def next_state(self):
        self.doors = random.randint(MIN_DOORS, MAX_DOORS)
        self.depth += 1

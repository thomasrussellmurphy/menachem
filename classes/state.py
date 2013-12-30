import random

# Constants
MIN_DOORS = 2
MAX_DOORS = 10

class State:
    name = 'player'
    depth = -1 # Need to call next_state once
    doors = -1 # Same
    color = None # Will be implemented later
    
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

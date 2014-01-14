import random
import io
import os

# Constants
RGB_MAX = 255
RGB_MIN = 0

class Color:
    
    def __init__(self):
        # Master color space, default black
        self.red = 0
        self.green = 0
        self.blue = 0
        
    def become_random_color(self):
        self.red = random.randint(RGB_MIN, RGB_MAX)
        self.green = random.randint(RGB_MIN, RGB_MAX)
        self.blue = random.randint(RGB_MIN, RGB_MAX)
        return self # to make initialization with random color easier

    def set_rgb(self, rgb_triple): # No validation!
        self.red = rgb_triple[0]
        self.green = rgb_triple[1]
        self.blue = rgb_triple[2]

    def get_rgb(self):
        return (self.red, self.green, self.blue)
    
    def get_name(self):
        return '' # TODO: implement color name generator based on color space position

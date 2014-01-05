import json # Needed to parse saved localization file

# TODO: Complete implementation and integrate into the State
class Localization:

    def __init__(self):
        self.locale_name = ''
        self.locale_dict = {}
        self.locale_default = 'en-US' # Constant?

    def set_locale(self, locale_name):
        return False # Success of setting the new locale
    
    def get_phrases(self, phrase_key):
        return [''] # this pulls the string array out of the dict
        
    def get_string(self, phrase_key, components...):
        return '' # We want to construct the full string with variable arguments

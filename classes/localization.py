import json # Needed to parse saved localization file
import io

# TODO: Complete implementation and integrate into the State
class Localization:

    def __init__(self):
        self.locale_name = ''
        self.locale_dict = {}
        self.locale_default = 'en-US' # Constant?
        self.set_locale(self.locale_default)

    def set_locale(self, locale_name):
        # will need exception handling with these...
        file = io.open('localization/' + locale_name + '/locale.json', 'r')
        self.locale_dict = json.load(file)
        self.locale_name = locale_name
        return False # Success of setting the new locale
    
    def get_phrases(self, phrase_key):
        # will need exception handling here, too
        return self.locale_dict[phrase_key]
        return [''] # this pulls the string array out of the dict
        
    def get_string(self, phrase_key, components):
        phrases = self.get_phrases(phrase_key)
        # interleave phrases and components
        return '' # We want to construct the full string with variable arguments

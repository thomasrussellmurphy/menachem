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
        try:
            file = io.open('localization/' + locale_name + '/locale.json', 'r')
        except (IOError) as err:
            print 'ERROR: ' + str(err)
            return False
            
        try:
            self.locale_dict = json.load(file)[0] # extract dict
        except (ValueError) as err:
            print 'ERROR: ' + str(err)
            return False
        
        self.locale_name = locale_name
        return True # Success of setting the new locale
    
    def get_phrases(self, phrase_key):
        try:
            return self.locale_dict[phrase_key]
        except (KeyError) as err:
            # fall back to default locale?
            return ['that key was not found. have fun with this.']
        
    def get_string(self, phrase_key, components):
        output = ''
        phrases = self.get_phrases(phrase_key)
        midstop = min(len(phrases),len(components))
        
        # interleave phrases and components        
        for i in range(0, midstop):
            output += phrases[i] + str(components[i])
        for i in range(midstop, len(phrases)):
            output += phrases[i]
        for i in range(midstop, len(components)):
            output += str(components[i])

        return output
    
    def get_locale(self):
        return 'Locale: ' + self.locale_name

    def get_localizations(self):
        return 'en-US' # need to scan filesystem for localization/*/locale.json files

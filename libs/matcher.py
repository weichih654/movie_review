from fuzzywuzzy import fuzz
class Matcher:
    def __init__ (self):
        pass

    def match (self, cont1, cont2):
        return fuzz.ratio(cont1, cont2)

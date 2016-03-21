from fuzzywuzzy import fuzz
class Matcher:
    def __init__ (self):
        pass

    def match (self, cont1, cont2):
        if cont1 is None or cont2 is None:
            return -1
        return fuzz.partial_ratio(cont1, cont2)

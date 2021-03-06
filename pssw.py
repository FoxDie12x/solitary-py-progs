import random
class Password:
    """Generates a random password for user, as well as determines the strength 
    of a given password."""
    
    __pssw = ''
    
    __WEAK = 'weak'
    __AVERAGE = 'average'
    __STRONG = 'strong'          
        

    __uc = 'uc'
    __lc = 'lc'
    __num = 'num'
    __special = 'special'
    __char_classes = [__uc, __lc, __num, __special]
    
    
    
    
    def __init__(self, pssw: str):
        self.__pssw = pssw
    
        
    
    def set_pssw(self, pssw: str):
        self._pssw = pssw
        
        
        
    def set_uppercase(self, isOn: bool): 
        if self.__contains_class(self.__char_classes, self.__uc) and not isOn:
            index = self.__char_classes.index(self.__uc)
            del self.__char_classes[index]
        elif not self.__contains_class(self.__char_classes, self.__uc) and isOn:
            self.__char_classes.append(self.__uc)

            
    
    
    
    def set_lowercase(self, isOn: bool):
        if self.__contains_class(self.__char_classes, self.__lc) and not isOn:
            index = self.__char_classes.index(self.__lc)
            del self.__char_classes[index]
        elif not self.__contains_class(self.__char_classes, self.__lc) and isOn:
            self.__char_classes.append(self.__lc)
    


    def set_numerical(self, isOn: bool):
        if self.__contains_class(self.__char_classes, self.__num) and not isOn:
            index = self.__char_classes.index(self.__num)
            del self.__char_classes[index]
        elif not self.__contains_class(self.__char_classes, self.__num) and isOn:
            self.__char_classes.append(self.__num)

        
        
    def set_specialchars(self, isOn: bool):
        if self.__contains_class(self.__char_classes, self.__special) and not isOn:
            index = self.__char_classes.index(self.__special)
            del self.__char_classes[index]
        elif not self.__contains_class(self.__char_classes, self.__special) and isOn:
            self.__char_classes.append(self.__special)
   
        
        
    def generate_pssw(self, length: int) -> str:
        # 65-90     A-Z
        # 97-122    a-z
        # 48-57     0-9
        # 33-47, 58-64, 91-96, 123-126  popular special chars
        
        if len(self.__char_classes) == 0:
            raise Exception('No character classes are selected. Please select at'
                '\nleast one character class in order to generate a password. To '
                '\nselect a character class, use one of the setter methods.')
        
        output = ''
        
        for x in range(length):
            rand_class = random.choice(self.__char_classes)
            if rand_class == self.__uc:     # A-Z
                output += chr(random.randrange(65, 90 + 1))
            elif rand_class == self.__lc:  # a-z
                output += chr(random.randrange(97, 122 + 1))
            elif rand_class == self.__num:  # 0-9
                output += chr(random.randrange(48, 57 + 1))
            elif rand_class == self.__special:   # special chars
                rand_char_set = random.randint(0, 3)
                if rand_char_set == 0:      # 33-47
                    output += chr(random.randrange(33, 47 + 1))
                elif rand_char_set == 1:    # 58-64
                    output += chr(random.randrange(58, 64 + 1))
                elif rand_char_set == 2:    # 91-96
                    output += chr(random.randrange(91, 96 + 1))
                else:    # 123-126
                    output += chr(random.randrange(123, 126 + 1))
        return output
    
    
    
    def __contains_class(self, ls: [], charclass: str) -> bool:
        try:
            ls.index(charclass)
        except ValueError:
            # charclass is not in list
            return False
        
        return True
    
    
    
    def get_strength(self, password: str) -> str:
        return self.__WEAK





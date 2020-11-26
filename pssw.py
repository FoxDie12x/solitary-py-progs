import random
class Password:
    """Generates a random password for user, as well as determines the strength 
    of a given password."""
    
    __pssw = ''
    
    __WEAK = 'weak'
    __AVERAGE = 'average'
    __STRONG = 'strong'            
    
    
    
    def __init__(self, pssw: str):
        self.__pssw = pssw
    
        
    
    def set_pssw(self, pssw: str):
        self._pssw = pssw
        
        
        
    def generate_pssw(self, length: int) -> str:
        # 65-90     A-Z
        # 97-122    a-z
        # 48-57     0-9
        # 33-47, 58-64, 91-96, 123-126  popular special chars
        
        output = ''
        
        for x in range(length):
            rand_nr = random.randint(0, 3)
            if rand_nr == 0:     # A-Z
                output += chr(random.randrange(65, 90 + 1))
            elif rand_nr == 1:  # a-z
                output += chr(random.randrange(97, 122 + 1))
            elif rand_nr == 2:  # 0-9
                output += chr(random.randrange(48, 57 + 1))
            else:   # special chars
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
    
    
    
    def get_strength(self, password: str) -> str:
        return self.__WEAK





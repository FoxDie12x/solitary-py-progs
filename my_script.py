def display_vertical_pyramid_pattern(n, s): 
    """Displays a pyramidical pattern of string s.
    
    The result will be a pyramid with the maximum number of occurences in 
    a single line consisting of n occurrences of string s.

    Attributes:
        n -- integer indicating the max number of occurrences for the line
        s -- string to repeat in a pattern
    """
    for x in range(n):
        print((s + ' ') * (x + 1) + '\n')

    for x in range((n - 1), 0, -1):
        print((s + ' ') * (x) + '\n')


def display_cube_pattern(n, s):
    """Displays a cubed pattern of string s.
    
    The cube is tilted 'sideways', i.e., it is a 'diamond'
    Attributes:
        n -- integer indicating the max width from of the diamond, i.e. diagonal length
        s -- string to repeat in a pattern
    """
    maxLength = len(s) if n <= 1 else ((len(s + ' ') * n) - 1)

    
    for x in range(n):        
        if x == 0:
            line = s            
            currentRowLength = len(line)
            addition = 1 if len(s) > 3 else 0
            print(' ' * ((maxLength // 2) - ((currentRowLength // 2) - addition)), end='')       
        else:
            line = (s + ' ') * x + s
            currentRowLength = len(line)    
            print(' ' * ((maxLength // 2) - ((currentRowLength // 2))), end='')                               
        print((s + ' ') * (x + 1))
        
    for x in range(n - 2, 0, -1):
        if x == 0:
            line = s            
            currentRowLength = len(line)    
            print(' ' * ((maxLength // 2) - ((currentRowLength // 2) - 1)), end='')       
        else:
            line = (s + ' ') * x + s
            currentRowLength = len(line)    
            print(' ' * ((maxLength // 2) - ((currentRowLength // 2))), end='')                               
        print((s + ' ') * (x + 1))
    else:
        if n > 1:            
            line = s            
            currentRowLength = len(line)    
            addition = 1 if len(s) > 3 else 0
            print(' ' * ((maxLength // 2) - ((currentRowLength // 2) - addition)), end='')   
            print(s)
        
        
        
        
def display_cube(n, char, /):
    """Displays a cube consisting of characters char
    
    Attributes:
        n -- integer number indicating the max width of the diamond, i.e., diagonal length of cube
        char -- the character to print. Note that if length of char > 1, then 
                only the first character will be used.
    """
    
    if len(char) == 0:
        print('Please pass a character in the second parameter.')
        
    if int(n) < 1:
        print('Please specify a positive integer power bigger bigger than or equal to 1.')
        
    
    ch = char[0]
    maxLength = 2 * (2 * n + 1)
    
    for x in range(n):
        
        lineLength = 2 * (2 * x + 1)
        spaces = (maxLength // 2) - (lineLength // 2) - 2
        print(' ' * spaces, end='')
        print(ch * lineLength)
            
    for x in range(n - 2, 0, -1):        
        lineLength = 2 * (2 * x + 1)
        spaces = (maxLength // 2) - (lineLength // 2) - 2
        print(' ' * spaces, end='')
        print(ch * lineLength)
    else:
        if n > 1:
            spaces = (maxLength // 2) - 3
            print(' ' * spaces, end='')
            print(ch * 2)

    
        

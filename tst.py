def get_new_prefix(depth) -> str:
    """ Formats a new prefix from a list of prefixes

    Attributes:
        list -- a list of strings
    """
    
    
    prefix = ''
    middle = ''
    if depth == 2:
        prefix = u'\u2502' + (' ' * depth) + '' + u'\u2514\u2500_'
    elif depth > 2:
        prefix = u'\u2502' + (u' ' * (depth + 1)) + '' + u'\u2514\u2500+'
        
    else:
        prefix = u'\u2514\u2500='
   
       

    postfix = ''
        
    return prefix
        

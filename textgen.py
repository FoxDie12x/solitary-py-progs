import os.path, random

def write_data(path: str):
    with open(path + '/' + 'file.txt', 'w') as file:        
        for line in range(50000):
            for char in range(255):
                int = random.randrange(97, 123)
                file.write(chr(int) + '')
            file.write('\n')
            
    

def specify_path() -> str: 
    location = input('Specify a directory where the files should be stored:')
    if os.path.isdir(location) == False:
        print('The path you specified is not a directory or does not exist.'
            '\nPlease try again.\n')
        specify_path()
    return location


def main():
    """Initializes and starts the program"""
    print(U'\tWelcome to \'RANDOM TEXT GENERATOR V9000 ULTIMATE PLUS XL MAX PRO\'\u00A9\u00AE,'
        '\n'
        '\n\t...the most useless program that generators crazy amounts of use-'        
        '\n\t-less characters for statistical reasons that benefit no single ' 
        '\n\thuman being. ')
    print()
    print('\t*****************************************************************')
    print('\t*****************************************************************')
    print('\t*****************************************************************')
    print()
    print('\tThe program will create generate random characters spread over one'
        '\n\tor multiple .txt files. You are asked to enter the number of files'
        '\n\tto write to, as well as the kinds of characters to use for the '
        '\n\ttext generation.')
        
    print('\tEach file written to will have 1 million lines and at most 255 '    
        '\n\tcharacters per line.')

    print()
    
    # Ask user whether to continue
    start = input('Are you ready to start this useless activity? (y/N): ')
    if start != 'y' and start != 'Y' and start != 'yes' and start != 'Yes':
        return


    # Get path of where to store the files from user input
    path = specify_path()
    
    # Write data
    write_data(path)
    
    
    
if __name__ == '__main__':
    try:    
        main()
    except (KeyboardInterrupt):
        print('\n\nProgram terminated by user. Wise decision!')
        

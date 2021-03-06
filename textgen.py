import os.path, random, chart

def write_data(path: str) -> str:
    """ Writes data to a file, and returns the file path """

    filePath = path + '/' + 'file.txt'
    writeFile =  open(filePath, 'w')        
    for line in range(1000000):
        for char in range(255):
            int = random.randrange(97, 123)
            writeFile.write(chr(int) + '')
        writeFile.write('\n')
    writeFile.close()
    return filePath
    
    

def specify_path() -> str: 
    location = input('Specify a directory where the files should be stored:')
    if os.path.isdir(location) == False:
        print('The path you specified is not a directory or does not exist.'
            '\nPlease try again.\n')
        specify_path()
    return location



def get_statistics_of_file(filePath):
    charsDict = {'totalCharacters': 0}
    with open(filePath, 'r') as f:
        for line in f.readlines():
            for letter in line:
                if ord(letter) == 10:
                    continue                    
                if (letter in charsDict) == False:
                    charsDict[letter] = 1
                else: 
                    charsDict[letter] = charsDict[letter] + 1       
                charsDict['totalCharacters'] = charsDict['totalCharacters'] + 1                                            
    return charsDict
                

    


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
    filePath =  write_data(path)
    
    # Get statistics about the new file
    stats =  get_statistics_of_file(filePath)
#    print(stats)
    chart.draw_chart(stats)
    
    
    
if __name__ == '__main__':
    try:    
        main()
    except (KeyboardInterrupt):
        print('\n\nProgram terminated by user. Wise decision!')
        



def main():
    chars = {'totalCharacters': 1275000, 'g': 49089, 'j': 49195, 't': 48753, 'i': 48976, 'u': 49256, 'y': 49619, 'n': 49058, 'k': 48723, 'p': 49195, 'w': 49095, 'o': 48469, 'f': 49375, 'z': 49161, 'r': 49002, 'x': 49207, 'a': 49173, 'q': 49115, 'c': 48879, 'm': 49096, 's': 49028, 'h': 49183, 'e': 48736, 'l': 49042, 'd': 48916, 'b': 48825, 'v': 48834}
    
    characterCount = chars['totalCharacters']
    del chars['totalCharacters']

    highestCharCount = 0
    highestValPerc = 0
    
    for element in chars:
        if (round(chars[element] / characterCount * 100, 2)) > highestValPerc:
            highestValPerc = round(chars[element] / characterCount * 100, 2)
            highestCharCount = chars[element]

        chars[element] = {
        'total': chars[element], 
        'percentage': round(chars[element] / characterCount * 100, 2)
        }
        
#    print(chars)
#    print(highestValPerc)
#    print(highestCharCount)



    


if __name__ == '__main__':
    main()

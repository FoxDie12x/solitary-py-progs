

def draw_chart(chars):
#    chars = {'totalCharacters': 1275000, 'g': 49089, 'j': 49195, 't': 48753, 'i': 48976, 'u': 49256, 'y': 49619, 'n': 49058, 'k': 48723, 'p': 49195, 'w': 49095, 'o': 48469, 'f': 49375, 'z': 49161, 'r': 49002, 'x': 49207, 'a': 49173, 'q': 49115, 'c': 48879, 'm': 49096, 's': 49028, 'h': 49183, 'e': 48736, 'l': 49042, 'd': 48916, 'b': 48825, 'v': 48834}
    
    characterCount = chars['totalCharacters']
    del chars['totalCharacters']

    highestCharCount = 0
    highestValPerc = 0
    
    for element in chars:
        if (int(chars[element]) > highestCharCount):
            highestCharCount = chars[element]
            
        if (round(chars[element] / characterCount * 100, 2)) > highestValPerc:
            highestValPerc = round(chars[element] / characterCount * 100, 2)
        chars[element] = {
        'count': chars[element], 
        'percentage': round(chars[element] / characterCount * 100, 2)
        }               
    
    print(chars)
    print(highestValPerc)
    print('highest char count:', highestCharCount)

    for x in range(20, 0, -1):
        if x % 5 == 0:            
            print(u'\u252C' if x == 20 else u'\u253C', end='') 
        else:        
            print(u'\u2502', end='') 


        for element in chars:
            countValue = ' '
            percValue = ' '
            if chars[element]['percentage'] > (highestValPerc - ((20 - x) * (highestValPerc / 750)) ):
                percValue = u'\u2573'
            else:
                pervCalue = '  '
            
            if (chars[element]['count']) > (highestCharCount - ((20 - x) * (highestCharCount / 500))):
                countValue = u'\u2503'
            else:
                countValue = ' '
                
#            countValue = ' '
            print(' ' + countValue + percValue + ' ', end='')

        
        print()
        
        if (x == 1):
            print(u'\u2514' + u'\u2500' * (len(chars)) * 4)
        if (x == 1):
            print(' ', end='')
            for element in chars:
                print(' ..' + ' ', end='')
            print()
            for element in chars:
                print('  ' + element + ' ', end='')            
    print()    




    
    


if __name__ == '__main__':
    draw_chart()

1:  Display a vertical pattern in cli.
    Example:
    
    test
    test test
    test test test
    test test test test 
    test test test test test 
    test test test test test test 
    test test test test test
    test test test test
    test test test 
    test test 
    test
    
    
2:  Display a diamond shaped pattern in cli.
    Example:
    
            test
         test test
       test test test
     test test test test 
       test test test
         test test 
            test
            
            
    Alternative example:
            aa
          aaaaaa 
        aaaaaaaaaa
      aaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaa    
      aaaaaaaaaaaaaa
        aaaaaaaaaa
          aaaaaa
            aa
            
    (The alternative example circumvents the problem of spacing of a string 
    as pattern).

3:  Display contents of directory
    
    Write a program that asks the user for a directory, and then displays the 
    contents of the directory as a tree.   
    
    
    
        
4:  Random text generator

    This program generates random text and dsiplays statistics about the text.
    The random text is saved into plain .txt-files(s). Storing the text can be 
    spread over multiple .txt-files.
    
    Text files should have limits:
        255 characters per line
        1 million lines per file
        
    - User input is required to specify the number of text files to write to.
    - User input is also required to specify *where* to store the output files.
    - User input is also required to specify the type of characters allowed to be 
    output (numbers, alphanumerical, punctuation characters, combinations and/or
    exclusion of certain or sets of characters, etc)
    
    
5:  Horoscope

    User is asked for his b-day. Bday must be given in ISO 8601 format 
    (yyyy-mm-dd). The program then displays the astrological sign of the user.
    
    
6:  Password utility
    
    This program should generate a random password for a user. The password's 
    strength varies according to which rules should apply. The rules to apply 
    will be set by user input. The following rules should be applicable:
        - minimum and maximum length for the password
        - whether the password should contain any letters, digits, or special chars
        - the minimum number of each character type (letter, digit, special chars) 
        and whether it should be unique chars
        - uppercase, lowercase or both
        
    The program should also be able to check a given password's strength. The 
    password to check should be a string passed to a function. The password's 
    strength is determined by:
        - length of the password (0-8 = weak, 9-16 = medium, 17-higher = strong)
        - whether there is a combination of letters, digits, and special chars
        (if only letters or digits = weak, 
        if at least 2 char types = medium, 
        if all character types present = strong)
        - whether there is repetition of a character (the more repetition, the weaker)
        - whether there is a sequence in characters (the stronger the sequence, the weaker)
        
        
        
    

        
    

            

        
        
    

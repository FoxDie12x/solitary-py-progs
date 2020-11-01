import os, os.path

class DirectoryContents:
    """ Displays contents of a directory specified by user
    """
    
    
    def __init__(self):
        self._iteration = 1
        self.parentPath = ''
        self.childPath = ''
        self.total_directories = 0
        self.total_files = 0



    def list_path_contents(self, path: str):
        """ Shows the contents of a directory as a tree.
        
        Attributes:
            path -- the (absolute) path of the directory
        """
            
        if os.path.isdir(path) == False:
            print('The path specified is not a directory or does not exist. '
                'Please enter an existing directory path.')
            return
           
        self.path = path
        contents = os.listdir(self.path)
        print(contents)
        self.total_directories = 0
        self.total_files = 0
        
        for x in contents:    
            self._iteration = 1         
            if os.path.isdir(self.path + '/' + x):                
                new_prefix = self.__prepare_prefix(self._iteration)
                print(new_prefix, x)
                self._iteration = self._iteration + 1
                self.total_directories = self.total_directories + 1
                self.__iterate_through_dir(self.path + '/' + x)
                
            else:    
                if x[0] != '.':                   
                    new_prefix = self.__prepare_prefix(1)
                    print(new_prefix, f'{x}')
                    self.total_files = self.total_files + 1
        
        print('total directories:', self.total_directories, '; total files:', self.total_files)
        
       
       
    def __iterate_through_dir(self, path: str):    
        """ Displays a tree of the path, or the filename if path is not a directory
        
        Attributes:
            path -- the absolute path of the directory
        """

        contents = os.listdir(path)

        for x in contents:
            if os.path.isdir(path + '/' + x):  
                new_prefix = self.__prepare_prefix(self._iteration)
                print(new_prefix, x)
                
                # Step forward
                self._iteration = self._iteration + 1                 
                self.total_directories = self.total_directories + 1
                self.__iterate_through_dir(path + '/' + x)
                
                # Step back one level
                self._iteration = self._iteration - 1
            else:
                if x[0] != '.':

                    new_prefix = self.__prepare_prefix(self._iteration)
                    print(new_prefix, f'{x}')
                    
                    # add to total files
                    self.total_files = self.total_files + 1



    def __prepare_prefix(self, depth: int) -> str:
        """ Formats a new prefix from a list of prefixes

        Attributes:
            list -- a list of strings
        """        
        
        prefix = ''
        if depth == 2:
            prefix = u'\u2502' + (' ' * depth) + '' + u'\u2514\u2500'
        elif depth > 2:
            prefix = u'\u2502' + (u' ' * (depth + 1)) + '' + u'\u2514\u2500'         
        else:
            prefix = u'\u2514\u2500'                
        return prefix
        
             

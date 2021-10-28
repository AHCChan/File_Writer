"""
WIDTH FILE WRITER
(version 1.0)
by Angelo Chan

This module contains a Class designed to write to basic flat files with a
maximum file width.
"""

# Imported Modules #############################################################

from File_Writer import *


# Classes ######################################################################

class Width_File_Writer(File_Writer):
    """
    The File Writer is a file writer designed to write to flat files with a
    set maximum "width". (Number of characters per row) Exceptions to this
    can be made.
    
    When the write head reaches the maximum width, a newline is automatically
    inserted. The only exception is when Write_F is used.
    """
    
    # Major Configurations #####################################################
    
    _CONFIG__file_width = 80
    
    # Minor Configurations #####################################################
    
    _CONFIG__print_errors = True
    _CONFIG__print_progress = False
    _CONFIG__print_metrics = True
    
    
    
    # Strings ##################################################################
    
    _MSG__object_type = "Width File Writer"

    _MSG__invalid_width = "\nERROR: Invalid width:\n\t{S}"
    
    
    
    # Constructor & Destructor #################################################
    
    def __init__(self, file_path="", auto_open=False):
        """
    `   Creates a Width File Writer object. The filepath will be tested if a
        filepath is supplied.
        """
        File_Writer.__init__(self, file_path, auto_open)
        self._index = 0
    
    
    
    # Parameter Configuration Methods ##########################################
    
    def Get_Width(self):
        """
        Return the file width setting.
        """
        return self._CONFIG__file_width
    
    def Set_Width(self, new_width):
        """
        Configures the File Writer to have a new maximum width per line.
        """
        try:
            new_width = int(new_width)
        except:
            self.printE(self._MSG__invalid_width.format(S = new_width))
            return
        self._CONFIG__file_width = new_width
    
    
    
    # File Writing Methods #####################################################
    
    def Write(self, string):
        """
        Write to the file, ensuring that the resulting text does not exceed a
        given number of characters per line.
        """
        length = len(string)
        total = self._index + length
        if total > self._CONFIG__file_width:
            print "DDD"
            print total, self._index, length
            gap = self._CONFIG__file_width - self._index
            self.file.write(string[:gap] + self.EOL)
            self._index = 0
            string = string[gap:]
            while len(string) > self._CONFIG__file_width:
                self.file.write(string[:self._CONFIG__file_width] + self.EOL)
                string = string[self._CONFIG__file_width:]
        if string:
            self.file.write(string)
            self._index += len(string)
        if self._index == self._CONFIG__file_width:
            self.file.write(self.EOL)
            self._index = 0
    
    def Write_1(self, char):
        """
        Write to the file, ensuring that the resulting text does not exceed a
        given number of characters per line.
        
        This simplified implementation is applied to chars.
        """
        self.file.write(char)
        self._index += 1
        if self._index == self._CONFIG__file_width:
            self.file.write(self.EOL)
            self._index = 0
    
    def Write_F(self, string):
        """
        Force-write to the file, ignoring file width constraints.
        """
        self.file.write(string)
        self._index += len(string)

    def Newline(self):
        """
        Start a new line.
        """
        self.file.write(self.EOL)
        self._index = 0



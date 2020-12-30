from . levels import L_LEVELS

class YuleLogger(object):
    """ Logger Class """

    _id_counter = 0

    def __init__(self, id=None, file_path=None):
        
        if id:
            self.id = str(id)
        else:
            YuleLogger._id_counter += 1
            self.id = f"Yule_Logger_{YuleLogger._id_counter}"
        self._file_path = file_path
        self._level = L_LEVELS['INFO']

    # PRINT LOG METHODS

    def info(self, msg):
        """ Set log level to INFO"""

        if self._level_check('INFO'):
            print(f"{self.id}: INFO - {msg}.")
    
    def warning(self, msg):
        """ Set log level to WARNING """

        if self._level_check('WARNING'):
            print(f"{self.id}: WARNING - {msg}.")
    
    def error(self, msg):
        """ Set log level to ERROR """

        if self._level_check('ERROR'):
            print(f"{self.id}: ERROR - {msg}.")

    # LEVEL METHODS

    def _level_check(self, level):
        """ Compares input level to self._level and returns bool"""
        return (self._level <= L_LEVELS[level])


    def set_level(self, level):
        """ Sets the logger level """

        if type(level) == int:
            if level in L_LEVELS.values():
                self._level = level
        elif type(level) == str and level.upper() in L_LEVELS.keys():
            self._level = L_LEVELS[str(level.upper())]
        else:
            raise TypeError(f"arg level must be type int or string, and must match an L_LEVELS value")
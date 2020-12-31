from yule.const import DEF_LEVELS, DEF_COLORS
from colorama import Fore, init as c_init
c_init()


class YuleLogger(object):
    """ Logger Class """

    _id_counter = 0

    def __init__(
        self,
        id=None,
        to_console=True,
        to_file=False,
        file_path=None,
        level=2,

    ):

        if id:
            self.id = str(id)
        else:
            YuleLogger._id_counter += 1
            self.id = f"Yule_Logger_{YuleLogger._id_counter}"

        self._to_console = to_console
        self._to_file = to_file
        self._file_path = file_path
        self.color_list = DEF_COLORS
        self._level_dict = DEF_LEVELS

        if type(level) == int and level in DEF_LEVELS.keys():
            self._level = level
        elif type(level) == str:
            self.id = level_from_str(level)

    # LOG METHODS

    def info(self, msg):
        """ Record Log Entry at level INFO"""

        if self._level_check(0):
            self._create_log(content=msg, i_level=0)

    def warning(self, msg):
        """ Record Log Entry at level WARNING """

        if self._level_check(1):
            self._create_log(content=msg, i_level=1)

    def error(self, msg):
        """ Record Log Entry at level ERROR """

        if self._level_check(2):
            self._create_log(content=msg, i_level=2)

    # LEVEL METHODS

    def set_level(self, level):
        """ Sets the logger level """
        s_level = confirm_int(level)
        self._level = s_level

    # PRIVATE METHODS

    def _level_check(self, level):
        """ Compares input level to self._level and returns bool"""
        return (self._level <= level)

    def _create_log(self, content, i_level):
        level_str = level_from_int(confirm_int(i_level))
        log_msg = f"{self.id} | {level_str}: {content}"
        if self._to_console:
            print(self.color_list[i_level] + log_msg + Fore.RESET)
        if self._to_file:
            pass


# **********FUNCTIONS**************

def confirm_int(i_level):
    if type(i_level) == int:
        return i_level
    if type(i_level) == str:
        return level_from_str(i_level)


def level_from_int(level):
    r_level = DEF_LEVELS[level]
    return r_level


def level_from_str(level):
    r_level = None
    for i in DEF_LEVELS.keys():
        if DEF_LEVELS[i] == level.upper():
            r_level = i
    return r_level

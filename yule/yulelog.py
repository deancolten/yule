from yule.const import DEF_LEVELS, DEF_COLORS, DEF_SYNTAX
from yule.log_file import LogFile
from yule.level import Level, YLevel
from datetime import datetime
from colorama import Fore, init as c_init
c_init()


class YuleLogger(object):
    """ Logger Class """

    # ID For Gefault Logger Name
    _id_counter = 0

    def __init__(
        self,
        id=None,
        to_console=True,
        to_file=False,
        file_path=None,
        level=Level.error,

    ):
        """Logger Init"""
        if id:
            self.id = str(id)
        else:
            YuleLogger._id_counter += 1
            self.id = f"Yule_Logger_{YuleLogger._id_counter}"

        self.color_list = DEF_COLORS

        self.to_console = to_console
        self.to_file = to_file
        self._file_path = file_path
        self._level_dict = DEF_LEVELS

        if type(level) == YLevel:
            self._level = level
        elif type(level) == int and level in DEF_LEVELS.keys():
            self._level = YLevel(level, DEF_LEVELS[level])
        elif type(level) == str:
            self._level = YLevel(value=level_from_str(
                level), name=DEF_LEVELS[level_from_str(level)])

        self._log_file = LogFile(name=self.id, location=self._file_path)

        self._syntaxer = YuleSyntax(
            log_name=self.id,
            syntax_string=None
        )

    # LOG METHODS

    def debug(self, msg):
        """ Record Log Entry at level DEBUG"""

        if self._level_check(0):
            self._record_log_entry(Entry(content=msg, level=Level.debug))

    def info(self, msg):
        """ Record Log Entry at level INFO"""

        if self._level_check(1):
            self._record_log_entry(Entry(content=msg, level=Level.info))

    def warning(self, msg):
        """ Record Log Entry at level WARNING """

        if self._level_check(2):
            self._record_log_entry(Entry(content=msg, level=Level.warning))

    def error(self, msg):
        """ Record Log Entry at level ERROR """

        if self._level_check(3):
            self._record_log_entry(Entry(content=msg, level=Level.error))

    # CONFIG METHODS

    def set_level(self, level):
        """ Sets the logger level """

        # input is YLevel
        if type(level) == YLevel:
            self._level = level

        # input is int or string
        else:
            s_level = confirm_int(level)
            if s_level in DEF_LEVELS.keys():
                r_level = YLevel(confirm_int(level), DEF_LEVELS[s_level])
                self._level = r_level
            else:
                raise ValueError(
                    "set_level() arg 'level' must be type int or YLevel")

    def set_file_directory(self, path):
        """Set log_file path"""
        self._file_path = path

    def clear_log_file(self):
        """clears log file"""
        self._log_file.clear_file()

    def set_syntax(self, syntax_string):
        """Set string used for custom syntax"""
        if type(syntax_string) == str:
            self._syntaxer.update_syntax(syntax_string)
        else:
            raise TypeError("arg syntax_string must be type str")

    # PRIVATE METHODS

    def _level_check(self, level):
        """ Compares input level to self._level and returns bool"""
        return (self._level.value <= level)

    def _record_log_entry(self, entry):
        """Creates log entry and prints to console and/or log file according to config"""

        # log entry to console and/or file
        log_msg = self._syntaxer.format_entry(entry)
        if self.to_console:
            print(self.color_list[entry.level.value] + log_msg + Fore.RESET)
        if self.to_file:
            self._log_file.record_entry(log_msg)


class Entry(object):
    """ Yule log entry object"""

    def __init__(self, content, level):
        self.content = content
        self.level = level

    def __repr__(self):
        return f"Yule Entry Object - Level:{self.level}; Content: {self.content}"


class YuleSyntax(object):

    """Syntax Class for YuleLog"""

    # class const
    PREPROCESS_CHARS = ['N']
    REALTIME_CHARS = ['D', 'T', 'M', 'L']
    DEFAULT_SYNTAX_STR = DEF_SYNTAX

    def __init__(self, log_name, syntax_string=None):
        """Initialize Syntax Object"""

        self.log_name = log_name
        if syntax_string:
            self.update_syntax(syntax_string)
        else:
            self.update_syntax(YuleSyntax.DEFAULT_SYNTAX_STR)

    def update_syntax(self, syntax_string):
        """Update self.syntax_string (Preprocessor String)"""

        pre_process_string = []
        push = pre_process_string.append
        skip = False

        for i in range(len(syntax_string)):
            if skip:
                skip = False
            else:
                if syntax_string[i] == '%':
                    ch = syntax_string[i+1]
                    if ch in YuleSyntax.PREPROCESS_CHARS:
                        if ch == 'N':
                            push(self.log_name)
                        skip = True
                    else:
                        push(syntax_string[i])
                else:
                    push(syntax_string[i])
        self.syntax_string = ''.join(pre_process_string)

    def format_entry(self, entry):
        """Uses preprocessed syntax string to generate formatted output string"""

        formatted = []
        push = formatted.append
        skip = False

        for i in range(len(self.syntax_string)):
            if skip:
                skip = False
            else:
                if self.syntax_string[i] == '%':
                    ch = self.syntax_string[i+1]
                    if ch in YuleSyntax.REALTIME_CHARS:
                        # DATE
                        if ch == 'D':
                            push(datetime.now().strftime('%D'))
                        # TIME
                        elif ch == 'T':
                            push(datetime.now().strftime('%T'))
                        # MESSAGE
                        elif ch == 'M':
                            push(str(entry.content))
                        # LEVEL
                        elif ch == 'L':
                            push(entry.level.name)
                        skip = True

                    else:
                        push(self.syntax_string[i])
                else:
                    push(self.syntax_string[i])
        return ''.join(formatted)

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

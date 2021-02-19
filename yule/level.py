

class YLevel(object):
    """Yule Level Object"""

    def __init__(self, value, name):

        if type(value) == int:
            self.value = value
        else:
            raise TypeError("Level value must be type int")

        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def __int__(self):
        return self.value


class Level(object):
    debug = YLevel(value=0, name='DEBUG')
    info = YLevel(value=1, name="INFO")
    warning = YLevel(value=2, name="WARNING")
    error = YLevel(value=3, name="ERROR")

    def __level_from_string(self, string):
        if string.lower() == 'debug':
            return self.debug
        elif string.lower() == 'info':
            return self.info
        elif string.lower() == 'warning':
            return self.warning
        elif string.lower() == 'error':
            return self.error

    def __level_from_int(self, num):
        if num == 0:
            return self.debug
        elif num == 1:
            return self.info
        elif num == 2:
            return self.warning
        elif num == 3:
            return self.error

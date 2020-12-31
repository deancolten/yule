"""
CURRENTLY DEPRICATED 
"""
from colorama import init, Fore, Back, Style
init()


def print_RED(i_func):
    def wrapper(*args, **kwargs):
        print(Fore.RED, Style.BRIGHT, end='')
        i_func(*args, **kwargs)
        print(Fore.RESET, end='')
    return wrapper


def print_BLUE(i_func):
    def wrapper(*args, **kwargs):
        print(Fore.BLUE, Style.BRIGHT, end='')
        i_func(*args, **kwargs)
        print(Fore.RESET, end='')
    return wrapper


def print_GREEN(i_func):
    def wrapper(*args, **kwargs):
        print(Fore.GREEN, Style.BRIGHT, end='')
        i_func(*args, **kwargs)
        print(Fore.RESET, end='')
    return wrapper


def print_YELLOW(i_func):
    def wrapper(*args, **kwargs):
        print(Fore.YELLOW, Style.BRIGHT, end='')
        i_func(*args, **kwargs)
        print(Fore.RESET, end='')
    return wrapper

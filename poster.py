from pyfiglet import figlet_format as formater
from termcolor import colored

def posterize(text,color):
    return colored((formater(text)),color)

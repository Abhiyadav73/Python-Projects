import pyperclip

def CamelCase(letter):
    split=letter.split()
    text="".join([part.capitalize() for part in split])
    return text
def pascalCase(letter):
    words=letter.split()
    other=words[1:]
    first=words[0].lower()+"".join([part.capitalize() for part in other])
    return first

def snake_case(letter):
    word=letter.split()
    text="_".join([part.lower() for part in word])
    return text

def kebabCase(letter):
    word=letter.split()
    text="-".join([part.lower() for part in word])
    return text

def Reverse(letter):
    return letter[::-1]

def UpperCase(letter):
    return letter.upper()

def LowerCase(letter):
    return letter.lower()

def copy_to_clipboard(letter):
    pyperclip.copy(letter)
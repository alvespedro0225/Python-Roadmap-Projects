from datetime import datetime

# utility functions for code readability

def get_current_time() -> str:
    return datetime.now().strftime("%d%m%Y, %H%M%S")
       
def is_braces(letter:str) -> bool:
    return letter == "\'" or letter == "\""

def is_space(letter:str) -> bool:
    return letter == " "
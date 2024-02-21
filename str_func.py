import re
def to_upper_case(s):
    """Convert a string to uppercase."""
    return s.upper()
<<<<<<< HEAD
def capitalize_words(s):
    """Capitalize the first letter of each word in a string, preserving spaces."""
    return ''.join(word.capitalize() if word.isalpha() else word for word in re.split('([^A-Za-z])', s))
=======
    
>>>>>>> develop

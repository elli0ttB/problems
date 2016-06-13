
"""
determine whether two strings are anagrams
"""

def are_anagrams(str1, str2):
    if type(str1) is not str:
        return False
    if type(str2) is not str:
        return False
    str1 = str1.upper().replace(" ", "")
    str2 = str2.upper().replace(" ", "")
    return sorted(str1) == sorted(str2)

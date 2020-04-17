'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

"""
I would just use a regex so for fun solution, I guess its not valid here:
"""
import re

s = "th is so thth why not use th for th helth tH"
regex = re.findall("th", s)
print(len(regex))

"""Real Solution below
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

def count_th(word):
    if word == "th":
        return 1
    elif len(word) <= 2:
        return 0
    firstTwo = word[0:2]
    following = word[1:]

    return count_th(firstTwo) + count_th(following)

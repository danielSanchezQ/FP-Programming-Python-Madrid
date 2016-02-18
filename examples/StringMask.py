from examples.GeneratorsExample import zipWith
#from examples.Composition import comp
from functools import reduce

"""
STRING MASK
CHALLENGE DESCRIPTION:

You’ve got a binary code which has to be buried among words in order to unconsciously pass the cipher.
Create a program that would cover the word with a binary mask. If, while covering, a letter finds itself as 1,
you have to change its register to the upper one, if it’s 0, leave it as it is.
Words are always in lower case and in the same row with the binary mask.

Input Example

hello 11001
world 10000
cba 111

Output Example
HEllO
World
CBA
"""

def comp(*args):
    def compose(f, g):
        def wrapperArgsFunction(*args, **kwargs):
            return f(g(*args, **kwargs))
        return wrapperArgsFunction
    return reduce(compose, args)

def parse(line):
    text, mask = line.strip().split(" ")
    return text, mask

def checkToUpper(letter, maskValue):
    return letter if maskValue == '0' else letter.upper()

def applyCheckToUpper(data):
    return zipWith(checkToUpper, *data)

doIt = comp(lambda x: "".join(x), applyCheckToUpper, parse)


if __name__ == "__main__":
    from itertools import tee
    with open("inputs/string_mask.txt", 'r') as f:
        l1, l2 = tee(f.readlines())
        for rl, l in zip(map(doIt, l1), l2):
            print("{:25} {:25}".format(*list(parse(l))), rl)

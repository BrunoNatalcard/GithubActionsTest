# You are given an input string 'S'. Your task is to find 
# and return all possible permutations of the input string
# Note: After, try to implement it without duplicates

# Obs: Try to use ARGParse to help in tests of github actions
# Obs2: Link the folder to github and use pull/push commands
import math
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-e", "--echo", help="echo the string u use here")
parser.add_argument("-s", "--square", help="display the square of a given number", type=int)
parser.add_argument("-p", "--phrase", help="string to test code")
args = parser.parse_args()

if args.echo:
    print (args.echo)
if args.square:
    print (args.square**2)
if args.phrase:
    stringS = args.phrase
else:
    stringS = "abc"

def noDualPermut(stringS):
    """
    Returns a set of unique permutations of the given string.
    """
    if len(stringS) == 1:
        return [stringS]
    result = []
    used_chars = []
    for i in range(len(stringS)):
        if stringS[i] in used_chars:
            continue
        used_chars.append(stringS[i])
        for perm in noDualPermut(stringS[:i] + stringS[i+1:]):
            result.append(stringS[i] + perm)
    return result

result3 = noDualPermut(stringS)

print (result3)
print (len(result3))
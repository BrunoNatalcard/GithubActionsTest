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

def find_permutations(stringS):
    if len(stringS) == 0:
        return []

    if len(stringS) == 1:
        return [stringS]

    result = []
    for each in range(len(stringS)):
        letter = stringS[each]
        subStringS = stringS[:each] + stringS[each+1:]
        subPermutations = find_permutations(subStringS)
        for permutation in subPermutations:
            result.append(letter + permutation)
    return result

result = find_permutations(stringS)

#print (result)
print (len(result))


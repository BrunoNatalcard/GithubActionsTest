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


print (len(stringS))
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', default=False, action='store_true', help='force noise when not at booming time')
parser.add_argument('-d', '--debug', default=False, action='store_true', help='short silent interval for debugging')
args = parser.parse_args()
print(args.force)
print(args.debug)
if(args.debug):
    print("ITS REAL")
else:
    print("BULLSHIT")
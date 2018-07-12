import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--base", help="1")
parser.add_argument("--local", help="2")
args = parser.parse_args()

if args.base:
    print('base install')
if args.local:
    print('local install')
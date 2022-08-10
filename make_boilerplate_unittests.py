'''
Script to generate empty unit tests for all functions in a script/module

Author: Chris Pyatt
'''

from inspect import getmembers, isfunction
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    --module, required=True, help='The module to generate empty tests for.'
)
parser.add_argument(
    --outfile, default='test_boilerplate.py', help='The filename to write output tests to.'
)

args = parser.parse_args()

import args.module 
 
with open(args.outfile, 'w') as fh:
    output = f'from {args.module} import *\nimport unittest\n\n\nclass TestModule(unittest.TestCase):\n'
    for i in getmembers(args.module, isfunction):
            f = i[0]
            test = f'\tdef test_{f}(self):\n\t\tpass\n\n'
            output = f'{output}{test}'
    output = f'{output}\nif __name__ == \'__main__\':\n\tunittest.main()\n'
    fh.write(output)


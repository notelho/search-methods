
# import sys

# print('Number of arguments:', len(sys.argv), 'arguments.')

# print('Argument List:', str(sys.argv))

# from classes.breadth_first import BreadthFirst

# a =  BreadthFirst([[1, 2, 3], ['x', 8, 4], [7, 6, 5]], [[1, 2, 3], [8, 'x', 4], [7, 6, 5]])


# import argparse

# parser = argparse.ArgumentParser(description='Search some files')

# parser.add_argument(dest='filenames', metavar='filename', nargs='*')

# parser.add_argument('-p', '--pat', metavar='pattern',
#                     required=True, dest='patterns',
#                     action='append',
#                     help='text pattern to search for')

# parser.add_argument('-v', dest='verbose',
#                     action='store_true', help='verbose mode')

# parser.add_argument('-o', dest='outfile', action='store', help='output file')

# parser.add_argument('--speed', dest='speed',
#                     action='store', choices={'slow', 'fast'},
#                     default='slow', help='search speed')

# args = parser.parse_args()

# print(parser.parse_args())

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-s', action='store', dest='simple_value',
                    help='Store a simple value')

parser.add_argument('-c', action='store_const', dest='constant_value',
                    const='value-to-store',
                    help='Store a constant value')

parser.add_argument('-t', action='store_true', default=False,
                    dest='boolean_switch',
                    help='Set a switch to true')
parser.add_argument('-f', action='store_false', default=False,
                    dest='boolean_switch',
                    help='Set a switch to false')

parser.add_argument('-a', action='append', dest='collection',
                    default=[],
                    help='Add repeated values to a list',
                    )

parser.add_argument('-A', action='append_const', dest='const_collection',
                    const='value-1-to-append',
                    default=[],
                    help='Add different values to list')
parser.add_argument('-B', action='append_const', dest='const_collection',
                    const='value-2-to-append',
                    help='Add different values to list')

parser.add_argument('--version', action='version', version='%(prog)s 1.0')

results = parser.parse_args()
print('simple_value     =', results.simple_value)
print('constant_value   =', results.constant_value)
print('boolean_switch   =', results.boolean_switch)
print('collection       =', results.collection)
print('const_collection =', results.const_collection)

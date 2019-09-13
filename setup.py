from src.classes.depth_first import DepthFirst
import argparse
import sys

sys.setrecursionlimit(100000)

search = DepthFirst([[2, 'x', 3], [1, 8, 4], [7, 6, 5]],
               [[1, 2, 3], [8, 'x', 4], [7, 6, 5]])

parser = argparse.ArgumentParser()

# --verbose | ativa logs
# -t, --test | roda teste facil/medio/dificil
# -o, --output | gera um arquivo com os logs
# -m, --method | escolhe o tipo de busca que vai realizar
# -i, --input | ativa input de uma matriz


# parser.add_argument('-m', '--method', action='store', dest='simple_value',
#                     help='Store a simple value')

# parser.add_argument('-c', action='store_const', dest='constant_value',
#                     const='value-to-store',
#                     help='Store a constant value')

# parser.add_argument('-t', action='store_true', default=False,
#                     dest='boolean_switch',
#                     help='Set a switch to true')
# parser.add_argument('-f', action='store_false', default=False,
#                     dest='boolean_switch',
#                     help='Set a switch to false')

# parser.add_argument('-a', action='append', dest='collection',
#                     default=[],
#                     help='Add repeated values to a list',
#                     )

# parser.add_argument('-A', action='append_const', dest='const_collection',
#                     const='value-1-to-append',
#                     default=[],
#                     help='Add different values to list')
# parser.add_argument('-B', action='append_const', dest='const_collection',
#                     const='value-2-to-append',
#                     help='Add different values to list')

parser.add_argument('--version', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

# print('simple_value     =', args.simple_value)

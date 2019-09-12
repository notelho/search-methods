from copy import copy, deepcopy

final = [[1, 2, 3], [8, 'x', 4], [7, 6, 5]]

lf = []

la = [[[2, 3, 4], [1, 8, 5], ['x', 7, 6]]]

def run():

    global la

    if not equal():

        next()

        run()

    else:

        print('got it: ' + str(la[0]))


def equal():

    global la

    if la[0] == final:

        return True

    return False


def next():

    global la, final

    if(len(la) > 0):

        print('next: ' + str(la[0]))

        move()

    else:

        print('not found')


def move():

    global la, lf

    for i in range(len(la[0])):

        for j in range(len(la[0][i])):

            if la[0][i][j] == 'x':

                insert((j - 1 > -1), i, j, i, j - 1)

                insert((i + 1 < len(la[0])), i, j, i + 1, j)

                insert((j + 1 < len(la[0][i])), i, j, i, j + 1)

                insert((i - 1 > -1), i, j, i - 1, j)

                lf.append(deepcopy(la[0]))

                la = la[1:]

                break


def insert(condition, fromi, fromj, toi, toj):

    global la, lf

    if(condition):

        a = deepcopy(la[0])

        b = a[fromi][fromj]

        a[fromi][fromj] = a[toi][toj]

        a[toi][toj] = b

        contains = False

        for closed in lf:

            if a == closed:

                contains = True

        if not contains:

            la.append(a)


run()
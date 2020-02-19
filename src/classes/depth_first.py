# from copy import copy, deepcopy


# class DepthFirst:

#     final = []

#     la = []

#     lf = []

#     def __init__(self, initial, final):
#         self.final = final
#         self.la.append(initial)
#         self.run()

#     def run(self):
#         if not self.equal():
#             self.next()
#             self.run()
#         else:
#             print('got it: ' + str(self.la[0]))

#     def equal(self):
#         if self.la[0] == self.final:
#             return True
#         return False

#     def next(self):
#         if(len(self.la) > 0):
#             print('next: ' + str(self.la[0]))
#             self.move()
#         else:
#             print('not found')

#     def move(self):
#         for i in range(len(self.la[0])):
#             for j in range(len(self.la[0][i])):
#                 if self.la[0][i][j] == 'x':

#                     if self.canMove('left', i, j):
#                         self.insert(i, j, i, j - 1)
#                         self.run()
#                         self.lf.append(deepcopy(self.la[0]))
#                         self.la = self.la[1:]


#                     if self.canMove('bottom', i, j):
#                         self.insert(i, j, i + 1, j)
#                         self.run()
#                         self.lf.append(deepcopy(self.la[0]))
#                         self.la = self.la[1:]


#                     if self.canMove('right', i, j):
#                         self.insert(i, j, i, j + 1)
#                         self.run()
#                         self.lf.append(deepcopy(self.la[0]))
#                         self.la = self.la[1:]


#                     if self.canMove('top', i, j):
#                         self.insert(i, j, i - 1, j)
#                         self.run()
#                         self.lf.append(deepcopy(self.la[0]))
#                         self.la = self.la[1:]

#                     break

#     def insert(self, fromi, fromj, toi, toj):
#         matrice = deepcopy(self.la[0])
#         pos = matrice[fromi][fromj]
#         matrice[fromi][fromj] = matrice[toi][toj]
#         matrice[toi][toj] = pos
#         contains = False
#         for closed in self.lf:
#             if matrice == closed:
#                 contains = True
#         if not contains:
#             self.la.append(matrice)

#     def canMove(self, direction, i, j):
#         if direction is 'top':
#             return (i - 1 > -1)
#         elif direction is 'right':
#             return (j + 1 < len(self.la[0][i]))
#         elif direction is 'left':
#             return (j - 1 > -1)
#         elif direction is 'bottom':
#             return (i + 1 < len(self.la[0]))
#         else:
#             return None


# # search = BreadthFirst([[1, 2, 3], ['x', 8, 4], [7, 6, 5]], [[1, 2, 3], [8, 'x', 4], [7, 6, 5]])



class Solution(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __is_valid_move(self, pos):
        if 0 <= pos[0] < len(self.matrix) and 0 <= pos[1] < len(self.matrix[0]) and self.matrix[pos[0]][pos[1]] is not None:
            return True
        return False

    def spiral_print(self):
        action_seq = [(0,+1), (+1, 0), (0, -1), (-1, 0)]
        curr = (0, 0)
        act = 0
        results = []
        totalGridNum = len(self.matrix) * len(self.matrix[0])
        results.append(self.matrix[curr[0]][curr[1]])

        while True:
        
            self.matrix[curr[0]][curr[1]] = None
            next_move = (curr[0] + action_seq[act][0], curr[1] + action_seq[act][1])

            if not self.__is_valid_move(next_move):
                act +=1
            else:
                results.append(self.matrix[next_move[0]][next_move[1]])
                curr = next_move

            if(act == len(action_seq)):
                act = 0

            if(len(results) == totalGridNum):
                return results



grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

print(Solution(grid).spiral_print())

# print(grid)





# core = (0,1)
# action_seq = [(0, +1), (+1, 0), (0, -1), (-1, 0)]

# print(action_seq[2][1])






# class Solution:
#     def matrix_spiral_print(self, grid):

#         isHorizontal = True
#         isGoingRevert = False
#         horizontalGoal = len(grid)
#         verticalGoal = len(grid[0]) - 1

#         horizontalStart = verticalStart = 0
#         totalGoal = horizontalGoal * verticalGoal
#         totalStart = 0

#         while totalStart <= totalGoal:

#             if(isHorizontal):
#                 print(grid[verticalStart][horizontalStart])
                
#                 totalStart += 1

#                 if(horizontalStart == horizontalGoal):
#                     isHorizontal = False
#                     horizontalGoal -= 1

#                     if(isGoingRevert):
#                         verticalStart = verticalGoal
#                     else:
#                         verticalStart = 0

#                 else:
#                     if(isGoingRevert):
#                         horizontalStart -= 1
#                     else:
#                         horizontalStart += 1
                

#             if(not isHorizontal):
#                 print(grid[verticalStart][horizontalStart])
                
#                 totalStart += 1

#                 if(verticalStart == verticalGoal):
#                     isHorizontal = True
#                     verticalGoal -= 1

#                     if(isGoingRevert):
#                         horizontalStart = horizontalGoal
#                     else:
#                         horizontalStart = 0
#                     isGoingRevert = not GoingRevert
                
#                 else:
#                     if(isGoingRevert):
#                         verticalStart -= 1
#                     else:
#                         verticalStart += 1


# import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []

    for i, row in enumerate(beliefs):
        new_row = []
        for j, cell in enumerate(row):
            if grid[i][j] == color:
                new_beliefs(cell * p_hit)
            else:
                new_beliefs(cell * p_miss)
        new_row.append(new_beliefs)
    new_beliefs.append(new_row)

    #정규화 과정을 통해 확률을 합쳐서 1로 만들어준다.
    total_belief = sum(sum(row) for row in new_beliefs)
    for i in range(len(new_beliefs)):   #각 행에 대해
        for j in range(len(new_beliefs[i])):    #각 열에 대해
            new_beliefs[i][j] /= total_belief #정규화


    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % height
            new_j = (j + dx ) % width
            # pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)
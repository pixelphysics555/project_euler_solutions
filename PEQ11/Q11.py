import numpy as np

with open('20x20GridPE11.txt', 'r') as Grid:
    lines = Grid.readlines()

new_lines = []
for line in lines:
    line = line.replace('\n', '')
    line = line.split(' ')
    for i in range(len(line)):
        line[i] = int(line[i])
    new_lines.append(line)

grid = np.array(new_lines)

# print(grid)

def mult_iter(ls):
    """Behaves like sum() function.
    Returns product of all the members of an iterable."""
    prod = 1
    for i in range(len(ls)):
        prod *= ls[i]
    return prod

def horz_prod():
    prod_list = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j + 3) not in range(len(grid[i])):
                break
            prod = mult_iter(grid[i, j:j + 4])
            prod_list.append(prod)
    return prod_list


def vert_prod():
    grid_t = grid.T # Transpose the array and use horz_prod().
    prod_list = []
    for i in range(len(grid_t)):
        for j in range(len(grid_t[i])):
            if (j + 3) not in range(len(grid_t[i])):
                break
            prod = mult_iter(grid_t[i, j:j + 4])
            prod_list.append(prod)
    return prod_list

def ldiag_prod(): # top left, bottom right; matrix left diag
    prod_list = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j + 3) not in range(len(grid[i])) or \
            (i + 3) not in range(len(grid)):
                break
            fourbyfour = grid[i:i + 4, j:j + 4]
            fbf_ldiag = []
            for k in range(len(fourbyfour)):
                fbf_ldiag.append(fourbyfour[k][k])
            prod = mult_iter(fbf_ldiag)
            prod_list.append(prod)
    return prod_list

def rdiag_prod(): # bottom left, top right; matrix right diag
    prod_list = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j + 3) not in range(len(grid[i])) or \
            (i + 3) not in range(len(grid)):
                break
            fourbyfour = grid[i:i + 4, j:j + 4]
            fbf_rdiag = []

            for k in range(len(fourbyfour)):
                for l in range(len(fourbyfour[k])):
                    if k + l == 3:
                        fbf_rdiag.append(fourbyfour[k][l])
            prod = mult_iter(fbf_rdiag)
            prod_list.append(prod)

    return prod_list

print(max(max(horz_prod()), max(vert_prod()), \
    max(ldiag_prod()), max(rdiag_prod())))

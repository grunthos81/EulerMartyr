import copy
grid = []
f = open("p081_matrix.txt", "r")
for line in f.readlines():
    grid.append([int(i) for i in line.strip().split(',')])

        
def p82(grid1, size):
    grid2 = copy.deepcopy(grid1)
    
    for y in range(1, size):
        for x in range(size-1,-1,-1):
            if y == size-1:
                grid2[x][y] += grid2[x][y-1]
            elif x == size-1:
                grid2[x][y] = grid2[x][y-1] + grid1[x][y]
            else:
                across = grid2[x][y-1]
                up = grid2[x+1][y]
                grid2[x][y] += min(across, up)
                
        for z in range(0, size):
            original = grid1[z][y]
            above = grid2[z-1][y]
            current = grid2[z][y]
            if original + above < current:
                grid2[z][y] = original + above
                
    return min([grid2[i][size-1] for i in range(0, size)])

answer = p82(grid, 80)
print(answer)




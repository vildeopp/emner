
grid = [['.', '.', '.', '.', '.', '.'],
      ['.', 'O', 'O', '.', '.', '.'],
      ['O', 'O', 'O', 'O', '.', '.'],
      ['O', 'O', 'O', 'O', 'O', '.'],
      ['.', 'O', 'O', 'O', 'O', 'O'],
      ['O', 'O', 'O', 'O', 'O', '.'],
      ['O', 'O', 'O', 'O', '.', '.'],
      ['.', 'O', 'O', '.', '.', '.'],
      ['.', '.', '.', '.', '.', '.']]

newGrid = []

for rows in grid: 
    newGrid.append([])

for y in range(len(grid)):
    for x in range(len(grid[0])): 
        newGrid[x].append(grid[y][x])

for line in newGrid: 
    print("".join(line))




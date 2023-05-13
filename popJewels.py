def countJewels(grid, row, col, color, count):
    if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]):
        return
    if grid[row][col] == 0 or grid[row][col] != color:
        return
    if grid[row][col] == color:
        counter = count[len(count) - 1] + 1
        count.append(counter)
        grid[row][col] = 0
        countJewels(grid, row + 1, col, color, count)
        countJewels(grid, row - 1, col, color, count)
        countJewels(grid, row, col + 1, color, count)
        countJewels(grid, row, col - 1, color, count)


def countExplodedGems(rows, cols, gems, hits):
    grid = [[0] * cols for _ in range(rows)]

    for gem in gems:
        row, col, color = gem
        grid[row][col] = color

    ExplodedGems = 0
    for hit in hits:
        # Last value of count is the number of explodes jewels
        count = [0]

        countJewels(grid, hit[0], hit[1],
                    grid[hit[0]][hit[1]], count)

        ExplodedGems += count[len(count) - 1]

    return ExplodedGems


rows = 8
cols = 9
gems = [[1, 2, 1], [1, 3, 1], [1, 4, 1], [1, 5, 1], [1, 6, 1], [1, 7, 1], [2, 2, 1], [2, 3, 2], [2, 4, 2], [2, 5, 2], [2, 6, 2], [2, 7, 1], [3, 2, 1], [3, 3, 2], [3, 4, 1], [3, 5, 1], [3, 6, 2], [3, 7, 1], [
    4, 2, 1], [4, 3, 2], [4, 4, 1], [4, 5, 1], [4, 6, 2], [4, 7, 1], [5, 2, 1], [5, 3, 2], [5, 4, 2], [5, 5, 2], [5, 6, 2], [5, 7, 1], [6, 2, 1], [6, 3, 1], [6, 4, 1], [6, 5, 1], [6, 6, 1], [6, 7, 1]]
hits = [[3, 4]]

print('Test 1: ' + str(countExplodedGems(rows, cols, gems, hits)))

rows = 8
cols = 9
gems = [[1, 2, 1], [1, 3, 1], [1, 4, 1], [1, 5, 1], [1, 6, 1], [1, 7, 1], [2, 2, 1], [2, 3, 2], [2, 4, 2], [2, 5, 2], [2, 6, 2], [2, 7, 1], [3, 2, 1], [3, 3, 2], [3, 4, 1], [3, 5, 1], [3, 6, 2], [3, 7, 1], [
    4, 2, 1], [4, 3, 2], [4, 4, 1], [4, 5, 1], [4, 6, 2], [4, 7, 1], [5, 2, 1], [5, 3, 2], [5, 4, 2], [5, 5, 2], [5, 6, 2], [5, 7, 1], [6, 2, 1], [6, 3, 1], [6, 4, 1], [6, 5, 1], [6, 6, 1], [6, 7, 1]]
hits = [[3, 4], [2, 4], [4, 4], [0, 0]]
print('Test 2: ' + str(countExplodedGems(rows, cols, gems, hits)))


rows = 7
cols = 12
gems = [[2, 6, 1], [0, 6, 1], [4, 6, 1], [4, 10, 2], [5, 8, 2], [2, 11, 2], [0, 7, 1], [2, 5, 1], [2, 7, 1], [5, 7, 1], [3, 8, 2], [5, 10, 2], [2, 4, 1], [0, 10, 2], [2, 9, 2], [0, 8, 2], [0, 9, 2], [
    3, 11, 2], [4, 5, 1], [1, 8, 2], [5, 5, 1], [3, 10, 2], [2, 2, 1], [4, 8, 2], [3, 6, 1], [1, 10, 2], [4, 9, 2], [5, 6, 1], [2, 8, 2], [3, 5, 1], [2, 3, 1], [2, 10, 2], [3, 7, 1], [4, 7, 1], [0, 5, 1]]
hits = [[2, 2], [2, 9], [2, 2], [0, 0], [0, 1], [0, 2], [0, 3]]


print('Test 3: ' + str(countExplodedGems(rows, cols, gems, hits)))

from itertools import product


def matrix_to_set(matrix):
    s = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]:
                s.add((i, j))

    return s


def set_to_table(s):
    if not set:
        mi = mj = ni = nj = 0
    else:
        mi = min(map(lambda x: x[0], s))
        mj = min(map(lambda x: x[1], s))
        ni = max(map(lambda x: x[0], s))
        nj = max(map(lambda x: x[1], s))

    table = [[0 for _ in range(nj - mj + 1)] for _ in range(ni - mi + 1)]

    for (i, j) in s:
        table[i - mi][j - mj] = 1

    return table


def get_generation(cells, generations):
    _cells = matrix_to_set(cells)

    for _ in range(generations):
        cells_neighbours = set()
        new_cells = set()

        for (i, j) in _cells:
            for (di, dj) in product((-1, 0, 1), (-1, 0, 1)):
                cells_neighbours.add((i + di, j + dj))

        for (i, j) in cells_neighbours:
            neighbours = 0
            for (di, dj) in product((-1, 0, 1), (-1, 0, 1)):
                if (i + di, j + dj) in _cells and (di, dj) != (0, 0):
                    neighbours += 1

            if neighbours == 3:
                new_cells.add((i, j))
            elif neighbours == 2 and (i, j) in _cells:
                new_cells.add((i, j))

        cells = new_cells

    return set_to_table(cells)


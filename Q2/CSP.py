from copy import deepcopy

import numpy as np


class CSP:
    def __init__(self, n):
        """
        Here we initialize all the required variables for the CSP computation,
        according to the n.
        """
        # Your code here
        self.n = n
        self.grid = np.array(np.zeros(shape=(n, n), dtype=int))
        self.domain = np.array(np.ones(shape=(n, n), dtype=int))
        self.number_of_iteration = 0

    def check_constraints(self) -> bool:
        """
        Here we check the grid horizontally, vertically and diagonally
        """
        col = 0
        grids = self.grid
        for i in range(self.n):
            if np.count_nonzero(grids[i] == 1) > 1:
                return False

        one_count = 0
        for i in range(self.n):
            for j in range(self.n):
                if grids[j][i] == 1:
                    one_count += 1
            if one_count > 1:
                return False
            one_count = 0

        one_count = 0
        for i in range(self.n):
            y_index = 0
            x_index = i
            while True:
                if y_index >= self.n or x_index >= self.n:
                    break
                if grids[y_index][x_index] == 1:
                    one_count += 1
                y_index += 1
                x_index += 1
            if one_count > 1:
                return False
            one_count = 0

        one_count = 0
        for i in range(self.n):
            y_index = i
            x_index = 0
            while True:
                if y_index >= self.n or x_index >= self.n:
                    break
                if grids[y_index][x_index] == 1:
                    one_count += 1
                y_index += 1
                x_index += 1
            if one_count > 1:
                return False
            one_count = 0

        one_count = 0
        for i in range(self.n):
            y_index = 0
            x_index = i
            while True:
                if y_index >= self.n or x_index < 0:
                    break
                if grids[y_index][x_index] == 1:
                    one_count += 1
                y_index += 1
                x_index -= 1
            if one_count > 1:
                return False
            one_count = 0

        one_count = 0
        for i in range(self.n):
            y_index = i
            x_index = self.n - 1
            while True:
                if y_index >= self.n or x_index < 0:
                    break
                if grids[y_index][x_index] == 1:
                    one_count += 1
                y_index += 1
                x_index -= 1
            if one_count > 1:
                return False
            one_count = 0
        return True

        pass

    def forward_check(self, i):
        """
        After assigning a queen to ith column, we can make a forward check
        to boost up the computing speed and prune our search tree.
        """
        pass

    def assign(self, row, column):
        """
        assign 1 to self.grid[row,colmn]
        """
        self.grid[row][column] = 1
        # fill me
        pass

    def _solve_problem_with_backtrack(self, i):
        """
         In this function we should set the ith queen in ith column and call itself recursively to solve the problem.
        """
        # Your code here
        self.number_of_iteration += 1
        if self.check_constraints() is False:
            return False, self.grid
        elif i == self.n:
            return True, self.grid
        for j in range(self.n):
            self.assign(i, j)
            if self._solve_problem_with_backtrack(i + 1)[0] is True:
                return True, self.grid
            self.grid[i][j] = 0
        return False, self.grid

    def solve_problem_with_backtrack(self):
        """
         In this function we should set the ith queen in ith column and call itself recursively to solve the problem
         and return solution's grid
        """
        result = self._solve_problem_with_backtrack(0)
        if result[0] is True:
            self.number_of_iteration -= 1
            return result[1]
        return None

    def _solve_problem_with_forward_check(self, i):
        """
         In this function we should set the ith queen in ith column and call itself recursively to solve the problem.
        """
        # Your code here
        if self.check_constraints() is False:
            return False, self.grid
        elif i == self.n:
            return True, self.grid
        for j in range(self.n):
            if self.grid[i][j] == 2:
                continue
            self.assign(i, j)
            self.number_of_iteration += 1
            new = deepcopy(self.grid)
            self.filter(i, j, 2, new)
            if self._solve_problem_with_forward_check(i + 1)[0] is True:
                return True, self.grid
            self.grid[i][j] = 0
            self.filter(i, j, 0, new)
        return False, self.grid

    def filter(self, i, j, value, new):
        for k in range(self.n):
            if k != i and self.grid[k][j] != 1:
                if (value == 0 and new[k][j] == 0) or value == 2:
                # if value == 2 and self.grid[k][j] == 0:
                #     new_grid[k][j] = f"{i}{j}"
                # if value == 0 and new_grid[k][j] != f"{i}{j}":
                #     continue
                    self.grid[k][j] = value
        for z in range(self.n):
            if z != j and self.grid[i][z] != 1:
                if (value == 0 and new[i][z] == 0) or value == 2:
                # if value == 2 and self.grid[i][z] == 0:
                #     new_grid[i][z] = f"{i}{j}"
                # if value == 0 and new_grid[i][z] != f"{i}{j}":
                #     continue
                    self.grid[i][z] = value
        k = i + 1
        z = j + 1
        while True:
            if k >= self.n or z >= self.n:
                break
            else:
                if self.grid[k][z] != 1:
                    if (value == 0 and new[k][z] == 0) or value == 2:
                        self.grid[k][z] = value

                k += 1
                z += 1
        k = i - 1
        z = j - 1
        while True:
            if k < 0 or z < 0:
                break
            else:
                if self.grid[k][z] != 1:
                    if (value == 0 and new[k][z] == 0) or value == 2:
                        self.grid[k][z] = value
                k -= 1
                z -= 1
        k = i + 1
        z = j - 1
        while True:
            if k >= self.n or z < 0:
                break
            else:
                if self.grid[k][z] != 1:
                    if (value == 0 and new[k][z] == 0) or value == 2:
                        self.grid[k][z] = value
                k += 1
                z -= 1
        k = i - 1
        z = j + 1
        while True:
            if k < 0 or z >= self.n:
                break
            else:
                if self.grid[k][z] != 1:
                    if (value == 0 and new[k][z] == 0) or value == 2:
                        self.grid[k][z] = value
                k -= 1
                z += 1

    def solve_problem_with_forward_check(self):
        """
         In this function we should set the ith queen in ith column and call itself recursively to solve the problem
         and return solution's grid
        """
        new_grid = deepcopy(self.grid)
        result = self._solve_problem_with_forward_check(0)
        if result[0] is True:
            for i in range(self.n):
                for j in range(self.n):
                    if self.grid[i][j] == 2:
                        self.grid[i][j] = 0
            return result[1]
        return None

from random import randint
from os import system

class NQueen:
    def __init__(self, size):
        self.list_queens = list()
        # self.list_queens.append(4)
        # self.list_queens.append(5)
        # self.list_queens.append(6)
        # self.list_queens.append(3)
        # self.list_queens.append(4)
        # self.list_queens.append(5)
        # self.list_queens.append(6)
        # self.list_queens.append(5)
        for i in range(size):
            self.list_queens.append(randint(0, size - 1))

    def get(self, col):
        return self.list_queens[col]

    def put(self, row, col):
        self.list_queens[col] = row

    def pick_up(self, col):
        self.list_queens[col] = -1

    def is_conflict(self, col1, col2):
        if (self.list_queens[col1] == self.list_queens[col2]):
            return True

        if (abs(self.list_queens[col1] - self.list_queens[col2]) == abs(col1 - col2)):
            return True

        return False

    def count_conflicts_at(self, col):
        count = 0
        index = col + 1
        while (index < self.get_size()):
            if (self.is_conflict(col, index)):
                count = count + 1
            index = index + 1
        return count

    def count_conflicts(self):
        count = 0
        col = 0
        while (col < self.get_size()):
            count = count + self.count_conflicts_at(col)
            col = col + 1
        return count

    def get_size(self):
        return len(self.list_queens)

    def print(self, table = True):
        if (table == False):
            print(self.list_queens)
            return

        for i in range(self.get_size()):
            for j in range(self.get_size()):
                if (self.list_queens[j] == i):
                    print('1  ', end='')
                else:
                    print('0  ', end='')
            print()

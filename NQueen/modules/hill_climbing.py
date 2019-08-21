from modules.nqueen import NQueen
from random import randint
import sys

class HillClimbing:
    def __init__(self, nq):
        self.nqueen = nq
        self.max_conflict = int((self.nqueen.get_size() * (self.nqueen.get_size() - 1)) / 2)
        self.minimum_conflict = self.max_conflict
        self.data = list()
        self.make_table()
    
    def make_table(self):
        i = 0
        j = 0
        while (i < self.nqueen.get_size()):
            self.data.append(list())
            while (j < self.nqueen.get_size()):
                self.data[i].append(self.max_conflict)
                j = j + 1
            i = i + 1
    
    def attach_conflict_number(self):
        row = 0
        col = 0
        cell_list = list()
        excessive_end = 0

        while (row < self.nqueen.get_size()):
            while (col < self.nqueen.get_size()):
                prev = self.nqueen.get(col)
                if (prev == row):
                    continue
                self.nqueen.put(row, col)
                self.data[row][col] = self.nqueen.count_conflicts()
                if (self.minimum_conflict >= self.data[row][col]):
                    if (self.minimum_conflict > self.data[row][col]):
                        excessive_end = len(cell_list)
                        self.minimum_conflict = self.data[row][col]
                    cell_list.append((row, col))
                self.nqueen.put(prev, col)
                col = col + 1
            row = row + 1

        return cell_list[excessive_end:]
    
    def solve(self):
        while(self.minimum_conflict != 0):
            cell_list = self.attach_conflict_number()
            if (len(cell_list) == 0):
                break
                
            rand_cell = cell_list[(randint(0, len(cell_list) - 1))]
            self.nqueen.put(rand_cell[0], rand_cell[1])

    def print(self):
        for l in range(len(self.data)):
            print(self.data[l])

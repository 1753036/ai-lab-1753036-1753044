 
class Table:
    def __init__(self, row_count, col_count):
        self.row_count = row_count
        self.col_count = col_count
        self.data_table = [[0] * col_count] * row_count

    def print(self):
        print(len(self.data_table))
        for row in self.data_table:
            for val in row:
                print(val)

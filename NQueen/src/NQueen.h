#pragma once

#include <vector>
#include <iostream>
#include <ctime>
#include <cstdlib>

class NQueen {
private:
    std::vector<int> mQueens;

public:
    NQueen(const int& size);

    void restart();
    
    void setRow(const int& column, const int& row);

    const int& getRow(const int& column);

    bool isConflict(const int& first_column, const int& second_column);

    int countConflicts();

    int getSize();

    void print();

    friend class Genetic;
};
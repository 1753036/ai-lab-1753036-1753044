#include "HillClimbing.h"

HillClimbing::HillClimbing(NQueen& nqueen)
:   mNQueen(nqueen)
,   mMaximum((nqueen.getSize() * (nqueen.getSize() - 1)) / 2)
,   mMinimum(mMaximum)
{
}

std::vector<Cell> HillClimbing::attach()
{
    std::vector<Cell> cells;

    for (int row = 0; row < mNQueen.getSize(); ++row)
    {
        for (int col = 0; col < mNQueen.getSize(); ++col)
        {
            int cur = mNQueen.getRow(col);
            
            if (cur == row)
            {
                continue;
            }

            mNQueen.setRow(col, row);
            int count = mNQueen.countConflicts();
            if (count == mMinimum)
            {
                cells.push_back(Cell(row, col));
            }
            else if (count < mMinimum)
            {
                cells.clear();
                cells.push_back(Cell(row, col));
                mMinimum = count;
            }
            mNQueen.setRow(col, cur);
        }
    }

    return cells;
}

void HillClimbing::solve()
{
    while (mMinimum != 0)
    {
        std::vector<Cell> cells = attach();
        if (cells.size() == 0)
        {
            break;
        }

        int index = rand() % cells.size();
        mNQueen.setRow(cells[index].col, cells[index].row);
    }
}
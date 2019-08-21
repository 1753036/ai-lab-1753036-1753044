#include "NQueen.h"

NQueen::NQueen(const int& size)
{
    for (int i = 0; i < size; ++i)
    {
        mQueens.push_back(rand() % size);
    }
}

void NQueen::restart()
{
    for (int i = 0; i < mQueens.size(); ++i)
    {
        mQueens[i] = rand() % mQueens.size();
    }
}
    
void NQueen::setRow(const int& column, const int& row)
{
    mQueens[column] = row;
}

const int& NQueen::getRow(const int& column)
{
    return mQueens[column];
}

bool NQueen::isConflict(const int& firstColumn, const int& secondColumn)
{
    if (mQueens[firstColumn] == mQueens[secondColumn])
    {
        return true;
    }

    if (abs(mQueens[firstColumn] - mQueens[secondColumn]) == abs(firstColumn - secondColumn))
    {
        return true;
    }

    return false;
}

int NQueen::countConflicts()
{
    int count = 0;
    for (int i = 0; i < mQueens.size(); ++i)
    {
        for (int j = i + 1; j < mQueens.size(); ++j)
        {
            if (isConflict(i, j))
            {
                count = count + 1;
            }
        }
    }
    return count;
}

int NQueen::getSize()
{
    return mQueens.size();
}

void NQueen::print()
{
    for (int i = 0; i < mQueens.size(); ++i)
    {
        std::cout << mQueens[i] << ", ";
    }
    
    std::cout << std::endl;
}
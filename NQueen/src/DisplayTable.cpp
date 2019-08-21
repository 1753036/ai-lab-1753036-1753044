#include "DipslayTable.h"

DisplayTable::DisplayTable(NQueen& nqueen)
:   mNQueen(nqueen)
{
}

void DisplayTable::print()
{
    std::cout << std::endl;
    for (int row = 0; row < mNQueen.getSize(); ++row)
    {
        for (int col = 0; col < mNQueen.getSize(); ++col)
        {
            if (mNQueen.getRow(col) == row)
            {
                std::cout << "1, ";
            }
            else
            {
                std::cout << "0, ";
            }
        }
        std::cout << std::endl;
    }
}
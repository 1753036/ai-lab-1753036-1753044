#include "Genetic.h"

Genetic::Genetic(int numP, int size)
{
    for (int i = 0; i < numP; ++i)
    {
        mPop.push_back(NQueen(size));
    }
}

NQueen Genetic::reproduce(int x, int y)
{
    int c = rand() % mPop[x].getSize();
    NQueen child(mPop[x].getSize());

    for (int i = 0; i < c; ++i)
    {
        child.mQueens[i] = mPop[x].mQueens[i];
    }

    for (int i = c; i < child.getSize(); ++i)
    {
        child.mQueens[i] = mPop[y].mQueens[i];
    }

    return child;
}

int Genetic::diff(NQueen& q, int num)
{
    int count = 0;
    for (int i = 0; i < q.getSize(); ++i)
    {
        if (num == q.getRow(i))
        {
            count += 1;
        }
    }
    return count;
}

void Genetic::mutate(NQueen& q)
{
    int col = rand() % q.getSize();
    for (int i = 0; i < q.getSize(); ++i)
    {
        int row = rand() % q.getSize();
        std::cout << diff(q, row) << std::endl;
        if (diff(q, row) == 0)
        {
            q.setRow(col, row);
            return;
        }
    }
}

void Genetic::solve()
{
    for (int i = 0; i < 5; ++i)
    {
        for (int j = 0; j < mPop.size(); ++j)
        {

            int x = rand() % mPop.size();
            int y = rand() % mPop.size();
            while (x == y)
            {
                y = rand() % mPop.size();
            }

            reproduce(x, y).print();
        }
    }
}
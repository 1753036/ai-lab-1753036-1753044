#include "NQueen.h"

struct Cell
{
    int row;
    int col;

    Cell(int r, int c) 
    : row(r), col(c)
    {

    }
};

class HillClimbing {
private:
    NQueen& mNQueen;
    int mMaximum;
    int mMinimum;
public:
    HillClimbing(NQueen& nqueen);

    std::vector<Cell> attach();

    void solve();

    void print();
};
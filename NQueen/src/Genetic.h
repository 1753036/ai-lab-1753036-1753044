#include "NQueen.h"

class Genetic {
private:
    std::vector<NQueen> mPop;

public:
    Genetic(int numP, int size);

    NQueen reproduce(int x, int y);

    void mutate(NQueen& q);

    int diff(NQueen& q, int num);

    void select();

    void solve();
};
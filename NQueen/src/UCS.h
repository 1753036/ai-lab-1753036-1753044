#include "NQueen.h"
#include <stack>

// g(n) the minimum conflicts at one cell
// if we get stuck then undo the move
class UCS {
private:
    NQueen& mNQueen;
public:
    UCS(NQueen& nqueen);

    void solve();
};
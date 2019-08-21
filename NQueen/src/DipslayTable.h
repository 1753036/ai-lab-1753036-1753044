#include "NQueen.h"

typedef std::vector<std::vector<int>> inttable;
class DisplayTable {
private:
    NQueen& mNQueen;
public:
    DisplayTable(NQueen& nqueen);

    void print();
};
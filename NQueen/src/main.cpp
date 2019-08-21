#include "NQueen.h"
#include "HillClimbing.h"
#include "DipslayTable.h"
#include "Genetic.h"
#include "UCS.h"
#include <chrono>

#define StartClock(name) clock_t name = clock()

#define PrintExecutionTime(name) std::cout << (double)(clock() - name) / CLOCKS_PER_SEC << "s" << std::endl

void tryUCS(int n)
{
    StartClock(start);

    NQueen nqueen(n);
    UCS ucs(nqueen); 
    ucs.solve();
    std::cout << nqueen.countConflicts() << std::endl;

    PrintExecutionTime(start);
}

void tryHillClimbing(int n)
{
    StartClock(start);

    NQueen nqueen(n);
    HillClimbing hc(nqueen);
    hc.solve();
    std::cout << nqueen.countConflicts() << std::endl;

    PrintExecutionTime(start);
}

void tryGenetic(int n)
{
    std::cout << "WTF" << std::endl;
    StartClock(start);
    Genetic gen(4, n);
    gen.solve();
    PrintExecutionTime(start);
}

int main()
{
    srand(time(nullptr));
    tryGenetic(10);
    tryHillClimbing(10);
    return 0;
}
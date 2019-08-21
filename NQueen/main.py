from modules.nqueen import NQueen
from modules.hill_climbing import HillClimbing
from random import randint
import time

nq = NQueen(10)
start = time.time()

hc = HillClimbing(nq)
hc.solve()
hc.print()
nq.print()

end = time.time()
print(end - start)
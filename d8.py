
import pyquil.quil as pq
import pyquil.api as api
from pyquil.gates import *
qvm = api.SyncConnection()
p = pq.Program()

#takes a classical registry of 3 bits, converts to base-10 number.
def bittonum(L):
    num = 1
    for index, bit in enumerate(L[0]):
        num += bit * (2 ** index)
    return num

def throw_octahedral_die():
    qubit_num = 3
    for i in range(qubit_num):
            p.inst(H(i))

    p.measure(0,0).measure(1,1).measure(2,2)

    return bittonum(qvm.run(p,range(3)))

print throw_octahedral_die()

import pyquil.quil as pq
import pyquil.api as api
from pyquil.gates import *
from numpy import log2, ceil
qvm = api.SyncConnection()
p = pq.Program()

#takes a classical registry of 3 bits, converts to base-10 number.
def bittonum(L):
    num = 1
    for index, bit in enumerate(L[0]):
        num += bit * (2 ** index)
    return num

#Returns a random number in range(1,8)
def throw_octahedral_die():
    qubit_num = 3
    for i in range(qubit_num):
            p.inst(H(i))

    p.measure(0,0).measure(1,1).measure(2,2)

    return bittonum(qvm.run(p,range(3)))


#Returns a random number between 1 and num_sides.
#Would be nice to have a slicker method. This rerolls if the number is too high.
def throw_polyhedral_die(num_sides):
    qubit_num = int(ceil(log2(num_sides)))
    for i in range(qubit_num):
            p.inst(H(i)).measure(i,i)
    roll = bittonum(qvm.run(p,range(qubit_num)))
    while roll > num_sides:
        roll = bittonum(qvm.run(p,range(qubit_num)))
    return roll

for i in range(10):
    print throw_polyhedral_die(150)
#print throw_octahedral_die()

import pyquil.quil as pq
import pyquil.api as api
from pyquil.gates import *
qvm = api.SyncConnection()
p = pq.Program()

p.inst(H(0), CNOT(0,1))

wvf, _ = qvm.wavefunction(p)

print wvf 

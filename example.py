import numpy as np
import QUBO2Ising as qb


QUBO_array = np.genfromtxt('example.csv', delimiter=',')
h, J = qb.QUBO2Ising(QUBO_array).generateIsing()

print(h, J)

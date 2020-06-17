Hello!

This is my first try at Object Oriented Programming.

Uploading something simple to try out and play with the platform.

## To install:
<code>pip install QUBO2Ising</code>

## Example code:

<code>import numpy as np
  
import QUBO2Ising as qb

QUBO_array = np.genfromtxt('example.csv', delimiter=',')

h, J = qb.QUBO2Ising(QUBO_array).generateIsing()

print(h, J)</code>

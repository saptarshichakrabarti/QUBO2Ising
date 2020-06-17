Hello!

This is my first try at Object Oriented Programming.

Uploading something simple to try out and play with the platform.

## To install:
<code>pip install QUBO2Ising</code>

## Example code:

<code>import numpy as np\n
import QUBO2Ising as qb\n
QUBO_array = np.genfromtxt('example.csv', delimiter=',')\n
h, J = qb.QUBO2Ising(QUBO_array).generateIsing()\n
print(h, J)</code>

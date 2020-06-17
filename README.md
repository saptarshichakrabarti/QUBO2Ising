Hello!

This is my first try at Object Oriented Programming.

Uploading something simple to try out and play with the platform.

## To install:
<code>pip install QUBO2Ising</code>

## Example code:

<code>import numpy as np</code>

<code>import QUBO2Ising as qb</code>

<code>QUBO_array = np.genfromtxt('example.csv', delimiter=',')</code></code>

<code>h, J = qb.QUBO2Ising(QUBO_array).generateIsing()</code>

<code>print(h, J)</code>

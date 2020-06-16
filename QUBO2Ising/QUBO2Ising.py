import numpy as np

class QUBO2Ising:
    
    """
    Module to generate Ising model from a QUBO array.
    
    Attributes:
            h (dict)
            J (dict)
    """
    
    def __init__(self, QUBO_array, h={}, J={}):
        self.QUBO_array = QUBO_array
        self.h = h
        self.J = J
        
    def generateIsing(self):
    
        # removing indices
        data = np.delete(self.QUBO_array, 0,0)
        data = np.delete(data, 0,1)
    
        r, c = data.shape
    
        #check for square matrix
        while not r == c:
            print("Not a square matrix.")
        
        # generating dictionary of 'h' (diagonal) values
        for i in range(r):
            self.h[i] = np.diag(data)[i]
        
        # generating dictionary of 'J' (upper triangle) values
        keys_J = []
        values_J = []
        for i in range(r):
            for j in range(c):
                if i<j:
                    xy =(i,j)
                    keys_J.append(xy)
                    values_J.append(data[i,j])
                    j += 1

        self.J = dict(zip(keys_J, values_J))
    
        return self.h, self.J
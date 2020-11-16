# animation nodes script for generating mandelbulb mask

import numpy as np

gridArray = grid.asNumpyArray().reshape(-1,3)
gx, gy, gz = gridArray[:,0], gridArray[:,1], gridArray[:,2]

def createMask(gx, gy, gz):
    n = iteration
    x, y, z = gx, gy, gz
    
    for i in range(n):
        r = x*x + y*y + z*z
        theta = np.arctan2(np.sqrt(x*x + y*y), z) + offset
        phi = np.arctan2(y, x) + offset
        #pow = (r**n).clip(-100000,100000)
        pow = (r**n)
        
        x = pow * np.sin(theta*n) * np.cos(phi*n) + gx
        y = pow * np.sin(theta*n) * np.sin(phi*n) + gy
        z = pow * np.cos(theta*n)+ gz
        
    return np.sqrt(x*x + y*y + z*z) < n

maskArray = createMask(gx, gy, gz)
mask = BooleanList.fromNumpyArray(maskArray.astype('b'))

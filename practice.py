import numpy as np

rg = np.random.default_rng()
a = np.floor(10 * rg.random((3, 4)))
c = a.view()

print(c.base is a)        
# print(c.base is a)   


a1 = np.arange(12)**2

j = np.array([[3, 4], [9, 7]])
# Indexing with arrays index 
print(a1[j])

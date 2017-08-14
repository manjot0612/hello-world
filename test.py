import numpy as np
a = np.random.rand(1000000)
b = np.random.rand(1000000)
import time 
tick = time.time()
c = np.dot(a,b)
to = time.time()
print(c)
print("vector"+ str(1000*(to - tick)))

c= 0
for i in range(1000000):
	c+= a[i]*b[i]

toc = time.time()

print(c)
print("non"+str(1000*(toc-tick)))
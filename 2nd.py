from matplotlib import pylab
print(pylab.__version__)

import numpy as np
x = np.linspace(0,20,25)
y=x*x+2
print(x)
print(y)
pylab.plot(x,y,'r')
pylab.show()

pylab.plot(x,y,'b')
pylab.subplot(1,2,2)
pylab.plot(y,x,'g')




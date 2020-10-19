import numpy as np
import matplotlib.pyplot as plt


# create two simple periodic signal
time = np.linspace(0,3,300)
x = [ np.sin( 2 * np.pi * 0.75 * time[i] ) for i in range(len(time))]
y = [ 10*i if i > 0 and i < 0.5 else 0 for i in x ]

plt.plot(time,y,)
plt.plot(time,x,'r--')
plt.legend(['output', 'input'])

plt.show()


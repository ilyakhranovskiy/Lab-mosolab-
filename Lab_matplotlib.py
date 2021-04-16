import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0,2,0.01)

s1 = np.sin(2*np.pi*t*2)
s2 = np.sin(2*np.pi*t*3)
s3 = np.sin(2*np.pi*t*4)
s4 = np.sin(2*np.pi*t*5)

fig=plt.figure(figsize=(10,10))

ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(t, s1, c='r',linewidth=4.0)
ax1.set(xlabel='Частота', title='Синус функція')
ax1.grid()

ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(t, s2, c='b',linewidth=4.0)
ax2.set(xlabel='Частота ', title='Синус функція')
ax2.grid()

ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(t, s3, c='g',linewidth=4.0)
ax3.set(xlabel='Частота',  title='Синус функція')
ax3.grid()

ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(t, s4, c='y',linewidth=4.0)
ax4.set(xlabel='Частота', title='Синус функція')
ax4.grid()

plt.show()

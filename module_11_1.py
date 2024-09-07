import matplotlib.pyplot as mp
import numpy as nmp

mp.style.use('_mpl-gallery')

y = [4.2, 3.5, 5.5, 9.6, 3.5, 6.6, 2.6, 3.0]
fig, ax = mp.subplots()

ax.stairs(y, linewidth=2.5)
ax.set(xlim=(0, 8), xticks=nmp.arange(1, 8),
       ylim=(0, 8), yticks=nmp.arange(1, 8))

mp.show()


mp.style.use('_mpl-gallery-nogrid')


x = [-3, -2, -1.6, -1.2, -.8, -.5, -.2, .1, .3, .5, .8, 1.1, 1.5, 1.9, 2.3, 3]
X, Y = nmp.meshgrid(x, nmp.linspace(-3, 3, 128))
Z = (1 - X/2 + X**5 + Y**3) * nmp.exp(-X**2 - Y**2)


fig, ax = mp.subplots()

ax.pcolormesh(X, Y, Z, vmin=-0.5, vmax=1.0)

mp.show()
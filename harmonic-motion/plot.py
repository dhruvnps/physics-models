import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
from math import sqrt
from math import cos, sin, e

time = 50

# spring constant
k = 200
# mass of object
m = 100
# max init displacement
max_A = 10
# init displacement
A = -max_A
decay = 0


def ω(): return sqrt(k / m)


def Ad(t): return A * e**(decay*-t)


def x(t): return [Ad(ti) * cos(ω() * ti) for ti in t]


def v(t): return [-ω() * Ad(ti) * sin(ω() * ti) for ti in t]


def a(t): return [-ω()**2 * Ad(ti) * cos(ω() * ti) for ti in t]


def KE(t): return [v2 * (m/2) for v2 in [ve**2 for ve in v(t)]]


# time range
t = np.arange(time, 0, -.01)


def plotVals(): return t, x(t)


fig, ax = plt.subplots()
plt.subplots_adjust(left=.15, right=.9, bottom=.35, top=.9)

p, = plt.plot(*plotVals(), lw=1)
plt.axhline(y=0, color='grey', lw=0.5)
# plt.ylim([,])
# plt.xlim([,])

sliders = [
    Slider(plt.axes([.15, .1, .75, .03]), 'spring k', 0.1, k * 2, k),
    Slider(plt.axes([.15, .15, .75, .03]), 'mass', 0.1, m * 2, m),
    Slider(plt.axes([.15, .2, .75, .03]), 'init. displ.', -max_A, max_A, A),
    Slider(plt.axes([.15, .25, .75, .03]), 'decay', 0, 5, decay),
]


def update(val):
    global k, m, A, decay
    k, m, A, decay = (slider.val for slider in sliders)
    t = np.arange(time, 0, -.01)
    p.set_xdata(plotVals()[0])
    p.set_ydata(plotVals()[1])


for slider in sliders:
    slider.on_changed(update)

plt.show()

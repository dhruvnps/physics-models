import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
from math import sqrt

# set height
h = 100

# defaults
k = 100
m = 70
g = 9.81
length = h


def GPE(x):
    '''GPE = mgΔh'''
    Δh = (h - x)
    return m * g * Δh


def EPE(x):
    '''EPE = ½kX²'''
    X = np.array(x - length)
    X[X < 0] = 0  # if X < 0 set to 0
    return (1/2) * k * X*X


def KE(x):
    '''KE = mgh - (GPE + KE)'''
    return m * g * h - (GPE(x) + EPE(x))


def v(x):
    '''v = √(2KE/m)'''
    ke = np.array(KE(x))
    ke[ke < 0] = 0  # if KE < 0 set to 0
    return np.sqrt(2 * ke / m)


def t(x):
    '''t = v/x'''
    return x / v(x)


x = np.arange(h, 0, -.01)

fig, ax = plt.subplots()
plt.subplots_adjust(left=.1, right=.9, bottom=.4, top=.9)

p, = plt.plot(x, v(x), lw=2)
l = plt.axvline(x=length, color='red')
plt.axhline(y=0, color='grey', lw=2)
ax.set_ylabel('velocity')
ax.set_xlabel('displacement')
text = []

# length, k, m, g
sliders = [
    Slider(plt.axes([.1, .1, .8, .03]), 'length', 0, h, length),
    Slider(plt.axes([.1, .15, .8, .03]), 'k', 0.1, 500, k),
    Slider(plt.axes([.1, .2, .8, .03]), 'm', 0.1, 100, m),
    Slider(plt.axes([.1, .25, .8, .03]), 'g', 0.1, 20, g),
]


def annotate():
    global text
    for item in text:
        item.remove()
    idx = np.argmax(v(x))
    pt = (x[idx], v(x[idx]))
    label = '{:.2f}'.format(pt[1])
    text = [ax.annotate(label, xy=pt, xytext=(pt[0], pt[1] + 5),
                        arrowprops=dict(arrowstyle='->'))]


def update(val):
    global length, k, m, g
    length, k, m, g = (slider.val for slider in sliders)
    p.set_ydata(v(x))
    l.set_xdata(length)
    annotate()


for slider in sliders:
    slider.on_changed(update)


plt.show()

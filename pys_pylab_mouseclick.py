from __future__ import print_function

import matplotlib
#matplotlib.use("WxAgg")
#matplotlib.use("TkAgg")
#matplotlib.use("GTKAgg")
#matplotlib.use("Qt4Agg")
#matplotlib.use("MacOSX")
import matplotlib.pyplot as plt
import numpy as np

#print("***** TESTING WITH BACKEND: %s"%matplotlib.get_backend() + " *****")


def OnClick(event):
    if event.dblclick:
        print("DBLCLICK", event)
    else:
        print("DOWN    ", event)


def OnRelease(event):
    print("UP      ", event)


fig, ax = plt.subplots(2, sharex=True)
#fig, ax = plt.subplots(2)
cid_up = fig.canvas.mpl_connect('button_press_event', OnClick)
cid_down = fig.canvas.mpl_connect('button_release_event', OnRelease)

# ax.text(0.5, 0.5, "Click on the canvas to test mouse events.",
#               ha="center", va="center")

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
ax[0].plot(t, s)
ax[1].scatter(t,s)
plt.show()

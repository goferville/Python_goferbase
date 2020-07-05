# -*- coding: utf-8 -*-
# Vispy demo modified
# mouse move to return world coordinates

"""
Demonstration of animated Line visual.
"""

import sys
import numpy as np
from vispy import app, scene

# vertex positions of data to draw
N = 126
pos = np.zeros((N, 2), dtype=np.float32)
#x_lim = [50., 750.]
#y_lim = [-2., 2.]

x = np.arange(0,4*np.pi,0.1)   # start,stop,step, N=126
y = np.sin(x)
pos[:, 0] = x
pos[:, 1] = y
# color array
color = np.ones((N, 4), dtype=np.float32)
color[:, 0] = np.linspace(0, 1, N)
color[:, 1] = color[::-1, 0]

canvas = scene.SceneCanvas(keys='interactive', show=True)
grid = canvas.central_widget.add_grid(spacing=0)



viewbox = grid.add_view(row=0, col=1, camera='panzoom')


# add some axes



x_axis = scene.AxisWidget(orientation='bottom')
x_axis.stretch = (1, 0.1)
grid.add_widget(x_axis, row=1, col=1)
x_axis.link_view(viewbox)
y_axis = scene.AxisWidget(orientation='left')
y_axis.stretch = (0.1, 1)
grid.add_widget(y_axis, row=0, col=0)
y_axis.link_view(viewbox)

print("y=:", viewbox.pos)



# add a line plot inside the viewbox
line = scene.Line(pos, color, parent=viewbox.scene)

posh=np.empty((2, 2), dtype=np.float32)
posh[0][0]=-5
posh[1][0]=50
posh[0][1]=3.38
posh[1][1]=3.38
posv=np.empty((2, 2), dtype=np.float32)
posv[0][1]=-5
posv[1][1]=5
colorh = np.ones((2, 4), dtype=np.float32)
colorh[:, 0] = np.linspace(0, 1, 2)
colorh[:, 1] = colorh[::-1, 0]
lineh = scene.Line(posh, colorh, parent=viewbox.scene)
linev = scene.Line(posv, colorh, parent=viewbox.scene)

# auto-scale to see the whole line.
viewbox.camera.set_range()

def update(ev):
    global pos, color, line, tform
    #pos[:, 1] = np.random.normal(size=N)
    #color = np.roll(color, 1, axis=0)

    print("mouse:", ev.pos)
    #line.set_data(pos=pos, color=color)




    w, h = viewbox.size
    print("canvas size", w, h)
    tform = viewbox.scene.transform
    print(tform)

    #tform = viewbox.camera._scene_transform
    print(tform)
    '''
    d0 = np.array([w, h/2, 0, 1])
    p0 = tform.imap(d0)
    '''

    d1 = np.array([ev.pos[0], ev.pos[1],0,1])
    p1 = tform.imap(d1)
    p1=p1
    #print("pMouse=", p0)
    posh[0,1]=p1[1]
    posh[1,1]=p1[1]
    print(posh)
    lineh.set_data(posh, colorh)

    '''
    posv[0, 0] = p1[0]
    posv[1, 0] = p1[0]
    print(posv)
    linev.set_data(posv, colorh)
    '''

    tf1 = line.transforms.get_transform('visual', 'canvas')
    print(tf1)
    p3=tf1.imap(d1)
    print(p3)
    posh[0, 1] = p3[1]
    posh[1, 1] = p3[1]
    posh[0, 0] = p3[0] - 500
    posh[1, 0] = p3[0] + 500
    print(posh)
    lineh.set_data(posh, colorh)
    posv[0, 0] = p3[0]
    posv[1, 0] = p3[0]
    posv[0, 1] = p3[1]-500
    posv[1, 1] = p3[1]+500
    print(posv)
    linev.set_data(posv, colorh)
#timer = app.Timer(
#timer.connect(update)
#timer.start(0)
canvas.events.mouse_move.connect(update)

#viewbox.camera.viewbox_mouse_event.connect(update)

if __name__ == '__main__' and sys.flags.interactive == 0:
    app.run()

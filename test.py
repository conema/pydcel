import pydcel.io

d = pydcel.io.ply2dcel('sampledata/simplegeom.ply')

gui = pydcel.dcelVis(d)
gui.mainloop()
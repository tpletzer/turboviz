import numpy as np


class VorticityCalc(object):
    def __init__(self, u, v, w, x, y, z):
        #copy in code
        pass

    def writeVTK(self, filename):
        #code
        pass

def test():
    x = np.linspace(0, 100, 2)
    y = np.linspace(0, 100, 3)
    z = np.linspace(0, 100, 4)
    xx, yy, zz = np.meshgrid(x, y, z)
    uu = np.ones_like(xx)
    vv = np.zeros_like(xx)
    ww = np.zeros_like(xx)
    vc = VorticityCalc(uu, vv, ww, x, y, z)
    vc.writeVTK('vorticity.vtk')

if __name__ == '__main__': test()
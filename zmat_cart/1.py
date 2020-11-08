
import numpy as np
import math as m


def cart2sph(x,y,z):
    XsqPlusYsq = x**2 + y**2
    r = m.sqrt(XsqPlusYsq + z**2)
    if r==0:
        theta0 = 0.0
    else:
        theta0 = m.degrees(m.acos(z/r))

    if x==0:
        phi0 = 90.0
    else:
        phi0 = m.degrees(m.acos(x/r))
    return(r, theta0, phi0)



def sph2cart(r,theta0,phi0):
    x = r * m.sin(m.radians(theta0)) * m.cos(m.radians(phi0))
    y = r * m.sin(m.radians(theta0)) * m.sin(m.radians(phi0))
    z = r * m.cos(m.radians(theta0))
    return(x,y,z)

theta0=45.
phi0=45.
(rr,tt,pp) = cart2sph(1.43912,1.46690,0.924339)
xxx = sph2cart(rr,tt+theta0,pp+phi0)
print(xxx)

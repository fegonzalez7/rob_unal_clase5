import roboticstoolbox as rtb
from spatialmath import *
from spatialmath.base import *
import numpy as np

if __name__ == "__main__":
    l = np.array([14.5, 10.7, 10.7, 9])
    qlims = np.array([[-3*np.pi/4, 3*np.pi/4],[-3*np.pi/4, 3*np.pi/4],[-3*np.pi/4, 3*np.pi/4],[-3*np.pi/4, 3*np.pi/4]])
    robot = rtb.DHRobot(
        [rtb.RevoluteDH(alpha=np.pi/2, d=l[0], qlim=qlims[0,:]),
        rtb.RevoluteDH(a=l[1], offset=np.pi/2, qlim=qlims[0,:]),
        rtb.RevoluteDH(a=l[2], qlim=qlims[0,:]),
        rtb.RevoluteDH(a=l[3], qlim=qlims[0,:])],
        name="Px_DH_std")
    print(robot)
    
    q = np.deg2rad(np.array([60, -50, -50, 10]))
    robot.plot(q,block=False)
    trplot( transl(0,0,0), color='rgb', width=1, frame='0', length=5)
    # robot.teach(np.array([0, 0, .25, 0]))
    a = robot.fkine(q)
    print(a)
    input() 
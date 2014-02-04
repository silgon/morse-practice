#!/usr/bin/python
# silgon <silgon3200@gmail.com>

from math import cos,sin,pi
def visAVis(poses,center,radius,sigma):
    """ create F Formation of the type Vis-A-Vis
    
    Arguments:
    - `poses`: the pose where the new humans will be created
    - `center`: list parameter (x,y,theta)
    - `radius`: float parameter distance from the center of the f_formation to the human
    - `sigma`: for the error in positions diag(sigma_x,sigma_y,sigma_theta)
    """
    i=len(poses)
    x,y,theta=center
    r=radius
    poses.append([x+r*cos(theta),y+r*sin(theta),theta+pi])
    poses.append([x-r*cos(theta),y-r*sin(theta),theta])
    print("Vis-a-Vis: "+"human"+str(i)+" and "+"human"+str(i+1))

def LFormation(poses,center,radius,sigma):
    """ create F Formation of the type L
    
    Arguments:
    - `poses`: the pose where the new humans will be created
    - `center`: list parameter (x,y,theta)
    - `radius`: float parameter distance from the center of the f_formation to the human
    - `sigma`: for the error in positions diag(sigma_x,sigma_y,sigma_theta)
    """
    i=len(poses)
    x,y,theta=center
    r=radius
    poses.append([x+r*cos(theta),y+r*sin(theta),theta+pi])
    poses.append([x+r*cos(theta+pi/2),y+r*sin(theta+pi/2),theta-pi/2])
    print("L Formation:  "+"human"+str(i)+" and "+"human"+str(i+1))

def circular4Formation(poses,center,radius,sigma):
    """ create F Formation of the type Circular with 4 people
    
    Arguments:
    - `poses`: the pose where the new humans will be created
    - `center`: list parameter (x,y,theta)
    - `radius`: float parameter distance from the center of the f_formation to the human
    - `sigma`: for the error in positions diag(sigma_x,sigma_y,sigma_theta)
    """
    i=len(poses)
    x,y,theta=center
    r=radius
    poses.append([x+r*cos(theta),y+r*sin(theta),theta+pi])
    poses.append([x+r*cos(theta+pi/2),y+r*sin(theta+pi/2),theta-pi/2])
    poses.append([x-r*cos(theta),y-r*sin(theta),theta])
    poses.append([x-r*cos(theta+pi/2),y-r*sin(theta+pi/2),theta+pi/2])
    print("Circular Formation: from "+"human"+str(i)+" to "+"human"+str(i+3))


def sideBySide(poses,center,radius,sigma):
    """ create F Formation of the type side-by-side
    In this case, the people are not looking to the center of the O-space (since they suppose to be walking)
    
    Arguments:
    - `poses`: the pose where the new humans will be created
    - `center`: list parameter (x,y,theta)
    - `radius`: float parameter distance from the center of the f_formation to the human
    - `sigma`: for the error in positions diag(sigma_x,sigma_y,sigma_theta)
    """
    i=len(poses)
    x,y,theta=center
    r=radius
    poses.append([x+r*cos(theta)+r*.6*cos(pi/2+theta),y+r*sin(theta)+r*.6*sin(pi/2+theta),theta+pi+pi/9])
    poses.append([x+r*cos(theta)-r*.6*cos(pi/2+theta),y+r*sin(theta)-r*.6*sin(pi/2+theta),theta+pi-pi/9])
    print("Side-by-side Formation:  "+"human"+str(i)+" and "+"human"+str(i+1))

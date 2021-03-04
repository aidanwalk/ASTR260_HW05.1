#Aidan Walk
#ASTR 260-001
#03 March 2021
#Globe Earth Calculations

import numpy as np

def grav_accel(p1, p2, m, radius):
    """ p1 = point where the mass element is
        p2 = point you are interested in
        m  = mass
        returns a vector of the gravitational accleration"""
    G = 6.6743e-11
    #FILL THE NEXT THREE LINES IN WITH CORRECT CODE
    m = m
    lenP2 = np.sqrt(p2[0]**2 + p2[1]**2 + p2[2]**2)
    rhat = np.array([p2[0]/lenP2, p2[1]/lenP2, p2[2]/lenP2])
    r = radius
    return -1*G*m/r**2*rhat

def point_in_sphere(x,y,z, radius=None, height=None):
    if x**2 + y**2 + z**2 <= radius**2:
        return True
    else:
        return False
        
def pointInCylinder(x, y, z, radius=None, height=None):
    if x**2 + y**2 <= radius**2 and \
       z <= height and z>=0:
        return True
    else:
        return False
        
def gravVector(x, y, z, dx, dy, dz, radius=None, p2=None, rho=None, function=None, height=None):
    grav_vec = 0
    for idx, xx in enumerate(x):
        #this is a trick to tell how long it will take
        print(idx, " of ", x.shape[0], "x steps.")
        for yy in y:
            for zz in z:
                if function(xx,yy,zz, radius=radius, height=height):
                    m = rho*dx*dy*dz
                    point = np.array([xx,yy,zz])
                    grav_vec += grav_accel(point, p2, m, radius)
    return grav_vec
    
if __name__ == "__main__":
    km = 1000 #1 km = 1000 meters
    rho = 5514 #kg/m^3, density of Earth
    r_earthGlobe = 6378*km #radius of globe Earth 
    h = 300.0*km #relatively coarse step size
    #set grid size same in x,y,z
    dx, dy, dz = h, h, h
    
    #Grid boundaries for Globe Earth
    #x, y, z define boundaries of grid, here 7000 km
    gx = np.arange(-7000*km, 7000*km, dx)
    gy = gx.copy()
    gz = gy.copy()
    
    #define points on the north pole, south pole, and equator
    point_northpole = np.array([0, 0, 1])
    point_equator   = np.array([1, 1, 0])
    point_southpole = np.array([0, 0, -1])
    
    #Globe Earth calc
    print('Calculating gravity vector at north pole...')
    grav_northPoleVec = gravVector(gx, gy, gz, dx, dy, dz, 
                              radius=r_earthGlobe, p2=point_northpole, rho=rho,
                              function=point_in_sphere)
    print('\n', 'Calculating gravity vector at Equator...')
    grav_equatorVec = gravVector(gx, gy, gz, dx, dy, dz, 
                                 radius=r_earthGlobe, p2=point_equator, rho=rho,
                                 function=point_in_sphere)
    print('\n', 'Calculating gravity vector at south pole...') 
    grav_southPoleVec = gravVector(gx, gy, gz, dx, dy, dz, 
                                 radius=r_earthGlobe, p2=point_southpole, rho=rho,
                                 function=point_in_sphere)
                                 
    
    #Flat Earth
    h = 600.0*km #redefine h b/c this computation takes longer
    dx, dy, dz = h, h, h
    thickness_earthFlat = 4750*km
    r_earthFlat = 20037*km
    #grid boundaries for Flat Earth
    fx = np.arange(-21000*km, 21000*km, dx)
    fy = fx.copy()
    fz = np.arange(0, 5500*km, dx)
    
    #define points on the north pole, south pole, and equator
    point_northpoleFlat = np.array([0, 0, 1])
    point_equatorFlat   = np.array([0.5, 0, 1])
    point_southpoleFlat = np.array([1, 0, 1])
 
    #Flat Earth calc
    print('\n\n\n', 'FLAT EARTH CALCULATIONS') 
    print('Calculating gravity vector at north pole...')
    grav_northPoleVec_Flat = gravVector(fx, fy, fz, dx, dy, dz, 
                              radius=r_earthFlat, p2=point_northpoleFlat, rho=rho,
                              function=pointInCylinder, height=thickness_earthFlat)
    print('\n', 'Calculating gravity vector at Equator...')
    grav_equatorVec_Flat = gravVector(fx, fy, fz, dx, dy, dz, 
                              radius=r_earthFlat, p2=point_equatorFlat, rho=rho,
                              function=pointInCylinder, height=thickness_earthFlat)
    print('\n', 'Calculating gravity vector at south pole...')
    grav_southPoleVec_Flat = gravVector(fx, fy, fz, dx, dy, dz, 
                              radius=r_earthFlat, p2=point_southpoleFlat, rho=rho,
                              function=pointInCylinder, height=thickness_earthFlat)
    
    #print all Values
    print('\n\n', 'GLOBE EARTH GRAVITY VECTORS:')
    print('North pole...', grav_northPoleVec)
    print('South pole..', grav_southPoleVec)
    print('Equator...', grav_equatorVec)
    
    print('\n', 'FLAT EARTH GRAVITY VECTORS:')
    print('North pole...', grav_northPoleVec_Flat)
    print('South pole..', grav_southPoleVec_Flat)
    print('Equator...', grav_equatorVec_Flat)
    
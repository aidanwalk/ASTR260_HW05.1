#Aidan Walk
#ASTR 260-001
#03 March 2021

import numpy as np

global a; global b
a=2; b=4

def fOfEllipse(x):
    y = b * np.sqrt( 1 - (x**2/a**2) )
    return y

def area(arr, dx=None):
    area = 4 * np.trapz(arr, dx=dx)
    return area

if __name__ =='__main__':
    #define bounds and steps
    steps = int(10e3)
    print('\n'+'Problem 1: Area of an Ellipse', '\n'+
          '1.', '\n', 'Calculating 1-D integral',
          'with step size =', steps, '...')
    bounds = np.linspace(0, a, steps)
    h = bounds[1]-bounds[0]
    #pass bounds through ellipse function solved for y
    for point in bounds:
        index = int(round(point/h))
        bounds[index] = fOfEllipse(bounds[index])
    
    #calculate integral of bounds array
    myAnswer = area(bounds, dx=h)
    #print answers
    actualAnswer = a*b*np.pi
    print('\t', 'Acutal answer: {:0.6f}'.format(actualAnswer))
    print('\t','    My answer: {:0.6f}'.format(myAnswer))
    
    #calculate number 2
    print('2.\n', 'Calculating 2-D integral', 
          ' with step size =', steps, '...')
    x = np.linspace(0, a, steps)
    y = np.linspace(0, b, steps)
    xs, ys = np.meshgrid(x, y)
    mask = 4.0*( (xs**2/a**2) + (ys**2/b**2) <=1)
    dx = x[1] - x[0]
    dy = y[1] - y[0]
    maskedIntegral = np.sum(mask*dx*dy)
    print('\t', 'My Answer: {:0.6f}'.format(maskedIntegral))
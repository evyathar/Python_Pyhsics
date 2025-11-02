import numpy as np
#import matplotlib.pyplot as plt

qn = int(input('enter question number: '))
a = float(input('enter acceleration: '))
print()

if qn == 2:
    t = float(input('enter t: '))
    ## your answer
    v = a * t
    
    ## output
    print(f'v={v:.5g} m/s')

    """
    t_range = np.arange(0, 8.0, 0.01)
    v_range = a * t_range
    plt.figure()
    plt.plot(t_range, v_range)
    plt.xlabel('t [s]')
    plt.ylabel('v(t) [m/s]')
    plt.title('Velocity vs Time (v0=0)')
    plt.grid(True)
    plt.show()
    """


if qn == 3:
    t = float(input('enter t: '))
    ## your answer
    x = 0.5 * a * t**2
    
    ## output
    print(f'x={x:.5g} m')

    """
    t_range = np.arange(0, 8.0, 0.01)
    x_range = 0.5 * a * t_range**2
    plt.figure()
    plt.plot(t_range, x_range)
    plt.xlabel('t [s]')
    plt.ylabel('x(t) [m]')
    plt.title('Position vs Time (v0=0)')
    plt.grid(True)
    plt.show()
   """


if qn == 4:
    v = float(input('enter v: '))
    ## your answer
    x = (v**2) / (2 * a)
    
    ## output
    print(f'x={x:.5g} m')

 
    """
    v_range = np.linspace(0, 8, 200)
    x_range = (v_range**2) / (2 * a)
    plt.figure()
    plt.plot(v_range, x_range)
    plt.xlabel('v [m/s]')
    plt.ylabel('x(v) [m]')
    plt.title('Position vs Velocity')
    plt.grid(True)
    plt.show()
    """


if qn == 7:
    ANS = False   
    print(ANS)


   
    """
    t = np.linspace(0, 5, 100)
    a_x, a_y = 1, 2
    v0_x, v0_y = 0, 0
    x = 0.5 * a_x * t**2
    y = 0.5 * a_y * t**2
    plt.figure()
    plt.plot(x, y)
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.title('Trajectory with constant acceleration (not a straight line)')
    plt.grid(True)
    plt.axis('equal')
    plt.show()
   
   """

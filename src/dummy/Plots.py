import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches



'''
General plotting
'''


#Data
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ave_max = [30, 31, 31, 31, 31, 31, 31, 31, 31, 31, 30, 29]
ave_min = [23, 24, 24, 24, 25, 24, 24, 24, 24, 24, 24, 23]


#Plot
plt.plot (months, ave_max, 'r-.', months, ave_min, 'c:')


#Info
plt.xlabel ('Months', color = '#1e8bc3')
plt.ylabel ('Temperature (°C)', color = '#e74c3c')
plt.title ('Temperature in Singapore', color = '#34495e')

up_legend = mpatches.Patch (color = 'red', label = 'High')
down_legend = mpatches.Patch (color = 'cyan', label = 'Low')
plt.legend (handles = [up_legend, down_legend] )


#Show
plt.show ()



'''
Subplotting
'''


#Data
years = [1996, 2000, 2004, 2008, 2012, 2016]
us = [101, 93, 101, 112, 103, 121]
russia = [63, 89, 90, 60, 68, 56]


#Plot
plt.subplot (211)
plt.plot (years, us, 'b-')


#Info
plt.xlabel ('Years', color = '#0000ff')
plt.ylabel ('Medals', color = '#0000ff')
us_legend = mpatches.Patch (color = 'blue', label = 'US')
plt.legend (handles = [us_legend] )


#Plot
plt.subplot (212)
plt.plot (years, russia, 'r-.')


#Info
plt.xlabel ('Years', color = '#ff0000')
plt.ylabel ('Medals', color = '#ff0000')
russia_legend = mpatches.Patch (color = 'red', label = 'Russia')
plt.legend (handles = [russia_legend] )


#Show
plt.show ()



'''
Linear function plotting
'''


#Data
x = np.linspace (-5, 5, 100)
gradt = 2
itrcp = 1
y =  gradt * x + itrcp


#Plot
plt.plot (x, y, '-r', label = 'y=2x+1')

plt.grid ()


#Info
plt.title ('Graph of y=2x+1')
plt.xlabel ('x', color = '#1C2833')
plt.ylabel ('y', color = '#1C2833')
plt.legend (loc = 'upper left')


#Show
plt.show ()



'''
Centering axis
'''


#Transformations
fig = plt.figure ()
ax = fig.add_subplot (1, 1, 1)

ax.spines ['left'].set_position ('center')
ax.spines ['bottom'].set_position ('center')
ax.spines ['right'].set_color ('none')
ax.spines ['top'].set_color ('none')

ax.xaxis.set_ticks_position ('bottom')
ax.yaxis.set_ticks_position ('left')

#Plot
plt.plot ()


#Show
plt.show ()



'''
Multiple linear functions centered
'''


#Data
x = np.linspace (-5, 5, 100)
fig, ax = plt.subplots ()


#Transformations
ax.spines ['left'].set_position ('center')
ax.spines ['bottom'].set_position ('center')
ax.spines ['right'].set_color ('none')
ax.spines ['top'].set_color ('none')

ax.xaxis.set_ticks_position ('bottom')
ax.yaxis.set_ticks_position ('left')


#Plot
plt.plot (x, 2*x+1, '-r', label = 'y=2x+1')
plt.plot (x, 2*x+3, ':b', label = 'y=2x+3')
plt.plot (x, 2*x-1, '-.g', label = 'y=2x-1')
plt.plot (x, 2*x-3, '--m', label = 'y=2x-3')

plt.grid ()


#Info
plt.legend (loc = 'upper left')


#Show
plt.show ()



'''
Trigonometric functions
'''


#Data
x = np.linspace (2 * -np.pi, 2 * np.pi, 250)
y = np.sin (x)
fig, ax = plt.subplots ()


#Transformations
ax.spines ['left'].set_position ('center')
ax.spines ['bottom'].set_position ('center')
ax.spines ['right'].set_color ('none')
ax.spines ['top'].set_color ('none')

ax.xaxis.set_ticks_position ('bottom')
ax.yaxis.set_ticks_position ('left')


#Plot
plt.plot (x, y, '-r', label = 'y=sin(x)')
plt.plot (x, 2*y, '-b', label = 'y=2sin(x)')
plt.plot (x, 3*y, '-g', label = 'y=3sin(x)')

plt.grid ()


#Info
plt.legend (loc = 'upper left')


#Show
plt.show ()



'''
Sine transformations
'''


#Data
x = np.linspace (-20, 20, 500)
y = np.sin (x) / x
fig, ax = plt.subplots ()


#Transformations
ax.spines ['left'].set_position ('center')
ax.spines ['bottom'].set_position ('zero')
ax.spines ['right'].set_color ('none')
ax.spines ['top'].set_color ('none')

ax.xaxis.set_ticks_position ('bottom')
ax.yaxis.set_ticks_position ('left')


#Plot
plt.plot (x, y, '-r', label = 'y=sin(x)/x')
plt.plot (x, 2*y, '-b', label = 'y=2sin(x)/x')
plt.plot (x, -y, '-g', label = 'y=-sin(x)/x')

plt.grid ()


#Info
plt.legend (loc = 'upper left')


#Show
plt.show ()
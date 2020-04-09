import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Circle
import mpl_toolkits.mplot3d.art3d as art3d
import numpy as np
import pandas as pd



def x_y_in_double_focus_distance (x0, y0, z0, x1, y1, z1, z2):
    return [(z2-z0)*(x1 - x0)/(z1 - z0) + x0, (z2-z0)*(y1 - y0)/(z1 - z0) + y0]
t = pd.read_csv('/home/yaroslav/Yaroslavus_GitHub/IACT_workshop_experiments/Summary_table.csv',
                       sep=' ', names=['number_kb','x_kb','y_kb', 'z_kb', 'alpha_YZ_kb', 'beta_XZ_kb', 'x_dev_exp', 'y_dev_exp', 'f_exp', 'f_kb', 'fix_angle'])
t_df = pd.DataFrame(t)
xy_new = []
for i in range (len(t["number_kb"])):
    xy_new.append(x_y_in_double_focus_distance(t['x_kb'][i], t['y_kb'][i], t['z_kb'][i], t["x_dev_exp"][i], t["y_dev_exp"][i], t['f_kb'][i], 2*t['f_kb'][i]))
xy_new_df = pd.DataFrame(xy_new)



#########################################################################################################
## Setting the plot options ##
#############################

fig = plt.figure(figsize=(200,200))
ax = plt.axes(projection="3d")

## Axes labels and the title ##

plt.xlabel('X, mm')
plt.ylabel('Y, mm')
plt.title("Изображение")

## Grid ##

major_ticks = np.arange(-10000, 10000, 1000)
#minor_ticks = np.arange(-10000, 10000, 200)

ax.set_xticks(major_ticks)
#ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
#ax.set_yticks(minor_ticks, minor=True)
ax.set_zticks(major_ticks)
#ax.set_zticks(minor_ticks, minor=True)

# And a corresponding grid
#ax.grid(which='both')

# Or if you want different settings for the grids:
#ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.8)

#########################################################################################################
## Formation of the focal plane objects ##
#########################################

## The plane ##

xs1 = np.linspace(-3000, 3000, 5)
ys1 = np.linspace(-3000, 3000, 5)
x1, y1 = np.meshgrid(xs1, ys1)
z1 = 0*x1 + 0*y1 + 4750
ax.plot_surface(x1, y1, z1, alpha=0.2)

## The circle ##

c1=Circle((0, 0), 1000, facecolor='none', edgecolor="blue", linewidth=10, alpha=1)
ax.add_patch(c1)
art3d.pathpatch_2d_to_3d(c1, z=4750, zdir="z")

## The dots ##

ax.scatter(t_df['x_dev_exp'], t_df['y_dev_exp'], 1000*t_df['f_exp'], color='red', s = 100, alpha=1);

#########################################################################################################
## Formation of the double-focal plane objects ##
################################################

## The plane ##

xs2 = np.linspace(-15000, 15000, 5)
ys2 = np.linspace(-15000, 15000, 5)
x2, y2 = np.meshgrid(xs2, ys2)
z2 = 0*x2 + 0*y2 + 9500
ax.plot_surface(x2, y2, z2, alpha=0.2, cstride=1, rstride=1, shade=False)

## The circle ##

c2=Circle((0, 0), 10000, facecolor='none', edgecolor="blue", linewidth=10, alpha=1)
ax.add_patch(c2)
art3d.pathpatch_2d_to_3d(c2, z=9500, zdir="z")

## The dots ##

ax.scatter(xy_new_df[0], xy_new_df[1], 2000*t_df['f_exp'], color='red', s = 100, alpha=1);

#########################################################################################################
## Formation of the lines between planes ##
##########################################

## Between mirrors and focal plane ##

for i in range(len(t_df)):
    z_line = [t_df['z_kb'][i], 1000*t_df["f_exp"][i]]
    x_line = [t_df['x_kb'][i], t_df["x_dev_exp"][i]]
    y_line = [t_df['y_kb'][i], t_df["y_dev_exp"][i]]
    ax.plot3D(x_line, y_line, z_line, 'red')

## Between focal plane and double-focal plane ##
    
for i in range(len(t_df)):
    z_line = [t_df['z_kb'][i], 2000*t_df["f_exp"][i]]
    x_line = [t_df['x_kb'][i], xy_new_df[0][i]]
    y_line = [t_df['y_kb'][i], xy_new_df[1][i]]
    ax.plot3D(x_line, y_line, z_line, 'red')

#########################################################################################################
## Formation of the mirrors and mirror surface ##
################################################

## Formation of the mirrors plates ##

ax.scatter(t_df['x_kb'], t_df['y_kb'], t_df['z_kb'], color='gray', s = 3000, alpha=0.7);

## Formation of the mirrors envelope curved surface ##

xs3 = np.linspace(-1500, 1500, 100)
ys3 = np.linspace(-1500, 1500, 100)
x3, y3 = np.meshgrid(xs3, ys3)
z3 = (x3**2 + y3**2)/7000
ax.plot_surface(x3, y3, z3, alpha=0.2, color='white')

#########################################################################################################
## Formation of the text numbers of all of the dots and mirrors ##
#################################################################

for g in range (len(t_df["number_kb"])):
    ax.text(t_df['x_kb'][g]+20, t_df['y_kb'][g]+20, t_df['z_kb'][g]+20, str(t_df["number_kb"][g]), size = 50)
    ax.text(t_df['x_dev_exp'][g], t_df['y_dev_exp'][g], 1000*t_df['f_exp'][g], str(t_df["number_kb"][g]), size = 50)
    ax.text(xy_new_df[0][g]+20, xy_new_df[1][g]+20, 2000*t_df['f_exp'][g]+20, str(t_df["number_kb"][g]), size = 50)

#########################################################################################################
## File saving ##
################

plt.savefig('try', fmt='png')
plt.savefig('try', fmt='pdf')

plt.show()
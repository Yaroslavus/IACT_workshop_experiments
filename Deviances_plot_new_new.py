import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import os
########################################################################################################
########################################################################################################
########################################################################################################
def x_y_in_double_focus_distance (x0, y0, z0, x1, y1, z1, z2):
    return [(z2-z0)*(x1 - x0)/(z1 - z0) + x0, (z2-z0)*(y1 - y0)/(z1 - z0) + y0]

def set_mirrors_coords (m, n, p, r):
    
    m['number'].append(n)
    m['x_coord'].append(float(r*np.cos(np.radians(p))))
    m['y_coord'].append(float(r*np.sin(np.radians(p))))
    
def init_IACT_mirrors_in_pandas_df (r, p):

    mirrors = {'number': [], 'x_coord': [], 'y_coord': []}

    set_mirrors_coords (mirrors, 18, 0, 0)

    #inner circle

    set_mirrors_coords (mirrors, 12, p, r)
    set_mirrors_coords (mirrors, 13, 2*p, r)
    set_mirrors_coords (mirrors, 19, 3*p, r)
    set_mirrors_coords (mirrors, 24, 4*p, r)
    set_mirrors_coords (mirrors, 23, 5*p, r)
    set_mirrors_coords (mirrors, 17, 6*p, r)

    #middle_circle

    set_mirrors_coords (mirrors, 6, 2/2*p, 2*r)
    set_mirrors_coords (mirrors, 7, 3/2*p, 2*r*np.cos(np.radians(p/2)))
    set_mirrors_coords (mirrors, 8, 4/2*p, 2*r)
    set_mirrors_coords (mirrors, 14, 5/2*p, 2*r)
    set_mirrors_coords (mirrors, 20, 6/2*p, 2*r)
    set_mirrors_coords (mirrors, 25, 7/2*p, 2*r)
    set_mirrors_coords (mirrors, 30, 8/2*p, 2*r)
    set_mirrors_coords (mirrors, 29, 9/2*p, 2*r*np.cos(np.radians(p/2)))
    set_mirrors_coords (mirrors, 28, 10/2*p, 2*r)
    set_mirrors_coords (mirrors, 22, 11/2*p, 2*r)
    set_mirrors_coords (mirrors, 16, 12/2*p, 2*r)
    set_mirrors_coords (mirrors, 11, 13/2*p, 2*r)

    #outer_circle

    set_mirrors_coords (mirrors, 10, 1/3*p, 3*r)
    set_mirrors_coords (mirrors, 5, 2/3*p, 3*r)
    set_mirrors_coords (mirrors, 1, 3/3*p, 3*r)
    set_mirrors_coords (mirrors, 2, 4/3*p, 3*r*np.cos(np.radians(p/2)))
    set_mirrors_coords (mirrors, 3, 5/3*p, 3*r*np.cos(np.radians(p/2)))
    set_mirrors_coords (mirrors, 4, 6/3*p, 3*r)
    set_mirrors_coords (mirrors, 9, 7/3*p, 3*r)
    set_mirrors_coords (mirrors, 15, 8/3*p, 3*r)
    set_mirrors_coords (mirrors, 26, 10/3*p, 3*r)
    set_mirrors_coords (mirrors, 31, 11/3*p, 3*r)
    set_mirrors_coords (mirrors, 35, 12/3*p, 3*r)
    set_mirrors_coords (mirrors, 34, 13/3*p, 3*r*np.cos(np.radians(p/2)))
    set_mirrors_coords (mirrors, 33, 14/3*p, 3*r*np.cos(np.radians(p/2)))
    set_mirrors_coords (mirrors, 32, 15/3*p, 3*r)
    set_mirrors_coords (mirrors, 27, 16/3*p, 3*r)
    set_mirrors_coords (mirrors, 21, 17/3*p, 3*r)

    mirrors_data_frame = pd.DataFrame(mirrors)    
    mirrors_data_frame.sort_values('number', inplace=True)

    return mirrors_data_frame

def init_plot (xlabel, ylabel, title, xlim, ylim, ticks_arrange, numb_ticks, ticks_alpha=0.8):

#    fig, ax = plt.subplots(figsize=(size,size))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    major_ticks = np.arange(-ticks_arrange, ticks_arrange, numb_ticks)
    ax.set_xticks(major_ticks)
    ax.set_yticks(major_ticks)
    ax.grid(which='major', alpha=ticks_alpha)
    ax.set_xlim([-xlim, xlim])
    ax.set_ylim([-ylim, ylim])
    
    return

def create_pandas_df_with_spot_results ():
    focal_spots = {'number': [], 'x_coord': [], 'y_coord': []}

    focal_spots['number'] = [18, 33, 34, 35, 31, 30, 29, 28, 27, 32, 21, 22, 16, 17, 11, 10, 12, 5, 6, 1, 2, 7, 8, 3, 4, 9, 15, 14, 20, 19, 13, 25, 26, 24, 23]
    focal_spots['x_coord'] = [0, l-463, r-185, r+76, r+122, r-108, l+391, l+84, l-80, l+13, l-258, l-32, l-107, l+181, l+134, l-107, l+309, l-209, l+217, l-177, l+158, l+408, r-235, r-201, r+43, r+122, r+215, r+72, r+160, r-160, r-244, r+33, r+220, r-348, l+420]
    focal_spots['y_coord'] = [0, d-27, d-60, d-120, d+14, d+37, d+163, d+134, d+243, d-198, d+521, d+474, d+630, d+658, u-323, u-296, u-372, u-245, u-70, u+115, u+134, u-160, u-73, u+22, u+104, u-70, u-522, u-470, u-105, u-745, u-463, d+283, d+344, d+427, d+412]

    for i in range (34):
        focal_spots['x_coord'][i] = - focal_spots['x_coord'][i]

    focal_spots_data_frame = pd.DataFrame(focal_spots)    
    focal_spots_data_frame.sort_values('number', inplace=True)

    return focal_spots_data_frame
########################################################################################################    
########################################################################################################
########################################################################################################    
r, d = 620, 600
p = 60
f = 4750
F = [f]*34
F2 = [2*f]*34
Z_0 = [0]*34
r = 436
l = -492
u = 645
d = -655

#script_dir = os.getcwd()
#os.remove (script_dir + "/.mess.txt")
#os.remove (script_dir + "/.mess.txt")

fig, ax = plt.subplots(figsize=(15,15))
init_plot ('X, mm', 'Y, mm', 'Spots', 1800, 1800, 1800, 180)
########################################################################################################
########################################################################################################
########################################################################################################
mirrors_data_frame_sorted = init_IACT_mirrors_in_pandas_df (r, p)
mirrors_data_frame_sorted.to_csv(r'/home/yaroslav/Yaroslavus_GitHub/IACT_workshop_experiments/mirrors.csv', header=None, index=None, sep=' ', mode='a')
mirrors_sorted = pd.read_csv('/home/yaroslav/Yaroslavus_GitHub/IACT_workshop_experiments/mirrors.csv', sep=' ', names=['number','x_coord','y_coord'])
mirrors_data_frame_sorted = pd.DataFrame(mirrors_sorted)
#print(mirrors_data_frame_sorted)

focal_spots_data_frame_sorted = create_pandas_df_with_spot_results ()
focal_spots_data_frame_sorted.to_csv(r'/home/yaroslav/Yaroslavus_GitHub/IACT_workshop_experiments/focal.csv', header=None, index=None, sep=' ', mode='a')
focal_spots_sorted = pd.read_csv('/home/yaroslav/Yaroslavus_GitHub/IACT_workshop_experiments/focal.csv', sep=' ', names=['number','x_coord','y_coord'])
focal_spots_data_frame_sorted = pd.DataFrame(focal_spots_sorted)
#print(focal_spots_data_frame_sorted)
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
double_focal_spots = []

for i in range (34):
    double_focal_spots.append(x_y_in_double_focus_distance(mirrors_data_frame_sorted['x_coord'][i], mirrors_data_frame_sorted['y_coord'][i], Z_0[i], focal_spots_data_frame_sorted["x_coord"][i], focal_spots_data_frame_sorted["y_coord"][i], F[i], F2[i]))

double_focal_spots_data_frame = pd.DataFrame(double_focal_spots)
########################################################################################################
########################################################################################################
########################################################################################################
plt.plot(mirrors_data_frame_sorted['x_coord'], mirrors_data_frame_sorted['y_coord'], 'o', color='gray', markersize=r/6.5, alpha=0.05)
plt.plot(focal_spots_data_frame_sorted['x_coord'], focal_spots_data_frame_sorted['y_coord'], 'o', color='red')
plt.plot(double_focal_spots_data_frame[0], double_focal_spots_data_frame[1], 'o', color='green')

for i in range (34):
    plt.annotate(mirrors_data_frame_sorted["number"][i], xy=(mirrors_data_frame_sorted["x_coord"][i],mirrors_data_frame_sorted["y_coord"][i]), xytext=(mirrors_data_frame_sorted["x_coord"][i],mirrors_data_frame_sorted["y_coord"][i]),fontsize=10)
    plt.annotate(focal_spots_data_frame_sorted["number"][i], xy=(focal_spots_data_frame_sorted["x_coord"][i],focal_spots_data_frame_sorted["y_coord"][i]), xytext=(focal_spots_data_frame_sorted["x_coord"][i]+20,focal_spots_data_frame_sorted["y_coord"][i]+20),fontsize=10)
    plt.annotate(focal_spots_data_frame_sorted['number'][i], xy=(double_focal_spots_data_frame[0][i], double_focal_spots_data_frame[1][i]), xytext=(double_focal_spots_data_frame[0][i]+20, double_focal_spots_data_frame[1][i]+20),fontsize=8)
########################################################################################################
########################################################################################################
########################################################################################################
"""
for i in ([3, 31, 0, 19, 32]):
    
    c = plt.Circle((double_focal_spots_data_frame[0][i], double_focal_spots_data_frame[1][i]), 9500*np.tan(np.radians(5)), facecolor='none', edgecolor="green", linewidth=1, alpha=1)
    ax.add_artist(c)

for i in ([19]):
    
    c = plt.Circle((double_focal_spots_data_frame[0][i], double_focal_spots_data_frame[1][i]), 9500*np.tan(np.radians(5+1)), facecolor='none', edgecolor="blue", linewidth=1, alpha=0.7)
    ax.add_artist(c)

for i in ([19]):
    
    c = plt.Circle((double_focal_spots_data_frame[0][i], double_focal_spots_data_frame[1][i]), 9500*np.tan(np.radians(5+2)), facecolor='none', edgecolor="blue", linewidth=1, alpha=0.6)
    ax.add_artist(c)

for i in ([32]):
    
    c = plt.Circle((double_focal_spots_data_frame[0][i], double_focal_spots_data_frame[1][i]), 9500*np.tan(np.radians(5+1)), facecolor='none', edgecolor="blue", linewidth=1, alpha=0.7)
    ax.add_artist(c)

for i in ([32]):
    
    c = plt.Circle((double_focal_spots_data_frame[0][i], double_focal_spots_data_frame[1][i]), 9500*np.tan(np.radians(5+2)), facecolor='none', edgecolor="blue", linewidth=1, alpha=0.6)
    ax.add_artist(c)
    
for i in ([32]):
    
    c = plt.Circle((double_focal_spots_data_frame[0][i], double_focal_spots_data_frame[1][i]), 9500*np.tan(np.radians(5+3)), facecolor='none', edgecolor="blue", linewidth=1, alpha=0.5)
    ax.add_artist(c)

for i in ([32]):
    
    c = plt.Circle((double_focal_spots_data_frame[0][i], double_focal_spots_data_frame[1][i]), 9500*np.tan(np.radians(5+4)), facecolor='none', edgecolor="blue", linewidth=1, alpha=0.4)
    ax.add_artist(c)
    
for i in ([32]):
    
    c = plt.Circle((double_focal_spots_data_frame[0][i], double_focal_spots_data_frame[1][i]), 9500*np.tan(np.radians(5+5)), facecolor='none', edgecolor="blue", linewidth=1, alpha=0.3)
    ax.add_artist(c)
#for i in range (len(focal_spots_data_frame_sorted)):
#    
#    c = plt.Circle((focal_spots_data_frame_sorted["x_coord"][i],focal_spots_data_frame_sorted["y_coord"][i]), 4750*np.tan(np.radians(5)), facecolor='none', edgecolor="red", linewidth=1, alpha=1)
#    ax.add_artist(c)

#c = plt.Circle((0,0), 9500*np.tan(np.radians(5)), facecolor='none', edgecolor="green", linewidth=1, alpha=0.5)
#ax.add_artist(c)
#plt.hlines(u, l, r, linestyle='-', edgecolor="black", linewidth=1, alpha=0.5)
#plt.hlines(d, l, r, linestyle='-', edgecolor="black", linewidth=1, alpha=0.5)
#plt.vlines(l, d, u, linestyle='-', edgecolor="black", linewidth=1, alpha=0.5)
#plt.vlines(r, d, u, linestyle='-', edgecolor="black", linewidth=1, alpha=0.5)

#plt.savefig('all points', fmt='png')"""
plt.show()
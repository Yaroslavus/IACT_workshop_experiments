import pandas as pd
import matplotlib.pyplot as plt 

def x_y_in_double_focus_distance (x0, y0, z0, x1, y1, z1, z2):
    return [(z2-z0)*(x1 - x0)/(z1 - z0) + x0, (z2-z0)*(y1 - y0)/(z1 - z0) + y0]


t = pd.read_csv('/home/yaroslav/Yaroslavus_GitHub/IACT_workshop_experiments/Summary_table.csv',
                       sep=' ', names=['number_kb','x_kb','y_kb', 'z_kb', 'alpha_YZ_kb', 'beta_XZ_kb', 'x_dev_exp', 'y_dev_exp', 'f_exp', 'f_kb', 'fix_angle'])

t_df = pd.DataFrame(t)

#fig = plt.figure(figsize=(15,15))
#ax = plt.axes()

fig, ax = plt.subplots(figsize=(15,15))
## Axes labels and the title ##
plt.xlabel('X, mm')
plt.ylabel('Y, mm')
plt.title("Изображение")
## Grid ##
major_ticks = np.arange(-4000, 4000, 200)
#minor_ticks = np.arange(-10000, 10000, 200)
ax.set_xticks(major_ticks)
#ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
#ax.set_yticks(minor_ticks, minor=True)
#ax.set_zticks(major_ticks)
#ax.set_zticks(minor_ticks, minor=True)
# And a corresponding grid
#ax.grid(which='both')
# Or if you want different settings for the grids:
#ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.8)
ax.set_xlim([-4000, 4000])
ax.set_ylim([-4000, 4000])
#ax=plt.gca()
#плот отклонений на фокусном расстоянии (напрямую из эксперимента)
plt.plot(t['x_dev_exp'], t["y_dev_exp"], 'o', color='red')

#for i in ([31, 24, 22, 30, 32, 9]):
#    
#    c1 = plt.Circle((t_df["x_dev_exp"][i],t_df["y_dev_exp"][i]), 4750*np.tan(np.radians(5)), facecolor='none', edgecolor="red", linewidth=1, alpha=0.5)
#    ax.add_artist(c1)
#    c2 = plt.Circle((t_df["x_dev_exp"][i],t_df["y_dev_exp"][i]), 9500*np.tan(np.radians(5)), facecolor='none', edgecolor="green", linewidth=1, alpha=1)
#    ax.add_artist(c2)
    
    
for i in range (len(t["number_kb"])):
    plt.annotate(t["number_kb"][i], xy=(t["x_dev_exp"][i],t["y_dev_exp"][i]), xytext=(t["x_dev_exp"][i]+20,t["y_dev_exp"][i]+20),fontsize=8)
#плот расположения зеркал
plt.plot(t['x_kb'], t["y_kb"], 'o', color='gray', markersize=60, alpha = 0.3)
for i in range (len(t["number_kb"])):
    plt.annotate(t["number_kb"][i], xy=(t["x_kb"][i],t["y_kb"][i]), xytext=(t["x_kb"][i],t["y_kb"][i]),fontsize=8)

#plt.xlabel('mm')
#plt.ylabel('mm')
#plt.savefig('deviations on the double focus distance', fmt='png')
   
#print(t)

xy_new = []

#print(xy_new)

for i in range (len(t["number_kb"])):
    xy_new.append(x_y_in_double_focus_distance(t['x_kb'][i], t['y_kb'][i], t['z_kb'][i], t["x_dev_exp"][i], t["y_dev_exp"][i], t['f_kb'][i], 2*t['f_kb'][i]))

xy_new_df = pd.DataFrame(xy_new)
#print(xy_new)    
plt.plot(xy_new_df[0], xy_new_df[1], 'o', color='green')
for i in range (len(t["number_kb"])):
    plt.annotate(t["number_kb"][i], xy=(xy_new_df[0][i],xy_new_df[1][i]), xytext=(xy_new_df[0][i]+20,xy_new_df[1][i]+20),fontsize=8)

    
#for i in ([31, 24, 22, 30, 32, 9]):
#    
#    c2 = plt.Circle((xy_new_df[0][i],xy_new_df[1][i]), 9500*np.tan(np.radians(5)), facecolor='none', edgecolor="green", linewidth=1, alpha=1)
#    ax.add_artist(c2)

#print(len(t['number_kb']))
#plt.savefig('all points', fmt='png')

plt.show()
#print(xy_new_df)
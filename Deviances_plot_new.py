import pandas as pd
import matplotlib.pyplot as plt

t = pd.read_csv('/home/yaroslav/Yaroslavus_GitHub/IACT_workshop_experiments/Summary_table.csv',
                       sep=' ', names=['mirror_number','X_coord','Y_coord', 'Z_coord', 'alpha', 'beta', 'x_dev', 'y_dev', 'z_dev', 'distance_to_focus', 'fix_angle'])


t_df = pd.DataFrame(t)

plt.figure(figsize=(10,10))

plt.plot(t['X_coord'], t["Y_coord"], 'o', color='red')
for i in range (len(t["mirror_number"])):
    plt.annotate(t["mirror_number"][i], xy=(t["X_coord"][i],t["Y_coord"][i]), xytext=(t["X_coord"][i]+20,t["Y_coord"][i]+20),fontsize=8)

plt.plot(t['x_dev'], t["y_dev"], 'o', color='blue')
for i in range (len(t["mirror_number"])):
    plt.annotate(t["mirror_number"][i], xy=(t["x_dev"][i],t["y_dev"][i]), xytext=(t["x_dev"][i]+20,t["y_dev"][i]+20),fontsize=8)

#plt.yscale('log')
#plt.grid(True)
#plt.legend(loc='upper left')
#gridsize=(10,10)

plt.xlabel('mm')
plt.ylabel('mm')
plt.savefig('pic_12_1_1', fmt='png')
#plt.savefig('pic_12_1_1', fmt='pdf')
#deviance_radius = 475
#u, d, r, l = 645, -655, 436, -492
#plt.hlines(u, l, r, linestyle='-', colors='b')
#plt.hlines(d, l, r, linestyle='-', colors='b')
#plt.vlines(l, d, u, linestyle='-', colors='b')
#plt.vlines(r, d, u, linestyle='-', colors='b')
#plt.hlines(0, -deviance_radius, deviance_radius, linestyle='-', colors='g')
#plt.vlines(0,  -deviance_radius, deviance_radius, linestyle='-', colors='g')
       
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

exp = pd.read_csv('/home/yaroslav/Yaroslavus_GitHub/IACT_workshop_experiments/Spot_experiments_results.csv',
                       sep=' ', names=['mirror_number','X_coord','Y_coord','distance_to_focus'])
kb = pd.read_csv('/home/yaroslav/Yaroslavus_GitHub/IACT_workshop_experiments/Mirror_coordinates_and_angles_from_KB.csv',
                       sep=' ', names=['X_coord','Y_coord','Z_coord','alpha (YZ-plane)', 'beta (XZ-plane)'])

exp = pd.DataFrame(exp)
kb = pd.DataFrame(kb)

plt.figure(figsize=(10,10))

plt.plot(exp['X_coord'], exp["Y_coord"], 'o', color='red')
for i in range (len(exp["mirror_number"])):
    plt.annotate(exp["mirror_number"][i], xy=(exp["X_coord"][i],exp["Y_coord"][i]), xytext=(exp["X_coord"][i]+20,exp["Y_coord"][i]+20),fontsize=8)
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
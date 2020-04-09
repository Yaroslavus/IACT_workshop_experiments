import telescope_in_workshop_functions as ft
import pandas as pd

Mirrors = ['']*34

with open('/home/yaroslav/Yaroslavus_GitHub/IACT_workshop_experiments/Summary_table.csv', 'r') as f:

    temp = f.read().splitlines()

for i in range(len(temp)):   

    k = list(temp[i].split())
    a = ft.mirror(float(k[0]), float(k[1]), float(k[2]), float(k[3]), float(k[4]), float(k[5]), float(k[6]), float(k[7]), float(k[8]), float(k[9]), float(k[10]))
    Mirrors[i] = a
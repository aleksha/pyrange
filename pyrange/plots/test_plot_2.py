import pyrange
import matplotlib.pyplot as plt
import random
import numpy as np
import argparse

'''
leave-one-out for each variable for selected materials (3 random materials by default)
'''

# read materials from the arguments
parser = argparse.ArgumentParser(description='does stuff')
parser.add_argument('materials', type=str, nargs='*', help='materials for the plot')
args = parser.parse_args()

random_mat_names = [tup.names[0] for tup in random.sample(pyrange.registry, k=3)]
materials = [pyrange.material(mat_name) for mat_name in (args.materials if len(args.materials) else random_mat_names)]

#TODO: rename
loo = lambda mylist, i: [x for j,x in enumerate(mylist) if j!=i]
ar = np.asarray
epsilon = 1e-6

for material in materials:
    x = material.table['kinetic_energy'][1:-1]
    n = len(x)
    
    csda_range_pred = []
    csda_range_true = material.table['csda_range'][1:-1]
    projected_range_pred = []
    projected_range_true = material.table['projected_range'][1:-1]
    detour_factor_pred = []
    detour_factor_true = material.table['detour_factor'][1:-1]
    total_stopping_power_pred = []
    total_stopping_power_true = material.table['total_stopping_power'][1:-1]

    for i in range(1, n+1):
        loo_table = {col:loo(material.table[col],i) for col in material.table}
        material.create_functions(loo_table)
        csda_range_pred.append(material.csda_range(x[i-1])[()])
        projected_range_pred.append(material.projected_range(x[i-1])[()])
        detour_factor_pred.append(material.detour_factor(x[i-1])[()])
        total_stopping_power_pred.append(material.total_stopping_power(x[i-1]))
    

    csda_range_pred = ar(csda_range_pred)
    csda_range_true = ar(csda_range_true)
    projected_range_pred = ar(projected_range_pred)
    projected_range_true = ar(projected_range_true)
    detour_factor_pred = ar(detour_factor_pred)
    detour_factor_true = ar(detour_factor_true)
    total_stopping_power_pred = ar(total_stopping_power_pred)
    total_stopping_power_true = ar(total_stopping_power_true)

    plt.plot(x,(csda_range_pred-csda_range_true)/(csda_range_true+epsilon),'o',label='CSDA range')
    plt.plot(x,(projected_range_pred-projected_range_true)/(projected_range_true+epsilon),'o',label='projected range')
    plt.plot(x,(detour_factor_pred-detour_factor_true)/(detour_factor_true+epsilon),'o',label='detour factor')
    plt.plot(x,(total_stopping_power_pred-total_stopping_power_true)/(total_stopping_power_true+epsilon),'o',label='total stopping power')
    plt.title(f'Relative error\nMaterial: {material.name}')
    ax = plt.gca()
    ax.legend()
    plt.show()
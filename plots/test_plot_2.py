from .. import pyrange
import matplotlib.pyplot as plt
import random
import numpy as np

'''
leave-one-out for 3 random materials for each variable
'''

mat_tuples = random.sample(pyrange.registry, k=3)
materials = [pyrange.material(tup.names[0]) for tup in mat_tuples]

#TODO: rename
foo = lambda mylist, i: [x for j,x in enumerate(mylist) if j!=i]
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

    for i in range(1, n+1):
        loo_table = {col:foo(material.table[col],i) for col in material.table}
        material.create_functions(loo_table)
        csda_range_pred.append(material.csda_range(x[i-1])[()])
        projected_range_pred.append(material.projected_range(x[i-1])[()])
        detour_factor_pred.append(material.detour_factor(x[i-1])[()])
    

    csda_range_pred = ar(csda_range_pred)
    csda_range_true = ar(csda_range_true)
    projected_range_pred = ar(projected_range_pred)
    projected_range_true = ar(projected_range_true)
    detour_factor_pred = ar(detour_factor_pred)
    detour_factor_true = ar(detour_factor_true)

    csda_range_true
    plt.plot(x,(csda_range_pred-csda_range_true)/(csda_range_true+epsilon),'o',label='CSDA range')
    plt.plot(x,(projected_range_pred-projected_range_true)/(projected_range_true+epsilon),'o',label='projected range')
    plt.plot(x,(detour_factor_pred-detour_factor_true)/(detour_factor_true+epsilon),'o',label='detour factor relative')
    ax = plt.gca()
    ax.legend()
    plt.show()
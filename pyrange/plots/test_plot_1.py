import pyrange
import matplotlib.pyplot as plt
import random
import numpy as np
import argparse
from functools import reduce

'''
plots NIST data together with interpolating function for 3 random materials 
'''

# read materials from the arguments
parser = argparse.ArgumentParser(description='does stuff')
parser.add_argument('materials', type=str, nargs='*', help='materials for the plot')
args = parser.parse_args()

random_mat_names = [tup.names[0] for tup in random.sample(pyrange.registry, k=3)]
materials = [pyrange.material(mat_name) for mat_name in (args.materials if len(args.materials) else random_mat_names)]

variables = lambda material: ((material.csda_range, material.table['csda_range'], 'csda_range'),
(material.projected_range, material.table['projected_range'], 'projected_range'),
(material.total_stopping_power, material.table['total_stopping_power'], 'total_stopping_power'),
(material.detour_factor, material.table['detour_factor'], 'detour_factor'))

concat = lambda x,y : np.concatenate((x,y))

for material in materials:
    for (function, y, variable_name) in variables(material):
        x = material.table['kinetic_energy']
        linspaces_list = [np.linspace(x[i], x[i+1], 10) for i in range(len(x)-1)]
        x_pred = reduce(concat,linspaces_list)
        y_pred = function(x_pred)
        plt.plot(x,y,'o')
        plt.plot(x_pred,y_pred)
        plt.title(f'Interpolation plot\nMaterial: {material.name}\nVariable: {variable_name}')
        plt.show()

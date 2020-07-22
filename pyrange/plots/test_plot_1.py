import pyrange
import matplotlib.pyplot as plt
import random
import numpy as np

'''
plots NIST data together with interpolating function for 3 random materials 
'''

mat_tuples = random.sample(pyrange.registry, k=3)
materials = [pyrange.material(tup.names[0]) for tup in mat_tuples]

variables = lambda material: ((material.csda_range, material.table['csda_range'], 'csda_range'),
(material.projected_range, material.table['projected_range'], 'projected_range'),
(material.total_stopping_power, material.table['total_stopping_power'], 'total_stopping_power'),
(material.detour_factor, material.table['detour_factor'], 'detour_factor'))

for material in materials:
    for (function, y, variable_name) in variables(material):
        x = material.table['kinetic_energy']
        x_pred = np.linspace(min(x), max(x), 300)
        y_pred = function(x_pred)
        plt.plot(x,y,'o')
        plt.plot(x_pred,y_pred)
        plt.title('Interpolation plot\nMaterial: {material.name}\nVariable: {variable_name}')
        plt.show()

import pyrange
import matplotlib.pyplot as plt
import random
import numpy as np

mat_tuples = random.sample(pyrange.registry, k=3)
materials = [pyrange.material(tup.names[0]) for tup in mat_tuples]

variables = lambda material: ((material.csda_range, material.table['csda_range'], 'csda_range'),
(material.projected_range, material.table['projected_range'], 'projected_range'),
(material.detour_factor, material.table['detour_factor'], 'detour_factor'))

for material in materials:
    for (function, y, variable_name) in variables(material):
        x = material.table['kinetic_energy']
        x_pred = np.linspace(min(x), max(x), 300)
        y_pred = function(x_pred)
        plt.plot(x,y,'o')
        plt.plot(x_pred,y_pred)
        plt.title(f'Material: {material.name}\n Variable: {variable_name}')
        plt.show()





# range(1,len() - 1) # make a for loop with these indices, remove them each step and interpolate over the remaining

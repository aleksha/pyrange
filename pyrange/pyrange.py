from scipy.interpolate import interp1d
import numpy as np
import re
import pathlib

from pyrange.registry import registry


data_path = pathlib.Path(__file__).parent.absolute() / "./data/"

def search(search_string):
    """Search name in the list of aliaces and display tuples
    which match search string"""
    for tup in registry:
        show_tup = False
        for alias in tup.names:
            if re.search(search_string, alias):
                show_tup = True
        if show_tup:
            print(tup)




class material:
    """Material class

        Density in g/cm3

        >>> import pyrange
        >>> pyrange.search("Гел")
        ('Helium.txt', 0.0001753, ['He', 'Helium', 'Гелий', 'Hélium', 'Elio', 'Helio'])
        >>> mat = pyrange.material("He")
        >>> mat.density
        0.0001753
        >>> mat.projected_range(10)
        array(690.24529378)
    """
    


    def __init__(self, name, density=None):
        self.name = name
        self.tup = self.find_material(name)
        self.density = density if density else self.tup.density
        self.is_dummy = (self.tup.filename == "None")

        zero_fn = lambda x: np.asarray(x)*0.
        self.projected_range = zero_fn
        self.csda_range = zero_fn
        self.detour_factor = zero_fn
        self.total_stopping_power = zero_fn

        self.table = {name:list() for name in ['kinetic_energy', 'projected_range', 'csda_range', 'detour_factor', 'total_stopping_power']} 

        if not self.is_dummy:
            self.read_table()
            self.create_functions()


    def create_functions(self, table = None):
            if not table:
                table = self.table
            
            self.projected_range = interp1d(
                table['kinetic_energy'], table['projected_range'], kind="cubic"
            )
            self.csda_range = interp1d(
                table['kinetic_energy'], table['csda_range'], kind="cubic"
            )
            self.detour_factor = interp1d(
                table['kinetic_energy'], table['detour_factor'], kind="cubic"
            )
            self.total_stopping_power = interp1d(
                table['kinetic_energy'], table['total_stopping_power'], kind="cubic"
            )

    def read_table(self):
        data_file = open(data_path / self.tup.filename, "r")
        for line in data_file:
            if line and not line.isspace() and line[0] != "#":
                columns = line.split()
                self.table['kinetic_energy'].append(float(columns[0]))
                self.table['projected_range'].append(float(columns[-2]) / self.density)
                self.table['csda_range'].append(float(columns[-3]) / self.density)
                self.table['detour_factor'].append(float(columns[-1]))
                self.table['total_stopping_power'].append(float(columns[3]) / self.density)

    def find_material(self, name):
        "Return tuple for the material if the name is in the list of aliases"
        for tup in registry:
            if name in tup.names:
                return tup
        print("ERROR: Material not found in the registry")
        return ("None", 1, ["None"])

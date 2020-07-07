from scipy.interpolate import interp1d
import numpy as np
import re

from registry import registry

data_path = "./data/"


def search(search_string):
    """Search name in the list of aliaces and display tuples
    which match search string"""
    for tup in registry:
        show_tup = False
        for alias in tup[2]:
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
        >>> mat.density()
        0.0001753
        >>> mat.projected_range(10)
        array(690.24529378)
    """

    def __init__(self, name, density=None):

        self.name = name
        self.tup = self.find_material(name)
        self.is_dummy = self.tup[0] == "None"

        if density is not None:
            self.tup[1] = density

        zero_fn = lambda x: 0.
        self.projected_range = zero_fn
        self.csda_range = zero_fn
        self.detour_factor = zero_fn

        self.kinetic_energy_list = []
        self.projected_range_list = []
        self.csda_range_list = []
        self.detour_factor_list = []

        if not self.is_dummy:
            self.read_lists()
            self.projected_range = interp1d(
                self.kinetic_energy_list, self.projected_range_list, kind="cubic"
            )
            self.csda_range = interp1d(
                self.kinetic_energy_list, self.csda_range_list, kind="cubic"
            )
            self.detour_factor = interp1d(
                self.kinetic_energy_list, self.detour_factor_list, kind="cubic"
            )

    def read_lists(self):
        data_file = open(data_path + self.tup[0], "r")
        for line in data_file:
            if line and not line.isspace() and line[0] != "#":
                columns = line.split()
                self.kinetic_energy_list.append(float(columns[0]))
                self.projected_range_list.append(float(columns[-2]) / self.density())
                self.csda_range_list.append(float(columns[-3]) / self.density())
                self.detour_factor_list.append(float(columns[-1]))

    def density(self):
        "Return density of material"
        return self.tup[1]

    def find_material(self, name):
        "Return tuple for the material if name in the list of aliases"
        for tup in registry:
            if name in tup[2]:
                return tup
        print("ERROR: Mo material found in registry")
        return ("None", 1, ["None"])

from scipy.interpolate import interp1d
import numpy as np
import re

from registry import registry

data_path = "./data/"

def search( search_string ):
    """Search name in the list of aliaces and display tuples
    which match search string"""
    for tup in registry:
        show_tup = False
        for alias in tup[2]:
            if re.search(search_string,alias):
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

    def __init__(self , name , density = None ):
        self.name = name
        self.tup  = self.find_material( name )
        self.is_dummy = False
        if self.tup[0]=="None":
            self.is_dummy = True
        if density is not None:
            self.tup[1] = density
        self.projected_range = self.zero
        if not self.is_dummy:
            self.projected_range = self.create_projected_range()

    def create_projected_range( self ):
        "Return function which calculates projected range"
        data_file = open( data_path + self.tup[0] ,"r")
        kinetic_energy = [] ; proj_range = []
        for line in data_file:
            if line and not line.isspace() and line[0]!="#":
                kinetic_energy.append( float(line[:-1].split("  ")[1]) )
                proj_range.append( float(line[:-1].split("  ")[6] )/ self.density() )
        f3 = interp1d(kinetic_energy, proj_range, kind='cubic')
        return(f3)

    def density( self ):
        "Return density of material"
        return(self.tup[1])

    def zero(self):
        "Return zero"
        return(0.)

    def find_material(self, name):
        "Return tuple for the material if name in the list of aliases"
        for tup in registry:
            if name in tup[2]:
                return(tup)
        print("ERROR: Mo material found in registry")
        return( ("None",1,["None"]) )

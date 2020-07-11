# pyrange
Python module to calculate range and stopping power for protons in different materials.

The module makes interpolation over tables provided bu National Institute of Standards and Technology.

**Proton tables:** https://physics.nist.gov/PhysRefData/Star/Text/PSTAR.html

Dependencies
------------
 - NumPy
 - SciPy

How-to use it
-------------
```python
>>> import pyrange
>>> pyrange.search("Гел")
('Helium.txt', 0.0001753, ['He', 'Helium', 'Гелий', 'Hélium', 'Elio', 'Helio'])
>>> mat = pyrange.material("He")
>>> mat.density
0.0001753
>>> mat.projected_range(10)
array(690.24529378)
>>> mat.projected_range( [1,10,100] )
array([1.21905305e+01, 6.90245294e+02, 4.52139190e+04])
```

To add material
---------------

Go to https://physics.nist.gov/PhysRefData/Star/Text/PSTAR-t.html

Select material and click __Submit__ button

Save file to **./data/** (don't forget to comment non-data strings with the hash sign)

Update **registry.py** by adding a tuple of the next structure:
 - First element is the filename.
 - Second is density, which should be in __g/cm3__ units.
 - Third is the list of names, which should contain: element sign or formula, name
   in different languages (English, Russian, German, French, Italian, and Spanish).
   

Make a pull request into master (development branch will appear soon).


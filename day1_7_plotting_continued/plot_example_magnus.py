# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import astropy.units as u
import astropy.constants as c
import numpy as np

# <markdowncell>

# Now we can define numbers *with* units

# <codecell>

1.5E14 * u.mm

# <markdowncell>

# We can list what units that `astropy.Quantities` can understand and convert between for that specific unit.

# <codecell>

u.mm.find_equivalent_units()

# <markdowncell>

# To convert to other units we do

# <codecell>

1.5E14 * u.mm.to(u.AU)

# <codecell>

distance = 1.5E14 * u.mm
distance.to(u.solRad)

# <markdowncell>

# Another example, converting between wavelength in mm and frequency in Hertz

# <codecell>

co_wl = 2.60076 * u.mm
co_wl

# <markdowncell>

# Following previous exampe, you would then simple convert it to `u.Hz`

# <codecell>

nu = co_wl.to(u.Hz)

# <markdowncell>

# This does not work because it does not understand that it is a spectral unit. In the `Quantities.unit` module there are several equivalencies, which are just a lookup table of how to convert certain units to one another. In this case we want the `u.spectral` equivalencies. It is also possible to define your own equivalencies. 

# <codecell>

u.spectral()

# <markdowncell>

# Now we can convert wavelength to frequency.

# <codecell>

nu = co_wl.to(u.Hz, equivalencies=u.spectral())
nu

# <codecell>

nu = co_wl.to(u.GHz, equivalencies=u.spectral())
nu

# <markdowncell>

# To demonstrate how this simplifies our lives, I will show how to calculate the Stefan-Boltzmann law:
# 
# $L = 4\pi\sigma_{sb}T^4$

# <codecell>

T = 5550 * u.K
R = 7e10 * u.cm
L = 4 * np.pi * R**2 * c.sigma_sb * T**4
L

# <markdowncell>

# All I have to care about is that I now what units I input. As output I get a rather complex and unnecessary unit... 
# 
# However, I can easily get the unit Watts, by just asking for it. It is easy to see how this simplifies large and complex calculations (Column densities, Flux etc.)

# <codecell>

L.to(u.W)

# <markdowncell>

# We can also ask for other units directly.

# <codecell>

L.to(u.L_sun)

# <markdowncell>

# What about functions? Let's say you make a function to calculate the Stefan-Boltzmann law, and you want to make sure the input has units.
# 
# Here you can use the decorator `@u.quantity_input()`

# <codecell>

@u.quantity_input(R=u.cm, T=u.K)
def sb_law(R,T):
    L = 4 * np.pi * R**2 * c.sigma_sb * T**4
    return L

# <markdowncell>

# Now we test it!

# <codecell>

sb_law(100,100)

# <markdowncell>

# The input had no units! Correct this.

# <codecell>

sb_law(1.0*u.R_sun, 100*u.K)

# <markdowncell>

# Note that the radius input had a different unit than `u.cm`, this is because `u.R_sun` is convertable to/from `u.cm`. 
# 
# ALSO, the output units is not the nicest, so lets fix this.

# <codecell>

@u.quantity_input(R=u.cm, T=u.K)
def sb_law(R,T):
    L = 4 * np.pi * R**2 * c.sigma_sb * T**4
    return L.to(u.L_sun)

# <codecell>

sb_law(1.0*u.R_sun, 100*u.K)

# <markdowncell>

# Now lets make a plot!

# <codecell>

T_range = np.arange(4000.,30000.,500.) * u.K
R_range = np.arange(0.1,10.) * u.R_sun
T_grid, R_grid = np.meshgrid(T_range, R_range)
L_grid = sb_law(R_grid,T_grid)

# <codecell>

import matplotlib.pyplot as plt

# Set up matplotlib and use a nicer set of plot parameters
%config InlineBackend.rc = {}
import matplotlib
#matplotlib.rc_file("../../templates/matplotlibrc")
import matplotlib.pyplot as plt
%matplotlib inline
matplotlib.style.use('ggplot')
plt.rcParams['axes.grid'] = False

# <markdowncell>

# Now a short example of how to plot contours...

# <codecell>

plt.contourf(R_grid,T_grid, np.log10(L_grid.value), 500, cmap='cubehelix')
cb = plt.colorbar()
cb.set_label(L_grid.unit)

plt.xlabel(R_grid.unit)
plt.ylabel(T_grid.unit)

lim_low = 1.
lim_up = 3.
fmt = {lim_low : 'Lower limit', lim_up : 'Upper limit'}
cs = plt.contour(R_grid,T_grid, np.log10(L_grid.value), levels=[lim_low, lim_up])
plt.clabel(cs, inline=1, fontsize=14, fmt=fmt, manual=[[4,5000],[4,15000]])

# <codecell>


# <codecell>



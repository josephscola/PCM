#!/usr/bin/env python
# coding: utf-8

# # Temperature Dependence of Polymer Viscosity
# 
# Polymers exhibit behavior during flow and deformation which depends on both temperature and time (frequency), that is, the viscoelastic response of a polymer will depend on the shear history. Only for Newtonian liquids, and in a first approximation for low molecular weight polymers, is the viscosity independent of the shear history. In this case, the temperature dependence of the viscosity may be decribed by an Arrhenius equation of the form
# 
# where T is the absolute temperature, R the universal gas constant, A a material constant, and E the activation energy. Knowledge of the two material-dependent parameters E and A allows for the prediction of the viscosity for any temperature. The two parameters are usually determined from a plot of log η against 1/T which yields a straight line:
# 
# For most polymer melts a straight line can only be drawn over a fairly small temperature range of about 50°C. In general, the lower the shear rate and the molecular weight the better the agreement.
# 
# Doolittle1 provided another equation that is much more accurate for entangled polymer systems. He postulated that the viscosity is an exponential function of the reciprocal of the fractional free volume f:
# 
# or
# 
# where A and B are constants and f is the free volume fraction,
# 
# f = vf / v = (v - vhc) / v
# 
# vhc is the inaccessible volume and v the measured (molar) volume. Similar to the (molar) polymer volume, it can be assumed that the fractional free volume f increases linearly with temperature. Choosing the free volume at the glass transition temperature Tg as the reference state, the free volume as a function of temperature may be written as
# 
# f = fg +  αf (T - Tg)
# 
# where fg is the fractional free volume at Tg and αf is the thermal expansion coefficient. It has been suggested that the two parameters have the univerals values
# 
# fg ≈ 0.025
# αf ≈ 4.8 x 10-4 K-1
# 
# Williams, Landel and Ferry (1955) have suggested that the viscosity η at a temperature T may be related to the viscosity ηg at the glass transition temperature:2
# 
# or
# 
# where aT is the so called WLF shift factor. Using the universal values of fg and αf  yields two new constants:
# 
# C1 = B / fg ≈ 17.44
# C2 = fg / αf = 51.6 K
# 
# The two constants are not universal at all. Only polymers with isoviscose behavior will obey the WLF equation. For all other polymers, the two parameters might be very different.
# 
# Many polymers have melt viscosities of about 1013 poise at their glass transition temperature. Lets assume a polymer has a glass transition temperature of about 373 K then the viscosity at 423 K is:
# 
# or η = 2.61 x 104 Poise.
# References & Notes
# 
#     A.K Doolittle, Journal of Applied Physics, Vol. 22, 12, 1471 - 1475 (1951)
# 
#     M.L Williams, R.F. Landel and J.D. Ferry, J. Am. Chem. Soc. 77, 3701-3707 (1955)
# 
# 

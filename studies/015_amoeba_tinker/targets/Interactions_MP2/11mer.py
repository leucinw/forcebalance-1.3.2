#!/usr/bin/env python

from extrap import *

Energies = {'434' : [  -839.04424019, -839.79040799, -840.03855886, -840.13079444],
            '515' : [  -839.04374322, -839.79020710, -840.03844712, -840.12994123],
            '551' : [  -839.04326503, -839.78986502, -840.03821997, -840.12952335],
            '443' : [  -839.04364997, -839.78964782, -840.03791999],
            '4412' : [ -839.04193693, -839.78810992, -840.03666220],
            'H2O' : [  -76.26090977 , -76.32899240 , -76.35190653, -76.36021090]}
            
for isomer in Energies:
    if isomer == 'H2O': continue
    Series = Energies[isomer]
    Water = Energies['H2O']
    print "Isomer", isomer
    for i in range(len(Series)):
        print "%i zeta:" % (i+2),
        cplx = Series[i]
        mon = Water[i]
        print 627.51 * (cplx - 11 * mon)

    for i in range(len(Series) - 1):
        print "%i-%i extrapolation:" % (i+2, i+3), 
        cplx = helg_extrap(Series[i],Series[i+1],i+2,i+3)
        mon = helg_extrap(Water[i],Water[i+1],i+2,i+3)
        print 627.51 * (cplx - 11 * mon)

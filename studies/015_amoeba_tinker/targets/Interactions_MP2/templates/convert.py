#!/usr/bin/env python

from forcebalance.molecule import Molecule
from numpy import *
import sys

MList = [('monomer_mp2.xyz', '1mer_template.arc'),
         ('octamer_s4.xyz', '8mer_template.arc'),
         ('octamer_d2d.xyz', '8mer_template.arc'),
         ('endecamer_n11_434_isomer.xyz', '11mer_template.arc'),
         ('endecamer_n11_515_isomer.xyz', '11mer_template.arc'),
         ('endecamer_n11_551_isomer.xyz', '11mer_template.arc'),
         ('endecamer_n11_443_isomer.xyz', '11mer_template.arc'),
         ('endecamer_n11_4412_isomer.xyz', '11mer_template.arc'),
         ('n16_boat_isomer.xyz', '16mer_template.arc'),
         ('n16_boat3_isomer.xyz', '16mer_template.arc'),
         ('n16_tip3p_isomer.xyz', '16mer_template.arc'),
         ('n16_abab_isomer.xyz', '16mer_template.arc'),
         ('n16_aabb_isomer.xyz', '16mer_template.arc'),
         ('n17_sphere.xyz', '17mer_template.arc'),
         ('n17_5525.xyz', '17mer_template.arc'),
         ('n20_dodecahedron_c1.xyz', '20mer_template.arc'),
         ('n20_fused_cubes_c2.xyz', '20mer_template.arc'),
         ('n20_facesharing_pentagonal_prisms_c1.xyz', '20mer_template.arc'),
         ('n20_edgesharing_pentagonal_prisms_c1.xyz', '20mer_template.arc')]

for xyzfnm, tempfnm in MList:
    M = Molecule(tempfnm)
    X = Molecule(xyzfnm)
    print xyzfnm, X.elem
    # Special correction for when O and H are out of order.
    if len(X.elem) == 18 and X.elem[:6] == ['O','O','O','O','O','O']:
        print "Reordering atoms"
        for i in range(6):
            M.xyzs[0][3*i] = X.xyzs[0][i]
            hi = 1
            for j in range(6,18):
                xo = X.xyzs[0][i]
                xh = X.xyzs[0][j]
                if linalg.norm(xh-xo) < 1.2:
                    M.xyzs[0][3*i+hi] = xh
                    hi += 1
            if hi != 3:
                print "Crap, I seem to have missed or overcounted hydrogens."
                sys.exit()
    else:
        M.xyzs = X.xyzs
    for i in range(len(M.xyzs[0])):
        if i%3 != 0: continue
        o = M.xyzs[0][i]
        h1 = M.xyzs[0][i+1]
        h2 = M.xyzs[0][i+2]
        oh1 = h1 - o
        oh2 = h2 - o
        a = linalg.norm(oh1)
        b = linalg.norm(oh2)
        t = 180. / pi * arccos(dot(oh1,oh2)/a/b)
        print a, b, t
    for i, xi in enumerate(M.xyzs[0]):
        for j, xj in enumerate(M.xyzs[0]):
            if i != j and linalg.norm(xi-xj) < 0.8:
                print "Crap!"
                sys.exit()

    M.write("../%s" % xyzfnm, ftype="tinker")

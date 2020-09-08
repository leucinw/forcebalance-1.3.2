#!/usr/bin/env python

from forcebalance.molecule import Molecule
from numpy import *
import sys

MList = [("01-Prism.xyz", "hexamer_template.arc"),
         ("02-Cage.xyz", "hexamer_template.arc"),
         ("03-Bag.xyz", "hexamer_template.arc"),
         ("04-Cyclic-Chair.xyz", "hexamer_template.arc"),
         ("05-Book-1.xyz", "hexamer_template.arc"),
         ("06-Book-2.xyz", "hexamer_template.arc"),
         ("07-Cyclic-Boat-1.xyz", "hexamer_template.arc"),
         ("08-Cyclic-Boat-2.xyz", "hexamer_template.arc"),
         ("penta.xyz", "pentamer_template.arc"),
         ("tetra.xyz", "tetramer_template.arc"),
         ("trimer.xyz", "trimer_template.arc"),
         ("smith01.xyz", "dimer_template.arc"),
         ("smith02.xyz", "dimer_template.arc"),
         ("smith03.xyz", "dimer_template.arc"),
         ("smith04.xyz", "dimer_template.arc"),
         ("smith05.xyz", "dimer_template.arc"),
         ("smith06.xyz", "dimer_template.arc"),
         ("smith07.xyz", "dimer_template.arc"),
         ("smith08.xyz", "dimer_template.arc"),
         ("smith09.xyz", "dimer_template.arc"),
         ("smith10.xyz", "dimer_template.arc"),
         ("monomer_exp.xyz", "monomer_template.arc"),
         ("monomer_mp2.xyz", "monomer_template.arc")]

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

#"monomer_mp2.xyz", 

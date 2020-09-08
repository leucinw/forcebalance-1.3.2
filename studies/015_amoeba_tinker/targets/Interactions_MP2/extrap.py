#!/usr/bin/env python

import os, sys
from lxml import etree
from forcebalance.molecule import pvec
import numpy as np

def helg_extrap(ex, ey, x, y):
    # Two-point Helgaker extrapolation
    # ex, x : Energy and zeta of smaller basis
    # ey, y : Energy and zeta of larger basis
    return (x**3*ex-y**3*ey)/(x**3-y**3)

def main():
    e3 = float(sys.argv[1])
    e4 = float(sys.argv[2])
    print "3-4 extrapolation:", helg_extrap(e3,e4,3,4)
    if len(sys.argv) > 3:
        e5 = float(sys.argv[3])
        print "4-5 extrapolation:", helg_extrap(e4,e5,4,5)
        
if __name__ == "__main__":
    main()

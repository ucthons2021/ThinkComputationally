#!/usr/bin/env python3

import numpy

def calc_pi_hitmiss(n):
    """Estimate pi using a hit-and-miss Monte-Carlo simulation.

    Pi is calculated by generating n points that are uniformly distributed
    in a square with sides of length 1. The probability for a point to be
    within within a circle around the origin with radius 1 is pi/4.

    Parameters:
      n:  number of points to generate
    """

    # generate the points as a 2 x n numpy array
    points = numpy.random.random((2,n))

    # calculate the radii
    r = numpy.hypot(points[0], points[1])

    # determine the fraction of points in the acceptance region
    frac = numpy.count_nonzero( r < 1 ) / n

    # pi is 4 times the expected acceptance fraction
    return frac * 4


# Define a main programme for testing
if __name__ == '__main__':
    print(calc_pi_hitmiss(100000))

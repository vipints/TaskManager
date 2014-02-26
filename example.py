#!/usr/bin/env python

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Written (W) 2008-2013 Christian Widmer
# Copyright (C) 2008-2013 Max-Planck-Society

import time

def compute_factorial(n):
    """
    computes factorial of n
    """

    print '*****'
    print 'Sleeping for 5 sec.'
    print '*****'

    time.sleep(5)

    ret = 1
    for i in xrange(n):
        ret=ret*(i+1)

    print 'completed calculations'
    print ret

    print '*****'
    print 'Sleeping for 5 sec.'
    print '*****'
    time.sleep(5)

def main(argv=None):
    """
    main function to set up example
    """

    # next we execute function on the cluster
    nb = 10
    compute_factorial(nb)


if __name__ == "__main__":
    main()


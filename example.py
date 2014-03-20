#!/usr/bin/env python
"""
example script to test the execution 
"""

import time

def compute_factorial(n):
    """
    computes factorial of n
    """

    print '*****'
    print 'Sleeping for 5 sec before starting'
    print '*****'
    time.sleep(5)

    result = 1
    for i in xrange(n):
        result=result*(i+1)

    print 'completed calculations', n, 'factorial is', result 

    print '*****'
    print 'Sleeping for 5 sec after finishing'
    print '*****'
    time.sleep(5)

def main(argv=None):
    """
    main function to set up example
    """

    nb = 10
    # next we execute function 
    compute_factorial(nb)

if __name__ == "__main__":
    main()

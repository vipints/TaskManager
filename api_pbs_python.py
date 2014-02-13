"""
The main pbs module
"""

import os 
import re 
import sys

HAVE_PBS_PYTHON = True
try:
    import pbs
    from PBSQuery import PBSQuery
except:
    print 'Failed to import pbs_python module'
    HAVE_PBS_PYTHON = False

def get_query():
    """
    Return query instance
    """
    return PBSQuery()

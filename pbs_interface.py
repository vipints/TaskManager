#!/usr/bin/env python  
"""
python utilities for TORQUE 

pbs_interface provides a high level front-end to pbs_python.
This module provides wrappers that simplify submission and collection of jobs.
"""

import os 
import re 
import sys
import uuid 
 

err_message = """
The 'pbs_interface' runner depends on 'pbs_python' which is not installed 
or not configured properly. please follow the instructions found at:

    https://oss.trac.surfsara.nl/pbs_python

Additional errors may follow:
%s
"""

HAVE_PBS_PYTHON = True
try:
    import pbs
    from PBSQuery import PBSQuery
except Exception, ECP:
    HAVE_PBS_PYTHON = False
    raise Exception( err_message % str( ECP ) )

try:
    import multiprocessing
except:
    print "Error importing multiprocessing module. Local computing limited to one CPU."


class PBSJobSetUP()
    """
    Job setup 
    """

    def __init__( self )
        """
        Job construction 
        """
        
        self.environment = None
        self.working_dir = None
        self.name = 'pi_' + str(uuid.uuid1()) 
        self.jobid = ""


class PBSJobRunner():
    """
    Job runner 
    """
    
    def __init__( self, ARG, nworkers ):
        """
        Default settings for Job starting
        """
        
        self.default_pbs_server = None
        self.mem = ""
        self.walltime = "" 
        self.nodes = "" 
        self.ppn = "" 
        self.host_name = "" 
        self.working_dir = os.getcwd()
        self.num_resubmits = 0 


def get_query():
    """
    Return query instance
    """
    return PBSQuery()





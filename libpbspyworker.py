#!/usr/bin/env python  
"""
python utilities for TORQUE 

libpbspyworker provides a high level front-end to pbs_python.
This module provides wrappers that simplify submission and collection of jobs.
"""

import os 
import re 
import sys
import uuid 
import inspect

err_message = """
The 'libpbspyworker' runner depends on 'pbs_python' which is not installed 
or not configured properly. please follow the instructions found at:

    https://oss.trac.surfsara.nl/pbs_python

Additional errors may follow:
%s
"""

HAVE_PBS_PYTHON = False

try:
    import pbs
    HAVE_PBS_PYTHON = True

except Exception, ECP:
    raise Exception( err_message % str( ECP ) )


class Job(object):
    """
    Job setup 
    """

    def __init__( self, fn, args, kwlist=dict(), param=None, cleanup=True ):
        """
        Job construction 
        """
        
        self.fn = fn.__name__
        self.args = args 
        self.kwlist = kwlist
        self.cleanup = cleanup

        self.environment = None
        self.working_dir = None

        if param != None:
            self.__set_parameters(param)

        self.ret = None
        self.outdir = None 

        self.name = 'pj_' + str(uuid.uuid1()) 
        self.jobid = ""

    def __set_function(self, fn):
        """
        setter for function that carefully take care of namespace, avoiding __main__ as a module
        """
        
        module = inspect.getmodule(fn)
        
        if module.__name__ != "__main__":
            self.fn = fn 

    def __set_parameters(self, param):
        """
        function to set the parameters from a dict 
        """

        assert param!=None

        for key, val in param.items():
            setattr(self, key, val)

        return self 

    def execute(self): 
        """ 
        execute the function fn with given arguments 
        return value to ret variable 
        """

        try:
            self.ret = apply(self.fn, self.args, self.kwlist)

        except Exception, e:
            print "Exception encountered"
            print e 


class PBSJob(Job):
    """
    Job runner 
    """
    
    def __init__( self, fn, args, kwlist=dict(), param=None, cleanup=True ):
        """
        Default settings for Job starting
        """
        
        Job.__int__( self, fn, args, kwlist, param=param, cleanup=cleanup )

        self.default_pbs_server = None
        self.mem = ""
        self.nodes = "" 
        self.ppn = "" 
        self.walltime = "" 

        #self.host_name = "" 
        self.working_dir = os.getcwd()
        #self.num_resubmits = 0 
        #self.pbs_queue_name = None 
    
def process_jobs(jobs, local=False, maxNumThreads=1):
    """
    function to decide whether a job to run on the cluster or locally
    """

    if not local and HAVE_PBS_PYTHON:
        local = False 



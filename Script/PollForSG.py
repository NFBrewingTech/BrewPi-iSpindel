# SG Polling script
# Greg Masem - ispindel@mas321.com
# 
# This processes the data coming from the iSpindel and averages/cleans it.
# It will store data as CSV
# It will output the data to a location for BrePI script to pull in when datapoits saved.   
# 
# 
#  
#          

import sys
import datetime
import time
import os

import threading
import thread

import numpy

from numpy import genfromtxt
import csv
import functools
import ConfigParser


def getValue():
        """Returns the latest temperature, batt & gravity values of the  Hydrometer""" 

	ispindelreading = genfromtxt("/var/www/html/data/iSpindel/SpinData.csv", delimiter = ',')
	return ispindelreading
    

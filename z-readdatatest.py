__author__ = 'bob.zhu'
import json
udid='7211b9754480c6ad07744002a1f832f78d57933e'
file_object = open(udid,'r')
line=file_object.readline()
while line<>'':
    print line
    line=file_object.readline()
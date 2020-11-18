#!/usr/bin/env python

import os
import sys
import re

def natural_sort(l):

    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]

    return sorted(l, key=alphanum_key)

def listFiles(path):
    
    entries = natural_sort(os.listdir(path))
    result = ""
    print(entries)
    
    for x in entries:
	        
	newPath = path+"/"+x

        if os.path.isdir(newPath):
	    result += listFiles(newPath)

	else: 
	    result += x

    return result

def listDirs(path,key):
	
    entries = natural_sort(os.listdir(path))

    for x in entries:
	        
	newPath = path+"/"+x

        if os.path.isdir(newPath):
	    listDirs(newPath,key)

	if x == key :
	    print(newPath)

def listFilesByYes(path):
    
    entries = natural_sort(os.listdir(path))
    result = ""
    #print(entries)
    
    for x in entries:
	        
	newPath = path+"/"+x

        if os.path.isdir(newPath):
	    result += listFilesByYes(newPath)

        if( "yes" in entries and x != "yes") :
	    result += x

    return result	    

if __name__ == "__main__":
    target = sys.argv[1]
    #result = listFilesByYes(target)
    listDirs(target,"yes")
    print(result)
	

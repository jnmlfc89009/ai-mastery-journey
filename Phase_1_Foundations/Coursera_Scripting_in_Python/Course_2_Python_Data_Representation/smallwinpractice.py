#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 22:31:08 2026

@author: jnmlfc89009
"""



def printlist(legoset):
    """Print task list"""
    print("========================")
    num = 1
    for task in legoset:
        print(num, task.rstrip())
        num += 1
    print("========================")
    

datafile1 = open("/Users/jnmlfc89009/Downloads/favlegosets.txt", "rt", encoding="utf-8")
printlist(datafile1)

datafile1.close()
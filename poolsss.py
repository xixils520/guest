#   coding=utf-8
from multiprocessing import Pool
import os,time,random
def run_task(name):
    print('Task %s (%s)...' % (name, os.getpid()))
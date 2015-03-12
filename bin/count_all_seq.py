#!/usr/bin/env python

import os, fnmatch;
import sys
import os.path
import seq_utils

def count_seqs(filename):
        line_cnts = []
        dir_files = []
        dir = filename
        path_dir = sorted(os.listdir(dir))
        #print path_dir
        for filename in path_dir:
                try:
                        if filename.endswith('.fasta'):
                                path = os.path.join(dir,filename)
                                #print "filename>>",path
                                input_file = open(path)
                                count_fasta = seq_utils.count_seqs(input_file)                      
                                print count_fasta,"in", filename
                        else:

                                break
 		except IOError as e:
                                print e.path, "no such file"

print count_seqs("/home/user/Documents/python/data")








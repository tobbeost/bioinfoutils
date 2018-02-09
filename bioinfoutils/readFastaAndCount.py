#!/usr/bin/env python3
from bioinfoutils import create_seqdict
import sys

    
def main(filename):
  seqdict=create_seqdict(filename)
  n=len(seqdict)
  print('number of sequences='+str(n))

if __name__=='__main__':
  main(sys.argv[1])

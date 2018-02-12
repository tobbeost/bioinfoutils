#!/usr/bin/env python3
from bioinfoutils import read_fasta
import sys,argparse


def parseArgs(argv):
  ''' 
    Function for parsing arguments 
  '''
  parser = argparse.ArgumentParser(description='Remove duplicated sequences and write to file')
  parser.add_argument('-i', dest='infile', help="The name of the fasta input file.", required=True)
  parser.add_argument('-o', dest='outfile', help="The name of the fasta output file. Created if not provided.")
  parser.add_argument('-saveAllNames',dest='saveAllNames',action="store_true",help='Save all names of the duplicated sequence, default=FALSE')
  arguments=parser.parse_args(argv)
  return arguments
  

def removeDuplicates(infile):
  seqdict={}
  n=0
  with open(infile) as f:
    for name,seq in read_fasta(f):
      n+=1
      #USE the seuquence as a key.
      if seq not in seqdict:
        seqdict[seq]=[]
        seqdict[seq].append(name)
      else:
        seqdict[seq].append(name)
  #print('number of sequences in input file:',n)
  return(seqdict)

def printFastaFile_inverted(seqdict,outfile,saveAllNames):
  with open(outfile,'w') as g:
    for seq in seqdict:
      if saveAllNames==False:
        g.write('>'+seqdict[seq][0]+'\n')
      else: 
        g.write('>'+';'.join(seqdict[seq])+'\n')
      length=80 #wrap at 80 characters
      seq=seq.rstrip()
      while len(seq) > 0:
        g.write(seq[:length]+'\n')
        seq = seq[length:]
    

def main(infile,outfile,saveAllNames):
  if outfile==None:
    outfile=infile.split('.')[0]+'_2.fasta.out'
  seqdict=removeDuplicates(infile)
  print('number of sequences in output file:'+str(len(seqdict)))
  printFastaFile_inverted(seqdict,outfile,saveAllNames)



if __name__=='__main__':
  arguments=parseArgs(sys.argv[1:])
  main(arguments.infile,arguments.outfile,arguments.saveAllNames)
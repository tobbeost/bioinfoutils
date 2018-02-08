#!/usr/bin/env python3
def read_fasta(infile):
  name, seq = None, []
  for line in infile:
    if line.startswith(">"):
      line=line.rstrip().lstrip(">")
      if name: yield (name, ''.join(seq))
      name, seq = line, []
    else:
      line = line.rstrip()
      seq.append(line)

  if name: yield (name, ''.join(seq))

def create_seqdict(filename):
  print('loading file '+filename)
  seqdict={}
  with open(filename) as f:
    for name,seq in read_fasta(f):
      if name not in seqdict:
        seqdict[name]=seq
      else:
        print('not all id:s are unique')
  return(seqdict)

def printFastaFile(seqdict,outfile):
  with open(outfile,'w') as g:
    for name in sorted(seqdict.iterkeys()):
      g.write('>'+name+'\n')
      length=80 #wrap at 80 characters
      seq=seqdict[name].rstrip()
      while len(seq) > 0:
        g.write(seq[:length]+'\n')
        seq = seq[length:]
        
        

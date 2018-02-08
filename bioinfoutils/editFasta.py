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
  
def printFastaFile(seqdict,outfile):
  with open(outfile,'w') as g:
    for name in sorted(seqdict.iterkeys()):
      g.write('>'+name+'\n')
      length=80 #wrap at 80 characters
      seq=seqdict[name].rstrip()
      while len(seq) > 0:
        g.write(seq[:length]+'\n')
        seq = seq[length:]

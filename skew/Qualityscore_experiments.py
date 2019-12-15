import os
from Bio import SeqIO as seqio
from Bio import SeqUtils as seq
from skewplot import *

path = "C:/Users/Statist Nr 27/Desktop/shared_OriC/Neuer Ordner/ncbi-genomes-2019-12-1/"

#def qual_score(skew):
#    score = 0
#    for i in range(len(skew)-1):
#        score += (skew[i+1]-skew[i])**2
#    score = score/len(skew)
#    return score


for file in os.listdir(path):
    if not file.endswith("fna"): continue

    try:
        fasta = seqio.read(path+file, 'fasta')
    except ValueError:
        print("Probably there is more than one read in: " + file)
        continue

    skew = seq.GC_skew(fasta.seq, window=500)

    #print(qual_score(skew))

    plot(fasta, skew, 500, 1000, True, dnaa='TTATCCACA',
         colors=['xkcd:blue' for i in range(4)])



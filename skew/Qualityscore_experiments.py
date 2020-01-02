import os
from Bio import SeqIO as seqio
from Bio import SeqUtils as seq
from skew.skewplot import *

path = "../data/bacteria_references/"
out_path = '../data/skew_regions.fasta'

#def qual_score(skew):
#    score = 0
#    for i in range(len(skew)-1):
#        score += (skew[i+1]-skew[i])**2
#    score = score/len(skew)
#    return score


def get_min_sequence(sequence, idx_base_min, window):
    window = int(window)

    idx_start = idx_base_min - window
    idx_end = idx_base_min + window

    n = len(sequence)
    if idx_start < 0:
        sub_seq = sequence[(idx_start+n):-1] + sequence[0:idx_end]
    elif idx_end >= n:
        sub_seq = sequence[idx_start:-1] + sequence[0:(idx_end % n)]
    else:
        sub_seq = sequence[idx_start:idx_end]
    return sub_seq, idx_start

# with open(out_path, "w+") as out_file:

oric_sequences = []

for file in os.listdir(path):
    if not file.endswith("fna"):
        continue

    try:
        # fasta = seqio.read(path+file, 'fasta')
        fasta = next(seqio.parse(path+file, "fasta"))
    except ValueError:
        print("Probably there is more than one read in: " + file)
        continue

    window = 500


    skew = seq.GC_skew(fasta.seq, window=window)
    from numpy import argmin
    idx_base_min = argmin(skew).tolist() * window
    subsequence, sub_seq_start = get_min_sequence(fasta, idx_base_min, window * 2)

    plot(fasta, skew, window, 1000, True, dnaa='TTATCCACA', colors=['xkcd:blue' for i in range(4)])

    skew = seq.GC_skew(subsequence.seq, window=10)
    idx_base_min_zoom = sub_seq_start + argmin(skew).tolist() * 10
    oric_sequence = get_min_sequence(fasta, idx_base_min_zoom, 1000)[0]
    oric_sequence.description = oric_sequence.description.replace('complete genome', '')
    oric_sequence.description = oric_sequence.description.replace('complete sequence', '')
    oric_sequence.description = oric_sequence.description + 'oric at {} +- 1000'.format(idx_base_min_zoom)
    oric_sequences.append(oric_sequence)

    # out_file.write(sub_seq.name + "\n")
    # for i in range(0, len(sub_seq), 60):
    #     line = sub_seq[i:i + 60].seq
    #     out_file.write(line + "\n")

seqio.write(oric_sequences, out_path, 'fasta')
print("File '" + out_path + "' written.")




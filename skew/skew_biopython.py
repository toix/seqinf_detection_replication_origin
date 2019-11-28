from Bio import SeqIO as seqio
from Bio import SeqUtils as seq
import matplotlib.pyplot as plt
from inspect import signature
import numpy as np

ecoli = seqio.read('ecoli.fasta', 'fasta')



dnaa = "TTATNCACA"


def similarity(char1, char2):
    if char1 == char2:
        return 1
    return 0


def hamming_dist(seq1, seq2):
    score = 0
    for i in range(len(seq1)):
        score += similarity(seq1[i], seq2[i])
    return score


def motif_distances(seq, motif):
    distances = []
    for i in range(len(seq)):
        print(i)
        if i+len(motif)-1 < len(seq):
            distances.append(hamming_dist(motif, seq[i:i+len(motif)]))
        else:
            distances.append(hamming_dist(motif, seq[i:]+seq[:(i+len(motif))%len(seq)]))
    return distances

def min_region(seq, min_skew_id, region_size):
    dev = int(region_size/2)

    if min_skew_id - dev >= 0 and min_skew_id + dev <= len(seq):
        return seq[min_skew_id-dev:min_skew_id+dev]

    if min_skew_id - dev < 0:
        return seq[min_skew_id - dev:] + seq[:min_skew_id + dev]

    if min_skew_id + dev > len(seq):
        return seq[min_skew_id - dev:] + seq[:min_skew_id+dev - len(seq)]


print(ecoli)
print('Length of genome: ' + str(len(ecoli.seq)))
print('Function GC_skew:\n' + seq.GC_skew.__doc__)
skew = seq.GC_skew(ecoli.seq, window=500)
print('Arguments: ' + str(signature(seq.GC_skew)))
# seq.xGC_skew(ecoli.seq)
#fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(20, 5))
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=False, figsize=(20, 5))
# ax1
pos = [x*500 for x in range(1,len(skew)+1)]
ax1.plot(pos, skew)

# ax2
y = 0
skew_acc = []
for s in skew:
    y += s
    skew_acc.append(y)
ax2.plot(pos, skew_acc)


regionsize = 4000
half_regionsize = int(regionsize/2)

# ax3
oriC_mid = np.argmin(np.array(skew_acc))
search_region = min_region(ecoli.seq, oriC_mid*500, regionsize)
scores = motif_distances(search_region, dnaa)
ax3.plot(range(oriC_mid-half_regionsize, oriC_mid+half_regionsize), scores)

ax3.set_xlim(oriC_mid-half_regionsize, oriC_mid+half_regionsize)

ax2.set_xlabel('Position')
ax1.set_ylabel('GC skew')
ax2.set_ylabel('cumulative GC skew')
for ax in [ax1, ax2]:
    ax.set_xlim(0, (len(skew_acc)+1)*500)
plt.suptitle('GC skew')
print('Position of minimum (OriC): ' + str(skew_acc.index(min(skew_acc))))
# fig.savefig('plot_skew.pdf')

plt.show()
#from PIL import ImageGrab
# im2 = ImageGrab.grab(bbox=None)
# im2.show()



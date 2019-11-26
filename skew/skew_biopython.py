from Bio import SeqIO as seqio
from Bio import SeqUtils as seq
import matplotlib.pyplot as plt
from inspect import signature

ecoli = seqio.read('ecoli.fasta', 'fasta')



dnaa = "TTATNCACC"


def similarity(char1, char2):
    if char1 == char2:
        return 1
    return 0


def hamming_dist(seq1, seq2):
    score = 0
    for i in range(len(seq1)):
        score += similarity(seq1[i], seq2[i])
    return score


distances = []
for i in range(len(ecoli.seq)):
    print(i)
    if i+len(dnaa)-1 < len(ecoli.seq):
        distances.append(hamming_dist(dnaa, ecoli.seq[i:i+len(dnaa)]))
    else:
        distances.append(hamming_dist(dnaa, ecoli.seq[i:]+ecoli.seq[:(i+len(dnaa))%len(ecoli.seq)]))



print(ecoli)
print('Length of genome: ' + str(len(ecoli.seq)))
print('Function GC_skew:\n' + seq.GC_skew.__doc__)
skew = seq.GC_skew(ecoli.seq, window=500)
print('Arguments: ' + str(signature(seq.GC_skew)))
# seq.xGC_skew(ecoli.seq)
#fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(20, 5))
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=False, figsize=(20, 5))
# ax1
pos = [x for x in range(1,len(skew)+1)]
ax1.plot(pos, skew)

# ax2
y = 0
skew_acc = []
for s in skew:
    y += s
    skew_acc.append(y)
ax2.plot(pos, skew_acc)

# ax3
ax3.plot(range(len(ecoli.seq)), distances)

ax2.set_xlabel('Position')
ax1.set_ylabel('GC skew')
ax2.set_ylabel('cumulative GC skew')
for ax in [ax1, ax2]:
    ax.set_xlim(0, len(skew_acc)+1)
plt.suptitle('GC skew')
print('Position of minimum (OriC): ' + str(skew_acc.index(min(skew_acc))))
# fig.savefig('plot_skew.pdf')

plt.show()
#from PIL import ImageGrab
# im2 = ImageGrab.grab(bbox=None)
# im2.show()



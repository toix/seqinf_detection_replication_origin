from Bio import SeqIO as seqio
from Bio import SeqUtils as seq
import matplotlib.pyplot as plt
from PIL import ImageGrab
from inspect import signature

ecoli = seqio.read('ecoli.fasta', 'fasta')
print(ecoli)
print('Length of genome: ' + str(len(ecoli.seq)))
print('Function GC_skew:\n' + seq.GC_skew.__doc__)
skew = seq.GC_skew(ecoli.seq)
print('Arguments: ' + str(signature(seq.GC_skew)))
# seq.xGC_skew(ecoli.seq)
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(20, 5))
pos = [x for x in range(1,len(skew)+1)]
ax1.plot(pos, skew)
y = 0
skew_acc = []
for s in skew:
    y += s
    skew_acc.append(y)
ax2.plot(pos, skew_acc)
ax2.set_xlabel('Position')
ax1.set_ylabel('GC skew')
ax2.set_ylabel('cumulative GC skew')
for ax in [ax1, ax2]:
    ax.set_xlim(0, len(skew_acc)+1)
plt.suptitle('GC skew')
print('Position of minimum (OriC): ' + str(skew_acc.index(min(skew_acc))))
# fig.savefig('plot_skew.pdf')
# plt.show()
# im2 = ImageGrab.grab(bbox=None)
# im2.show()



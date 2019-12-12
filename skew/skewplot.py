import matplotlib.pyplot as plt
import numpy as np
from findmotif import *
from zoomeffect import zoom_effect

def calcmotif(regionsize, dnaa, skew_acc, windowsize, fasta):
    half_regionsize = int(regionsize / 2)
    oriC_mid = np.argmin(np.array(skew_acc)) * windowsize + int(windowsize / 2)
    search_region = min_region(fasta.seq, oriC_mid, regionsize)
    scores = motif_distances(search_region, dnaa)
    x = range(oriC_mid-half_regionsize, oriC_mid+half_regionsize)
    return x, scores

def cskew(skew):
    y = 0
    skew_acc = []
    for s in skew:
        y += s
        skew_acc.append(y)
    return skew_acc


def plot(fasta, skew, windowsize, regionsize, show, dnaa=None, colors = None, save=None):
    if colors == None:
        colors = ['xkcd:blue' for i in range(4)]
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=False, figsize=(20, 5))
    pos = [x * windowsize + windowsize / 2 for x in range(1, len(skew) + 1)]

    # ax1
    ax1.plot(pos, skew, colors[0])

    # ax2
    skew_acc = cskew(skew)
    ax2.plot(pos, skew_acc,color=colors[1])

    # ax3
    x, scores = calcmotif(regionsize, dnaa, skew_acc, windowsize, fasta)
    ax3.plot(x, scores, color=colors[2])
    ax3.set_xlim(x[0], x[-1])

    ax3.set_xlabel('Genome Position', labelpad=10)
    ax1.set_ylabel('GC skew')
    ax2.set_ylabel('cumulative GC skew')
    ax3.set_ylabel('motif scores')
    zoom_effect(ax2,ax3, x[0], x[-1], color=colors[3])
    ax2.xaxis.tick_top()
    ax2.xaxis.set_ticklabels([])
    ax1.tick_params(axis='both', which='major', pad=8)
    fig.align_ylabels([ax1,ax2,ax3])
    for ax in [ax1, ax2]:
        ax.set_xlim(1, (len(skew_acc)+1)*windowsize)
    plt.suptitle('GC skew')
    print('Position of minimum (OriC): ' + str(skew_acc.index(min(skew_acc))))

    plt.subplots_adjust(wspace=0, hspace=0.4, left=0.1, right=0.9)

    if save != None:
        fig.savefig(save)
    if show == True:
        plt.show()
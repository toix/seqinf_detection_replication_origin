from os import makedirs, path

import matplotlib.pyplot as plt
import numpy as np
from skew.findmotif import *
from skew.zoomeffect import zoom_effect
from dnaa.alignment import align_motif_to_sequence


def calcmotif(regionsize, dnaa, skew_acc, windowsize, fasta):
    oriC_mid = np.argmin(np.array(skew_acc)) * windowsize + int(windowsize / 2)
    search_region = min_region(fasta.seq, oriC_mid, regionsize)
    scores = align_motif_to_sequence(search_region, dnaa)
    half_align_size = int(len(scores) / 2)
    x = range(oriC_mid-half_align_size, oriC_mid+half_align_size)
    return x, scores, 0


def accumlate_skew(skew):
    y = 0
    skew_acc = []
    for s in skew:
        y += s
        skew_acc.append(y)
    return skew_acc


def cwindowskew(skew):
    windowsize = int(len(skew ) /2)
    window_skew = np.zeros(len(skew))

    long_skew = 3* skew
    ls_pos = len(window_skew) - int(windowsize/2)

    window_skew[0] = np.sum(long_skew[ls_pos:ls_pos + windowsize])

    for i in range(1, len(window_skew)):
        window_skew[i] = window_skew[i - 1] - long_skew[ls_pos+i-1] + long_skew[ls_pos + windowsize+i-1]

    return window_skew.tolist()


def getFastaName(fasta):
    name = ','.join(fasta.description.split(',')[:-1])
    name = ' '.join(name.split()[1:])
    if name.endswith(' '):
        name = name[:-1]
    if name.endswith(','):
        name = name[:-1]
    return name


def plot(fasta, skew, skew_window, oric_window, show, dnaa_motif=None, save=None, colors=None):
    if colors == None:
        colors = ['xkcd:blue' for i in range(4)]
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=False, figsize=(16, 6))
    pos = [x * skew_window + skew_window / 2 for x in range(1, len(skew) + 1)]

    # ax1
    ax1.plot(pos, skew, colors[0])

    # ax2
    skew_acc = accumlate_skew(skew)
    ax2.plot(pos, skew_acc,color=colors[1])

    # ax3
    x, scores, motif_count = calcmotif(oric_window, dnaa_motif, skew_acc, skew_window, fasta)
    ax3.plot(x, scores, color=colors[2])
    ax3.set_xlim(x[0], x[-1])
    ax3.set_ylim(0, 9*2)  # limit y-axis to motif length

    ax3.set_xlabel('Genome Position', labelpad=10)
    ax1.set_ylabel('GC skew')
    ax2.set_ylabel('cumulative GC skew')
    ax3.set_ylabel('motif scores')
    zoom_effect(ax2, ax3, x[0], x[-1], color=colors[3])
    ax2.xaxis.tick_top()
    ax2.xaxis.set_ticklabels([])
    ax1.tick_params(axis='both', which='major', pad=8)
    fig.align_ylabels([ax1,ax2,ax3])
    for ax in [ax1, ax2]:
        ax.set_xlim(1, (len(skew_acc)+1) * skew_window)

    name = getFastaName(fasta)
    plt.suptitle('OriC Analysis for "{}"'.format(name))
    print('Position of minimum (OriC): ' + str(skew_acc.index(min(skew_acc)) * skew_window)) #added *windowsize for correct position
    # print('Motif count (allows 1 mismatch): ' + str(motif_count))

    plt.subplots_adjust(wspace=0, hspace=0.4, left=.06, right=.98)

    if save is not None:
        if not path.exists(path.dirname(save)):
            makedirs(path.dirname(save))
        fig.savefig(save)
        print("File '" + save + "' written.")
    if show:
        plt.show()
    plt.close()
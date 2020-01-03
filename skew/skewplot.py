import matplotlib.pyplot as plt
import numpy as np
from skew.findmotif import *
from skew.zoomeffect import zoom_effect

def calcmotif(regionsize, dnaa, skew_acc, windowsize, fasta):
    half_regionsize = int(regionsize / 2)
    oriC_mid = np.argmin(np.array(skew_acc)) * windowsize + int(windowsize / 2)
    search_region = min_region(fasta.seq, oriC_mid, regionsize)
    scores = motif_distances(search_region, dnaa)
    motif_count = count_motif(scores)
    x = range(oriC_mid-half_regionsize, oriC_mid+half_regionsize)
    return x, scores, motif_count

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


def plot(fasta, skew, windowsize, regionsize, show, dnaa=None, colors=None, save=None):
    if colors == None:
        colors = ['xkcd:blue' for i in range(4)]
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=False, figsize=(20, 5))
    pos = [x * windowsize + windowsize / 2 for x in range(1, len(skew) + 1)]

    # ax1
    ax1.plot(pos, skew, colors[0])

    # ax2
    skew_acc = accumlate_skew(skew)
    ax2.plot(pos, skew_acc,color=colors[1])

    # other quality score
    #x = 0
    #for i in range(len(skew_acc)-100):
    #    x += ((skew_acc[i+51]-skew_acc[i+50]) - (skew_acc[i+100] - skew_acc[i])/100)**2
    #x = x/(len(skew_acc)-100)
    #print(x)

    # descent = (max(skew_acc) - min(skew_acc)) / abs(np.argmin(np.array(skew_acc)) - np.argmax(np.array(skew_acc)))
    # x = 0
    # for i in range(len(skew_acc)-1):
    #     x += (abs(skew_acc[i+1]-skew_acc[i]) - descent)**2
    # x = x/len(skew_acc)
    # print(x)
    #window_skew_acc = cwindowskew(skew)
    #ax2.plot(pos, window_skew_acc, color='r')

    # ax3
    x, scores, motif_count = calcmotif(regionsize, dnaa, skew_acc, windowsize, fasta)
    ax3.plot(x, scores, color=colors[2])
    ax3.set_xlim(x[0], x[-1])
    ax3.set_ylim(0, len(dnaa))  # limit y-axis to motif length

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
    print('Position of minimum (OriC): ' + str(skew_acc.index(min(skew_acc))*windowsize)) #added *windowsize for correct position
    print('Motif count (allows 1 mismatch): ' + str(motif_count))

    plt.subplots_adjust(wspace=0, hspace=0.4, left=0.1, right=0.9)

    if save != None:
        fig.savefig(save)
    if show == True:
        plt.show()
import argparse
from Bio import SeqIO as seqio
from Bio import SeqUtils as seq
# from inspect import signature
from skew.skewplot import *

def parseargs():
    parser = argparse.ArgumentParser(
        description='Calculate and plot GC-skew, find motif')
    parser.add_argument("fasta", help="enter path to your FASTA sequence file", )
    parser.add_argument("--plot", default=True, action='store_true', help="specify this option if you want to show the plot of the GC skew")
    parser.add_argument("--saveplot", default=None, type=str, help="specify the path for saving the plot of the GC skew")
    parser.add_argument("--skewwindow", type=int, default=100, help="window size used for calculation of the GC skew")
    parser.add_argument("--searchwindow", type=int, default=2000, help="specify size of region around the minimum of the GC skew in which motifs will be searched")
    parser.add_argument("--motif", default='data/bacteria/dnaa.fna', help="specify fasta file with motif sequences")
    parser.add_argument("--colors", default=['xkcd:blue' for i in range(4)], nargs=4, help="specify colors for plot")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parseargs()
    fasta = next(seqio.parse(args.fasta, "fasta"))
    print('Genome: ' + fasta.description)
    print('Length of genome: ' + str(len(fasta.seq)))
    print('GC skew: (G-C)/(G+C)')
    skew = seq.GC_skew(fasta.seq, window=args.skewwindow)
    if args.plot and args.saveplot != None:
        name, gc_min_pos = plot(fasta, skew, args.skewwindow, args.searchwindow, True, dnaa_motif=args.motif, save=args.saveplot,
             colors=args.colors)
    elif args.plot:
        name, gc_min_pos = plot(fasta, skew, args.skewwindow, args.searchwindow, True, dnaa_motif=args.motif,
             colors=args.colors)
    elif args.saveplot != None:
        name, gc_min_pos = plot(fasta, skew, args.skewwindow, args.searchwindow, False, dnaa_motif=args.motif, save=args.saveplot,
             colors=args.colors)

    plt.suptitle('OriC Analysis for "{}"'.format(name))
    print('Position of minimum (OriC): {}'.format(gc_min_pos))



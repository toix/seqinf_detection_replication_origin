import argparse
from Bio import SeqIO as seqio
from Bio import SeqUtils as seq
# from inspect import signature
from skewplot import *

def parseargs():
    parser = argparse.ArgumentParser(
        description='Calculate and plot GC-skew, find motif')
    parser.add_argument("fasta", help="enter path to your FASTA sequence file", )
    parser.add_argument("--plot", default=True, action='store_true', help="specify this option if you want to show the plot of the GC skew")
    parser.add_argument("--saveplot", default=None, type=str, help="specify the path for saving the plot of the GC skew")
    parser.add_argument("--window", default=500, help="window size used for calculation of the GC skew")
    parser.add_argument("--searchwindow", default=1000, help="specify size of region around the minimum of the GC skew in which motifs will be searched")
    parser.add_argument("--motif", default='TTATCCACA', help="specify motif to be searched")
    parser.add_argument("--colors", default=['xkcd:blue' for i in range(4)], nargs=4, help="specify colors for plot")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parseargs()
    fasta = seqio.read(args.fasta, 'fasta')
    print('Genome: ' + fasta.description)
    print('Length of genome: ' + str(len(fasta.seq)))
    print('GC skew: (G-C)/(G+C)')
    skew = seq.GC_skew(fasta.seq, window=args.window)
    if args.plot and args.saveplot != None:
        plot(fasta, skew, args.window, args.searchwindow, True, dnaa=args.motif, save=args.saveplot,
             colors=args.colors)
    elif args.plot:
        plot(fasta, skew, args.window, args.searchwindow, True, dnaa=args.motif,
             colors=args.colors)
        from numpy import argmin
        argmin(skew).tolist() * args.window
    elif args.saveplot != None:
        plot(fasta, skew, args.window, args.searchwindow, False, dnaa=args.motif, save=args.saveplot,
             colors=args.colors)



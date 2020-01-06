from argparse import ArgumentParser
from os import listdir

from Bio import SeqIO, SeqUtils

from skew.skew_biopython import plot


def parseargs():
    parser = ArgumentParser(description='Calculate and plot GC-skew, find motif')
    parser.add_argument("--skewwindow", type=int, default=100, help="window size used for calculation of the GC skew")
    parser.add_argument("--searchwindow", type=int, default=2000, help="specify size of region around the minimum of the GC skew in which motifs will be searched")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parseargs()

    data_sets = [
        {'folder': 'data/ecoli/ref_seq', 'type': 'species reference'},
        {'folder': 'data/salmonella/ref_seq', 'type': 'species reference'},
        {'folder': 'data/thermotoga/ref_seq', 'type': 'species reference'},
        {'folder': 'data/vibrio/ref_seq', 'type': 'species reference'},
        {'folder': 'data/families/enterobacteriaceae/ref_seq', 'type': 'family'},
        {'folder': 'data/families/vibrionaceae/ref_seq', 'type': 'family'},
        {'folder': 'data/known_oric/ref_seq', 'type': 'bacteri references with known oric'},
        {'folder': 'skew/Ecoli/genomes', 'type': 'species'},
        {'folder': 'skew/Salmonella/genomes', 'type': 'species'},
        {'folder': 'skew/Thermotoga/genomes', 'type': 'species'},
        {'folder': 'skew/Vibrio/genomes', 'type': 'species'},
        {'folder': 'skew/Wigglesworthia/genomes', 'type': 'species'},
    ]

    for data_set in data_sets:
        folder = '/'.join(data_set['folder'].split('/')[:-1])
        for file in listdir(data_set['folder']):
            if not file.endswith("fna") and not file.endswith("fasta"):
                continue

            fasta = next(SeqIO.parse(data_set['folder'] + '/' + file, "fasta"))
            # print('Genome: ' + fasta.description)
            # print('Length of genome: ' + str(len(fasta.seq)))
            # print('GC skew: (G-C)/(G+C)')
            skew = SeqUtils.GC_skew(fasta.seq, window=args.skewwindow)
            file_name = '.'.join(file.split('.')[:-1])
            plot_file = folder + '/plots/{}.pdf'.format(file_name)
            plot(fasta, skew, args.skewwindow, args.searchwindow, show=False, dnaa_motif='data/bacteria/dnaa.fna', save=plot_file)

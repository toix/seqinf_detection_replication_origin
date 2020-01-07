import numpy as np
from argparse import ArgumentParser
from os import listdir, path, makedirs

from Bio import SeqIO, SeqUtils

from dnaa.alignment import compute_motif_from_occurances
from skew.findmotif import min_region
from skew.skew_biopython import plot
from skew.skewplot import accumlate_skew


def parseargs():
    parser = ArgumentParser(description='Calculate and plot GC-skew, find motif')
    parser.add_argument("--skewwindow", type=int, default=100, help="window size used for calculation of the GC skew")
    parser.add_argument("--searchwindow", type=int, default=2000, help="specify size of region around the minimum of the GC skew in which motifs will be searched")
    args = parser.parse_args()
    return args


def list_to_file(my_list, file_name):
    with open(file_name, 'w') as f:
        for item in my_list:
            line = ','.join(str(x).replace(',', ' ') for x in item)
            f.write("%s\n" % line)

    print("File '" + file_name + "' written.")


def createLogoFile(logo_file, motif):
    if not path.exists(path.dirname(logo_file)):
        makedirs(path.dirname(logo_file))
    motif.weblogo(logo_file)
    print("File '" + logo_file + "' written.")


if __name__ == '__main__':
    args = parseargs()

    data_sets = [
        {'folder': 'data/ecoli/ref_seq'},
        {'folder': 'data/salmonella/ref_seq'},
        {'folder': 'data/thermotoga/ref_seq'},
        {'folder': 'data/vibrio/ref_seq'},
        {'folder': 'data/families/enterobacteriaceae/ref_seq'},
        {'folder': 'data/families/vibrionaceae/ref_seq'},
        {'folder': 'data/known_oric/ref_seq'},
        {'folder': 'skew/Ecoli/genomes'},
        {'folder': 'skew/Salmonella/genomes'},
        {'folder': 'skew/Thermotoga/genomes'},
        {'folder': 'skew/Vibrio/genomes'},
        {'folder': 'skew/Wigglesworthia/genomes'},
    ]

    evaluation_data = [['folder', 'file', 'accession', 'name', 'length', 'GC min pos']]

    for data_set in data_sets:
        folder = '/'.join(data_set['folder'].split('/')[:-1])
        for file in listdir(data_set['folder']):
            if not file.endswith("fna") and not file.endswith("fasta"):
                continue

            # plot
            fasta = next(SeqIO.parse(data_set['folder'] + '/' + file, "fasta"))
            skew = SeqUtils.GC_skew(fasta.seq, window=args.skewwindow)
            file_name = '.'.join(file.split('.')[:-1])
            plot_file = folder + '/plots/{}.pdf'.format(file_name)
            species_name, gc_min_pos = plot(fasta, skew, args.skewwindow, args.searchwindow, show=False, dnaa_motif='data/bacteria/dnaa.fna', save=plot_file)

            # species motif
            skew_acc = accumlate_skew(skew)
            oriC_mid = np.argmin(np.array(skew_acc)) * args.skewwindow + int(args.skewwindow / 2)
            search_region = min_region(fasta.seq, oriC_mid, args.searchwindow)
            species_motif = compute_motif_from_occurances(search_region, motif_file='data/bacteria/dnaa.fna', approx_fales_positive_rate=0.0002)

            if species_motif is not None:
                logo_file = folder + '/motifs/{}.pdf'.format(file_name)
                createLogoFile(logo_file, species_motif)
            else:
                print("Warning: DnaA Boxes found in {}". format(species_name))

            evaluation_data.append([data_set['folder'], file_name, fasta.description.split()[0], species_name, len(fasta.seq), gc_min_pos])

    list_to_file(evaluation_data, 'OriEval.csv')



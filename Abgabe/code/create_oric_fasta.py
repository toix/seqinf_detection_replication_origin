import os
from Bio import SeqIO as seqio
from Bio import SeqUtils as seq

from modules.skewplot import accumlate_skew
from modules.skewplot import plot


def parseargs():
    import argparse
    parser = argparse.ArgumentParser(
        description='Writes new fasta file containing 2000 bases around the GC-skew minimum')
    parser.add_argument("folder", type=str, help="path to a directory containing FASTA files")
    parser.add_argument("out", type=str, help="path to a FASTA file where to write the resulting OriC sequences")
    parser.add_argument("--skewwindow", type=int, default=1000, help="window size used for calculation of the GC skew")
    parser.add_argument("--zoomwindow", type=int, default=100, help="window size used for second more precise (zoomed) calculation of the GC skew")
    parser.add_argument("--searchwindow", type=int, default=2000, help="specify size of region around the minimum of the GC skew in which motifs will be searched")
    args = parser.parse_args()
    return args


def get_min_sequence(sequence, idx_base_min, window):
    window = int(window)

    idx_start = int(round(idx_base_min - window/2))
    idx_end = int(round(idx_base_min + window/2))

    n = len(sequence)
    if idx_start < 0:
        sub_seq = sequence[(idx_start+n):-1] + sequence[0:idx_end]
    elif idx_end >= n:
        sub_seq = sequence[idx_start:-1] + sequence[0:(idx_end % n)]
    else:
        sub_seq = sequence[idx_start:idx_end]
    return sub_seq, idx_start


def main():
    args = parseargs()
    folder = args.folder
    out_file = args.out
    skew_window = args.skewwindow
    oric_window = args.searchwindow

    oric_sequences = []

    for file in os.listdir(folder):
        if not file.endswith("fna") and not file.endswith("fasta"):
            continue

        fasta = next(seqio.parse(folder +'/'+ file, "fasta"))

        skew = seq.GC_skew(fasta.seq, window=skew_window)
        skew = accumlate_skew(skew)
        from numpy import argmin
        idx_base_min = int(argmin(skew).tolist()) * skew_window
        subsequence, sub_seq_start = get_min_sequence(fasta, idx_base_min, skew_window*2)


        skew = seq.GC_skew(subsequence.seq, window=args.zoomwindow)
        skew = accumlate_skew(skew)
        idx_base_min = sub_seq_start + int(argmin(skew).tolist()) * args.zoomwindow
        oric_sequence = get_min_sequence(fasta, idx_base_min, oric_window)[0]

        oric_sequence.description = oric_sequence.description.replace('complete genome', '')
        oric_sequence.description = oric_sequence.description.replace('complete sequence', '')
        oric_sequence.description = oric_sequence.description + '{} bases around gc minimum at {}'.format(oric_window, idx_base_min)

        oric_sequences.append(oric_sequence)

    seqio.write(oric_sequences, out_file, 'fasta')
    print("File '" + out_file + "' written.")

main()



import os
from Bio import SeqIO as seqio
from Bio import SeqUtils as seq

from skew.skewplot import accumlate_skew
from skew.skewplot import plot

#def qual_score(skew):
#    score = 0
#    for i in range(len(skew)-1):
#        score += (skew[i+1]-skew[i])**2
#    score = score/len(skew)
#    return score


def parseargs():
    import argparse
    parser = argparse.ArgumentParser(
        description='Calculate and plot GC-skew, find motif')
    parser.add_argument("folder", type=str, help="path to a directory containing FASTA files")
    parser.add_argument("out", type=str, help="path to a FASTA file where to write the resulting OriC sequences")
    parser.add_argument("--window", type=int, default=500, help="window size used for calculation of the GC skew")
    parser.add_argument("--searchwindow", type=int, default=1000, help="specify size of region around the minimum of the GC skew in which motifs will be searched")
    args = parser.parse_args()
    return args


def get_min_sequence(sequence, idx_base_min, window):
    window = int(window)

    idx_start = idx_base_min - window
    idx_end = idx_base_min + window

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
    in_path = args.folder
    out_file = args.out
    skew_window = args.window
    oric_window = args.searchwindow

    oric_sequences = []

    for file in os.listdir(in_path):
        if not file.endswith("fna") and not file.endswith("fasta"):
            continue

        try:
            # fasta = seqio.read(path+file, 'fasta')
            fasta = next(seqio.parse(in_path +'/'+ file, "fasta"))
        except ValueError:
            print("Probably there is more than one read in: " + file)
            continue


        skew = seq.GC_skew(fasta.seq, window=skew_window)
        skew = accumlate_skew(skew)
        from numpy import argmin
        idx_base_min = argmin(skew).tolist() * skew_window
        subsequence, sub_seq_start = get_min_sequence(fasta, idx_base_min, skew_window)

        # plot(fasta, skew, skew_window, oric_window, True, dnaa='TTATCCACA', colors=['xkcd:blue' for i in range(4)])

        skew = seq.GC_skew(subsequence.seq, window=10)
        skew = accumlate_skew(skew)
        idx_base_min = sub_seq_start + argmin(skew).tolist() * 10
        oric_sequence = get_min_sequence(fasta, idx_base_min, oric_window)[0]

        oric_sequence.description = oric_sequence.description.replace('complete genome', '')
        oric_sequence.description = oric_sequence.description.replace('complete sequence', '')
        oric_sequence.description = oric_sequence.description + 'oric at {} +- {}'.format(idx_base_min, oric_window)

        oric_sequences.append(oric_sequence)

        # out_file.write(sub_seq.name + "\n")
        # for i in range(0, len(sub_seq), 60):
        #     line = sub_seq[i:i + 60].seq
        #     out_file.write(line + "\n")

    seqio.write(oric_sequences, out_file, 'fasta')
    print("File '" + out_file + "' written.")

main()



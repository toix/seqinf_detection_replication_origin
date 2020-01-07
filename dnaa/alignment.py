from Bio import motifs


def align_motif_to_sequence(sequence, motif_file):
    """
    if score of reverse complement is higher -> use it instead
    https://biopython-tutorial.readthedocs.io/en/latest/notebooks/14%20-%20Sequence%20motif%20analysis%20using%20Bio.motifs.html
    :param sequence:
    :param motif_file: fasta file path containing motifs
    :return:
    """
    with open(motif_file) as handle:
        motif = motifs.read(handle, "sites")
        motif.pseudocounts = 1
        # distribution = motif.pssm.distribution(background=motif.background)
        # threshold = distribution.threshold_fpr(0.0001)
        # print("Alignment threshold: %5.3f" % threshold)
        # return motif.pssm.search(sequence, threshold=threshold)
        pssm = motif.pssm
        scores = pssm.reverse_complement().calculate(sequence)
        scores_rev = pssm.calculate(sequence)
        for pos in range(0, len(scores)):
            if scores_rev[pos] < 0 and scores[pos] < 0:
                scores[pos] = 0
            elif scores_rev[pos] > scores[pos]:
                scores[pos] = -scores_rev[pos]
        return scores



# prf_aligner = ProfileAligner('data/bacteria/dnaa.fna')
# from Bio import SeqIO
# fasta = SeqIO.read('data/ecoli/ref_seq/GCF_000005845.2_ASM584v2_genomic.fna', 'fasta')
# alignment = prf_aligner.find_motif(fasta.seq)
# for position, score in alignment:
#     print("Position %d: score = %5.3f %s" % (position, score, fasta.seq[position:(position+10)]))
# print(alignment)
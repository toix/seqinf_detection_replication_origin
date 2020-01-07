from Bio import motifs, SeqRecord


def get_positive_motif_scores(sequence, motif_file):
    """
    complement is with negative score;

    https://biopython-tutorial.readthedocs.io/en/latest/notebooks/14%20-%20Sequence%20motif%20analysis%20using%20Bio.motifs.html
    :param sequence:
    :param motif_file: fasta file path containing motifs
    :return: all positive scores
    """
    with open(motif_file) as handle:
        motif = motifs.read(handle, "sites")
        motif.pseudocounts = 1
        pssm = motif.pssm
        scores = pssm.reverse_complement().calculate(sequence)
        scores_rev = pssm.calculate(sequence)
        for pos in range(0, len(scores)):
            if scores_rev[pos] < 0 and scores[pos] < 0:
                scores[pos] = 0
            elif scores_rev[pos] > scores[pos]:
                scores[pos] = -scores_rev[pos]
        return scores, motif


def find_motif_matches(sequence, motif_file, approx_fales_positive_rate):
    """
    complement has negative position

    approximate false positive rate: 0.0002

    https://biopython-tutorial.readthedocs.io/en/latest/notebooks/14%20-%20Sequence%20motif%20analysis%20using%20Bio.motifs.html
    :param sequence:
    :param motif_file: fasta file path containing motifs
    :return:
    """
    with open(motif_file) as handle:
        motif = motifs.read(handle, "sites")
        motif.pseudocounts = 1
        pssm = motif.pssm
        distribution = pssm.distribution(background=motif.background)
        threshold = distribution.threshold_fpr(approx_fales_positive_rate)
        print("Alignment threshold: %5.3f" % threshold)
        return pssm.search(sequence, threshold=threshold), len(motif)


def compute_motif_from_occurances(sequence, motif_file, approx_fales_positive_rate):
    if type(sequence) is SeqRecord:
        sequence = sequence.seq

    motif_matches, motif_length = find_motif_matches(sequence, motif_file, approx_fales_positive_rate)
    found_sequences = []
    for pos, score in motif_matches:
        if pos >= 0:
            found_sequences.append(sequence[pos:pos+motif_length])
        else:
            found_sequences.append(sequence[pos:pos+motif_length].reverse_complement())

    if len(found_sequences) < 1:
        return None
    return motifs.create(found_sequences)
def min_region(seq, min_skew_id, regionsize):
    dev = int(regionsize/2)

    if min_skew_id - dev >= 0 and min_skew_id + dev <= len(seq):
        return seq[min_skew_id-dev:min_skew_id+dev]

    if min_skew_id - dev < 0:
        return seq[min_skew_id - dev:] + seq[:min_skew_id + dev]

    if min_skew_id + dev > len(seq):
        return seq[min_skew_id - dev:] + seq[:min_skew_id+dev - len(seq)]

def similarity(char1, char2):
    if char1 == char2:
        return 1
    return 0


def hamming_dist(seq1, seq2):
    score = 0
    for i in range(len(seq1)):
        score += similarity(seq1[i], seq2[i])
    return score


def motif_distances(seq, motif):
    distances = []
    for i in range(len(seq)):
        if i+len(motif)-1 < len(seq):
            distances.append(hamming_dist(motif, seq[i:i+len(motif)]))
        else:
            distances.append(hamming_dist(motif, seq[i:]+seq[:(i+len(motif))%len(seq)]))
    return distances

#Counts motifs in zoom region, allows one mismatch in the motif
def count_motif(distances):
    counter = 0
    for i in range(len(distances)):
        if distances[i] >= 8:
            counter += 1
    return counter

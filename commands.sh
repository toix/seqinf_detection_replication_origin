export PATH=/mnt/c/drive/uni/seq_inf/seqinf_project/tools/meme/bin:/mnt/c/drive/uni/seq_inf/seqinf_project/tools/meme/libexec/meme-5.1.0:$PATH
cd /mnt/c/drive/uni/seq_inf/seqinf_project/data/bacteria/meme
meme /mnt/c/drive/uni/seq_inf/seqinf_project/data/bacteria/skew_regions.fasta -dna -oc . -nostatus -time 18000 -mod anr -nmotifs 3 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 4
mast meme.xml /mnt/c/drive/uni/seq_inf/seqinf_project/data/bacteria/skew_regions.fasta -oc . -nostatus

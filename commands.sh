export PATH=/mnt/c/drive/uni/seq_inf/seqinf_project/tools/meme/bin:/mnt/c/drive/uni/seq_inf/seqinf_project/tools/meme/libexec/meme-5.1.0:$PATH

export PYTHONPATH=$PYTHONPATH:/mnt/c/drive/uni/seq_inf/seqinf_project

# bacteria
cd /mnt/c/drive/uni/seq_inf/seqinf_project
python skew/create_oric_fasta.py data/bacteria/ref_seq data/bacteria/skew_regions.fasta

cd data/bacteria/meme
meme /mnt/c/drive/uni/seq_inf/seqinf_project/data/bacteria/skew_regions.fasta -dna -oc . -nostatus -time 18000 -mod anr -nmotifs 3 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 4
mast meme.xml /mnt/c/drive/uni/seq_inf/seqinf_project/data/bacteria/skew_regions.fasta -oc . -nostatus

# ecoli
cd /mnt/c/drive/uni/seq_inf/seqinf_project
python skew/create_oric_fasta.py skew/Ecoli/genomes data/ecoli/skew_regions.fasta

cd data/ecoli/meme
meme /mnt/c/drive/uni/seq_inf/seqinf_project/data/ecoli/skew_regions.fasta -dna -oc . -nostatus -time 18000 -mod anr -nmotifs 3 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 4
mast meme.xml /mnt/c/drive/uni/seq_inf/seqinf_project/data/ecoli/skew_regions.fasta -oc . -nostatus

# thermotoga
cd /mnt/c/drive/uni/seq_inf/seqinf_project
python skew/create_oric_fasta.py skew/Thermotoga/genomes data/thermotoga/skew_regions.fasta

cd data/thermotoga/meme
meme /mnt/c/drive/uni/seq_inf/seqinf_project/data/thermotoga/skew_regions.fasta -dna -oc . -nostatus -time 18000 -mod anr -nmotifs 3 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 4
mast meme.xml /mnt/c/drive/uni/seq_inf/seqinf_project/data/thermotoga/skew_regions.fasta -oc . -nostatus

# cholerae
cd /mnt/c/drive/uni/seq_inf/seqinf_project
python skew/create_oric_fasta.py skew/Vibrio/genomes data/cholerae/skew_regions.fasta

cd data/cholerae/meme
meme /mnt/c/drive/uni/seq_inf/seqinf_project/data/cholerae/skew_regions.fasta -dna -oc . -nostatus -time 18000 -mod anr -nmotifs 3 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 4
mast meme.xml /mnt/c/drive/uni/seq_inf/seqinf_project/data/cholerae/skew_regions.fasta -oc . -nostatus

# salmonella
cd /mnt/c/drive/uni/seq_inf/seqinf_project
python skew/create_oric_fasta.py skew/Salmonella/genomes data/salmonella/skew_regions.fasta

cd data/salmonella/meme
meme /mnt/c/drive/uni/seq_inf/seqinf_project/data/salmonella/skew_regions.fasta -dna -oc . -nostatus -time 18000 -mod anr -nmotifs 3 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 4
mast meme.xml /mnt/c/drive/uni/seq_inf/seqinf_project/data/salmonella/skew_regions.fasta -oc . -nostatus


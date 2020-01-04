# dependencies
pip install numpy
pip install matplotlib
pip install biopython

# preparation
export PATH=/mnt/c/drive/uni/seq_inf/seqinf_project/tools/meme/bin:/mnt/c/drive/uni/seq_inf/seqinf_project/tools/meme/libexec/meme-5.1.0:$PATH
export PYTHONPATH=$PYTHONPATH:/mnt/c/drive/uni/seq_inf/seqinf_project
cd /mnt/c/drive/uni/seq_inf/seqinf_project

# DoriC
meme /mnt/c/drive/uni/seq_inf/seqinf_project/data/bacteria/doric_bactria.fasta -dna -oc data/bacteria/meme_doric -nostatus -time 30000 -mod anr -nmotifs 5 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 4
mast data/bacteria/meme_doric/meme.xml /mnt/c/drive/uni/seq_inf/seqinf_project/data/bacteria/doric_bactria.fasta -oc data/bacteria/meme_doric -nostatus

# bacteria
python skew/create_oric_fasta.py data/bacteria/ref_seq data/bacteria/skew_regions.fasta

meme /mnt/c/drive/uni/seq_inf/seqinf_project/data/bacteria/skew_regions.fasta -dna -oc data/bacteria/meme -nostatus -time 30000 -mod anr -nmotifs 3 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 4
mast data/bacteria/meme/meme.xml /mnt/c/drive/uni/seq_inf/seqinf_project/data/bacteria/skew_regions.fasta -oc data/bacteria/meme -nostatus

# ecoli
python skew/create_oric_fasta.py skew/Ecoli/genomes data/ecoli/skew_regions.fasta

meme /mnt/c/drive/uni/seq_inf/seqinf_project/data/ecoli/skew_regions.fasta -dna -oc data/ecoli/meme -nostatus -time 30000 -mod anr -nmotifs 3 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 4
mast data/ecoli/meme/meme.xml /mnt/c/drive/uni/seq_inf/seqinf_project/data/ecoli/skew_regions.fasta -oc data/ecoli/meme -nostatus

# thermotoga
python skew/create_oric_fasta.py skew/Thermotoga/genomes data/thermotoga/skew_regions.fasta

meme /mnt/c/drive/uni/seq_inf/seqinf_project/data/thermotoga/skew_regions.fasta -dna -oc data/thermotoga/meme -nostatus -time 30000 -mod anr -nmotifs 3 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 4
mast data/thermotoga/meme/meme.xml /mnt/c/drive/uni/seq_inf/seqinf_project/data/thermotoga/skew_regions.fasta -oc data/thermotoga/meme -nostatus

# cholerae
python skew/create_oric_fasta.py skew/Vibrio/genomes data/cholerae/skew_regions.fasta

meme /mnt/c/drive/uni/seq_inf/seqinf_project/data/cholerae/skew_regions.fasta -dna -oc data/cholerae/meme -nostatus -time 30000 -mod anr -nmotifs 3 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 4
mast data/cholerae/meme/meme.xml /mnt/c/drive/uni/seq_inf/seqinf_project/data/cholerae/skew_regions.fasta -oc data/cholerae/meme -nostatus

# salmonella
python skew/create_oric_fasta.py skew/Salmonella/genomes data/salmonella/skew_regions.fasta

meme /mnt/c/drive/uni/seq_inf/seqinf_project/data/salmonella/skew_regions.fasta -dna -oc data/salmonella/meme -nostatus -time 30000 -mod anr -nmotifs 3 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 4
mast data/salmonella/meme/meme.xml /mnt/c/drive/uni/seq_inf/seqinf_project/data/salmonella/skew_regions.fasta -oc data/salmonella/meme -nostatus


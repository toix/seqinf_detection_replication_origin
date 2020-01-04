# dependencies
pip install numpy
pip install matplotlib
pip install biopython

# preparation
export PATH=/mnt/c/drive/uni/seq_inf/seqinf_project/tools/meme/bin:/mnt/c/drive/uni/seq_inf/seqinf_project/tools/meme/libexec/meme-5.1.0:$PATH
export PYTHONPATH=$PYTHONPATH:/mnt/c/drive/uni/seq_inf/seqinf_project
cd /mnt/c/drive/uni/seq_inf/seqinf_project

# DoriC
meme data/bacteria/doric_bactria.fasta -dna -oc data/bacteria/meme_doric -nostatus -time 30000 -mod anr -nmotifs 5 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 4 -csites 30000
mast data/bacteria/meme_doric/meme.xml data/bacteria/doric_bactria.fasta -oc data/bacteria/meme_doric -nostatus
cmd.exe /C start 'C:\drive\uni\seq_inf\seqinf_project\data\bacteria\meme_doric\meme.html'

# DoriC 500
meme data/bacteria/doric_bactria_500.fasta -dna -oc data/bacteria/meme_doric_500 -nostatus -time 30000 -mod anr -nmotifs 5 -minw 9 -maxw 30 -objfun classic -revcomp -markov_order 4
mast data/bacteria/meme_doric_500/meme.xml data/bacteria/doric_bactria_500.fasta -oc data/bacteria/meme_doric_500 -nostatus
cmd.exe /C start 'C:\drive\uni\seq_inf\seqinf_project\data\bacteria\meme_doric_500\meme.html'

# bacteria
python skew/create_oric_fasta.py data/bacteria/ref_seq data/bacteria/skew_regions.fasta

meme data/bacteria/skew_regions.fasta -dna -oc data/bacteria/meme -nostatus -time 30000 -mod anr -nmotifs 3 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 4
mast data/bacteria/meme/meme.xml data/bacteria/skew_regions.fasta -oc data/bacteria/meme -nostatus
cmd.exe /C start 'C:\drive\uni\seq_inf\seqinf_project\data\bacteria\meme\meme.html'

# ecoli
python skew/create_oric_fasta.py skew/Ecoli/genomes data/ecoli/skew_regions.fasta

meme data/ecoli/skew_regions.fasta -dna -oc data/ecoli/meme -nostatus -time 30000 -mod anr -nmotifs 3 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 4
mast data/ecoli/meme/meme.xml data/ecoli/skew_regions.fasta -oc data/ecoli/meme -nostatus
cmd.exe /C start 'C:\drive\uni\seq_inf\seqinf_project\data\ecoli\meme\meme.html'

# ecoli family + salmonella family
python skew/create_oric_fasta.py data/families/enterobacteriaceae/ref_seq data/families/enterobacteriaceae/skew_regions.fasta

meme data/families/enterobacteriaceae/skew_regions.fasta -dna -oc data/families/enterobacteriaceae/meme -nostatus -time 30000 -mod anr -nmotifs 3 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 4
mast data/families/enterobacteriaceae/meme/meme.xml data/families/enterobacteriaceae/skew_regions.fasta -oc data/families/enterobacteriaceae/meme -nostatus
cmd.exe /C start 'C:\drive\uni\seq_inf\seqinf_project\data\families\enterobacteriaceae\meme\meme.html'

# thermotoga
python skew/create_oric_fasta.py skew/Thermotoga/genomes data/thermotoga/skew_regions.fasta

meme data/thermotoga/skew_regions.fasta -dna -oc data/thermotoga/meme -nostatus -time 30000 -mod anr -nmotifs 3 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 4
mast data/thermotoga/meme/meme.xml data/thermotoga/skew_regions.fasta -oc data/thermotoga/meme -nostatus
cmd.exe /C start 'C:\drive\uni\seq_inf\seqinf_project\data\thermotoga\meme\meme.html'

# cholerae
python skew/create_oric_fasta.py skew/Vibrio/genomes data/cholerae/skew_regions.fasta

meme data/cholerae/skew_regions.fasta -dna -oc data/cholerae/meme -nostatus -time 30000 -mod anr -nmotifs 3 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 4
mast data/cholerae/meme/meme.xml data/cholerae/skew_regions.fasta -oc data/cholerae/meme -nostatus
cmd.exe /C start 'C:\drive\uni\seq_inf\seqinf_project\data\cholerae\meme\meme.html'

# cholerae family
python skew/create_oric_fasta.py data/families/vibrionaceae/ref_seq data/families/vibrionaceae/skew_regions.fasta

meme data/families/vibrionaceae/skew_regions.fasta -dna -oc data/families/vibrionaceae/meme -nostatus -time 30000 -mod anr -nmotifs 3 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 4
mast data/families/vibrionaceae/meme/meme.xml data/families/vibrionaceae/skew_regions.fasta -oc data/families/vibrionaceae/meme -nostatus
cmd.exe /C start 'C:\drive\uni\seq_inf\seqinf_project\data\families\vibrionaceae\meme\meme.html'

# salmonella
python skew/create_oric_fasta.py skew/Salmonella/genomes data/salmonella/skew_regions.fasta

meme data/salmonella/skew_regions.fasta -dna -oc data/salmonella/meme -nostatus -time 30000 -mod anr -nmotifs 3 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 4
mast data/salmonella/meme/meme.xml data/salmonella/skew_regions.fasta -oc data/salmonella/meme -nostatus
cmd.exe /C start 'C:\drive\uni\seq_inf\seqinf_project\data\salmonella\meme\meme.html'

# salmonella family -> same as ecoli

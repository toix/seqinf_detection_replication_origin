# seqinf_detection_replication_origin
Sequence Bioinformatics, WS 2019/20<br/>
Project No. 15: Detection of the Replication Origin in Bacterial Genomes

### Git setup:
* download and install git with default parameters: https://git-scm.com/downloads<br/>
* navigate to your workspace directory with cli (or git bash)<br/>
* git clone https://github.com/toix/seqinf_detection_replication_origin.git seqinf_project<br/>


## Run a python script using windows cli (cmd)
+ cd <project root directory>
+ set PYTHONPATH=%PYTHONPATH%;%cd%
+ python skew/create_all_plots.py


## TODOs
* [Tobias] test meme on multiple ecoli oriC sequences 👍 worked for DoriC of all ecoli references (first motif is DnaA): http://meme-suite.org/opal-jobs/appMEME_5.1.015761936134292082624049/mast.html
* [Antonia] AT Skew
* [Tobias] (find and download reference sequences) 👍 @see download fasta files of genomes
* (Skew quality: throw out low organisms with chaotic curves)
* find minimum 👍
* [Tobias] Skew at minimum with higher resolution 👍 implemented with a resolution of 10: skew/create_oric_fasta.py
* done! [Lena] DoriC: Where is the minimum related to DnaA motif in ecoli (expected relative position, high variance?)
* [Tobias] create a fasta file with all OriC regions 👍 skript: skew/create_oric_fasta.py; results all bacteria reference sequences: data/bacteria/skew_regions.fasta
* [Tobias] execute local version of meme 👍 results for all bacteria reference sequences: data/bacteria/meme/mast.html
* [Tobias] test meme on species specific sequences (skew/Thermotoga) 👍 motif is shifted (data/ecoli/meme/meme.html) or no motif was found (data/thermotoga/meme/meme.html)
* [Tobias] disable the meme sites limit for DoriC
* [Tobias] compute motif for families 👍 worked for Escherichia coli and Salmonella enterica: data/families/enterobacteriaceae/meme/meme.html; found the motif with low significance for Vibrio cholerae: data/families/vibrionaceae/meme/meme.html; there are no more sequences for Thermotogaceae family
* [Tobias] profile alignment
* [Kilian] task 3 of the project sheet asks to compute the motifs of the 4 species, since using meme only one species does not give clear results 
   I tried using BLAST on the cropped OriC regions with the common DNAa box of all bacteria as query, see the results in data/. The motif does not occur in thermotoga, but there is a very similar conserved motif.
   TTATCCACA is conserved in the three other species 
* Compute the DnaA motifs for further genomes of your choice. 👍
* [Lena?] Biologists long believed that each bacterial chromosome has only one oriC. Find a paper in which this has been shown not to be true.
* [Kilian] For the bacterium Wigglesworthia glossinidia how many minima do you detect in the skew diagram? Do you find DnaA boxes in the vicinity of both? What do you conclude? -> articles/Genome_sequence_of_wigglesworthia.pdf skew/Wigglesworthia/plots/Wigglesworthia glossinidia endosymbiont of Glossina brevipalpis.pdf

## download fasta files of genomes
+ URL: https://www.ncbi.nlm.nih.gov/assembly
+ example search query for ecoli: "Escherichia coli"[Organism] AND (bacteria[filter] AND "latest refseq"[filter] AND "complete genome"[filter] AND (all[filter] NOT "derived from surveillance project"[filter] AND all[filter] NOT anomalous[filter] AND all[filter] NOT partial[filter]))
+ query for all bacteria reference sequences: "Bacteria"[Organism] AND "complete genome"[filter] AND "reference genome"[filter]
+ For Organisms replace "Bacteria"[Organism] with: "Escherichia coli"[Organism], "Vibrio cholerae"[Organism], "Thermotoga petrophila"[Organism], "Salmonella enterica"[Organism]
+ For Families replace "Bacteria"[Organism] with: "Enterobacteriaceae"[Organism], "Vibrionaceae"[Organism], "Thermotogaceae"[Organism]
+ keep the report.txt file for other downloads

## OriEval (evaluate skew)
* see plots, genomes, OriEval.xlsx
* plotted 10 organisms for each strain
* (for Thermotoga petrophila only one genome was available, hence other 
strains were plotted too for comparison)
* The Excel table lists the GC minimum for each strain in comparison 
with the DoriC minimum and checks whether our minimum lies at least 
within the oriC region given in the DoriC database
* Furthermore, number of DNAa motifs were counted in the zoom region 
around our minimum (allowing for one mismatch position; see also in the 
code)
* Motif positions were read approximately from the plot and compared to 
the oriC range given in the DoriC database
* Note: DoriC gives the number of DNAa motifs in the oriC region hence a 
comparision between our motif count and DoriC would not make sense since 
we are working in a different range/position

* Code: 
	* I've added the motif count and adapted the y-axis of the 
distance plot so it has a fixed height of the maximal Hamming score 
(otherwise the axis would be different in every plot)
	* Can we somehow read the positions of the motifs directly or 
even print them? Ideas?

## GC-minimum related to oriC (for zoom function)
* See xlxs dist_min_to_oriC
	* E.coli: max range 451 nucleotides around min
	* V. cholarea: max range 18331
	* S. enterica: max range 781
	* Thermotoga: max range 562
* For Therotoga several other subspecies were used for the calcuation 
too since only one genome file was available for T. petrophila
* Note: did not consider the DnaA gene location since in many case it 
does not even correspond to the oriC location

## HowTo meme
+ http://meme-suite.org/tools/meme
+ Input the primary sequences: Upload a fasta file with multiple sequences
+ Select the site distribution: any (anr)
+ Enter a job description
+ What should be used as the background model: 4th
+ How wide can motifs be: 9 to 9

## HowTo use meme cli
+ use Ubuntu terminal or Windows WSL: https://www.microsoft.com/de-de/p/ubuntu/9nblggh4msv6
+ sudo apt update
+ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1
+ sudo apt install ghostscript zlib1g-dev perl libxml2-dev libexpat1-dev libxslt1.1 libxslt1-dev autoconf automake libtool libxml-parser-perl
+ tar zxf meme-5.1.0.tar.gz
+ cd meme-5.1.0
+ ./configure --prefix=/mnt/c/drive/uni/seq_inf/seqinf_project/tools/meme --with-url=http://meme-suite.org/ --enable-build-libxml2 --enable-build-libxslt
+ make
+ make test
+ make install
+ export PATH=/mnt/c/drive/uni/seq_inf/seqinf_project/tools/meme/bin:/mnt/c/drive/uni/seq_inf/seqinf_project/tools/meme/libexec/meme-5.1.0:$PATH
+ cd /mnt/c/drive/uni/seq_inf/seqinf_project/data/bacteria/meme
+ meme /mnt/c/drive/uni/seq_inf/seqinf_project/data/bacteria/skew_regions.fasta -dna -oc . -nostatus -time 18000 -mod anr -nmotifs 3 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 4
+ mast meme.xml /mnt/c/drive/uni/seq_inf/seqinf_project/data/bacteria/skew_regions.fasta -oc . -nostatus

-----

## Literature
### Skew
* new directory skew  
    * ecoli.fasta:  
        * genome of e. coli (not sure if this is the right one, where should we get them from?)
    * skew_biopython.py  
        * Code:
            * uses biopython
            * GC_skew returns (G-C)/(G+C) for default window size of 100, Plot: plot_skew.pdf. 
            * xGC_skew returns None, plots GC skew on plasmid, can not be saved directy, thus screenshot with PIL.ImageGrab. Plot: xGC_plot.pdf
    * plot_skew.pdf
        * linear plot by matplotlib
	* xGC_plot.pdf
        + plot on plasmid by xGC_skew

### Literature Research (Skew)
Strand Composition Asymmetry:<br/>
* leading strand: more G and A
* lagging strang: more C and T
* nucleotide composition changes at ori and terminus:
	* usually at pos. of 50% of the genome length (?)
	* E. coli: 
		* G > C clockwise from ori to terminus
		* C > G counterclockwise

GC-Skew:<br/>
* regular GC-skew: uses sliding window approach
* cumulative GC-skew: without sliding window, (G-C)/(G+C)
* window size is critical:
	*too small: many fluctuations
	*too large: might hide precise coordinates of minima/maxima

Z-curve:<br/>
* three dimensional curve
* "purple diamonds" indicate distribution of DnaA boxes (they can be all over the genome)
* arrows indicate ori; use RY minimum (marks change from CT rich to AG rich region)
* inverse Z-transform used to reconstruct corresponding DNA sequence
* paper by Zhang (2004): Z-curve suggests 3 oris in Sulfolobus sulfataricus
* software: Zplotter online

Tools for skew:<br/>
see paper Development Skew Calculation in articles directory

### OriFinder (2008)
+ "Jointly using the three methods (GC-skew, location of the dnaA gene and distribution of DnaA boxes)" (information how to join the methods is missing)
+ "DnaA and its binding sites are well conserved throughout the bacterial kingdom"
+ "Out of the 568 chromosomes, there are only 342 chromosomes (342/ 568 = 60.2%) whose oriCs are adjacent to dnaA gene and near the switch of GC-skew"
+ ~40% of 568 genomes cannot be solved using only the information of GC-skew, location of the dnaA gene and distribution of DnaA boxes.
+ "the oriC regions can be identified for over 98% chromosomes out of the 568 bacterial chromosomes analyzed"

### Literature Research (OriFinder, 2018)
See papers: Recent development of Ori-Finder; Ident. of repl. origins
* input: fasta
* approximate oriC location defined with skew
* use window in this region to search for clusters of DnaA motifs
	* user can pre-define DnaA boxes depending on species
	* check for motifs differing by not more than 1 base (can be adapted)
	* idea for our project: search for potential motifs in this window rather than working with predefined consensus sequ.
	
### Identification of replication origins.pdf (2008):
* only smooth gc-curves (class 1 and 2a) with global minima are OK to predict origins (~80% of Eubacterial and none of Archaeal chromosomes)
* Over-represented motifs identified in this region (GC skew) are likely DnaA-boxes. The positional weight matrix (PWM) may be derived from these boxes and used to find clusters of candidate DnaA-boxes in the remaining genomes from this taxon.
* clusters of the DnaA-boxes may occur not only at the replication origins. For example REGULATION of replication initiation in e.coli
* Prediction with DnaA motif (no skew?) from related bacterias for a Actinobacteria worked but didn't for two Cyanobacteria (class 3a and 2b)

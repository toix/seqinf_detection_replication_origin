# seqinf_detection_replication_origin
Sequence Bioinformatics, WS 2019/20<br/>
Project No. 15: Detection of the Replication Origin in Bacterial Genomes

### Git setup:
* download and install git with default parameters: https://git-scm.com/downloads<br/>
* navigate to your workspace directory with cli (or git bash)<br/>
* git clone https://github.com/toix/seqinf_detection_replication_origin.git seqinf_project<br/>


## TODOs
* [Tobias] test meme on multiple ecoli oriC sequences 👍 worked for DoriC of all ecoli references (first motif is DnaA): http://meme-suite.org/opal-jobs/appMEME_5.1.015761936134292082624049/mast.html
* [Antonia] AT Skew
* [Tobias] (find and download reference sequences) 👍 @see download fasta files of genomes
* (Skew quality: throw out low organisms with chaotic curves)
* find minimum
* Skew at minimum with higher resolution
* done! [Lena] DoriC: Where is the minimum related to DnaA motif in 
ecoli (expected relative position, high variance?)
* create a fasta file with all regions
* tasks from project sheet

## download fasta files of genomes
+ URL: https://www.ncbi.nlm.nih.gov/assembly
+ example search query for ecoli: "Escherichia coli"[Organism] AND (bacteria[filter] AND "latest refseq"[filter] AND "complete genome"[filter] AND (all[filter] NOT "derived from surveillance project"[filter] AND all[filter] NOT anomalous[filter] AND all[filter] NOT partial[filter]))

## OriEval
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
(otherwise the axis would be different in everey plot)
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

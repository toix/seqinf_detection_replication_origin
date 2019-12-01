# seqinf_detection_replication_origin
Sequence Bioinformatics, WS 2019/20<br/>
Project No. 15: Detection of the Replication Origin in Bacterial Genomes

### Git einrichten:
* download and install git with default parameters: https://git-scm.com/downloads<br/>
* navigate to your workspace directory with cli (or git bash)<br/>
* git clone https://github.com/toix/seqinf_detection_replication_origin.git seqinf_project<br/>

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

### Literature Research (OriFinder)
See papers: Recent development of Ori-Finder; Ident. of repl. origins
* input: fasta
* approximate oriC location defined with skew
* use window in this region to search for clusters of DnaA motifs
	* use can pre-define DnaA boxes depending on species
	* check for motifs differing by not more than 1 base (can be adapted)
	* idea for our project: search for potential motifs in this window rather than working with predefined consensus sequ.
	

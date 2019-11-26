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


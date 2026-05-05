# Lemur Parameters

## Parameter descriptions

### Main arguments:
```sh
  -i INPUT, --input INPUT
                        Input FASTQ file for the analysis
  -o OUTPUT, --output OUTPUT
                        Folder where the Lemur output will be stored
  -d DB_PREFIX, --db-prefix DB_PREFIX
                        Path to the folder with marker gene DB for each marker gene
  --tax-path TAX_PATH   Path to the taxonomy.tsv file 
  -t NUM_THREADS, --num-threads NUM_THREADS
                        Number of threads you want to use
  --aln-score {AS,edit,markov}
                        AS: Use SAM AS tag for score, edit: Use edit-type distribution for score, markov: Score CIGAR as Markov chain
  -r RANK, --rank RANK  Taxonomic rank used for final aggregation
  --min-aln-len-ratio MIN_ALN_LEN_RATIO
                        Minimum ratio of alignment length to marker gene length [default: 0.75]
  --min-fidelity MIN_FIDELITY
                        Minimum acceptable log(P)/aln_length [deafult: 0.5]
  --ref-weight REF_WEIGHT
                        Scale factor for log(P) dependent on alignment length: log(P) <- log(P) + REF_WEIGHT * log(aln_length_ratio) [default: 1.0]
```

### minimap2 arguments: _Clarification source_: [lh3.github.io/minimap2](https://lh3.github.io/minimap2/minimap2.html)
```sh
  --mm2-N MM2_N         minimap max number of secondary alignments per read [50]
  --mm2-K MM2_K         minibatch size for minimap2 mapping [500M] # increase this for faster runtime(?) ; range [not sure(?)]
  # -K NUM 	        Number of bases loaded into memory to process in a mini-batch [500M]. Similar to option -I, K/M/G/k/m/g suffix is accepted. A large NUM helps load balancing in the multi-threading mode, at the cost of increased memory. 
  --mm2-type {map-ont,map-hifi,map-pb,sr} # type of sequencing data
                        ONT: map-ont [map-ont], PacBio (hifi): map-hifi, PacBio (CLR): map-pb, short-read: sr
  # see elaboration in section below

```
#### Minimap2 (`--mm2-type` / `-x`) elaborated
-x STR 	Preset []. This option applies multiple options at the same time. It should be applied before other options because options applied later will overwrite the values set by -x. Available STR are:
- `map-ont` 	Align noisy long reads of **~10% error rate** to a reference genome. This is the **default mode**.
- `lr:hq` 	Align accurate long reads (error rate <1%) to a reference genome (`-k19 -w19 -U50,500 -g10k`). This was recommended by ONT developers for recent Nanopore reads produced with **chemistry v14** that can reach **~99% in accuracy**. It was shown to work better for accurate Nanopore reads than map-hifi.
- `map-hifi` 	Align PacBio high-fidelity (HiFi) reads to a reference genome (`-xlr:hq -A1 -B4 -O6,26 -E2,1 -s200`). It differs from lr:hq only in scoring. It has not been tested whether lr:hq would work better for PacBio HiFi reads.
- `map-pb` 	Align older PacBio continuous long (CLR) reads to a reference genome (`-Hk19`). Note that this data type is effectively deprecated by HiFi. Unless you work on very old data, you probably want to use map-hifi or lr:hq.
    
Other options available in minimap2, may not be relevant for lemur though? 
- `map-iclr` 	Align Illumina Complete Long Reads (ICLR) to a reference genome (`-k19 -B6 -b4 -O10,50`). This was recommended by Illumina developers.
- `asm5` 	Long assembly to reference mapping (`-k19 -w19 -U50,500 --rmq -r1k,100k -g10k -A1 -B19 -O39,81 -E3,1 -s200 -z200 -N50`). Typically, the alignment will not extend to regions with 5% or higher sequence divergence. Use this preset if the **average divergence is not much higher than 0.1%**.
- `asm10` 	Long assembly to reference mapping (`-k19 -w19 -U50,500 --rmq -r1k,100k -g10k -A1 -B9 -O16,41 -E2,1 -s200 -z200 -N50`). Use this if the **average divergence is around 1%**.
- `asm20` 	Long assembly to reference mapping (`-k19 -w10 -U50,500 --rmq -r1k,100k -g10k -A1 -B4 -O6,26 -E2,1 -s200 -z200 -N50`). Use this if the **average divergence is around several percent**.
- `splice` 	Long-read spliced alignment (`-k15 -w5 --splice -g2k -G200k -A1 -B2 -O2,32 -E1,0 -C9 -z200 -ub --junc-bonus=9 --cap-sw-mem=0 --splice-flank=yes`). In the splice mode, 1) long deletions are taken as introns and represented as the ‘N’ CIGAR operator; 2) long insertions are disabled; 3) deletion and insertion gap costs are different during chaining; 4) the computation of the ‘ms’ tag ignores introns to demote hits to pseudogenes.
- `splice:hq` 	Spliced alignment for accurate long RNA-seq reads such as PacBio iso-seq (`-xsplice -C5 -O6,24 -B4`).
- `splice:sr` 	Spliced alignment for short RNA-seq reads (`-xsplice:hq --frag=yes --end-bonus=10 -2K50m --heap-sort=yes --pe-ind-chain --secondary=no`).
- `sr` 	Short-read alignment without splicing (`-k21 -w11 --sr --frag=yes -A2 -B8 -O12,32 -E2,1 -r100 -p.5 -N20 -f1000,5000 -n2 -m25 -s40 -g100 -2K50m --heap-sort=yes --secondary=no`).
- `ava-pb` 	PacBio CLR all-vs-all overlap mapping (`-Hk19 -Xw5 -e0 -m100`).
- `ava-ont` 	Oxford Nanopore all-vs-all overlap mapping (`-k15 -Xw5 -e0 -m100 -r2k`).

### Miscellaneous arguments:
```sh
  --keep-alignments     Keep SAM files after the mapping (might require a lot of disk space)
  -e LOG_FILE, --log-file LOG_FILE
                        File for logging [default: stdout]
  --sam-input SAM_INPUT Use a SAM file as input and skip read mapping step
  --verbose             Enable DEBUG level logging
  --save-intermediate-profile
                        Will save abundance profile at every EM step
  --width-filter        Apply uniform coverage filter
```

### Additional flags:
```sh
  -h, --help            show usage help message and exit
  -v, --version         show program's version number and exit
```

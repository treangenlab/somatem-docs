# Lemur Parameters

### Parameter descriptions

Main arguments:
```
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
                        Minimum acceptable log(P)/aln_length [deafult: log(0.5)]
  --ref-weight REF_WEIGHT
                        Scale factor for log(P) dependent on alignment length: log(P) <- log(P) + REF_WEIGHT * log(aln_length_ratio) [default: 1.0]
```

minimap2 arguments:
```
  --mm2-N MM2_N         minimap max number of secondary alignments per read [50]
  --mm2-K MM2_K         minibatch size for minimap2 mapping [500M]
  --mm2-type {map-ont,map-hifi,map-pb,sr}
                        ONT: map-ont [map-ont], PacBio (hifi): map-hifi, PacBio (CLR): map-pb, short-read: sr
```

Miscellaneous arguments:
```
  --keep-alignments     Keep SAM files after the mapping (might require a lot of disk space)
  -e LOG_FILE, --log-file LOG_FILE
                        File for logging [default: stdout]
  --sam-input SAM_INPUT Use a SAM file as input and skip read mapping step
  --verbose             Enable DEBUG level logging
  --save-intermediate-profile
                        Will save abundance profile at every EM step
  --width-filter        Apply uniform coverage filter
```

Additional flags:
```
  -h, --help            show usage help message and exit
  -v, --version         show program's version number and exit
```

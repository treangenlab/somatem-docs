# Emu Parameters

### usage: 
You can get the usage by running `emu abundance --help`

```sh
usage: emu abundance [-h] [--type {map-ont,map-pb,sr,lr:hq,map-hifi,splice:hq}] [--min-abundance MIN_ABUNDANCE] [--db DB]
                     [--N N] [--K K] [--mm2-forward-only] [--output-dir OUTPUT_DIR] [--output-basename OUTPUT_BASENAME]
                     [--keep-files] [--keep-counts] [--keep-read-assignments] [--output-unclassified] [--threads THREADS]
                     [--min-pid MIN_PID] [--min-align-len MIN_ALIGN_LEN] [--max-align-len MAX_ALIGN_LEN]
                     input_file [input_file ...]
```

### Abundance Estimation Parameters

```sh
# Command: --type
# Default: map-ont
# Description: denote sequencer [short-read:sr, Pac-Bio:map-pb, ONT:map-ont, Nanopore Q20:lr:hq, PacBio HiFi:map-hifi, traditional cDNA:splice:hq]
--type <sequencer_type>

# Command: --min-abundance
# Default: 0.0001
# Description: generates results with species relative abundance above this value in addition to full results; .01 = 1%
--min-abundance <value>

# Command: --db
# Default: $EMU_DATABASE_DIR
# Description: path to emu database; directory must include the following files: species_taxid.fasta, taxonomy.tsv
--db <database_path>

# Command: --N
# Default: 50
# Description: max number of alignments utilized for each read in minimap2
--N <number>
# Note: somatem uses a more descriptive name for this parameter: emu_N_minimap_max_alignments

# Command: --K
# Default: 500M
# Description: minibatch size for mapping in minimap2
--K <size>
# Note: somatem uses a more descriptive name for this parameter: emu_K_minibatch_size

# Command: --mm2-forward-only
# Default: FALSE
# Description: force minimap2 to consider the forward transcript strand only (for long mRNA/cDNA reads)
--mm2-forward-only

# Command: --min-pid
# Default: 0
# Description: minimum percent identity (PID) based on NM tag
--min-pid <percentage>

# Command: --min-align-len
# Default: 0
# Description: minimun aligned query length (excluding clipped bp)
--min-align-len <length>

# Command: --max-align-len
# Default: 2000
# Description: maximum aligned query length (excluding clipped bp)
--max-align-len <length>

# Command: --output-dir
# Default: ./results
# Description: directory for output results
--output-dir <directory>

# Command: --output-basename
# Default: stem of input_file(s)
# Description: basename of all output files saved in output-dir; default utilizes basename from input file(s)
--output-basename <basename>

# Command: --keep-files
# Default: FALSE
# Description: keep working files in output-dir (alignments [.sam], reads of specified length [.fa])
--keep-files

# Command: --keep-counts
# Default: FALSE
# Description: include estimated read counts for each species in output*
--keep-counts

# Command: --keep-read-assignments
# Default: FALSE
# Description: output .tsv file with read assignment distributions: each row as an input read; each entry as the likelihood it is derived from that taxa (taxid is the column header); each row sums to 1
--keep-read-assignments

# Command: --output-unclassified
# Default: FALSE
# Description: generate three additional sequence files: unmapped, filtered mapped, and unclassified mapped input reads**
--output-unclassified

# Command: --threads
# Default: 3
# Description: number of threads utilized by minimap2
--threads <number>

# Notes:
# *Estimated read counts are based on likelihood probabilities and therefore may not be integer values. They are calculated as the product of estimated relative abundance and total classified reads.
# **Unmapped reads: reads that did not align to any reference; Filtered mapped: reads that aligned but were filtered out based on thresholds; Unclassified mapped: reads that aligned but could not be assigned to a specific taxonomic level.
```

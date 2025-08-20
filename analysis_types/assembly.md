What does "genome or metagenome assembly" mean?

Source: _This document was generated using [seqera AI chat](https://seqera.io/ask-ai/chat)_

**Assembly** is the computational process of reconstructing longer DNA sequences (contigs and scaffolds) from short sequencing reads by finding overlapping regions between reads.

## Genome Assembly

**Definition**: Reconstructing a single organism's complete genome from sequencing reads

**Input**: Sequencing reads from a pure culture or isolated organism **Output**: Contiguous sequences (contigs) representing the organism's chromosomes/plasmids

### Process:

1. **Overlap Detection**: Find reads that share identical sequences
2. **Graph Construction**: Build overlap graphs connecting related reads
3. **Path Finding**: Trace paths through the graph to create longer sequences
4. **Scaffolding**: Use paired-end/mate-pair information to order and orient contigs

### Example:

`Raw reads: ATCGATCG, TCGATCGA, GATCGATT Assembled contig: ATCGATCGATT`

## Metagenome Assembly

**Definition**: Reconstructing genomes from mixed microbial communities without prior separation

**Input**: Sequencing reads from environmental samples containing multiple organisms 
**Output**: Contigs representing fragments from various organisms in the community

### Key Challenges:

- **Species Mixing**: Reads from different organisms must be separated
- **Uneven Coverage**: Some organisms are more abundant than others
- **Strain Variation**: Closely related strains complicate assembly
- **Repetitive Regions**: Shared sequences between species cause confusion

### Approaches:

1. **Co-assembly**: Assemble all reads together, then separate by organism
2. **Individual Assembly**: Classify reads first, then assemble each organism separately
3. **Hybrid Methods**: Combine both approaches

## Assembly Quality Metrics

**Contiguity**:

- **N50**: Length where 50% of assembly is in contigs of this size or larger
- **Number of contigs**: Fewer is generally better
- **Total length**: Should match expected genome size

**Completeness**:

- **BUSCO scores**: Presence of universal single-copy genes
- **Coverage depth**: How many times each base is sequenced

## Common Tools

### Genome Assemblers:

- **SPAdes**: Versatile, good for bacterial genomes
- **Canu**: Long-read assembly (PacBio, Nanopore)
- **Flye**: Long-read assembly with repeat resolution

### Metagenome Assemblers:

- **MEGAHIT**: Fast, memory-efficient
- **metaSPAdes**: Extension of SPAdes for metagenomes
- **IDBA-UD**: Iterative assembly with varying k-mer sizes

## Why Assembly Matters

**Advantages over read-based analysis**:

- **Gene Context**: See complete genes and operons
- **Novel Discovery**: Find genes not in reference databases
- **Structural Variants**: Detect rearrangements and insertions
- **Functional Annotation**: Predict protein functions from complete sequences

**Applications**:

- **Genome Annotation**: Identifying genes and their functions
- **Comparative Genomics**: Comparing genomes across species
- **Metagenome-Assembled Genomes (MAGs)**: Reconstructing individual genomes from metagenomes
- **Biosynthetic Gene Clusters**: Finding natural product pathways

Assembly transforms fragmented sequencing data into meaningful biological sequences that can be analyzed for genes, functions, and evolutionary relationships!
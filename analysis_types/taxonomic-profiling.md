What does "_taxonomic profiling_" mean?

Source: _This document was generated using [seqera AI chat](https://seqera.io/ask-ai/chat)_

**Taxonomic profiling** is the process of identifying and quantifying the different organisms (species, genera, families, etc.) present in a biological sample, particularly in microbiome or metagenomic studies.

# What Taxonomic Profiling Tells You

1. **Identity**: What organisms are present?
    - Organism here includes Bacteria, archaea, viruses, fungi, parasites, and also eukaryotes
    - Species-level identification when possible

2. **Abundance**: How much of each organism is present?
    - Relative abundance (percentages)
    - Absolute abundance (if calibrated, using a reference DNA using spike-ins)

3. **Diversity**: How diverse is the community?
Note that these metrics are computed based on the taxonomic profile output external tools not in Somatem yet.
    - Alpha diversity (within-sample diversity)
    - Beta diversity (between-sample differences)

# How It Works

**Input**: Raw sequencing reads from your sample

**Process**:
    - Compare reads against reference databases
    - Assign taxonomic labels to reads
    - Aggregate results by taxonomic levels
    - Calculate relative abundances

**Output**: Taxonomic composition table showing something like this:
```sh

Organism                    Relative Abundance
Escherichia coli           15.2%
Bacteroides fragilis       12.8%
Lactobacillus acidophilus   8.3%
... and so on ...
```

# Key Concepts

**Taxonomic Hierarchy**:
    - Kingdom → Phylum → Class → Order → Family → Genus → Species
    - Results can be reported at any level

**Resolution Limitations**:
    - Some reads can only be classified to genus level
    - Closely related species may be difficult to distinguish

**Applications**:
    - Clinical: Pathogen detection, microbiome health assessment
    - Environmental: Soil/water microbiome characterization
    - Food: Quality control, fermentation monitoring
    - Research: Understanding microbial communities

_Taxonomic profiling_ essentially answers "who's there and how much of each" in your microbial community!
# Plannning tools
_This is a work in progress document to plan the tools to be included in the pipeline ([flowchart](../docs/SOMAteM-sketch-v1.2.jpg)). This should be moved to the [wiki](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages#cloning-wikis-to-your-computer) when it is finalized, for posterity. A shorter summary of the tools and what they do will be in the readme_

## Summary Table

| Category                     | Tool                                                                                                | Nextflow Implementation                                                                             |
| ---------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Quality Control**          | [NanoPlot](https://github.com/wdecoster/NanoPlot)                                                   | [nf-core/nanoplot](https://github.com/nf-core/modules/tree/master/modules/nf-core/nanoplot)         |
|                              | [hostile](https://github.com/bede/hostile)                                                          | [nf-core/hostile](https://github.com/nf-core/modules/tree/master/modules/nf-core/hostile)          |
|                              | [chopper](https://github.com/wdecoster/chopper)                                                     | [nf-core/chopper](https://github.com/nf-core/modules/tree/master/modules/nf-core/chopper)          |
| **Assembly**                 | [Flye](https://github.com/fenderglass/Flye)                                                 		 |  [nf-core/flye](https://github.com/nf-core/modules/tree/master/modules/nf-core/flye)             |
| 		                       | [myloasm](https://github.com/bluenote-1577/myloasm)                                                  | -                                                                                                  |
| **Binning**                  | [SemiBin2](https://github.com/BigDataBiology/SemiBin)                                               | -                                                                                                   |
| **Bin QC**				   | [CheckM2](https://github.com/chklovski/CheckM2)													 | -																								 |
| **SNP/SV Detection**         | [rhea](https://github.com/treangenlab/rhea) (SV, timecourse)                                        | -                                                                                                   |
| **Taxonomic Profiling**      | [Emu](https://github.com/treangenlab/emu)                                                           | [gms-16s](https://github.com/genomic-medicine-sweden/gms_16S)                                       |
|                              | [Lemur](https://github.com/treangenlab/lemur) + [MAGnet](https://github.com/treangenlab/magnet)<br> | -                                                                                                   |
|                              | [Sylph](https://github.com/bluenote-1577/sylph)                                                     | -                                                                                                   |
|							   | [SingleM pipe](https://github.com/wwood/singlem)													 | -																								 |
| **Functional Annotation**    | [SeqScreen](https://gitlab.com/treangenlab/seqscreen)                                               | [DSL1 to 2](https://gitlab.com/treangenlab/seqscreen/-/tree/to-dsl2?ref_type=heads)             |
|							   | [bakta](https://github.com/oschwengers/bakta)														 | - 																								 |
| **Community Assessment**	   | [SingleM appraise](https://github.com/wwood/singlem)												 | -																								 |
| **Reporting, Visualization** | [taxburst](https://github.com/taxburst/taxburst)                                                    | -																								 |
|                              | [MetagenomeScope](https://github.com/marbl/MetagenomeScope)                                         | -                                                                                                   
Total number of unique tools: 17
Number with nextflow implmentations: 7ish/17?
Soon to be _many_ more...

### Archived tools
_These will be implemented in the future ; moving them here to preserve the links etc_

| Category                     | Tool                                                                                                | Nextflow Implementation                                                                             |
| ---------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
|  **Quality Control**         | [filtlong](https://github.com/rrwick/Filtlong)                                                      | [nf-core/filtlong](https://github.com/nf-core/modules/tree/master/modules/nf-core/filtlong)         |
| **Assembly**                 | [MetaCompass](https://github.com/marbl/MetaCompass)                                                | -               																					 |
| **Pangenomics**              | [parsnp](https://github.com/marbl/parsnp)<br>                            			                 | -                                                                                                   |
|                              | [tMHG-Finder](https://github.com/yongze-yin/tMHG-Finder)                                            | -                                                                                                    |
| **Taxonomic Profiling**      | [MetaPhlAn](https://github.com/biobakery/MetaPhlAn)												 | -																								 |
| **Metabolic Reconstruction** | [Bakdrive](https://gitlab.com/treangenlab/bakdrive)                                                 | -                                                                                                   |
|                              | [micom](https://github.com/micom-dev/micom)                                                         | -                                                                                                   |


---

*Table summarizes all the tools listed below; tools are grouped by category and ordered by priority. Tools with available nextflow implementations are linked above. Tools are listed in order of priority within each category.*

Original plan from flowchart sketched on whiteboard on 2025-05-13: Inputs from Todd Treangen


## TODO:
- [x] Add github links and citations for these tools
- [ ] List the LLM questions that will lead to each step
- [ ] Check and link the pipelines for which nextflow DSL1 or DSL2 implementation exists + citations


## Major decision points
- 3 broad branches of the pipeline
  - 16S
  - metagenomic classification
  - assembly based metagenomics
- 1 vs n samples
  - Rheaa is good for n samples so it will dictate the rest of the pipeline 
- Type of data technology: (ideas for more detailed options [flye docs](github.com/mikolmogorov/Flye/blob/flye/docs/USAGE.md#-supported-input-data))
  - Nanopore (ONT)
  - Pacbio (Pacbio)
  - Synthetic long reads (Illumina)
- Assembly vs reads
- Reference guided vs de novo assembly

## Tools list

### Quality control / preprocessing

- [NanoPlot](https://github.com/wdecoster/NanoPlot): QC plotting suite for long-read sequencing data and alignments. _for QC on the raw files / final reads after filtering_. [nf-core/module](https://github.com/nf-core/modules/tree/master/modules/nf-core/nanoplot) | [citation](https://academic.oup.com/bioinformatics/article/39/5/btad311/7160911?login=true)
- [hostile](https://github.com/bede/hostile): A tool for filtering reads that align to a host genome (_removes host contamination from microbial metagenomes_). nf-core/modules: [hostile-clean](https://nf-co.re/modules/hostile_clean/); [hostile-fetch](https://nf-co.re/modules/hostile_fetch/), [code](https://github.com/nf-core/modules/tree/master/modules/nf-core/hostile) | [citation](https://doi.org/10.1093/bioinformatics/btad728)
- [chopper](https://github.com/wdecoster/chopper): A tool to filter nanopore sequencing reads by quality and length ; *Use to filter out low quality and short reads*. [nf-core/module](https://nf-co.re/modules/chopper/), [code](https://github.com/nf-core/modules/tree/master/modules/nf-core/chopper) | [citation](https://doi.org/10.1093/bioinformatics/bty149)
- [filtlong](https://github.com/rrwick/Filtlong): Quality filtering tool for long-reads by read quality and length [nf-core/module](https://nf-co.re/modules/filtlong/), [code](https://github.com/nf-core/modules/tree/master/modules/nf-core/filtlong) | no citation


### Assembly

**De novo assembly**: _Note: uses a lot of RAM: 32 GB minimum_

- [Flye](https://github.com/fenderglass/Flye): De novo assembler for single-molecule sequencing reads using repeat graphs (PacBio and Oxford Nanopore). [nf-core/module](https://nf-co.re/modules/flye/), [code](https://github.com/nf-core/modules/tree/master/modules/nf-core/flye) | [citation](https://doi.org/10.1038/s41592-020-00971-x)
- [myloasm](https://github.com/bluenote-1577/myloasm) Myloasm is a de novo metagenome assembler, it takes long reads and outputs polished contigs in a single command. (not published yet but probably will be by the time Somatem manuscript is out, very complete github & docs already made, also Jim Shaw & Hang Li collab).

**Reference guided**
We aim to implement a reference-guided assembler in the future, however, meta-compass is currently short-read only...
- [meta-compass](https://github.com/marbl/MetaCompass): A metagenomic reference-guided assembler that leverages multiple reference genomes

### Binning
Currently we only use one binner but we have aspirations to include mutliple binners + refinement tools down the read.
- [SemiBin2](https://github.com/BigDataBiology/SemiBin) SemiBin2 uses self-supervised learning to learn feature embeddings from the contigs with emphasis on long-read sequencing data. [citation](https://doi.org/10.1093/bioinformatics/btad209)



## Pangenomic analyses
- [parsnp](https://github.com/marbl/parsnp): A fast microbial core-genome alignment tool, which can output core genome phylogeny, multiple genome alignments and SNP calls. [citation](https://academic.oup.com/bioinformatics/article/40/5/btae311/7667868)  
- [tMHG-Finder](https://github.com/yongze-yin/tMHG-Finder): Tool for tree guided maximal homologous group (MHG) identification from multiple genomes. MHGs enable more accurate phylogenetic reconstruction than gene annotations, accounting for horizontal gene transfer. [citation](https://www.biorxiv.org/content/10.1101/2025.03.16.643543v1.full) & [older MHG-finder](https://doi.org/10.1371/journal.pcbi.1010216)


### SNP and SV Detection
Includes gene duplication loss

- [rhea](https://github.com/treangenlab/rhea): Detects structural variants (SV, >10 bp indels) and HGT between temporally evolving microbial metagenomic samples for large cohorts of related or similar genomes (1:n samples). [citation](https://academic.oup.com/bioinformatics/article/40/Supplement_1/i58/7700881): _Kristen et al., Bioinformatics, 2024_

### Taxonomic classification/profiling
- [Emu](https://github.com/treangenlab/emu): Taxonomic classification, and abundance estimation of 16S rRNA reads for long-read data. Nextflow DSL2 implementation: [gms-16s](https://github.com/genomic-medicine-sweden/gms_16S) + [gms-16S citation](https://link.springer.com/article/10.1007/s10096-025-05158-w) | [citation](https://www.nature.com/articles/s41592-022-01520-4)
- [Lemur](https://github.com/treangenlab/lemur): For rapid and accurate taxonomic profiling on long-read metagenomic datasets. [citation](https://www.biorxiv.org/content/10.1101/2024.06.01.596961v2.full)
	- [MAGnet](https://github.com/treangenlab/magnet): Refines taxonomic profiles for accuracy using reference genome mapping from all the reads. _same citation as Lemur_: [citation](https://www.biorxiv.org/content/10.1101/2024.06.01.596961v2.full)
- [Sylph](https://github.com/bluenote-1577/sylph): A tool for rapid and accurate species level taxonomic profiling of metagenomic data using k-mer sketches. [citation](https://www.nature.com/articles/s41587-024-02412-y): _Shaw et al., Nature Biotechnology, 2024_ | [documentation](https://sylph-docs.github.io/)
- [MetaPhlAn](https://github.com/biobakery/MetaPhlAn) Including because recent support for long reads and will make a lightweight functional annotation analysis when combined with HUMAnN.
- [Centrifuger](https://github.com/mourisl/centrifuger) might be better for large databases due to compression? | [citation](https://link.springer.com/article/10.1186/s13059-024-03244-4)

### Functional annotation
- [SeqScreen](https://gitlab.com/treangenlab/seqscreen): Functional screening of pathogenic sequences in metagenomic data.
[nextflow: DSL1 to 2 transition](https://gitlab.com/treangenlab/seqscreen/-/tree/to-dsl2?ref_type=heads) | [citation](https://link.springer.com/article/10.1186/s13059-022-02695-x): _Balaji et al., Genome Biology, 2022_
	- _includes **antibiotic resistance genes**_. 
- [HUMAnN](https://github.com/biobakery/humann): HMP Unified Metabolic Analysis Network - profiling microbial community metabolic potential (? / Not for long reads? (*says Austin*) - *eukaryotic; RAM intensive*; )
- [bakta](https://github.com/oschwengers/bakta)

### Read Classification
_How is this different from taxonomic classification?_

- [SeqScreen](https://gitlab.com/treangenlab/seqscreen): Functional screening of pathogenic sequences in metagenomic data. 
- [Centrifuge](https://github.com/DaehwanKimLab/centrifuge): A rapid and memory-efficient classification system for metagenomic sequences

### Pathogen identification
- [MAGnet](https://github.com/treangenlab/magnet): Metagenomic Analysis of Genomes in the ENvironmental Toolkit
- [SeqScreen](https://gitlab.com/treangenlab/seqscreen): Functional screening of pathogenic sequences in metagenomic data

### Metabolic reconstruction
- [Bakdrive](https://gitlab.com/treangenlab/bakdrive) / [recent/private version](https://github.com/treangenlab/bakdrive): _Can take in Emu output_. [citation](https://academic.oup.com/bioinformatics/article/39/Supplement_1/i47/7210449): _Wang et al., Bioinformatics, 2023_
  - [micom](https://github.com/micom-dev/micom): _Best to use with bakdrive_. [citation](https://journals.asm.org/doi/10.1128/msystems.00606-19): _Diener et al., mSystems, 2020_

### Final: Validation / QC
- [CheckM2](https://github.com/chklovski/CheckM2)
- [SingleM appraise](https://github.com/wwood/singlem)
_Check how MetAMOS implements this says Todd_
- Check if tools ran correctly


### Report
- nextflow execution report (html)
- [MultiQC](https://github.com/MultiQC/MultiQC)
- [SingleM appraise](https://github.com/wwood/singlem)
_Check how MetAMOS report was made from scratch says Todd_ 


### Visualization tools
- [taxburst](https://github.com/taxburst/taxburst)
- [MetagenomeScope](https://github.com/marbl/MetagenomeScope): Web based visualization tool for metagenomic assembly graphs.
- [emperor](https://biocore.github.io/emperor/build/html/index.html) Interactive ordination plot viz

### Databases
- bacterial: [RefSeq](https://www.ncbi.nlm.nih.gov/refseq/)
- viral: [NCBI Viral Genomes](https://www.ncbi.nlm.nih.gov/genome/viruses/)

# Other workflows to learn from
- [CAMP](https://github.com/Meta-CAMP) ; [paper](https://www.biorxiv.org/content/10.1101/2023.04.09.536171v3.full) is a snakemake workflow that aims to be one-click deployment but also modular. They work with long-reads and hybrid assemblies along with short-reads. They are also incorporating an LLM called bootcamp similar to omi. So they might really beat us with the Somatem?
- [aviary](https://github.com/rhysnewell/aviary) is a snakemake workflow that Austin espouses, but Todd doesn't like that it's not published.
> (_Austin_) This is the pipeline used for our previous depletion paper and also put together by Ben woodcraft’s group, has singlem and all the rest of their m tools 
- [cloudres](https://github.com/maxlcummins/cloudres): MLST assignment and AMR detection. _could learn/borrow code_
- [mmlong2](https://github.com/Serka-M/mmlong2) Genome-centric long-read metagenomics workflow for automated recovery and analysis of prokaryotic genomes with Nanopore or PacBio HiFi sequencing data.
- [MUFFIN](https://github.com/RVanDamme/MUFFIN) MUFFIN is a hybrid assembly and differential binning workflow for metagenomics, transcriptomics and pathway analysis.
- [mapo tofu](https://github.com/ikmb/TOFU-MAaPO) is a nextflow pipeline for short reads. 
  - Can borrow their [Sylph module](https://github.com/ikmb/TOFU-MAaPO/blob/master/modules/sylph.nf)?
- [BugBuster](https://github.com/gene2dis/BugBuster)
  - _No tool in our list_

# Derivatives of this doc

*Stuff from this document was re-formatted/summarized into a few other documents for easier access. I used Windsurf AI for this so keeping these in the same repo keeps them easy to iterate on with AI when changes occur*

List
- `tool_voting.csv`: Contains tool names with category for Todd to vote on/suggest new ones
- `tool_links.csv`: contains links to the github and citations for easy parsing into embeddings making by Sahil
- `mock_nf_params.yaml`: is a dadasnake inspired yaml formatted with the tools in this list
	- I want sahil to edit this file as appropriate (write access needed); so will need to copy ~~move~~ it into the `omi` repo.
	- will explore making a sub-module that's shared in both repos in the future if > 2 changes are being made by Sahil..
	- (*Not possible to use git supported soft links to share with another computer*) But need some simlink mechanism to keep the files linked // need some way to sync their commit history as well - *currently will need to do this manually?*

## LLM Bioinformatics Training Pairs
`llm_bioinformatics_training_pairs_with_output.csv`
16/Jul/25 - flowchart -> questions

I generated these questions using chatGPT with the following prompt (_condensed 3 serial prompts into 1_):

```prompt
I am building an LLM to be used by biologists without bioinformatics background to run bioinformatic tools. The broad modality of my tools is listed with specific tools in brackets.
How would a biologist with metagenomic data at hand describe questions that each of the following bioinformatic tools would answer. Give me 3 questions for each modality.
- Annotated genome (Bakta | Prokka)
- Pangenomics (tmhg-finder)
- Metagenomic taxonomic profiling
- Read classification (SeqScreen)
- 16S taxonomic profiling

Please output this as a csv file. And include the typical output of the tool as well. Such as 
**“What genes are present in this genome, and what do they do?”**  
_(→ Functional annotation of coding sequences, gene product names, EC numbers, etc.)
```

TODO: 
- [ ] Add more nodes to this list or use the full flowchart. _This was only a starting point with a few key nodes to get started._

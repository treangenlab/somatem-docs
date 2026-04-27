# SeqScreen
[![Anaconda-Server Badge](https://anaconda.org/bioconda/seqscreen/badges/version.svg)](https://anaconda.org/bioconda/seqscreen)
[![Anaconda-Server Badge](https://anaconda.org/bioconda/seqscreen/badges/downloads.svg)](https://anaconda.org/bioconda/seqscreen)
[![Anaconda-Server Badge](https://anaconda.org/bioconda/seqscreen/badges/license.svg)](https://anaconda.org/bioconda/seqscreen)
[![Anaconda-Server Badge](https://anaconda.org/bioconda/seqscreen/badges/latest_release_date.svg)](https://anaconda.org/bioconda/seqscreen)

### Sequence of Interest Screening (SeqScreen) pipeline

Welcome to the Sequence of Interest Screening (SeqScreen) repo!

The **[SeqScreen wiki pages](https://gitlab.com/treangenlab/seqscreen/wikis/home)** have helpful instructions for installing the software and explaining its analytical components. 

**An Important Note for SeqScreen Users:** It is critical that the SeqScreen pipeline, as well as any customized final reporting guidelines that are developed to interpret SeqScreen outputs, be thoroughly tested before deploying in a sequence screening framework. It is your responsibility as a SeqScreen user to ensure that any conclusions drawn from its outputs are consistent with the latest regulations and best practices for your specific use case. Please reach out to Dr. Mike Nute <mn56@rice.edu> if you would like to discuss sequence screening options in more detail.


## Running the SeqScreen pipeline
The following command will run the SeqScreen pipeline in fast mode (default) on a Linux server:

```bash
seqscreen --fasta /Path/to/input.fasta --databases /Path/to/seqscreen_databases/ --working /Path/to/output_directory
```

The following command will run the SeqScreen pipeline in sensitive mode:

```bash
seqscreen --fasta /Path/to/input.fasta --sensitive --databases /Path/to/seqscreen_databases/ --working /Path/to/output_directory
```

The following command will run the SeqScreen pipeline in ont mode:

```bash
seqscreen --fasta /Path/to/input.fasta --ont --databases /Path/to/seqscreen_databases/ --working /Path/to/output_directory
```

The help command will display a list of all possible flags:

```bash
seqscreen --help
```


## Outputs of the SeqScreen pipeline

All outputs will be saved in the directory passed to the `--working` flag. There are various intermediate outputs created in during a pipeline run, but the final report files are saved in the `output_directory/report_generation/` directory.

One of the SeqScreen outputs is a tab-delimited report file. More details about the final report and the TSV header fields can be found [here](https://gitlab.com/treangenlab/seqscreen/wikis/09.-Report-Generation-Workflow).


## Overview of workflows

The pipeline can be broadly divided into five broad workflows:

1. Initialization: *Preprocessing and input validation*
2. SeqMapper: *Rapid alignment of the input queries against a custom database*
3. Protein and Taxonomic Identification: *Sensitive taxonomic classification of query sequence*
4. Functional Annotation: *Biological process and molecular function GO term predictions*
5. Final Report Generation: *Summarize findings in easy to parse report*

!<img src="https://gitlab.com/treangenlab/seqscreen/raw/master/figures/220823_SeqScreen_Workflow.png" width="500" height="970">


*Rev KLT 20-November-2024*

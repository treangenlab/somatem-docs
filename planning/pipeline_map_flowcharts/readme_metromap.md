Details how the flowcharts were created and used.

# metromap
using package : [nf-metro](https://github.com/pinin4fjords/nf-metro)

_notes copied and updated from [dev_notes.md](https://github.com/treangenlab/somatem/blob/main/docs/dev_notes.md#metro-map-nf-metro)_

## metro map: nf-metro
Update: 
- Using nf-metro to make a base chart from `flowchart_metro.mmd`, later edited by hand in Inkscape
- If > 3 tools are added and the pipeline needs to be changed significantly, it may be easier to create a new version starting from the `mmd` file

**Key versions:**
- v1.3 : Shortened / less wordy, tool name in newline ; pre-processing top to bottom
- Find v1.3.5 : edited by hand in prashant's local computer / box folder! 
  - fixed some alignment issues with the assembly branch etc.
- v1.3.6 : styled with tool names in green, and mono font (using python script: `archive/svg_colourize_text.py`)


- nf-metro: run with this ; need each branch to be labelled A -->|label| B
```bash
cd docs/somatem-docs/planning/flowcharts
micromamba activate nf-metro # activate the envelope

# render the metro map from example file
nf-metro render nf-metro/simple_pipeline.mmd -o nf-metro/simple_pipeline.svg --theme light

# render the actual metro map
nf-metro render flowchart_metro.mmd --theme light
```


_handy commands: code to add in .mmd_
```sh
# top level
%%metro title: nf-core/rnaseq
%%metro file: fastq_in | FASTQ
%%metro line: taxp | taxonomic profiling | #4CAF50

# within subgraphs
subgraph preprocessing [Pre-processing]
        %%metro exit: right | star_salmon, star_rsem, hisat2, bowtie2_salmon
        %%metro exit: bottom | pseudo_salmon, pseudo_kallisto

        %%metro entry: left | star_salmon, star_rsem, hisat2, bowtie2_salmon

        %%metro direction: TB

# between sections 
%% Inter-section edges
fastqc_filtered -->|star_salmon,star_rsem| star
...

```

- `metro validate` 
- `metro build`
- `metro publish`



# Archives

First iterations of the flowcharts are stored in the `archive` directory.
- `archive/Somatem_sketch-v1.2.jpg` is the first iteration of the flowchart drawn on the whiteboard.
- further versions were made with mermaid.js (and modified with gui at mermaid website)



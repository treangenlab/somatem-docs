What does "functional profiling for sequences of concern including pathogens" mean in SeqScreen?

Source: _This document was generated using [seqera AI chat](https://seqera.io/ask-ai/chat)_

In the context of **SeqScreen**, "functional profiling for sequences of concern including pathogens" refers to a comprehensive bioinformatics approach that goes beyond simple taxonomic identification to characterize DNA sequences based on their **biological functions** and **pathogenic potential**.

## Key Components:

### **1. Functions of Sequences of Concern (FunSoCs)**

SeqScreen uses a custom framework called **FunSoCs** - a curated set of 32 functional categories that describe specific roles sequences play in:

- **Microbial pathogenesis** (how pathogens cause disease)
- **Antibiotic resistance mechanisms**
- **Virulence factors** (toxins, adhesion, invasion)
- **Host immune evasion**
- **Countermeasure resistance**

### **2. What "Functional Profiling" Means:**

Rather than just identifying _what organism_ a sequence comes from, SeqScreen determines:

- **What the sequence does** (its biological function)
- **How it contributes to pathogenicity**
- **What mechanisms it uses to cause harm**
- **What cellular processes it affects**

### **3. Sequences of Concern Categories:**

SeqScreen identifies sequences involved in:

- **Cytotoxicity** (cell damage/death)
- **Adhesion** (pathogen attachment to host)
- **Invasion** (entering host cells)
- **Immune evasion** (avoiding host defenses)
- **Antibiotic resistance**
- **Toxin production**
- **Virulence regulation**

## **Why This Approach Matters:**

### **Beyond Taxonomic Classification:**

- Traditional tools identify _E. coli_ but can't distinguish between harmless _E. coli K-12_ and pathogenic _E. coli O157_
- SeqScreen identifies the **Shiga toxin** genes that make O157 dangerous

### **Novel Pathogen Detection:**

- Can identify pathogenic functions even in **unknown or engineered organisms**
- Detects functional markers of pathogenicity without needing exact taxonomic matches
- Useful for **synthetic biology screening** and **biosecurity**

### **Clinical Applications:**

- Identifies pathogenic sequences in **metagenomic samples**
- Detects **low-abundance pathogens** in clinical samples
- Provides **functional context** for understanding disease mechanisms

## **Technical Implementation:**

SeqScreen combines:

1. **Ensemble machine learning** models trained on curated pathogenic sequences
2. **Alignment-based tools** (DIAMOND, BLAST) for sequence similarity
3. **Gene Ontology (GO) terms** and UniProt annotations
4. **Expert curation** of pathogenic functions

## **Example Output:**

Instead of just reporting "bacterial sequence detected," SeqScreen provides:

- **Protein function**: "Botulinum toxin A"
- **FunSoC assignment**: "disable organ," "cytotoxicity"
- **Pathogenic mechanism**: Blocks neurotransmitter release
- **Taxonomic context**: _Clostridium botulinum_

This functional approach enables **precise pathogen characterization**, **biosecurity screening**, and **detection of emerging threats** based on their predicted biological functions rather than just their taxonomic identity.
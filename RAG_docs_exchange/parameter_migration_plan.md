# Parameter Migration Workflow Plan

This document describes the workflow for extracting tool parameters from README files and adding them to the Nextflow configuration.

## Workflow Overview

**Goal:** Extract parameter sections from tool README files and integrate them into the somatem pipeline configuration.

**Applies to:** Any tool documentation file in `githubs/` directory (e.g., Lemur, Kraken2, etc.)

---

## Step 1: Extract Parameter Section

### Action
Cut the `### Parameter descriptions` section from the tool README file.

### Source File Format
```
docs/somatem-docs/RAG_docs_exchange/githubs/<TOOL>_README.md
```

### Target File Format
```
docs/somatem-docs/RAG_docs_exchange/tool_parameters/<tool>_params.md
```

### Procedure
1. Open `<TOOL>_README.md`
2. Locate the `### Parameter descriptions` section heading
3. Identify the end of the section (usually the next `##` heading or end of file)
4. Cut the entire section from the README
5. Create the target file at `../tool_parameters/<tool>_params.md` if it doesn't exist
6. Paste the parameter section into the target file

### Example
**Source:** `docs/somatem-docs/RAG_docs_exchange/githubs/Lemur_README.md` (lines 65-113)
**Target:** `docs/somatem-docs/RAG_docs_exchange/tool_parameters/lemur_params.md`

---

## Step 2: Identify Parameters

### Action
Parse the extracted parameter file to identify all configurable parameters.

### Parameter Patterns to Look For
- Short form: `-i INPUT`, `-r RANK`
- Long form: `--input`, `--rank`, `--min-aln-len-ratio`
- Descriptions following the parameter names

### Output Format
Create a list of parameter names (long form preferred):
```
input
output
db-prefix
tax-path
num-threads
aln-score
rank
min-aln-len-ratio
...
```

---

## Step 3: Add to various nextflow Config files

### Action
Add identified parameters to various parameter files with tool name prefix. 
The parameter file depends on the tool category (e.g., taxonomic_profiling, assembly, etc.). 
Example: `conf/parameters/taxonomic_profiling.config` for `lemur` tool.

### Prefix Format
```
<tool>_<parameter_name>
```

Examples:
- `mm2-type` → `lemur_mm2-type`
- `input` → `lemur_input`
- `min-aln-len-ratio` → `lemur_min-aln-len-ratio`

### Config Section Location
Add under the appropriate params section in the appropriate config file (example: `conf/parameters/taxonomic_profiling.config` for `lemur` tool).

### Template Entry (Example)
```groovy
params {
    // <Tool Name> Parameters
    <tool>_<param1> = <default_value>
    <tool>_<param2> = <default_value>
    // ...
}
```

---

## File Paths Reference

| Component | Path |
|-----------|------|
| Source READMEs | `docs/somatem-docs/RAG_docs_exchange/githubs/` |
| Target Params | `docs/somatem-docs/RAG_docs_exchange/tool_parameters/` |
| Main Config | `nextflow.config` |
| Taxonomic Config | `conf/parameters/taxonomic_profiling.config` |
| Preprocessing Config | `conf/parameters/preprocessing.config` |
| Assembly Config | `conf/parameters/assembly_mags.config` |

---

## Tool Categories

| Category | Tools | Config File |
|----------|-------|-------------|
| Taxonomic Profiling | Lemur, Kraken2, Centrifuge | `conf/parameters/taxonomic_profiling.config` |
| Preprocessing | Chopper, NanoPlot | `conf/parameters/preprocessing.config` |
| Assembly/MAGs | AGB, CheckM2, Bakta | `conf/parameters/assembly_mags.config` |

---

## Checklist Template

- [ ] Step 1: Cut parameter section from README
- [ ] Step 2: Move to `../tool_parameters/<tool>_params.md`
- [ ] Step 3: Parse and list all parameters
- [ ] Step 4: Add to appropriate config file with `<tool>_` prefix
- [ ] Step 5: Verify no duplicates exist in config
- [ ] Step 6: Document default values if available

---

## Step 4: Wire Parameters to Module Config

### Action
Connect the prefixed parameters to the tool's module block in `conf/modules.config`.

### Location
Find the `withName: '<TOOL>'` block in `conf/modules.config`.

### Procedure
1. Locate the tool's module block (e.g., `withName: 'LEMUR'`)
2. Add parameter references to `ext.args` list
3. Format: `"--cli-option \${params.<tool>_<param>}"`

### Template
```groovy
withName: '<TOOL>' {
    ext.args = [
        "--<option1> \${params.<tool>_<param1>}",
        "--<option2> \${params.<tool>_<param2>}",
    ].join(' ')
}
```

### Example (Lemur)
```groovy
withName: 'LEMUR' {
    ext.args = [
        "--rank \${params.lemur_rank}",
        "--tax-path \${params.lemur_tax-path}",
        "--mm2-type \${params.lemur_mm2-type}",
    ].join(' ')
}
```

### Notes
- Use `\${}` syntax for variable interpolation in the config
- Only add parameters relevant to the pipeline workflow
- Keep existing parameters (e.g., `storeDir`, `ext.prefix`) intact

---

## Step 5: Verify No Duplicates

### Action
Check that no parameter names conflict with existing parameters in the config files.

### Procedure
1. Search the target config file for existing `<tool>_<param>` patterns
2. Check `nextflow.config` for any global params with the same name
3. Verify no naming collisions with other tools' parameters

### Commands
```bash
# Search for existing lemur parameters
grep -n "lemur_" conf/parameters/taxonomic_profiling.config
grep -n "lemur_" nextflow.config
```

### Resolution
If duplicates found:
- Rename parameter with more specific prefix (e.g., `lemur_align_mm2-type`)
- Or consolidate with existing parameter if functionally equivalent

---

## Step 6: Document Default Values

### Action
Record default values for each parameter from the tool documentation.

### Source
Extract defaults from:
- The `../tool_parameters/<tool>_params.md` file (parameter descriptions)
- Tool's `--help` output
- Tool's official documentation

### Target
Add defaults to the config file alongside each parameter:

```groovy
params {
    // Lemur Parameters
    lemur_rank = 'species'                              // Default: species
    lemur_mm2-type = 'map-ont'                          // Default: map-ont
    lemur_min-aln-len-ratio = 0.75                    // Default: 0.75
}
```

### Documentation Format
Include inline comments showing the default value:
```groovy
<tool>_<param> = <value>    // Default: <default_value> [<source>]
```

---

## Quick Reference

### File Order of Operations
1. `githubs/<TOOL>_README.md` → cut parameters
2. `tool_parameters/<tool>_params.md` → paste & reference
3. `conf/parameters/<category>.config` → add params with defaults
4. `conf/modules.config` → wire params to module

### Naming Convention
| Component | Format | Example |
|-----------|--------|---------|
| Tool prefix | lowercase | `lemur` |
| Parameter | original name | `mm2-type` |
| Full param | `<tool>_<param>` | `lemur_mm2-type` |

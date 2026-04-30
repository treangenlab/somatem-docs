# Parameter Migration Automation

This directory contains tools for automating the parameter migration workflow.

## Files

- `parameter_migration_automation.py` - Main automation script
- `README_automation.md` - This file
- `parameter_migration_plan.md` - Manual workflow documentation

## Usage

### Basic Usage
```bash
cd docs/somatem-docs/RAG_docs_exchange
python parameter_migration_automation.py <tool_name>
```

### Example
```bash
# Migrate lemur parameters
python parameter_migration_automation.py lemur

# Migrate kraken2 parameters  
python parameter_migration_automation.py kraken2
```

## What It Does

1. **Extracts** parameter section from `<tool>_README.md`
2. **Parses** CLI options and their metadata
3. **Creates** `<tool>_params.md` with extracted parameters
4. **Generates** config entries for Nextflow
5. **Creates** module wiring snippets

## Output Files

For each tool, the script creates:

- `tool_parameters/<tool>_params.md` - Extracted parameter documentation
- `tool_parameters/<tool>_config_entries.txt` - Nextflow config entries
- `tool_parameters/<tool>_module_wiring.txt` - modules.config wiring

## Integration Workflow

1. **Run automation** for a tool
2. **Review generated files** for accuracy
3. **Copy config entries** to appropriate config file
4. **Copy module wiring** to modules.config
5. **Test** the integration

## Features

- **Automatic parameter parsing** from CLI documentation
- **Type inference** for different parameter types
- **Default value extraction** from documentation
- **Memory size conversion** (e.g., 500M → bytes)
- **Boolean flag handling** with conditional inclusion
- **Error handling** for missing files or sections

## Limitations

- Requires standardized parameter documentation format
- May need manual review for complex parameter patterns
- Config file placement must be done manually

## Future Enhancements

- **Direct config file modification** (instead of generating snippets)
- **Batch processing** of multiple tools
- **Parameter validation** against tool help output
- **Integration tests** for generated configurations

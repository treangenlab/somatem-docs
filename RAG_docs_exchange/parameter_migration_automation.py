#!/usr/bin/env python3
"""
Parameter Migration Automation Tool

Automates the extraction and migration of tool parameters from README files
to Nextflow configuration files.

Usage:
    python parameter_migration_automation.py <tool_name>

Author: Windsurf AI, SWE-1.5
"""

import re
import os
import sys
from pathlib import Path
from typing import List, Dict, Tuple, Optional

class ParameterExtractor:
    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
        self.githubs_dir = base_dir / "githubs"
        self.tool_params_dir = base_dir / "tool_parameters"
        
    def extract_parameter_section(self, tool_name: str) -> Optional[str]:
        """Extract parameter section from tool README"""
        readme_path = self.githubs_dir / f"{tool_name}_README.md"
        
        if not readme_path.exists():
            print(f"Error: README file not found: {readme_path}")
            return None
            
        with open(readme_path, 'r') as f:
            content = f.read()
            
        # Find parameter section using regex pattern
        # Matches any line with one or more '#' followed by any text containing 'parameter' (case-insensitive)
        param_match = re.search(r'^#+.*parameter.*$', content, re.MULTILINE | re.IGNORECASE)
        if not param_match:
            print(f"Error: Parameter section not found in {readme_path}")
            return None
        
        param_start = param_match.start()
            
        # Find next section or end of file
        next_section = content.find("\n##", param_start + 1)
        if next_section == -1:
            param_section = content[param_start:]
        else:
            param_section = content[param_start:next_section]
            
        return param_section.strip()
    
    def parse_parameters(self, param_section: str) -> List[Dict]:
        """Parse CLI parameters from the extracted section"""
        parameters = []
        
        # Pattern to match parameter definitions (more flexible)
        # Examples: -i INPUT, --input INPUT, --option {choices}, --flag
        # Also matches: |--db| $EMU_DATABASE_DIR| path to emu database; etc.
        param_pattern = r'(?:^\s*|.*?)(-\w|--[\w-]+)(?:\s+[\w-]+)?(?:\s+\{([^}]+)\})?(?:\s*\|\s*[^|]+)?\s*$'
        
        lines = param_section.split('\n')
        current_param = None
        
        for line in lines:
            line = line.strip()
            
            # Skip empty lines and section headers
            if not line or line.startswith('#') or line.startswith('```'):
                continue
                
            # Check if line contains a parameter definition
            param_match = re.match(param_pattern, line)
            if param_match:
                # Extract parameter info
                cli_option = param_match.group(1)
                choices = param_match.group(2)
                
                # Clean up parameter name (remove dashes, convert to underscores)
                param_name = cli_option.lstrip('-').replace('-', '_')
                
                param_info = {
                    'cli_option': cli_option,
                    'param_name': param_name,
                    'choices': choices,
                    'description': '',
                    'default_value': None,
                    'param_type': self._infer_param_type(choices)
                }
                
                parameters.append(param_info)
                current_param = param_info
            elif current_param and line:
                # This is likely a description line
                if current_param['description']:
                    current_param['description'] += ' ' + line
                else:
                    current_param['description'] = line
                    
                # Extract default value from description
                default_match = re.search(r'\[default:\s*([^\]]+)\]', line)
                if default_match:
                    current_param['default_value'] = default_match.group(1).strip()
                    
        return parameters
    
    def _infer_param_type(self, choices: Optional[str]) -> str:
        """Infer parameter type from choices or patterns"""
        if choices:
            # Enumerated choices - string type
            return 'string'
        return 'string'  # Default to string, can be refined
    
    def generate_config_entries(self, tool_name: str, parameters: List[Dict]) -> str:
        """Generate Nextflow config entries"""
        config_lines = [f"    // {tool_name.title()} Parameters"]
        
        for param in parameters:
            param_name = f"{tool_name}_{param['param_name']}"
            default = param['default_value'] or '""'
            
            # Handle special cases for default values
            if default == '""':
                config_line = f'    {param_name} = ""    // Default: empty string'
            elif default.isdigit():
                config_line = f'    {param_name} = {default}    // Default: {default}'
            elif 'M' in default:  # Handle memory sizes like 500M
                # Convert to bytes
                size_mb = int(default.replace('M', ''))
                size_bytes = size_mb * 1024 * 1024
                config_line = f'    {param_name} = {size_bytes:,}    // Default: {default}'
            else:
                config_line = f'    {param_name} = "{default}"    // Default: {default}'
                
            config_lines.append(config_line)
            
        return '\n'.join(config_lines)
    
    def generate_module_wiring(self, tool_name: str, parameters: List[Dict]) -> str:
        """Generate modules.config wiring"""
        lines = [
            f"withName: '{tool_name.upper()}' {{",
            "    ext.args = ["
        ]
        
        for param in parameters:
            param_name = f"{tool_name}_{param['param_name']}"
            cli_option = param['cli_option']
            
            # Handle boolean flags vs value parameters
            if not param['default_value'] or param['default_value'] == '""':
                # Boolean flag
                lines.append(f'        params.{param_name} ? "--{cli_option}" : "",')
            else:
                # Value parameter
                lines.append(f'        "--{cli_option} ${{params.{param_name}}}",')
                
        lines.extend([
            '    ].findAll { x -> x != "" }.join(\' \')',
            '}'
        ])
        
        return '\n'.join(lines)
    
    def migrate_tool(self, tool_name: str) -> bool:
        """Complete migration workflow for a tool"""
        print(f"Migrating parameters for {tool_name}...")
        
        # Step 1: Extract parameter section
        param_section = self.extract_parameter_section(tool_name)
        if not param_section:
            return False
            
        # Step 2: Parse parameters
        parameters = self.parse_parameters(param_section)
        if not parameters:
            print(f"No parameters found for {tool_name}")
            return False
            
        print(f"Found {len(parameters)} parameters")
        
        # Step 3: Create parameter file
        param_file = self.tool_params_dir / f"{tool_name}_params.md"
        with open(param_file, 'w') as f:
            f.write(f"# {tool_name.title()} Parameters\n\n")
            f.write("### Parameter descriptions\n\n")
            f.write(param_section)
            
        print(f"Created {param_file}")
        
        # Step 4: Generate config entries
        config_entries = self.generate_config_entries(tool_name, parameters)
        config_file = self.tool_params_dir / f"{tool_name}_config_entries.txt"
        with open(config_file, 'w') as f:
            f.write(config_entries)
            
        print(f"Generated config entries in {config_file}")
        
        # Step 5: Generate module wiring
        module_wiring = self.generate_module_wiring(tool_name, parameters)
        module_file = self.tool_params_dir / f"{tool_name}_module_wiring.txt"
        with open(module_file, 'w') as f:
            f.write(module_wiring)
            
        print(f"Generated module wiring in {module_file}")
        
        return True

def main():
    if len(sys.argv) != 2:
        print("Usage: python parameter_migration_automation.py <tool_name>")
        print("Example: python parameter_migration_automation.py lemur")
        sys.exit(1)
        
    tool_name = sys.argv[1].lower()
    base_dir = Path(__file__).parent
    
    extractor = ParameterExtractor(base_dir)
    success = extractor.migrate_tool(tool_name)
    
    if success:
        print(f"\n✅ Migration completed for {tool_name}")
        print(f"📁 Check the tool_parameters directory for generated files")
    else:
        print(f"\n❌ Migration failed for {tool_name}")
        sys.exit(1)

if __name__ == "__main__":
    main()

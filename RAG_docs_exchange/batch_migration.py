#!/usr/bin/env python3
"""
Batch Parameter Migration Tool

Process multiple tools at once for parameter migration.

Author: Windsurf AI, SWE-1.5
"""

import os
import re
import sys
from pathlib import Path
from parameter_migration_automation import ParameterExtractor
# from parameter_migration_automation import migrate_tool

def find_available_tools(base_dir: Path) -> list:
    """Find all tools with README files that haven't been migrated yet"""
    githubs_dir = base_dir / "githubs"
    tool_params_dir = base_dir / "tool_parameters"
    tools = []
    already_migrated = []
    
    if githubs_dir.exists():
        for file in githubs_dir.glob("*_README.md"):
            tool_name = file.stem.replace("_README", "")
            
            # Check if parameter file already exists
            param_file = tool_params_dir / f"{tool_name.lower()}_params.md"
            if param_file.exists():
                already_migrated.append(tool_name)
            else:
                tools.append(tool_name)
    
    # Print already migrated tools
    if already_migrated:
        print(f"Already migrated ({len(already_migrated)}): {', '.join(sorted(already_migrated))}")
    
    return sorted(tools)

def batch_migrate(tool_names: list = None):
    """Migrate multiple tools"""
    base_dir = Path(__file__).parent
    extractor = ParameterExtractor(base_dir)
    
    if tool_names is None:
        tool_names = find_available_tools(base_dir)
        
    print(f"Found tools: {', '.join(tool_names)}")
    
    results = {}
    no_section = []
    no_params = []
    successful = []
    
    for tool in tool_names:
        success = extractor.migrate_tool(tool)
        results[tool] = success
        
        if success:
            successful.append(tool)
        else:
            # Categorize failure type
            readme_path = extractor.githubs_dir / f"{tool}_README.md"
            if not readme_path.exists():
                continue  # Already filtered out earlier
                
            with open(readme_path, 'r') as f:
                content = f.read()
                
            param_match = re.search(r'^#+.*parameter.*$', content, re.MULTILINE | re.IGNORECASE)
            if not param_match:
                no_section.append(tool)
            else:
                no_params.append(tool)
        
    # Summary
    print(f"\n{'='*50}")
    print("MIGRATION SUMMARY")
    print(f"{'='*50}")
    
    if successful:
        print(f"✅ Successful ({len(successful)}): {', '.join(successful)}")
    if no_section:
        print(f"⚠️  No parameter section ({len(no_section)}): {', '.join(no_section)}")
    if no_params:
        print(f"⚠️  No parameters found ({len(no_params)}): {', '.join(no_params)}")
        
    return len(no_section) + len(no_params) == 0

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Batch migrate tool parameters")
    parser.add_argument("tools", nargs="*", help="Specific tools to migrate (default: all)")
    parser.add_argument("--list", action="store_true", help="List available tools")
    
    args = parser.parse_args()
    
    base_dir = Path(__file__).parent
    
    if args.list:
        tools = find_available_tools(base_dir)
        print("Available tools:")
        for tool in tools:
            print(f"  - {tool}")
        return
        
    success = batch_migrate(args.tools if args.tools else None)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()

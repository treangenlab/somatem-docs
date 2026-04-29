#! /usr/bin/env python3
# This script colourizes text in an SVG file : picks the second line of multiline text (index 1)
# Use case : somatem_metromap_v1.3.5
# Run in micromamba environment 'utils' : micromamba run -n utils python svg_colourize_text.py
# Author: Gemini AI pro ; 19/Mar/26
# Edits: PK : 19/Mar/26

import lxml.etree as ET

file_path = r"C:\Users\ppres\Box\TreangenLab_PK\files\flowchart"
input_file = "somatem_metromap_v1.3.5.svg"
output_file = "somatem_metromap_v1.3.5_colored.svg"

# Load your SVG
tree = ET.parse(file_path + "\\" + input_file)
root = tree.getroot()
ns = {'svg': 'http://www.w3.org/2000/svg'}

# Find all text elements
for text in root.xpath('//svg:text', namespaces=ns):
    tspans = text.xpath('./svg:tspan', namespaces=ns)
    
    # If there is more than one line (tspan)
    if len(tspans) > 1:
        # Target the second line (index 1) : modify to green, Liberation Mono
        line_b = tspans[1]
        line_b.set("style", "fill:#188038; font-family:Liberation Mono;") 

# Save the result
tree.write(file_path + "\\" + output_file, encoding="utf-8", xml_declaration=True)
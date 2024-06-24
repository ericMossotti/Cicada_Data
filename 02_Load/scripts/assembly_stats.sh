#!/bin/bash

# Write file with Python package function, assembly_stats
python assembly_stats "$fasta_file" > "$summary_stats"

printf "%s" "$(<"$summary_stats")"

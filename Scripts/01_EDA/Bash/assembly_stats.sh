#!/bin/bash

# ---- Bash script is run from within a Python environment

# Variables passed to the bash script
#fasta_file="$1"
#summary_stats="$2"

# Write file with Python package function, assembly_stats
python assembly_stats "$fasta_file" > "$summary_stats"

printf "%s" "$(<"$summary_stats")"

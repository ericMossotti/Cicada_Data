# Cicada Data

This project demonstrates another way of reporting statistical analysis results while independently reproducing DNA Zoo's summary table on the 17-year cicada genome assembly.

## Objective

To reproduce DNA Zoo's summary table on the 17-year cicada and provide an accessible data analysis (DA) pipeline, documenting every data processing step.

## Pipeline Overview

The analysis pipeline consists of four main stages:

1. Extract
2. Transform
3. Load
4. Present

## Key Features

- Reproduces genome assembly statistics for the 17-year cicada
- Implements an ETL (Extract, Transform, Load) pipeline
- Uses Python, R, and Bash
- Provides step-by-step documentation of the data processing

## Getting Started

1. Clone the index.qmd and styles.scss files from this repository
2. Ensure you have Python, R, and Bash installed
3. Install required packages
4. Run all of the code chunks in the index.qmd file to reproduce the analysis

## File Structure

- `01_Extract/`: Data extraction scripts and raw data
- `02_Transform/`: Data transformation scripts and intermediate data
- `03_Load/`: Data loading scripts
- `04_Present/`: Data presentation scripts and final outputs
- `index.qmd`: Quarto markdown document containing the analysis

## Data Source

All data used in this project is freely available from a public database hosted by DNA Zoo.

## Author

Eric Mossotti (ecmossotti@gmail.com)

## License

This project is licensed under CC BY-SA.

## Acknowledgements

This work builds upon the original research by DNA Zoo and the assembly_stats Python package developed by Mike Trizna.

For more details, please refer to the `index.qmd` file in this repository.

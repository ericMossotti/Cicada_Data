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

## Getting Started with Reproducing this Analysis

1. Open your IDE for working on quarto projects
2. In your IDE terminal window (such as Rstudio or VScode):
   `cd ~/desired_projects_folder`
3. Again in terminal:
   `git clone https://github.com/ericMossotti/Cicada_Data.git`
4. Within the cloned repository folder: 
   `cd ~/desired_folder/Cicada_Data`
   `quarto create project`
   `pip install -r requirements.txt`
5. Open the file located at `renv/activate.R`, then `Run` it
6. In IDE console window:
   Run `renv::restore()`, then likely type `y` for installing packages
7. Open the `index.qmd` file
8. Switch to the `Source` view
9. Go to line 296 (assuming nothing else was changed) and change the code that reads `{.bash}` or `bash`  to `{bash}`. Or simply search `bash` using IDE find tools to find this code.
10. Remain in index.qmd
11. `Run All` in your IDE to run all code chunks.

## File Structure

- `01_Extract/`: Data extraction scripts and raw data
- `02_Transform/`: Data transformation scripts and intermediate data
- `03_Load/`: Data loading scripts
- `04_Present/`: Data presentation scripts and final outputs
- `index.qmd`: Quarto markdown document containing the analysis

## Data Source

All data used in this project is freely available from a public database hosted by DNA Zoo.

## Author

Eric Mossotti

## License

This project is licensed under CC BY-SA.

## Acknowledgements

This work builds upon the original research by DNA Zoo and the assembly_stats Python package developed by Mike Trizna.

For more details, please refer to the `index.qmd` file in this repository.

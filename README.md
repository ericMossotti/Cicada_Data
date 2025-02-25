# Cicada Data

[Full Publication Link](https://eric-mossotti.quarto.pub/cicada_data/)

This project demonstrates another way of reporting statistical analysis results while independently reproducing DNA Zoo's summary table on the 17-year cicada genome assembly.

## Objective

To reproduce DNA Zoo's summary table on the 17-year cicada and provide an accessible data analysis (DA) pipeline, documenting every data processing step.

## Pipeline Overview

The analysis pipeline consists of four main stages:

1.  Extract
2.  Transform
3.  Load
4.  Present

## Key Features

-   Reproduces genome assembly statistics for the 17-year cicada
-   Implements an ETL (Extract, Transform, Load) pipeline
-   Uses Python, R, and Bash
-   Provides step-by-step documentation of the data processing

## Getting Started with Reproducing this Analysis

First, have R and Python installed globally on your system.

In Rstudio:

Go to: `File`

Click `New Project`

Select `Version Control`

Paste this repo's code link

in R console:

``` r
install.packages("renv")
```

``` r
renv::restore()
```

``` r
renv::snapshot()
```

Follow prompts to install R and Python packages during these steps where necessary. If doing this without an R console, you might be able to run that R code in R-code chunk(s) within the `index.qmd` file of the project.

## File Structure

-   `01_Extract/`: Data extraction scripts and raw data
-   `02_Transform/`: Data transformation scripts and intermediate data
-   `03_Load/`: Data loading scripts
-   `04_Present/`: Data presentation scripts and final outputs
-   `index.qmd`: Quarto markdown document containing the analysis

## Data Source

All data used in this project is freely available from a public database hosted by DNA Zoo.

## Author

Eric Mossotti

## License

This project is licensed under CC BY-SA.

## Acknowledgements

This work builds upon the original research by DNA Zoo and the assembly_stats Python package developed by Mike Trizna.

For more details, please refer to the `index.qmd` file in this repository.

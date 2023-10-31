# CardGen

A simple tool for generating ready-to-print cards for game betatesting. This script converts source TSV file (CSV with tabs used as separators) to a PDF.

## Required packages

`pdftk`, `inkscape` and `python3` (including library `svgwrite`)

## How to run it

1. Prepare your input TSV files and name them coresponding to their meaning (for example `Hero.tsv` for a table of hero cards),
2. run the script `generovani.sh` with input file names as arguments,
3. print the output file `output.pdf` with 16 pages on a side and with option "Fit to printable area".

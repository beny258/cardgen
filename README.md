# CardGen

A simple tool for generating ready-to-print cards for game betatesting. This script converts source TSV file (CSV with tabs used as separators) to a PDF.

## Required packages

`pdftk`, `inkscape` and `python3` (including library `svgwrite` and `unidecode`)

## How to run it

1. Prepare your input TSV files and name them coresponding to their meaning (for example `Hero.tsv` for a table of hero cards),
2. you can optionally modify the input format in `auxs/input_format.py`,
3. run the script `cardgen.sh` with input file names as arguments,
4. print the output file `output.pdf` with 16 pages on a side and with option "Fit to printable area".

You must run the script from the script folder. The filepaths in arguments must be relative.

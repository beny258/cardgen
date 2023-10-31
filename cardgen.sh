version=1.1

removeauxfiles=true
showonlyhelp=false

while getopts n? flag
do
    case "${flag}" in
        n) removeauxfiles=false;;
        ?) showonlyhelp=true;;
    esac
done

shift $((OPTIND-1))

echo "Script for card generation."
echo "Version ${version}"
echo "Needed packages: python3 (including library svgwrite), pdftk, inkscape"
echo "Use option -n for keeping the temporary files."
echo "Default input file name is 'cards.tsv'. Add arguments to change that."

if [ $showonlyhelp = false ]; then
    echo "--------------------------------------------------------------"
    
    cd auxs
    mkdir -p cards_svg

    echo "Generating SVG files."
    python3 generate_svg.py $@

    cd cards_svg

    echo "Converting to PDF."
    inkscape -b "#ffffff" --export-type="pdf" `find z_*`

    echo "Combining to a single file."
    pdftk `find *.pdf` cat output ../output.pdf

    cd ..

    if [ $removeauxfiles = true ]; then
        echo "Deleting auxiliary files."
        rm -rf cards_svg
    fi

    cd ..

    echo "Done."
fi

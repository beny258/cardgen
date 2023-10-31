version=1.0a

removeauxfiles=true
showonlyhelp=false

while getopts n? flag
do
    case "${flag}" in
        n) removeauxfiles=false;;
        ?) showonlyhelp=true;;
    esac
done

echo "Skript pro generování karet pro hru Stezkoversum."
echo "Verze ${version}"
echo "Nutné balíčky: python3 (s knihovnou svgwrite), pdftk, inkscape"
echo "Použijte možnost -n pro zachování pomocných souborů."
echo "Název vstupního CSV souboru musí být karty.csv."
echo "--------------------------------------------------------------"

if [ $showonlyhelp = false ]; then
    mkdir -p karty_aux

    echo "Generuji SVG karty."
    python3 generovani.py

    cd karty_aux

    echo "Převádím do PDF."
    inkscape -b "#ffffff" --export-type="pdf" `find z_*`

    echo "Sjednocuji do jediného souboru."
    pdftk `find *.pdf` cat output ../karty.pdf

    cd ..

    if [ $removeauxfiles = true ]; then
        echo "Mažu pomocné soubory."
        rm -rf karty_aux
    fi

    echo "Hotovo. Soubor karty.pdf vygenerován."
fi

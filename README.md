Postup pro automatické generování grafiky na tisk karet:

1. stáhni si soubory `generovani.sh` a `generovani.py`
2. do stejné složky ulož karty k tisku pod názvem `karty.csv` (dělení tabulátorem, první řádek je hlavička)
3. v terminálu spusť skript `generovani.sh` (musíš mít na svém stroji balíčky pdftk, inkscape, python3 s knihovnou svgwrite)
4. vygenerovaný soubor `karty.pdf` vytiskni jednostranně barevně s šestnácti kartami na jedné stránce a s možností "Fit to printable area"

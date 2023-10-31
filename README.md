Postup pro automatické generování grafiky na tisk karet:

1. stáhni si soubory `generovani.sh` a `generovani.py` (musí být ve stejném adresáři)
2. připrav si soubory k tisku ve formátu `.tsv` a pojmenuj je podle typu karet (například `Hero.tsv`)
3. v terminálu spusť skript `generovani.sh` a do argumentu přidej názvy vstupních souborů (musíš mít na svém stroji balíčky pdftk, inkscape, python3 s knihovnou svgwrite)
4. vygenerovaný soubor `output.pdf` vytiskni jednostranně s šestnácti kartami na jedné stránce a s možností "Fit to printable area"

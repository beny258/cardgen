import csv
import svgwrite
import sys
from unidecode import unidecode

DEFAULT_INPUT_FILE_NAME = "cards.tsv"
DEFAULT_INPUT_TABLE_NAME = "".join(DEFAULT_INPUT_FILE_NAME.split('.')[:-1])

HEADER_ROWS_COUNT = 2
INPUT_FORMAT = "nahcb__"
# n = name
# c = class
# a = attack
# h = health
# b = ability (effect)
# t = tribe
# e = edition
# _ = unused column


def format_row(row):
    name, card_class, attack, health, ability, tribe, edition = ""
    row_list = list(row)
    for i, mark in enumerate(INPUT_FORMAT):
        if i >= len(row_list):
            break
        value = row_list[i]
        if mark == 'n':
            name = value
        elif mark == 'c':
            card_class = value
        elif mark == 'a':
            attack = value
        elif mark == 'h':
            health = value
        elif mark == 'b':
            ability = value
        elif mark == 't':
            tribe = value
        elif mark == 'e':
            edition = value
    return name, card_class, attack, health, ability, tribe, edition
    

def create_svg_card(name, card_class, attack, health, ability, tribe, edition, table_name):
    # Set the size of the SVG card
    card_width = 74  # mm
    card_height = 105   # mm

    # Create a new SVG drawing
    normalized_name = unidecode(name.replace(" ", "_"))
    normalized_table_name = unidecode(table_name.replace(" ", "_"))
    dwg = svgwrite.Drawing(filename=f"cards_svg/z_{normalized_table_name}_{normalized_name}.svg", size=(f"{card_width}mm", f"{card_height}mm"))

    # Define styles for text and other elements
    title_style = "font-size: 12pt; font-weight: bold;"
    attribute_style = "font-size: 10pt; font-weight: bold;"
    ability_style = "font-size: 10pt; shape-inside:url(#rectAbility)"

    # Add card name
    dwg.add(dwg.text(name, insert=(5, 25), fill='black', style=title_style))

    # Add card class and other info
    card_info = ""
    card_info += (" - " if card_info != "" and table_name != "" else "") + table_name
    card_info += (" - " if card_info != "" and card_class != "" else "") + card_class
    card_info += (" - " if card_info != "" and edition != "" else "") + edition
    card_info += (" - " if card_info != "" and tribe != "" else "") + tribe
    dwg.add(dwg.text(card_info, insert=(5, 45), fill='black', style=attribute_style))

    # Add attack and health information
    attack_health = ""
    attack_health += (" / " if attack_health != "" and attack != "" else "") + f"{attack}"
    attack_health += (" / " if attack_health != "" and health != "" else "") + f"{health}"
    dwg.add(dwg.text(attack_health, insert=(5, 65), fill='black', style=attribute_style))

    # Add ability information (if available)
    if ability:
        # Create a rectangle to constrain the ability text
        rect = dwg.rect(insert=(5, 85), size=(260, 300), fill="none", stroke="none", id="rectAbility")
        dwg.add(rect)

        dwg.add(dwg.text(ability, fill='black', style=ability_style))

    # Save the SVG file
    dwg.save()


def generate_svg_cards(csv_file):
    table_name = "".join(csv_file.split('.')[:-1])
    if table_name == "":  # in case input file has no sufix
        table_name = csv_file
    card_count = 0
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        card_reader = csv.reader(csvfile, delimiter='\t')
        for _ in range(HEADER_ROWS_COUNT):
            next(card_reader)  # skip the header rows
        for row in card_reader:
            name, card_class, attack, health, ability, tribe, edition = format_row(row)
            create_svg_card(name, card_class, attack, health, ability, tribe, edition, table_name if table_name != DEFAULT_INPUT_TABLE_NAME else "")
            card_count += 1
    return card_count


def main():
    csv_database = [DEFAULT_INPUT_FILE_NAME]
    if (len(sys.argv) > 1):
        csv_database = sys.argv[1:]
    generated_card_count = 0
    for csv_table in csv_database:
        generated_card_count += generate_svg_cards(csv_table)
    print("Generated", generated_card_count, "cards from total of", len(csv_database), "input files.")


if __name__ == "__main__":
    main()

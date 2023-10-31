import csv
import svgwrite
import sys
from unidecode import unidecode

def create_svg_card(name, card_class, attack, health, ability, table_name):
    # Set the size of the SVG card
    card_width = 74  # mm
    card_height = 105   # mm

    # Create a new SVG drawing
    normalized_name = unidecode(name.replace(" ", "_"))
    normalized_table_name = unidecode(table_name.replace(" ", "_"))
    dwg = svgwrite.Drawing(filename=f"cards_aux/z_{normalized_table_name}_{normalized_name}.svg", size=(f"{card_width}mm", f"{card_height}mm"))

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
    card_count = 0
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        card_reader = csv.reader(csvfile, delimiter='\t')
        next(card_reader)  # Skip header row
        next(card_reader)  # Skip second header row
        for row in card_reader:
            name, attack, health, card_class, ability, _, _ = row
            create_svg_card(name, card_class, attack, health, ability, table_name if table_name != "karty" else "")
            card_count += 1
    return card_count

if __name__ == "__main__":
    csv_database = ["cards.tsv"]
    if (len(sys.argv) > 1):
        csv_database = sys.argv[1:]
    generated_card_count = 0
    for csv_table in csv_database:
        generated_card_count += generate_svg_cards(csv_table)
    print("Generated", generated_card_count, "cards from total of", len(csv_database), "input files.")

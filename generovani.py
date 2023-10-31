import csv
import svgwrite
from unidecode import unidecode

def create_svg_card(name, card_class, edition, tribe, attack, health, ability):
    # Set the size of the SVG card
    card_width = 74  # mm
    card_height = 105   # mm

    # Create a new SVG drawing
    normalized_name = unidecode(name.replace(" ", "_"))
    dwg = svgwrite.Drawing(filename=f"karty_aux/z_{normalized_name}.svg", size=(f"{card_width}mm", f"{card_height}mm"))

    # Define styles for text and other elements
    title_style = "font-size: 12pt; font-weight: bold;"
    attribute_style = "font-size: 10pt; font-weight: bold;"
    ability_style = "font-size: 10pt; shape-inside:url(#rectAbility)"

    # Add card name
    dwg.add(dwg.text(name, insert=(5, 25), fill='black', style=title_style))

    # Add card class, edition, and tribe
    card_info = f"{card_class} - {edition} - {tribe}"
    dwg.add(dwg.text(card_info, insert=(5, 45), fill='black', style=attribute_style))

    # Add attack and health information
    attack_health = f"{attack} / {health}"
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
    card_count = 0
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        card_reader = csv.reader(csvfile, delimiter='\t')
        next(card_reader)  # Skip header row
        for row in card_reader:
            name, card_class, edition, tribe, attack, health, ability, image, char = row
            create_svg_card(name, card_class, edition, tribe, attack, health, ability)
            card_count += 1
    return card_count

if __name__ == "__main__":
    csv_database = "karty.csv"
    generated_card_count = generate_svg_cards(csv_database)
    print("Vygenerováno", generated_card_count, "karet.")

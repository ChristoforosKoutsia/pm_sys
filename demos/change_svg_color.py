import os

# Just a simple script to create svgs with new color

def change_svg_color(input_path, output_path, original_color, new_color):
    # Load the SVG content from the input file
    with open(input_path, 'r') as f:
        svg_content = f.read()

    # Modify the SVG content to replace the original_color with new_color
    modified_svg = svg_content.replace(original_color, new_color)

    # Save the modified SVG to the output file
    with open(output_path, 'w') as f:
        f.write(modified_svg)

def process_folder(input_folder, output_folder, original_color, new_color):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    files = os.listdir(input_folder)

    # Process each SVG file
    for file_name in files:
        if file_name.endswith('.svg'):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)
            change_svg_color(input_path, output_path, original_color, new_color)

if __name__ == "__change_svg_color__":
    input_folder_path = "../pm_sys/ui/img/feather"
    output_folder_path = "../pm_sys/ui/img/feather_dark"
    new_color = "#d0d0dc"  # Replace with the desired new color in hexadecimal format
    original_color = "currentColor"

    process_folder(input_folder_path, output_folder_path, original_color, new_color)
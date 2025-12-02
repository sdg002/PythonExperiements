def create_svg_line(file_path):
    """Creates an SVG file with a simple line."""
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200">
        <line x1="10" y1="10" x2="190" y2="190" stroke="black" stroke-width="2"/>
    </svg>"""

    with open(file_path, "w") as file:
        file.write(svg_content)

    print(f"SVG file created at: {file_path}")


if __name__ == "__main__":
    output_file = "simple_line.svg"
    create_svg_line(output_file)

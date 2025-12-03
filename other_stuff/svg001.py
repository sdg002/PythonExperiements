"""
This script creates an SVG file with a simple line using the svgwrite package.
"""
import svgwrite


def create_svg_line_with_svgwrite(file_path):
    """Creates an SVG file with a simple line using the svgwrite package."""
    # Create an SVG drawing object
    dwg = svgwrite.Drawing(file_path, size=("200px", "120px"))

    # Add a line to the drawing
    width = 190
    height = 100
    dwg.add(dwg.line(start=(10, 10), end=(width, height),
            stroke=svgwrite.rgb(0, 0, 0, '%'), stroke_width=2))
    dwg.add(dwg.line(start=(20, 10), end=(width-10, height-10),
            stroke=svgwrite.rgb(0, 0, 0, '%'), stroke_width=2))
    dwg.add(dwg.line(start=(10, height), end=(height, 10),
            stroke=svgwrite.rgb(0, 0, 0, '%'), stroke_width=2))

    # Save the SVG file
    dwg.save()
    print(f"SVG file created at: {file_path}")


if __name__ == "__main__":
    OUTPUT_FILE = "simple_line_with_svgwrite.svg"
    create_svg_line_with_svgwrite(OUTPUT_FILE)

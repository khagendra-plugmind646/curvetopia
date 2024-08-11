import os
import numpy as np
import matplotlib.pyplot as plt
from read_csv import read_csv
from svg_to_png import polylines2svg
from identify_shapes import identify_circle, identify_line
from detect_symmetry import detect_symmetry
from complete_curve import complete_curve

def plot(paths_XYs, output_file=None):
    plt.figure(figsize=(10, 10))
    for path_XYs in paths_XYs:
        for XY in path_XYs:
            plt.plot(XY[:, 0], XY[:, 1], marker='o')
    plt.title('Beautified Doodles')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.gca().set_aspect('equal', adjustable='box')
    if output_file:
        plt.savefig(output_file)
        print(f"Final plot saved to {output_file}")
    else:
        plt.show()

def process_csv(csv_path):
    try:
        # Read the CSV data
        paths_XYs = read_csv(csv_path)
        
        # Check if data was read correctly
        if not paths_XYs:
            print(f"No data found in {csv_path}")
            return

        # Process each shape path
        for path_XYs in paths_XYs:
            for XY in path_XYs:
                # Detect symmetry
                if detect_symmetry(XY):
                    print("Symmetry detected in shape.")
                
                # Complete curve if shape has fewer than 100 points
                if XY.shape[0] < 100:
                    XY = complete_curve(XY)

        # Plot the shapes
        final_png_path = csv_path.replace('.csv', '_processed_plot.png')
        plot(paths_XYs, output_file=final_png_path)

        # Generate SVG path
        svg_path = csv_path.replace('.csv', '.svg')
        polylines2svg(paths_XYs, svg_path)
        print(f"SVG saved to {svg_path}")

    except Exception as e:
        print(f"Error processing {csv_path}: {e}")

def process_svg(svg_path):
    # Implement SVG processing if needed
    print(f"SVG file processing is not yet implemented for {svg_path}")

# Process all files in the problems directory
csv_directory = 'problems'
for file_name in os.listdir(csv_directory):
    file_path = os.path.join(csv_directory, file_name)
    if os.path.isfile(file_path):
        if file_name.endswith('.csv'):
            print(f"Processing CSV file {file_path}...")
            process_csv(file_path)
        elif file_name.endswith('.svg'):
            print(f"Processing SVG file {file_path}...")
            process_svg(file_path)
        else:
            print(f"File {file_path} is neither CSV nor SVG, skipping...")
    else:
        print(f"Directory {file_path} is not a file, skipping...")

print("Processing complete.")
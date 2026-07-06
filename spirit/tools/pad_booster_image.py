import os
import sys
import argparse
from PIL import Image

def pad_booster_image(src_path, dest_path=None):
    if not os.path.exists(src_path):
        print(f"Error: Source file '{src_path}' does not exist.")
        return False
        
    if dest_path is None:
        dest_path = src_path
        
    try:
        img = Image.open(src_path)
    except Exception as e:
        print(f"Error opening image '{src_path}': {e}")
        return False

    # Target dimensions inside 512x512: max height 496
    target_height = 496
    aspect_ratio = img.width / img.height
    target_width = int(target_height * aspect_ratio)

    print(f"Resizing booster artwork from {img.width}x{img.height} to {target_width}x{target_height}...")
    resized_img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)

    print("Creating transparent 512x512 canvas...")
    canvas = Image.new('RGBA', (512, 512), (0, 0, 0, 0))

    # Center horizontally and set top padding to 16
    left_padding = (512 - target_width) // 2
    top_padding = 16

    print(f"Pasting artwork at position (x={left_padding}, y={top_padding})...")
    canvas.paste(resized_img, (left_padding, top_padding), resized_img)

    print(f"Saving final image to '{dest_path}'...")
    canvas.save(dest_path)
    print("Padding and resizing complete!")
    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Pads and resizes any portrait booster pack image into a transparent 512x512 canvas matching PTCGO standards.")
    parser.add_argument("src_path", help="Path to the custom booster pack PNG image.")
    parser.add_argument("-o", "--output", help="Optional path to save the formatted image. If omitted, overwrites the source image.")
    
    args = parser.parse_args()
    pad_booster_image(args.src_path, args.output)

# main.py

from codemap_spiral import spiral_chain
from codemap_viewer import print_spiral

tesseract_root = spiral_chain(depth=4)
print_spiral(tesseract_root)
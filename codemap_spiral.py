# codemap_spiral.py

from codemap_tesseract import CodemapTesseract

def spiral_chain(depth=5):
    root = CodemapTesseract()
    current = root
    for _ in range(depth - 1):
        current = current.build_next_tesseract()
    return root
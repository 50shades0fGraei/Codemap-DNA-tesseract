# codemap_viewer.py

def print_spiral(tesseract):
    current = tesseract
    while current:
        print(f"\n🌀 Generation {current.generation}")
        print(f"Traits: {current.traits}")
        print(f"Planes: {current.path['planes']}")
        print(f"Duality: {current.path['duality']}")
        current = current.child

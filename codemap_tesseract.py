# codemap_tesseract.py

import random
from codemap_constants import TRAITS, PLANES, DUALITY

class CodemapTesseract:
    def __init__(self, generation=0, parent=None):
        self.generation = generation
        self.parent = parent
        self.traits = self.lock_traits()
        self.path = self.compile_path()
        self.output = self.manifest_entity()
        self.child = None

    def lock_traits(self):
        # Randomly select 4 traits for this tesseract
        return random.sample(TRAITS, 4)

    def compile_path(self):
        # Build a symbolic execution path from traits and planes
        return {
            "planes": random.sample(PLANES, 4),
            "duality": random.choice(DUALITY),
            "traits": self.traits
        }

    def manifest_entity(self):
        # Create a symbolic print of this tesseract's identity
        return {
            "type": "Codemap Entity",
            "generation": self.generation,
            "traits": self.traits,
            "path": self.path
        }

    def build_next_tesseract(self):
        # Recursive expansion
        self.child = CodemapTesseract(generation=self.generation + 1, parent=self)
        return self.child
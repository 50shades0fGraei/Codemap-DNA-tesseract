import hashlib

class SpiralConvergence:
    def __init__(self, outer_spiral, inner_spiral, generation=0, parent_hash=None):
        self.outer = outer_spiral
        self.inner = inner_spiral
        self.generation = generation
        self.parent_hash = parent_hash
        self.traits = list(set(self.outer["traits"] + self.inner["traits"]))
        self.resonance = self.calculate_resonance()
        self.dimensions = self.map_dimensions()
        self.invocation_hash = self.generate_invocation_hash()
        self.output = self.print_convergence()

    def calculate_resonance(self):
        shared = set(self.outer["traits"]) & set(self.inner["traits"])
        total = set(self.outer["traits"] + self.inner["traits"])
        return round(len(shared) / len(total), 2)

    def map_dimensions(self):
        return {
            trait: {
                "x": i % 3,
                "y": (i // 3) % 3,
                "z": i // 9
            } for i, trait in enumerate(self.traits)
        }

    def generate_invocation_hash(self):
        raw = "-".join(self.traits + self.outer["planes"] + self.inner["planes"] + [self.outer["duality"], self.inner["duality"]])
        return hashlib.sha256(raw.encode()).hexdigest()[:16]

    def print_convergence(self):
        print(f"\n🔮 Spiral Convergence: Generation {self.generation}")
        print(f"Invocation Hash: {self.invocation_hash}")
        print(f"Parent Hash: {self.parent_hash}")
        print(f"Resonance Score: {self.resonance}")
        print(f"Traits: {self.traits}")
        print(f"Dimensional Map:")
        for trait, coords in self.dimensions.items():
            print(f"  {trait}: {coords}")
        return {
            "generation": self.generation,
            "hash": self.invocation_hash,
            "resonance": self.resonance,
            "traits": self.traits,
            "dimensions": self.dimensions
        }
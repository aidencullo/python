from dataclasses import dataclass, asdict

@dataclass
class Recipe:
    id: str
    name: str
    ingredients: list[str] = None
    steps: list[str] = None

    def __post_init__(self):
        self.ingredients = [i.lower() for i in (self.ingredients or [])]
        self.steps = self.steps or []

    def __repr__(self):
        return f"Recipe(id={self.id}, name={self.name})"


r = Recipe(1, "daniel")
print(r)

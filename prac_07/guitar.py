"""
guitar
Estimate: 2 minutes
Actual: 5 minutes
"""
CURRENT_YEAR = 2023
VINTAGE = 50


class Guitar:
    """Store guitar information."""

    def __init__(self, name="", year=0, cost=0):
        """Guitar initial information."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string format."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Ger age of a guitar based on CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Check if the guitar is a vintage and return a Boolean."""
        return self.get_age() >= VINTAGE

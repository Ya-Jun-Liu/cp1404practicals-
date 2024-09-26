class Band:
    """Band class."""

    def __init__(self, name=""):
        """Construct a Band with a name and and empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        band = []
        for musician in self.musicians:
            band.append(f"{musician}")
        return f"{self.name} ({','.join(band)})"

    def add(self, musician):
        """Add a musician to band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the musician playing their first (or no) instrument."""
        band = ""
        for musician in self.musicians:
            if not musician.instruments:
                band += f"{musician.name} needs an instrument!\n"
            else:
                band += f"{musician.name} is playing: {musician.instruments[0]}\n"
        return band

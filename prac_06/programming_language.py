class ProgrammingLanguage:
    """Information on a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Set car details as parameters."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the language is dynamically typed and return a Boolean."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a sting of the ProgrammingLanguage."""
        return f"{self.name},{self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def test(self):
        """Check which language is dynamically typed."""
        python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
        ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
        visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

        languages = [python, ruby, visual_basic]  # new list
        print(python)

        print("The dynamically typed languages are:")
        for language in languages:
            if language.is_dynamic():
                print(language.name)

    if __name__ == "__main__":
        test()

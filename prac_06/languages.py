"""
languages
Estimate: 30 minutes
Actual: 60 minutes
"""
from prac_06.programming_language import ProgrammingLanguage


# import the class from file


def main():
    """Print the dynamically typed languages from the file."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [python, ruby, visual_basic]

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()

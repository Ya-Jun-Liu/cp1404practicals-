import wikipedia


def main():
    """Prompt user input and print the title, summary, and the URL."""
    user_input = input("Search:")
    while user_input != '':
        user_input = user_input.strip()
        try:
            page = wikipedia.page(user_input)
            page_summary = wikipedia.summary(user_input)
            print("\ntitle:", page.title)
            print("Summary:", page_summary)
            print("URL:", page.url)
        except wikipedia.exceptions.DisambiguationError:
            print("DisambiguationError. Try another query!")
        except wikipedia.exceptions.PageError:
            print("PageError. Try another query!")

        user_input = input("\nSearch: (blank to exit)")
    print("Thank you!")


main()

import wikipedia


def main():
    """Prompt user input and print the title, summary, and the URL."""
    user_input = input("Search:")
    while user_input != '':
        user_input = user_input.strip()
        try:
            page_summary = wikipedia.summary(user_input)
            page = wikipedia.page(user_input)
            print("\ntitle:")
            print(user_input.title())
            print("\nSummary:")
            print(page_summary)
            print("\nURL:")
            print(page.url)
        except wikipedia.exceptions.DisambiguationError:
            print("DisambiguationError. Try another query!")
        except wikipedia.exceptions.PageError:
            print("PageError. Try another query!")

        user_input = input("Search:")
    print("Thank you!")


main()

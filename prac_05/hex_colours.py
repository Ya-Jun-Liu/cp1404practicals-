COLOUR_CODE = {"Amber": "#ffbf00", "Aqua": "#00ffff",
               "Apricot": "#fbceb1", "Asparagus": "#87a96b",
               "BlueViolet": "#8a2be2", "Camel": "#c19a6b",
               "Crystal": "#a7d8de", "DarkGreen": "#006400",
               "DarkOrchid4": "#68228b", "GhostWhite": "#f8f8ff"}

colour_name = input("Enter colour name: ")
while colour_name != "":
    print(f"The colour code for {colour_name} is {COLOUR_CODE[colour_name]}")
    colour_name = input("Enter colour name: ")

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic label creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names:
        self.names_dictionary = ['Alice', 'Bob', 'Kate', 'Zac']

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')

        # Create Labels from data and add them to the GUI.
        for name in self.names_dictionary:
            # create a label for each data entry, specifying the text
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

        return self.root


DynamicLabelsApp().run()

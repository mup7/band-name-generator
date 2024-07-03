import tkinter

# Constant for the title font used in the application
TITLE_FONT = ("Arial", 15, "normal")

class Root():
    """Class to create and manage the Tkinter root window and its widgets."""

    def __init__(self):
        """Initialize the root window and its widgets."""
        self.root = tkinter.Tk()
        self.root.config(padx=25, pady=25)
        self.root.title("Band Name Generator")

        # Welcome label with a title font
        self.label1 = tkinter.Label(text="Welcome to the Band Name Generator", font=TITLE_FONT)
        self.label1.pack()

        # Label asking for the name of the city
        self.label2 = tkinter.Label(text="What's the name of the city you grew up in?")
        self.label2.pack()

        # Entry widget for the user to input the city name
        self.city_name = tkinter.Entry()
        self.city_name.pack()
        self.city_name.focus()  # Set focus on the city name entry widget

        # Label asking for the name of the pet
        self.label3 = tkinter.Label(text="What's the name of your pet?")
        self.label3.pack()

        # Entry widget for the user to input the pet name
        self.pet_name = tkinter.Entry()
        self.pet_name.pack()

        # Button to submit the inputs and generate the band name
        self.submit_button = tkinter.Button(text="Generate Band Name", command=self.generate_band_name)
        self.submit_button.pack()

        # Label to display the result or any messages to the user
        self.result_label = tkinter.Label(text="")
        self.result_label.pack()

        # Start the Tkinter event loop
        self.root.mainloop()
    
    def generate_band_name(self):
        """Generate and display a band name based on user inputs."""
        # Check if the city name input is empty
        if len(self.city_name.get()) < 1:
            self.result_label.config(text="Please, tell me the name of the city you grew up in!")
        # Check if the pet name input is empty
        elif len(self.pet_name.get()) < 1:
            self.result_label.config(text="Please, tell me the name of your pet!")
        # If both inputs are provided, generate the band name
        else:
            self.band_name = f"{self.city_name.get().title()} {self.pet_name.get().title()}"
            self.result_label.config(text=f"Your band name could be {self.band_name}!")
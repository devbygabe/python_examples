class Car:
    """Represents a car object."""

    miles = 0

    def __init__(self, colour, make, model, miles=0):
        """Set initial deatsils of car."""
        self.colour = colour
        self.make = make
        self.model = model
        self.miles = miles

    def add_miles(self, miles):
        """Increase miles by given number."""
        self.miles += miles

    def display_miles(self):
        """Print the current miles value."""
        print(
            f"{self.make} {self.model} ({self.colour}) "
            f"has driven {self.miles} miles."
        )


astra = Car("Red", "Vauxhall", "Astra")
astra.display_miles()
astra.add_miles(100)
astra.display_miles()

astra = Car("Blue", "Toyota", "Prius")
astra.display_miles()
astra.add_miles(50)
astra.display_miles()

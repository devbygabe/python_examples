class User:
    """Represents a user of the store."""

    def __init__(self, name, password):
        """Initialise data for store user."""
        self._name = name
        self._password = password
        self._logged_in = False

    def login(self, password):
        """Check password and logs user in."""
        if password == self._password:
            self._logged_in = True
        else:
            print("Incorrect password.")

    def show_staus(self):
        """Print the status of user."""
        if self._logged_in:
            print(f"{self._name} is logged in.")


customer = User(name="Bruce", password="Secret01")
customer.login("IncorrectPassword")
customer.show_staus()
customer.login("Secret01")
customer.show_staus()


class Admin(User):
    """Admin of the store."""

    def __init__(self, name, password, staff_id):
        """Initialise data for store admin."""
        super.__init__(name, password)
        self._staff_id = staff_id

    def add_product(self, product):
        """Add product to the store."""
        if self._logged_in:
            print(f"{self._name} ({self._staff_id}) ")
            print(f"added {product} to the store.")
        else:
            print("Login to add product.")


staff = Admin(name="Gabriel", password="Password1", staff_id=1234)
staff.add_product("Coffee")
staff.login("Password1")
staff.add_product("Coffee")

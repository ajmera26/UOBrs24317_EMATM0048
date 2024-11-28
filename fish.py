class Fish:
    """
    A class to represent a fish species.

    Attributes:
    name (str): The name of the fish species.
    fertilizer (float): The amount of fertilizer required per fish (in ml).
    feed (float): The amount of feed required per fish (in kg).
    salt (float): The amount of salt required per fish (in kg).
    maintenance_time (float): The maintenance time required per fish (in days).
    demand (int): The demand for the fish per quarter.
    price (float): The price per fish.
    """

    def __init__(self, name, fertilizer, feed, salt, maintenance_time, demand, price):
        """
        Initialize a fish species with its attributes.

        Args:
        name (str): The name of the fish species.
        fertilizer (float): Fertilizer required per fish.
        feed (float): Feed required per fish.
        salt (float): Salt required per fish.
        maintenance_time (float): Maintenance time per fish.
        demand (int): Demand for the fish per quarter.
        price (float): Price per fish.
        """
        self.name = name
        self.fertilizer = fertilizer
        self.feed = feed
        self.salt = salt
        self.maintenance_time = maintenance_time
        self.demand = demand
        self.price = price

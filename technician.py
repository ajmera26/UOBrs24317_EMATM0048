class Technician:
    """
    A class to represent a technician.

    Attributes:
    name (str): The name of the technician.
    weekly_rate (float): The weekly rate of the technician.
    specialty (str): The specialty of the technician (if any).
    """

    def __init__(self, name, weekly_rate, specialty=None):
        """
        Initialize a technician with a name, weekly rate, and optional specialty.

        Args:
        name (str): The name of the technician.
        weekly_rate (float): The technician's weekly rate.
        specialty (str, optional): The fish species the technician specializes in.
        """
        self.name = name
        self.weekly_rate = weekly_rate
        self.specialty = specialty

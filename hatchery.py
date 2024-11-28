from fish import Fish
from technician import Technician
import math

class Hatchery:
    """
    The main class to manage the hatchery operations, including finances, supplies, and technicians.
    """

    def __init__(self):
        """
        Initialize the hatchery with default cash, supplies, fish species, and technicians.
        """
        self.cash = 10000
        self.technicians = []
        self.fish_species = [
            Fish("Clef Fins", 100/1000, 12, 2, 2.0, 25, 250),
            Fish("Timpani Snapper", 50/1000, 9, 2, 1.0, 10, 350),
            Fish("Andalusian Brim", 90/1000, 6, 2, 0.5, 15, 250),
            Fish("Plagal Cod", 100/1000, 10, 2, 2.0, 20, 400),
            Fish("Fugue Flounder", 200/1000, 12, 2, 2.5, 30, 550),
            Fish("Modal Bass", 300/1000, 12, 6, 3.0, 50, 500)
        ]
        self.fertilizer_stock = 20
        self.feed_stock = 400
        self.salt_stock = 200
        self.aux_fertilizer_stock = 10
        self.aux_feed_stock = 200
        self.aux_salt_stock = 100
        self.depreciation_rate_fertilizer = 0.4
        self.depreciation_rate_feed = 0.1
        self.total_days_per_tech = 45

    def add_technician(self, name, specialty=None):
        """
        Add a technician to the hatchery.

        Args:
            name (str): The name of the technician.
            specialty (str, optional): The fish species the technician specializes in.
        """
        if len(self.technicians) >= 5:
            print("Cannot hire more than 5 technicians.")
        else:
            self.technicians.append(Technician(name, 500, specialty))
            print(f"Hired {name}, weekly rate=500 in quarter {len(self.technicians)}")

    def remove_technician(self, name):
        """
        Remove a technician from the hatchery.

        Args:
            name (str): The name of the technician to remove.
        """
        self.technicians = [tech for tech in self.technicians if tech.name != name]
        print(f"Let go {name}, weekly rate=500 in quarter")

    def apply_depreciation(self):
        """
        Apply depreciation to the stock of supplies in the hatchery.
        Depreciation reduces stock based on the depreciation rate.
        """
        self.fertilizer_stock = math.ceil(self.fertilizer_stock * (1 - self.depreciation_rate_fertilizer))
        self.feed_stock = math.ceil(self.feed_stock * (1 - self.depreciation_rate_feed))
        self.salt_stock = math.ceil(self.salt_stock * 1)
        self.aux_fertilizer_stock = math.ceil(self.aux_fertilizer_stock * (1 - self.depreciation_rate_fertilizer))
        self.aux_feed_stock = math.ceil(self.aux_feed_stock * (1 - self.depreciation_rate_feed))
        self.aux_salt_stock = math.ceil(self.aux_salt_stock * 1)

    def calculate_total_available_weeks(self):
        """
        Calculate the total number of available technician weeks dynamically at a specific time.
        - Regular technicians start with 9 weeks per quarter.
        - Technicians with a specialty start with 6 weeks (2/3 of 9 weeks) per quarter.
        - Dynamically computes the remaining weeks at a specific time in the quarter.

        Returns:
            float: Total number of available technician weeks remaining.
        """
        total_available_weeks = 0

        for technician in self.technicians:
            if technician.specialty:
                total_available_weeks += (9 * 2 / 3)
            else:
                total_available_weeks += 9

        weeks_worked = getattr(self, "_weeks_worked", 0)
        total_available_weeks -= weeks_worked

        return max(0, total_available_weeks)

    def sell_fish(self, fish_name, quantity):
        """
        Sell fish from the hatchery, updating the stock, cash balance, and technician labor.

        Args:
            fish_name (str): The name of the fish species to be sold.
            quantity (int): The quantity of fish to sell.
        """
        while True:
            fish = next((f for f in self.fish_species if f.name == fish_name), None)
            if not fish:
                print(f"Fish {fish_name} not found!")
                return

            required_fertilizer = fish.fertilizer * quantity
            required_feed = fish.feed * quantity
            required_salt = fish.salt * quantity
            required_maintenance_time = (fish.maintenance_time * quantity) / 5

            available_fertilizer = self.fertilizer_stock + self.aux_fertilizer_stock
            available_feed = self.feed_stock + self.aux_feed_stock
            available_salt = self.salt_stock + self.aux_salt_stock
            available_weeks = self.calculate_total_available_weeks()

            if (required_fertilizer > available_fertilizer or
                required_feed > available_feed or
                required_salt > available_salt or
                required_maintenance_time > available_weeks):
                
                print(f"Fish {fish_name}, demand {fish.demand}, sell {quantity}: 0")
                print("Insufficient resources:")
                if required_fertilizer > available_fertilizer:
                    print(f"  Fertilizer needed {required_fertilizer}, available {available_fertilizer}")
                if required_feed > available_feed:
                    print(f"  Feed needed {required_feed}, available {available_feed}")
                if required_salt > available_salt:
                    print(f"  Salt needed {required_salt}, available {available_salt}")
                if required_maintenance_time > available_weeks:
                    print(f"  Labor needed {required_maintenance_time:.2f} weeks, available {available_weeks:.2f} weeks")
                
                quantity = int(input(f"Enter a new quantity for {fish_name}: "))
            else:
                break

        self.cash += fish.price * quantity
        self._deduct_stock("fertilizer", required_fertilizer)
        self._deduct_stock("feed", required_feed)
        self._deduct_stock("salt", required_salt)

        if not hasattr(self, "_weeks_worked"):
            self._weeks_worked = 0
        self._weeks_worked += required_maintenance_time

        print(f"Fish {fish_name}, demand {fish.demand}, sell {quantity}: {quantity}")

    def _deduct_stock(self, supply, required_amount):
        """
        Deduct the stock from both main and auxiliary supplies.

        Args:
            supply (str): The type of supply (fertilizer, feed, salt).
            required_amount (float): The amount of supply to deduct.
        """
        if supply == "fertilizer":
            main_stock = self.fertilizer_stock
            aux_stock = self.aux_fertilizer_stock
        elif supply == "feed":
            main_stock = self.feed_stock
            aux_stock = self.aux_feed_stock
        elif supply == "salt":
            main_stock = self.salt_stock
            aux_stock = self.aux_salt_stock
        else:
            raise ValueError("Invalid supply type. Must be 'fertilizer', 'feed', or 'salt'.")

        if required_amount <= main_stock:
            if supply == "fertilizer":
                self.fertilizer_stock -= required_amount
            elif supply == "feed":
                self.feed_stock -= required_amount
            elif supply == "salt":
                self.salt_stock -= required_amount
        else:
            remaining_amount = required_amount - main_stock
            if supply == "fertilizer":
                self.fertilizer_stock = 0
                self.aux_fertilizer_stock -= remaining_amount
            elif supply == "feed":
                self.feed_stock = 0
                self.aux_feed_stock -= remaining_amount
            elif supply == "salt":
                self.salt_stock = 0
                self.aux_salt_stock -= remaining_amount

    def pay_technicians(self):
        """
        Pay all technicians for their work during the quarter.
        Each technician is paid based on their weekly rate for 12 weeks per quarter.
        """
        total_payment = 0
        for technician in self.technicians:
            payment = technician.weekly_rate * 12
            total_payment += payment
            self.cash -= payment
            print(f"Paid {technician.name}, weekly rate={technician.weekly_rate}, amount {payment:.2f}")
        
        print(f"Paid rent/utilities 1500")
        self.cash -= 1500
        
        print(f"Remaining cash after payments: {self.cash:.2f}")

    def calculate_warehouse_costs(self):
        """
        Calculate and return the total cost for both the main and auxiliary warehouses.
        These costs are based on the current stock of supplies and their respective costs per unit.
        """
        cost_main_fertilizer = self.fertilizer_stock * 0.10
        cost_main_feed = self.feed_stock * 0.001 * 1000
        cost_main_salt = self.salt_stock * 0.001 * 1000

        cost_aux_fertilizer = self.aux_fertilizer_stock * 0.10
        cost_aux_feed = self.aux_feed_stock * 0.001 * 1000
        cost_aux_salt = self.aux_salt_stock * 0.001 * 1000

        total_cost = (cost_main_fertilizer + cost_main_feed + cost_main_salt +
                      cost_aux_fertilizer + cost_aux_feed + cost_aux_salt)

        self.cash -= total_cost

        print(f"Warehouse Main: Fertiliser cost {cost_main_fertilizer:.2f}")
        print(f"Warehouse Main: Feed cost {cost_main_feed:.2f}")
        print(f"Warehouse Main: Salt cost {cost_main_salt:.2f}")
        print(f"Warehouse Auxiliary: Fertiliser cost {cost_aux_fertilizer:.2f}")
        print(f"Warehouse Auxiliary: Feed cost {cost_aux_feed:.2f}")
        print(f"Warehouse Auxiliary: Salt cost {cost_aux_salt:.2f}")
        print(f"Total warehouse costs: {total_cost:.2f}")

    def restock_supplies(self, vendor_choice):
        """
        Restock supplies from the selected vendor.
        Vendor 1 = Slippery Lakes, Vendor 2 = Scaly Wholesaler

        Args:
            vendor_choice (int): The vendor number (1 or 2).
        """
        vendor_prices = {
            1: {"fertilizer": 0.30, "feed": 0.10, "salt": 0.05},
            2: {"fertilizer": 0.20, "feed": 0.40, "salt": 0.25}
        }

        if vendor_choice not in [1, 2]:
            print("Invalid vendor choice.")
            return

        prices = vendor_prices[vendor_choice]

        cost_fertilizer = (20 - self.fertilizer_stock) * prices["fertilizer"]
        cost_feed = (400 - self.feed_stock) * prices["feed"]
        cost_salt = (200 - self.salt_stock) * prices["salt"]

        total_cost = cost_fertilizer + cost_feed + cost_salt
        if self.cash >= total_cost:
            self.cash -= total_cost
            self.fertilizer_stock = 20
            self.feed_stock = 400
            self.salt_stock = 200
            self.aux_fertilizer_stock = 10
            self.aux_feed_stock = 200
            self.aux_salt_stock = 100
            print(f"Restocking completed. Vendor {vendor_choice} supplies.")
        else:
            print(f"Can't restock supplies, insufficient funds. Total needed: {total_cost}, available: {self.cash}")

        print(f"Hatchery Name: Eastaboga, Cash: {self.cash:.2f}")
        print("Warehouse Main")
        print(f" Fertiliser, {self.fertilizer_stock:.2f} (capacity=20)")
        print(f" Feed, {self.feed_stock:.2f} (capacity=400)")
        print(f" Salt, {self.salt_stock:.2f} (capacity=200)")
        print("Warehouse Auxiliary")
        print(f" Fertiliser, {self.aux_fertilizer_stock:.2f} (capacity=10)")
        print(f" Feed, {self.aux_feed_stock:.2f} (capacity=200)")
        print(f" Salt, {self.aux_salt_stock:.2f} (capacity=100)")
        print("Technicians")
        for technician in self.technicians:
            print(f" Technician {technician.name}, weekly rate={technician.weekly_rate}")
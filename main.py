from hatchery import Hatchery

def main():
    """
    Run the hatchery simulation based on user input for quarters and operations.
    """
    hatchery = Hatchery()

    while True:
        try:
            quarters = int(input("Enter the number of quarters to simulate (default is 8): ") or 8)
            if quarters <= 0:
                raise ValueError("Number of quarters must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number of quarters.")

    for quarter in range(1, quarters + 1):
        hatchery._weeks_worked = 0
        print(f"====== SIMULATING QUARTER {quarter} ======")

        # Add or remove technicians
        while True:
            try:
                tech_change = int(input("Enter technicians to add/remove (e.g., +2 or -1): "))
                if tech_change + len(hatchery.technicians) > 5:
                    raise ValueError("Cannot have more than 5 technicians.")
                if tech_change < 0 and len(hatchery.technicians) + tech_change < 1:
                    raise ValueError("There must be at least one technician at all times.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid number of technicians to add/remove.")

        if tech_change > 0:
            for _ in range(tech_change):
                while True:
                    name = input("Enter technician name: ")
                    if not name:
                        print("Technician name cannot be empty.")
                        continue
                    if any(tech.name == name for tech in hatchery.technicians):
                        print("A technician with the same name already exists.")
                        continue
                    break
                specialty = input("Enter specialty (optional, press Enter to skip): ")
                hatchery.add_technician(name, specialty or None)
        elif tech_change < 0:
            for _ in range(abs(tech_change)):
                while True:
                    name = input("Enter technician name to remove: ")
                    if not name:
                        print("Technician name cannot be empty.")
                        continue
                    if not any(tech.name == name for tech in hatchery.technicians):
                        print("No technician found with that name.")
                        continue
                    break
                hatchery.technicians = [tech for tech in hatchery.technicians if tech.name != name]
                print(f"Removed technician {name}")

        # Sell fish
        for fish in hatchery.fish_species:
            while True:
                try:
                    quantity = int(input(f"Enter quantity to sell for {fish.name} (max {fish.demand}): "))
                    if quantity < 0 or quantity > fish.demand:
                        raise ValueError(f"Quantity must be between 0 and {fish.demand}.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}. Please enter a valid quantity.")
            hatchery.sell_fish(fish.name, quantity)

        hatchery.pay_technicians()
        hatchery.calculate_warehouse_costs()

        # End-of-quarter operations
        hatchery.apply_depreciation()

        print(f"End of Quarter {quarter}: Hatchery Cash = {hatchery.cash:.2f}")

        print("List of Vendors:")
        print("1. Slippery Lakes")
        print("2. Scaly Wholesaler")
        while True:
            try:
                vendor_choice = int(input("Enter the number of the vendor to purchase supplies from: "))
                if vendor_choice not in [1, 2]:
                    raise ValueError("Invalid vendor choice. Please enter 1 or 2.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid vendor number.")
        print(f"Restocking from vendor {vendor_choice}...")
        hatchery.restock_supplies(vendor_choice)

        # Check if the hatchery goes bankrupt
        if hatchery.cash < 0:
            print(f"Bankrupt after Quarter {quarter}!")
            break

    print("Simulation Ended")

if __name__ == "__main__":
    main()
# Hatchery Simulation
## Overview
This project simulates the operations of a fish hatchery, including managing supplies, hiring technicians, selling fish, and performing other key activities such as restocking and paying employees. The simulation is divided into quarters, and user inputs control various aspects of the hatchery’s operations.

### **Files**

The project consists of the following Python files:

_technician.py_:  
Contains the Technician class, which represents a technician and their details.  
_fish.py_:  
Contains the Fish class, which represents different species of fish.  
_hatchery.py_:  
Contains the Hatchery class, which manages hatchery operations such as cash balance, stock management, and technician work.
_main.py_:  
The main program file that simulates hatchery operations based on user inputs.


### Classes
1. Technician (technician.py)  
This class represents a technician working in the hatchery. The technician has the following attributes:

name (str): The name of the technician.
weekly_rate (float): The weekly rate of the technician.
specialty (str, optional): The fish species the technician specializes in.
python

2. Fish (fish.py)  
This class represents a species of fish in the hatchery. It includes attributes related to the maintenance and sale of the fish:

name (str): The name of the fish species.
fertilizer (float): The amount of fertilizer required per fish (in ml).
feed (float): The amount of feed required per fish (in kg).
salt (float): The amount of salt required per fish (in kg).
maintenance_time (float): The time (in days) required to maintain the fish.
demand (int): The demand for the fish per quarter.
price (float): The price at which each fish is sold.
python

3. Hatchery (hatchery.py)  
The Hatchery class manages the operations of the hatchery, such as inventory, technician management, and the selling of fish. Key attributes and methods include:

      - cash: The current cash balance of the hatchery.
      - technicians: A list of technicians working in the hatchery.
      - fish_species: A list of different fish species available for sale.
      - fertilizer_stock, feed_stock, salt_stock: The stock levels of supplies.
      - Methods to add/remove technicians, apply depreciation to supplies, sell fish, calculate labor and warehouse costs, pay technicians, and restock supplies.

    Key methods include:

      - add_technician: Adds a technician to the hatchery.
      - remove_technician: Removes a technician from the hatchery.
      - apply_depreciation: Depreciates the stock of supplies.
      - sell_fish: Sells a given quantity of fish and updates the stock and cash balance.
      - pay_technicians: Pays technicians based on their weekly rate for the quarter.
      - calculate_warehouse_costs: Calculates the total warehouse costs based on supply usage.

4. Main (main.py)  
  The main.py file runs the simulation, allowing the user to interact with the hatchery by providing inputs for:

  - The number of quarters to simulate.
  - Adding/removing technicians.
  - Selling fish species.
  - Restocking supplies.
  - Paying technicians at the end of each quarter.
  - Checking for bankruptcy.



### Features
Technician Management: Hire and fire technicians, each with a weekly rate and a possible specialty in a specific fish species.
Fish Sales: Sell fish based on supply levels, maintaining the correct balance of fertilizer, feed, and salt.
Stock Management: Track the hatchery's inventory and restock supplies at the end of each quarter.
Finances: Pay technicians, calculate warehouse costs, and monitor the hatchery’s cash flow to avoid bankruptcy.
Depreciation: Supplies lose value over time, simulating real-world conditions where stock depletes and deteriorates.  

### Running the Simulation
1. Clone or download the repository.
2. Install any necessary dependencies (if applicable).
3. Run main.py to start the simulation.
4. Input the required values for each quarter as prompted.

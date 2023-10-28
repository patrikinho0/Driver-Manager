import json
from driver import Driver

def add_new_driver(name):
    driver_id = 0

    # Read from the json file
    with open("drivers.json", "r") as file:
        drivers = json.load(file)

    # Go through the content of the file and create a variable with name parameter from the user
    for driver in drivers:
        if(int(driver_id) == (driver["id"])):
            driver_id += 1
    new_driver = Driver(driver_id, name)

    # Add new driver to a dict
    drivers.append(new_driver.to_dict())

    # Dump the new driver to the json file
    with open("drivers.json", "w") as file:
        json.dump(drivers, file, indent=2)

def remove_driver(driver_id):

    # Read from the json file
    with open("drivers.json", "r") as file:
        drivers = json.load(file)

    # Create a variable with the driver's id
    drivers = [driver for driver in drivers if driver["id"] != driver_id]

    # Dump the drivers variable without the removed driver
    with open("drivers.json", "w") as file:
        json.dump(drivers, file, indent=2)

def create_reservation(driver_id, reservation_detail):

    # Read from the json file
    with open("drivers.json", "r") as file:
        drivers = json.load(file)

    # Go through the content of the file and check
    for driver in drivers:
        if driver["id"] == driver_id:
            if driver["status"] == 'Free':
                driver["reservation_detail"] = reservation_detail
                driver["status"] = "Busy"
            else:
                print("Driver is already on a reservation.")

    # Dump the created reservation to the json file
    with open("drivers.json", "w") as file:
        json.dump(drivers, file, indent=2)

def conclude_reservation(driver_id):

    # Read from the json file
    with open("drivers.json", "r") as file:
        drivers = json.load(file)

    # Go through the content of the file and check
    for driver in drivers:
        if driver["id"] == driver_id:
            if driver["status"] == "Busy":
                driver["reservation_detail"] = None
                driver["status"] = "Free"
            else:
                print("Driver doesn't have an active reservation.")

    # Dump the concluded reservation to the json file
    with open("drivers.json", "w") as file:
        json.dump(drivers, file, indent=2)

def display_drivers():

    # Read from the json file
    with open("drivers.json", "r") as file:
        drivers = json.load(file)

    # Print all drivers
    print("All drivers: \n")
    for driver in drivers:
        print("Id: ", driver["id"])
        print("Name: ", driver["name"])
        print("Status: ", driver["status"])
        print("Reservation Details: ", driver["reservation_detail"])

    return drivers



# For manual testing uncomment the following functions:

#add_new_driver("exampleName")
#remove_driver(0)
#create_reservation(1, "From Zgierz to Lodz")
#conclude_reservation(0)
#display_drivers()
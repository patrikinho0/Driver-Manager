from utils import add_new_driver, remove_driver, create_reservation, conclude_reservation, display_drivers
from colors import Colors as C
from time import sleep
import os

os.system('cls||clear')
print(C.OKCYAN + "Welcome to the Drivers Manager" + C.ENDC)
sleep(2)

while True:
    os.system('cls||clear')
    print(C.BOLD + "1. Add Driver" + C.ENDC)
    print(C.BOLD + "2. Remove Driver" + C.ENDC)
    print(C.BOLD + "3. Create Reservation" + C.ENDC)
    print(C.BOLD + "4. Conclude Reservation" + C.ENDC)
    print(C.BOLD + "5. Display Drivers" + C.ENDC)
    print(C.BOLD + "6. Exit" + C.ENDC + "\n")

    choice = input("Enter your choice: ")

    if choice == '1':
        os.system('cls||clear')
        driver_name = input("Enter driver name: ")
        os.system('cls||clear')
        print(C.OKBLUE + "Adding new driver.." + C.ENDC)
        sleep(2)
        add_new_driver(driver_name)

    elif choice == '2':
        os.system('cls||clear')
        driver_id = int(input("Enter driver ID: "))
        os.system('cls||clear')
        print(C.WARNING + "Removing driver.." + C.ENDC)
        sleep(2)
        remove_driver(driver_id)

    elif choice == '3':
        os.system('cls||clear')
        driver_id = int(input("Enter driver ID: "))
        reservation_details = input("Enter reservation details: ")
        os.system('cls||clear')
        print(C.OKGREEN + "Creating reservation.." + C.ENDC)
        sleep(2)
        create_reservation(driver_id, reservation_details)

    elif choice == '4':
        os.system('cls||clear')
        driver_id = int(input("Enter driver ID: "))
        os.system('cls||clear')
        print(C.OKCYAN + "Concluding reservation.." + C.ENDC)
        sleep(2)
        conclude_reservation(driver_id)

    elif choice == '5':
        os.system('cls||clear')
        print(C.OKGREEN + "Displaying drivers.." + C.ENDC)
        sleep(2)
        display_drivers()

    elif choice == '6':
        os.system('cls||clear')
        print(C.HEADER + "Exiting.." + C.ENDC)
        sleep(2)
        break

    else:
        os.system('cls||clear')
        print(C.FAIL + "INVALID CHOICE!" + C.ENDC)
        sleep(2)
        os.system('cls||clear')
        print(C.FAIL + "Returning to the choice menu.." + C.ENDC)
        sleep(2)
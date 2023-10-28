# Driver Manager Application 

A simple command-line driver management application with basic functionalities such as adding new drivers, displaying all drivers, and various other options.

## Installation 

To use the Driver Manager Application, follow steps below:

1. Clone the repository:
   ```
   git clone https://github.com/patrikinho0/fourth-assignment-patrikinho0.git
   ```

2. Run the application using your IDE terminal, in the main.py file.

## Files 

The application consists of the following files:

1. `main.py`: Contains the main logic and user interface for the Driver Manager Application.
2. `utils.py`: Includes various utility functions to support the main functionality of the application.
3. `tests.py`: Contains unit tests to ensure the proper functioning of the application.
4. `driver.py`: Defines the Driver class used in the application.
5. `colors.py`: Contains various custom colors for the terminal.

# Functionality

The application allows users to perform the following operations:
<br><br>

- Add a new driver.
   - python3 utils.py add_new_driver(name)

- Remove a driver.
  - python3 utils.py remove_driver(id)

- Create a reservation.
  - python3 utils.py create_reservation(driver_id, reservation_detail)

- Conclude a reservation.
  - python3 utils.py conclude_reservation(driver_id)

- Display all drivers.
  - python3 utils.py display_drivers()
<br><br>

## Manual testing

The application allows the user to test the application manually:

Step 1. Clone the repository:
   ```
   git clone https://github.com/patrikinho0/fourth-assignment-patrikinho0.git
   ```

Step 2. Go into the utils.py file

Step 3. Uncomment the following functions and fill the example arguments within your liking:
```py
# add_new_driver("exampleName")

# remove_driver(0)

# create_reservation(1, "From Lodz to Gdansk")

# conclude_reservation(0)

# display_drivers()
```

<br>

<p align="center">Made by: <a href="https://github.com/patrikinho0">patrikinho0</a></p>

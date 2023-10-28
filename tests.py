import unittest
from driver import Driver
from utils import *
import json
import os


class TestMathMethods(unittest.TestCase):
    
    def setUp(self):
          self.sample_driver = {
            "name": "Patrick"
        }
    def test_add_driver(self):
        
        current_directory = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(current_directory, "drivers.json")
        
        existing_data = []
        switch = False
            
        add_new_driver(
             self.sample_driver["name"]
          )
        
        with open(path, 'r') as file:
            existing_data = json.load(file)
        
        for element in existing_data:
                if element.get("name") == existing_data[-1].get("name"):
                    switch = True
                else:
                    switch = False
        self.assertTrue(switch)

    def test_remove_driver(self):
        example_id = 0
        switch = False

        remove_driver(example_id)

        with open("drivers.json", "r") as file:
             drivers = json.load(file)

        for driver in drivers:
             if driver["id"] != example_id:
                 switch = True
             else:
                  switch = False
        self.assertTrue(switch)

    def test_create_reservation(self):
         example_id = 1
         example_reservation_text = "qwerty"

         create_reservation(example_id, example_reservation_text)

         with open("drivers.json", "r") as file:
              drivers = json.load(file)

         for driver in drivers:
              if driver["id"] == example_id and driver["reservation_detail"] == example_reservation_text:
                   self.assertTrue(driver["id"] == example_id and driver["reservation_detail"] == example_reservation_text)

    def test_conclude_reservation(self):
         example_id = 2

         conclude_reservation(example_id)

         with open("drivers.json", "r") as file:
              drivers = json.load(file)

         for driver in drivers:
              if driver["id"] == example_id:
                   self.assertTrue(driver["id"] == example_id)
    
    def test_display_all_drivers(self):

        switch = False
        displayed_data = display_drivers()

        for element in displayed_data:
             if element != None:
                  switch = True
             else:
                  switch = False
        self.assertTrue(switch)


if __name__ == '__main__':
    unittest.main()
"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    limo = Car(100, "Limo") # Create new Car object
    limo.add_fuel(20) # Add 20 more units of fuel
    print(f"Limo has fuel: {limo.fuel}") # Print amount of fuel
    limo.drive(115) # Attempt to drive 115 km
    print(limo)


main()
import math

# Inputs for the mass and radius of the celestial and ship in kilograms and meters, respectively
Mass_Celestial = int(input("What is the mass of the celestial body in kilograms? "))
Mass_Ship = int(input("What is the mass of the ship in kilograms? "))
Radius_Celestial = int(input("What is the radius of the celestial body in meters? "))  
Radius_Ship = int(input("What is the radius of the ship in meters? "))   

def density_celestial_body(Mass_Celestial, Radius_Celestial):
    """
    Calculate the density of a celestial body given its mass and radius.

    Make sure inputs are positive numbers. If not, print an error message and return None.
    
    Inputs:
    mass: the mass of the celestial body in kilograms
    radius: the radius of the celestial body in meters

    Outputs:
    The density of the celestial body in kilograms per cubic meter.
    """
    if Mass_Celestial <= 0 or Radius_Celestial <= 0:
        print("Invalid inputs for celestial body density calculation.")
        return None
    else:
        volume = (4/3) * math.pi * (Radius_Celestial ** 3)
    return Mass_Celestial / volume

def density_ship(Mass_Ship, Radius_Ship):
    """
    Calculate the density of a ship given its mass and radius.

    Make sure inputs are positive numbers. If not, print an error message and return None.

    Inputs:
    mass: the mass of the ship in kilograms
    radius: the radius of the ship in meters

    Outputs:
    The density of the ship in kilograms per cubic meter.
    """
    if Mass_Ship <= 0 or Radius_Ship <= 0:
        print("Invalid inputs for ship density calculation.")
        return None
    else:
        volume = (4/3) * math.pi * (Radius_Ship ** 3)
    return Mass_Ship / volume

def roche_limit(Radius_Celestial, Radius_Ship, density_celestial_body, density_ship):
    """
    Calculate the Roche limit for a ship orbiting a celestial body.

    Make sure inputs are positive numbers. If not, print an error message and return None.

    Inputs:
    radius_celestial: the radius of the celestial body in meters
    radius_ship: the radius of the ship in meters
    density_celestial: the density of the celestial body in kilograms per cubic meter
    density_ship: the density of the ship in kilograms per cubic meter

    Outputs:
    The Roche limit in meters.
    """
    if Radius_Celestial <= 0 or Radius_Ship <= 0 or density_celestial_body <= 0 or density_ship <= 0:
        print("Invalid inputs for Roche limit calculation.")
        return None
    else:
        roche_limit_value = Radius_Celestial * (2 * (density_celestial_body / density_ship)) ** (1/3)
        return roche_limit_value

roche_limit_value = roche_limit(Radius_Celestial, Radius_Ship, density_celestial_body(Mass_Celestial, Radius_Celestial), density_ship(Mass_Ship, Radius_Ship))
print(f"The Roche limit for the ship orbiting the celestial body is: {roche_limit_value} meters.")

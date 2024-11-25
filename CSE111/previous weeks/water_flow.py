import math

def water_column_height(tower_height, tank_height):
    """Calculates and returns the height of a column of water from a tower height and a tank wall height"""
    return tower_height+((tank_height*3)/4)

def pressure_gain_from_water_height(height):
    """Calculates and returns the pressure casued by Earth's gravity pulling on the water stored in an elevated tank"""
    return (998.2*9.80665*height)/1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculates and returns the water pressure lost beacause of the friction between the water and the walls of the a pipe that it flows through"""
    #represents the density of water (998.2 kilogram/meter^3)
    p = 998.2
    top = (-1*friction_factor)*pipe_length*p*(fluid_velocity ** 2)
    bottom = 2000*pipe_diameter
    
    return top/bottom

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Calculates the water pressure lost because of fittings such as 45° and 90° bends that are in a pipeline"""
    #represents the density of water (998.2 kilogram/meter^3)
    p = 998.2
    return (-0.04*p*(fluid_velocity**2)*quantity_fittings)/2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    "Calculates and returns the Reynolds number for a pipe with water flowing through it"
    #represents the dynamic viscosity of water (0.0010016 Pascal seconds)
    visc = 0.0010016
    #represents the density of water (998.2 kilogram/meter^3)
    p = 998.2
    return (p*hydraulic_diameter*fluid_velocity)/visc

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Calculates the water pressure lost because of water moving from a pipe with a large diameter into a pipe with a smaller diameter"""
    #represents the density of water (998.2 kilogram/meter^3)
    p = 998.2
    #first calculation, of which im unsure of the name but its important
    k = (0.1+(50/reynolds_number))*((larger_diameter/smaller_diameter)**4-1)
    return (-k*p*fluid_velocity**2)/2000

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

def kps_to_psi(pressure):
    """converts kPs to psi"""
    return pressure*0.145038


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    ameri = input("Sorry to subject you to non-american measurements, do you want the result in freedom units?(Y/N): ")
    american = ameri.lower()

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    eagle = kps_to_psi(pressure)

    if american == "y" or american=="yes":
        print("That's what I'm talking about 🦅")
        print(f"Pressure at house: {eagle:.1f} psi (Freedom) & {pressure:.1f} kilopascals (Non-Freedom)")
    else:
        print("Of course, my good sir 💂")
        print(f"Pressure at place of residence: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()
import math

def main():
    """Executes all the code needed for the program"""
    picnic = [6.83,	10.16, 0.28]
    tall = [7.78, 11.91, 0.43]
    two = [8.73, 11.59, 0.45]
    twohalf = [10.32, 11.91, 0.61]
    cylinder = [10.79, 17.78, 0.86]
    five = [13.02, 14.29, 0.83]
    sixz =	[5.40, 8.89, 0.22]
    short =	[6.83, 7.62, 0.26]
    ten = [15.72, 17.78, 1.53]
    twoeleven =	[6.83, 12.38, 0.34]
    three = [7.62, 11.27, 0.38]
    threethree = [8.10, 11.11, 0.42]
    print(f"#1 Picnic: {compute_storage_efficiency(picnic[0],picnic[1]):.2f}")
    print(f"#1 Tall: {compute_storage_efficiency(tall[0],tall[1]):.2f}")
    print(f"#2: {compute_storage_efficiency(two[0],two[1]):.2f}")
    print(f"#2.5: {compute_storage_efficiency(twohalf[0],twohalf[1]):.2f}")
    print(f"#3 Cylinder: {compute_storage_efficiency(cylinder[0],cylinder[1]):.2f}")
    print(f"#5: {compute_storage_efficiency(five[0],five[1]):.2f}")
    print(f"#6Z: {compute_storage_efficiency(sixz[0],sixz[1]):.2f}")
    print(f"#8Z short: {compute_storage_efficiency(short[0],short[1]):.2f}")
    print(f"#10: {compute_storage_efficiency(ten[0],ten[1]):.2f}")
    print(f"#211: {compute_storage_efficiency(twoeleven[0],twoeleven[1]):.2f}")
    print(f"#300: {compute_storage_efficiency(three[0],three[1]):.2f}")
    print(f"#303: {compute_storage_efficiency(threethree[0],threethree[1]):.2f}")


def compute_volume(radius, height):
    """Computes the volume of a given can, based on parameters"""
    return math.pi*(radius*radius)*height

def compute_surface_area(radius, height):
    """Computes the surface area of a given can, based on parameters"""
    return (math.pi*2)*radius*(radius+height)

def compute_storage_efficiency(radius,height):
    """Computes the storage efficiency of a given can"""
    volume = compute_volume(radius,height)
    surface_area = compute_surface_area(radius,height)
    return volume/surface_area

main()
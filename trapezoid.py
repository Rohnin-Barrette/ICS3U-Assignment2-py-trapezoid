#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sep 2021
# This program calculates the area and perimeter of a trapezoid


def main():

    # input
    a_base = int(
        input("Enter the length of the a base of the trapezoid (cm): ")
    )
    b_base = int(
        input("Enter the length of the b base of the trapezoid (cm): ")
    )
    c_side = int(
        input("Enter the length of the c side of the trapezoid (cm): ")
    )
    d_side = int(
        input("Enter the length of the d side of the trapezoid (cm): ")
    )
    height = int(input("Enter the height of the trapezoid (cm): "))

    # process
    area = ((a_base + b_base) / 2) * height
    perimeter = a_base + b_base + c_side + d_side

    # output
    print("")
    print("The area of the trapezoid is {0} cm².".format(area))
    print("The perimeter of the trapezoid is {0} cm.".format(perimeter))
    print("\nDone.")


if __name__ == "__main__":
    main()

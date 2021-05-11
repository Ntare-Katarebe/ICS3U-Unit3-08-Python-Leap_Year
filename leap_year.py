#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program tells you leap years
#    with numbers inputted from the user


def main():
    # This function tells tells you leap years

    # input
    leap_string = input("Please enter the year: ")
    print("")

    # process/output
    try:
        leap_year = int(leap_string)
        if (leap_year % 4) == 0:
            if (leap_year % 100) == 0:
                if (leap_year % 400) == 0:
                    print("{0} is a leap year".format(leap_year))
                else:
                    print("{0} is not a leap year".format(leap_year))
            else:
                print("{0} is a leap year".format(leap_year))
        else:
            print("{0} is not a leap year".format(leap_year))
    except Exception:
        print("{} is not an number".format(leap_string))
    finally:
        print("Thanks for trying")
    print("\nDone")


if __name__ == "__main__":
    main()

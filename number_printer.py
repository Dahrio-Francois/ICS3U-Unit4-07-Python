#!/usr/bin/env python3

# Created by: Andrew-Ten-Den
# Created on: May 2022
# This program uses a while statement to print numbers from
# 1000 to 2000, 5 numbers at a time


def main():
    # This function uses a while statement to print numbers from
    # 1000 to 2000, 5 numbers at a time

    integer = 1000
    counter = 0

    # process & output
    while integer < 1999:
        counter = counter + 1
        print(
            "{0} {1} {2} {3} {4}".format(
                integer, integer + 1, integer + 2, integer + 3, integer + 4
            )
        )
        integer = 1000 + (5 * counter)
    print("2000")


if __name__ == "__main__":
    main()

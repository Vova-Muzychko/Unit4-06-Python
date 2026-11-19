#!/usr/bin/env python3

# Created by: Vova M
# Created on: November19, 2026
# This program prints all valid RGB colours using nested loops


def main():
    # this function uses a nested loop to print all RGB colours

    counter1 = 0
    counter2 = 0
    counter3 = 0

    # process & output
    for counter1 in range(256):
        for counter2 in range(256):
            for counter3 in range(256):
                print(
                    "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(
                        counter1,
                        counter2,
                        counter3,
                        "RGB("
                        + str(counter1)
                        + ","
                        + str(counter2)
                        + ","
                        + str(counter3)
                        + ")",
                    )
                )


if __name__ == "__main__":
    main()

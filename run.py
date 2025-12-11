import sys
from helpers import Helpers

if __name__ == "__main__":
    if len(sys.argv) == 1:
        Helpers().print_usage()
    if len(sys.argv) <= 3:
        print("== == == ERROR: Invalid number of arguments == == ==")
        Helpers().print_usage()
        sys.exit(1)

    if "--year" in sys.argv and "-y" in sys.argv:
        print("== == == ERROR: Please specify only one of --year or -y == == ==")
        Helpers().print_usage()
        sys.exit(1)

    year = (
        Helpers().safe_flag(sys.argv, "--year") or
        Helpers().safe_flag(sys.argv, "-y") or
        2025
    )

    if "--round" in sys.argv and "-ro" in sys.argv:
        print("== == == ERROR: Please specify only one of --round or -ro == == ==")
        Helpers().print_usage()
        sys.exit(1)

    round_number = (
            Helpers().safe_flag(sys.argv, "--round") or
            Helpers().safe_flag(sys.argv, "-r") or
            1
    )

    if "--race" in sys.argv and "-r" in sys.argv:
        print("ERROR: Please specify only one of --race or -r")
        Helpers().print_usage()
        sys.exit(1)

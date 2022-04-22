"""spaceflights file for ensuring the package is executable
as `spaceflights` and `python -m spaceflights`
"""
import sys
from spaceflights import run


def main():
    run(sys.argv[1:])


if __name__ == "__main__":
    main()
    # sys.exit()

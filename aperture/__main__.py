"""Run Aperture with python -m aperture."""

import argparse

from aperture import __version__


def main():
    parser = argparse.ArgumentParser(
        prog="aperture",
        description="Aperture - Network diagnostics and authorized web self-hosting (in development).",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.parse_args()
    parser.print_help()


if __name__ == "__main__":
    main()

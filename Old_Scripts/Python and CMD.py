#!/usr/bin/python3

import argparse

def main():
    parser = argparse.ArgumentParser(description='Platform flag parser')
    parser.add_argument('-platform', type=str, help='Set the platform', required=True)
    args = parser.parse_args()

    print(f"Hello there. Platform selected: {args.platform}")

if __name__ == '__main__':
    main()
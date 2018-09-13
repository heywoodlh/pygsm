#!/usr/bin/env python3
import serial
import argparse

parser = argparse.ArgumentParser(description='Enable receiving phone calls')
parser.add_argument('-i', '--interface', help='serial interface', metavar='TTY', required=True)

args = parser.parse_args()


def main():
    phone = serial.Serial(args.interface, 115200, timeout=5)
    try:
        phone.write(b'AT+CLIP=1\r')
    finally:
        phone.close()

if __name__ == '__main__':
    main()

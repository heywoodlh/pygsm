#!/usr/bin/env python3
import serial
import time
import sys
import argparse

parser = argparse.ArgumentParser(description="Utility for dealing with calls over GSM via serial connection")

subparsers = parser.add_subparsers(help='make or receive calls', dest='command')


### Sender subparser

parser_make = subparsers.add_parser('make', help='make phone call')
parser_make.add_argument('-i', '--interface', help='serial interface', metavar='TTY', required=True)
parser_make.add_argument('-r', '--recipient', help='phone number to call', metavar='NUM', required=True)

### Reader subparser

parser_receive = subparsers.add_parser('receive', help='answer incoming phone calls')
parser_receive.add_argument('-i', '--interface', help='serial interface', metavar='TTY', required=True)


args = parser.parse_args()

def makeCall(phone, recipient):
    try:
        phone.write(b'ATD' + recipient.encode() + b';\r')
        fin = input('Type "end" to hang up\n')
        while fin not in ['end', '"end"']:
            fin = input('Type "end" to hang up\n')
        phone.write(b'ATH\r')
    finally:
        phone.close()

def answerCall():
    print('answer call function')

def main():
    phone = serial.Serial(args.interface, 115200, timeout=5)
    if sys.argv[1] == 'make':
        makeCall(phone, args.recipient)
    elif sys.argv[1] == 'receive':
        answerCall()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

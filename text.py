#!/usr/bin/env python3
import time
import serial
import argparse
import sys


parser = argparse.ArgumentParser(description="Utility for dealing with texts over GSM via serial connection")

subparsers = parser.add_subparsers(help='send or read messages', dest='command')


### Sender subparser

parser_send = subparsers.add_parser('send', help='send text messages')
parser_send.add_argument('-i', '--interface', help='serial interface', metavar='TTY', required=True)
parser_send.add_argument('-r', '--recipient', help='phone number to send to', metavar='NUM', required=True)
parser_send.add_argument('-m', '--message', help='message contents', metavar='MES')

### Reader subparser

parser_read = subparsers.add_parser('read', help='read text messages')
parser_read.add_argument('-i', '--interface', help='serial interface', metavar='TTY', required=True)



args = parser.parse_args()


def sendText(phone, recipient, message):
    try:
        time.sleep(0.5)
        phone.write(b'ATZ\r')
        time.sleep(0.5)
        phone.write(b'AT+CMGF=1\r')
        time.sleep(0.5)
        phone.write(b'AT+CMGS="' + recipient.encode() + b'"\r')
        time.sleep(0.5)
        phone.write(message.encode() + b"\r")
        time.sleep(0.5)
        phone.write(bytes([26]))
        time.sleep(0.5)
    finally:
        phone.close()


def main():
    phone = serial.Serial(args.interface, 115200, timeout=5)
    if sys.argv[1] == 'send':
        sendText(phone, args.recipient, args.message)
    elif sys.argv[1] == 'read':
        print('read')
    else: 
        parser.print_help()





if __name__ == '__main__':
    main()

#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-H", "--Host", dest="tgtHost", help="specify a target host")
parser.add_argument("-p", "--port", dest="tgtPort", type=int, help="specify a target port")
args = parser.parse_args()

print args.tgtHost, args.tgtPort

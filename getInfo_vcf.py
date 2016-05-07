#!/usr/bin/env python
#-*- coding: utf-8 -*-

import binascii
import string

inFileName = ""
inFileStream = open(inFileName, "r")
outFileName = "AddressBook.txt"
outFileStream = open(outFileName, "w")

lines = inFileStream.readlines()

for line in lines:
    number = None
    name = None
    if line[0:2] == 'FN':
        if line[2] == ';':
            name = line[43:-1].replace('=', '')
            name = binascii.a2b_hex(name)
        elif line[2] == ':':
            name = line[3:-1].replace('=', '')
            #name = binascii.a2b_hex(name)
        outFileStream.write(name + '\n')
    elif line[0:3] == 'TEL':
        startIndex = line.index(':') + 1
        number =  line[startIndex:-1].replace('-', '')
    if number != None:
        outFileStream.write(number + '\n')
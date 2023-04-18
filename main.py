import parse
import os, sys

try:
    if len(sys.argv) < 2:
        i = 0
        while True:
            i += 1
            cmd = input("> ")
            parse.parse_line(cmd, i)
    else:
        parse.parse_document(sys.argv[1])
except IndexError:
    None

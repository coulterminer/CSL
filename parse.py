import datetime
import os
import sys
import socket
import platform

parser_config = {"Version":""}

string_storage = {}
int_storage = {}
bool_storage = {}

def parse_document(path):
    f = open(path, "r")
    fl = f.readlines()

    for x in fl:
        if x.split()[0] == "@CSL":
            parser_config["Version"] = x.split()[1]
        
        if x.split()[0] == "call":
            if x.split()[1] == "time":
                if x.split()[2] == "now":
                    print(datetime.datetime.now())
        
        if x.split()[0] == "string":
            if x.split()[1] == "new":
                if x.split()[3] == "=":
                    string_storage[x.split()[2]] = x.split()[4]
                    print(string_storage)
        
        if x.split()[0] == "int":
            if x.split()[1] == "new":
                try:
                    if x.split()[3] == "=":
                        int_storage[x.split()[2]] = int(x.split()[4])
                        print(int_storage)
                except ValueError:
                    print("Cannot define an int like that")
        
        if x.split()[0] == "bool":
            if x.split()[1] == "new":
                try:
                    if x.split()[3] == "=":
                        bool_storage[x.split()[2]] = bool(x.split()[4])
                        print(bool_storage)
                except ValueError:
                    print("Cannot define an int like that")

        if x.split()[0] == "CONCLEAR":
            if platform.system != "Windows":
                os.system("clear")
            else:
                os.system("cls")

        
        if x.split()[0] == "out":
            message = x.split()
            message.pop(0)
            
            print(' '.join(message))

def parse_line(line, line_no):
    if line.split()[0] == "out":
        message = line.split()
        message.pop(0)
        print(message)
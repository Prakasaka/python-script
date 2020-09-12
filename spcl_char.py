#!/usr/bin/env python3

from random import choice
import argparse

# colors for strings
def bold(bold): return f"\033[1;0m{bold}\033[0m"
def red(red): return f"\033[1;31m{red}\033[0m"
def green(green): return f"\033[1;32m{green}\033[0m"

# Main function for replace some normal characters with special characters
def nor_to_spcl():
    char = name.replace('a', '4')
    char = char.replace('c', '<')
    char = char.replace('e', '3')
    char = char.replace('h', '#')
    char = char.replace('i', '!')
    char = char.replace('o', '0')
    char = char.replace('s', '$')
    char = char.replace('t', '7')
    print(green(f"\nYour special string - {char}"))

# This function for limiting characters
def char_limit():
    if len(name) <= 1:
        print(red("Use minimum 2 or more characters"))
    elif len(name) < 25:
        nor_to_spcl()
    else:
        print(red("You can't use more than 25 characters"))

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument('-s', action='store', help='Replace some normal characters (from a string) with special characters')
args = parser.parse_args()

# Here i defined characters limit only for Arguments. In input we can use unlimited characters
if not args.s:
    name = input(bold("Enter your string : ")).lower()
    if len(name) <= 1:
        print(red("Use minimum 2 or more characters"))
    else:
        nor_to_spcl()
else:
    name = args.s.lower()
    char_limit()

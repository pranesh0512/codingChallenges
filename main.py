#!/usr/bin/env python


import argparse
import sys


class CCWC:

    def __init__(self, filename):
        self.filename = filename

    def count_bytes(self):
        try:
            if self.filename:
                with open(self.filename, 'rb') as file:
                    byte_count = len(file.read())
            else:
                byte_count = len(sys.stdin.read().encode())
            return byte_count
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found")
            return -1

    def count_lines(self):
        try:
            if self.filename:
                with open(self.filename, 'r') as file:
                    line_count = sum(1 for line in file)
            else:
                line_count = sum(1 for line in sys.stdin)
            return line_count
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return -1

    def count_words(self):
        try:
            if self.filename:
                with open(self.filename, 'r') as file:
                    content = file.read()
                    word_count = len(content.split())
            else:
                word_count = len(sys.stdin.read().split())
            return word_count
        except Exception as e:
            print(f"Error: file '{self.filename}' not found")
            return -1

    def count_characters(self):
        try:
            if self.filename:
                with open(self.filename, 'r') as file:
                    content = file.read()
                    char_count = len(content)
            else:
                char_count = len(sys.stdin.read())
            return char_count
        except FileNotFoundError:
            print(f"Error: file '{self.filename}' not found")
            return -1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count the number of bytes and arguments in a file')
    parser.add_argument('filename', nargs='?', help='Name of the file to count bytes in.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c', action='store_true', help='Count bytes')
    group.add_argument('-l', action='store_true', help='Count lines')
    group.add_argument('-w', action='store_true', help='Count words')
    group.add_argument('-m', action='store_true', help='Count characters')
    args = parser.parse_args()

    if not any([args.c, args.l, args.w, args.m]):
        args.c = args.l = args.w = args.m = True
    if args.filename:
        ccwc = CCWC(args.filename)
    else:
        ccwc = CCWC(None)

    if args.c:
        byte_count = ccwc.count_bytes()
        if byte_count != -1:
            print(f"Number of bytes in '{args.filename}': {byte_count}")

    if args.l:
        line_count = ccwc.count_lines()
        if line_count != -1:
            print(f"Number of lines in '{args.filename}': {line_count}")

    if args.w:
        word_count = ccwc.count_words()
        if word_count != -1:
            print(f"Number of words in '{args.filename}': {word_count}")

    if args.m:
        character_count = ccwc.count_characters()
        if character_count != -1:
            print(f"Number of characters in '{args.filename}': {character_count}")

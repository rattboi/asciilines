#!/usr/bin/env python3.7

import argparse
import sys

class Tvg:
    def __init__(self):
        self.canvas_y = 0
        self.canvas_x = 0
        self.vectors = []

    def set_dimensions(self, y, x):
        self.canvas_y = int(y)
        self.canvas_x = int(x)

    def add_vectors(self, vectors):
        for v in vectors:
            self.vectors.append(v)

    def valid_vector(pot_vec):
        if len(pot_vec) != 5:
            return False

        # decompose vector into components
        char, col, row, drc, length = pot_vec

        # verify char is 1 character long
        if len(char) != 1:
            return False
        # verify col is an int
        try:
            int(col)
        except ValueError:
            return False
        # verify row is an int
        try:
            int(row)
        except ValueError:
            return False
        # verify drc is h/v
        if drc not in ['h', 'v']:
            return False
        # verify length is int and > 0
        try:
            a = int(length)
            if a < 1:
                return False
        except ValueError:
            return False

        # if we've gotten this far, it's probably a vector
        return True

    def parse(self, filename):
        with open(filename, "r") as tvgfile:
            try:
                canvas_dimensions = tvgfile.readline().split()
                self.set_dimensions(canvas_dimensions[0], canvas_dimensions[1])
            except IndexError as e:
                print("ERROR: Couldn't parse canvas dimensions")
                sys.exit(1)
            vectors = [v.split() for v in tvgfile if Tvg.valid_vector(v.split())]
            self.add_vectors(vectors)

    def render(self):
        # initialize the canvas
        canvas = []
        for y in range(self.canvas_y):
            new = []
            for x in range(self.canvas_x):
                new.append('.')
            canvas.append(new)

        for v in self.vectors:
            char, row, col, drc, length = v
            row = int(row)
            col = int(col)
            length = int(length)
            if drc == 'h':
                col_start = col
                col_end = col + length
                if (row >= 0 and row < self.canvas_y):
                    for x in range(col_start, col_end):
                        if (x >= 0 and x < self.canvas_x):
                            canvas[row][x] = char
            else:
                row_start = row
                row_end = row + length
                if (col >= 0 and col < self.canvas_x):
                    for y in range(row_start, row_end):
                        if (y >= 0 and y < self.canvas_y):
                            canvas[y][col] = char

        for y in range(self.canvas_y):
            for x in range(self.canvas_x):
                print(canvas[y][x], end = '')
            print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse and render a TVG (Text Vector Graphics) file to stdout')
    parser.add_argument('filename', metavar='FILENAME', help='the TVG file to parse and render')
    args = parser.parse_args()

    tvg = Tvg()
    tvg.parse(args.filename)
    tvg.render()

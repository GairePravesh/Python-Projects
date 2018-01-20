'''
Pravesh Gaire

Python3.5 regex

filtering gcode data using simple regex implementation to find x and y coordinates
'''

import re
numbers = []

def append_if_different(x, y):
    if not numbers or (x, y) != numbers[-1]:
        numbers.append((x, y))

with open("g_code.nc","r") as inp:
    for line in inp:
        matches = re.findall(r'[XY]([-+]?\d+)', line)
        if len(matches) == 2:
            append_if_different(int(matches[0]), int(matches[1]))

with open("test.txt", "w") as outp:
    for xy in numbers:
        outp.write("{} {}\n".format(*xy))


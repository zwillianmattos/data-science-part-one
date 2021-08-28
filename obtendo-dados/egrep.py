import sys, re

regex = sys.arg[1]

for line in sys.stdin:
    if re.search(regex, line):
        sys.stdout.write(line)
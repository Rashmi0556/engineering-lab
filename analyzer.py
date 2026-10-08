import sys

filename = sys.argv[1]
count = 0

with open(filename) as f:
    for line in f:
        if line.strip():
            count += 1

print(f"Total requests: {count}")
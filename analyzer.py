import sys

filename = sys.argv[1]
total = 0
status_counts = {}
path_counts = {}

with open(filename) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        date, time, method, path, status = line.split()
        total += 1
        status_counts[status] = status_counts.get(status, 0) + 1
        path_counts[path] = path_counts.get(path, 0) + 1

print(f"Total requests: {total}")

print("\nStatus codes:")
for status, n in sorted(status_counts.items()):
    print(f"  {status}: {n}")

print("\nTop 3 paths:")
top = sorted(path_counts.items(), key=lambda x: x[1], reverse=True)[:3]
for path, n in top:
    print(f"  {path}: {n}")
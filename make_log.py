import random
paths = ["/api/login", "/api/users", "/api/orders", "/home", "/api/pay"]
codes = [200, 200, 200, 404, 500]
with open("sample.log", "w") as f:
    for i in range(20):
        f.write(f"2026-10-08 10:{i:02d}:22 GET {random.choice(paths)} {random.choice(codes)}\n")
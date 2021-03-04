#!/usr/bin/env python3

from datetime import datetime

start = datetime.now()
print("Please look up the value of Pi on the internet.")
print()

val = input("Enter your value: ")
end = datetime.now()

print("value:", val)
print("duration:", end-start)

with open("internet.yaml", "w") as f:
    f.write(f"value: \"{val}\"\n")
    f.write(f"duration: {end-start}\n")

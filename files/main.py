import dolphin_memory_engine as dme
import random
import time

target_address = input("Enter the address to randomize (hex, e.g., 0x8053A381): ").strip()
min_val = input("Enter minimum value (decimal): ").strip()
max_val = input("Enter maximum value (decimal): ").strip()

try:
    target_address = int(target_address, 16)
    min_val = int(min_val)
    max_val = int(max_val)
except ValueError:
    print("Invalid input! Address must be hex, values must be integers.")
    exit(1)

if not dme.is_hooked():
    print("Hooking Dolphin...")
    dme.hook()

print(f"Randomizing address {hex(target_address)} between {min_val} and {max_val}...")
UPDATE_DELAY = 0.01666

try:
    while True:
        value = random.randint(min_val, max_val)
        dme.write_byte(target_address, value)
        time.sleep(UPDATE_DELAY)
except KeyboardInterrupt:
    print("Stopped.")
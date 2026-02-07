import dolphin_memory_engine as dme
import random
import time

ADDRESSES = [
    0x80428A9A,
    0x80428A9C,
    0x80428A9E,
    0x80428AA0
]

MIN_VAL = 0
MAX_VAL = 160
UPDATE_DELAY = 0.01666

if not dme.is_hooked():
    print("Hooking Dolphin...")
    dme.hook()

print(f"Randomizing {len(ADDRESSES)} halfword addresses between {MIN_VAL} and {MAX_VAL}...")

try:
    while True:
        for addr in ADDRESSES:
            value = random.randint(MIN_VAL, MAX_VAL)
            value_bytes = value.to_bytes(2, byteorder='big')
            dme.write_bytes(addr, value_bytes)
        time.sleep(UPDATE_DELAY)
except KeyboardInterrupt:
    print("Stopped.")

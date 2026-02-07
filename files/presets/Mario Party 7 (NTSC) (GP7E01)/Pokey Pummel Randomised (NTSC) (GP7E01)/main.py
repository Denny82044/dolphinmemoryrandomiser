import dolphin_memory_engine as dme
import random
import time

ADDRESSES = [
    0x80540981,
    0x80540A61,
    0x8053A381,
    0x80540B41
]

MIN_VAL = 0
MAX_VAL = 4
UPDATE_DELAY = 0.01666

if not dme.is_hooked():
    print("Hooking Dolphin...")
    dme.hook()

print(f"Randomizing {len(ADDRESSES)} addresses between {MIN_VAL} and {MAX_VAL}...")

try:
    while True:
        for addr in ADDRESSES:
            value = random.randint(MIN_VAL, MAX_VAL)
            dme.write_byte(addr, value)
        time.sleep(UPDATE_DELAY)
except KeyboardInterrupt:
    print("Stopped.")

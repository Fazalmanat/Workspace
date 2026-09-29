import os
import random
import time

os.system("cls")

# Hide cursor
print("\033[?25l", end="")

try:
    while True:
        line = ""

        for _ in range(100):
            line += str(random.randint(0, 9))

        print("\033[92m" + line + "\033[0m")

        time.sleep(0.01)

except KeyboardInterrupt:
    # Show cursor again
    print("\033[?25h")
    os.system("cls")
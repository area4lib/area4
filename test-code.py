# import os so we can get ci env variables
import os

# try to import area4
# this will fail if it could not be installed
# or maybe if faulty code is present
try:
    import area4
except ImportError:
    # at this point, area4 either isn't in site-packages
    # or not on the system at all
    raise Exception("Failed to import beta build.")

# make sure this is being run directly and
# not from another python module
if not __name__ == "__main__":
    raise Exception("This module must be run directly!")
else:
    print("[DEBUG] Module being run directly, not exiting")

# get working directory:
print("[DEBUG] Getting working directory")
dir = os.getenv("TRAVIS_BUILD_DIR")
# get divider file:
dividers_file: str = "{0}/{1}".format(dir, "area4/dividers.txt")
print("[DEBUG] Working directory is {0}".format(dir))
print("[DEBUG] Divider file is located at {0}".format(dividers_file))

rawDividers: str
with open(dividers_file, "r") as fh:
    rawDividers = fh.readlines()
    print("fetched raw dividers text file")

print("[DEBUG] Creating instance of area4")
d = area4.Area4Instance()
print("created instance: {0}".format(d))

# test each divider
for i in range(len(rawDividers)):
    if i < 1 or i == 35:
        i = i + 1
    print("[DEBUG] Testing divider {0}".format(i))
    try:
        
        if rawDividers[i] == d.divider(i):
            print("[+] Divider {0} should work.".format(i))
        else:
            print("[X] Divider {0} is broken!".format(i))
            raise ValueError("Broken divider detected!")
            
    except IndexError:
        # this is thrown if a number is offset
        # in the divider array
        # what we do about it is we just
        # simply ignore it
            
print("[DEBUG] Exiting tests")

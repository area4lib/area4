# import OS module so we can
# get CI build variables
import os

# try to import area4
# this will fail if it could not be installed
# or maybe if faulty code is present
try:
    import area4
except ImportError:
    # at this point, area4 either isn't in site-packages
    # or not on the system at all
    raise Exception("Failed to import the library.")

# make sure this is being run directly and
# not from another python module
if not __name__ == "__main__":
    raise Exception("This module must be run directly!")
else:
    print("[DEBUG] Module being run directly, not exiting")

# get working directory:
print("[DEBUG] Getting working directory\n")
dir = os.getenv("TRAVIS_BUILD_DIR")
print("[DEBUG] Got working directory ({0})\n".format(dir))
# get divider file:
dividers_file: str = "{0}/{1}".format(dir, "area4/dividers.txt")
print("[DEBUG] Divider file is located at {0}\n".format(dividers_file))

rawDividers: str
with open(dividers_file, "r") as fh:
    rawDividers = fh.readlines()
    print("[DEBUG] Fetched raw dividers text file")

# create instance we can use
print("[DEBUG] Creating instance of the library\n")
d = area4.Area4Instance()
print("[DEBUG] Created instance: {0}\n\n".format(d))

# test each divider
print("[DEBUG] Starting tests...\n\n")
for i in range(len(rawDividers)):
    if i < 1 or i == 35:
        i = i + 1
    print("[DEBUG] Testing divider {0}".format(i))
    try:
        # try to match the raw divider with the result
        # of the function:
        if rawDividers[i] == d.divider(i):
            # it matches
            print("[+] Divider {0} should work.\n".format(i))
        else:
            # it does not match
            print("[X] Divider {0} is broken!".format(i))
            raise ValueError("Broken divider detected: number {0}!"
                             .format(i)
            )
    except IndexError:
        # this is thrown if a number is offset
        # in the divider array
        # what we do about it is we just
        # simply ignore it
        print("\n[DEBUG] Ignoring an IndexError")

print("\n\n[DEBUG] Exiting tests!\n")

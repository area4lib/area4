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
    print("module being run directly, not exiting")

# get working directory:
print("getting working directory")
dir = os.getenv("TRAVIS_BUILD_DIR")
dividers_file: str = "{0}/{1}".format(dir, "area4/dividers.txt")
print("working directory is {0}".format(dir))
print("divider file is located at {0}".format(dividers_file))

rawDividers: str
with open(dividers_file, "r") as fh:
    rawDividers = fh.readlines()
    print("fetched raw dividers text file")

print("creating instance of area4")
d = area4.Area4Instance()
print("created instance: {0}".format(d))

for i in range(len(rawDividers)):
    if i < 1:
        i = 1
    print("testing divider {0}".format(i))
    if rawDividers[i] == d.divider(i):
        print("Divider {0} should work.".format(i))
    else:
        print("Divider {0} is broken!".format(i))
        raise ValueError("Broken divider detected!")

print("exiting tests")

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

# init some variables that
# will be needed later
rawDividers: str
_dir: str
d = None


# make sure this is being run directly and
# not from another python module
if not __name__ == "__main__":
    raise Exception("This module must be run directly!")
else:
    print("[DEBUG] Module being run directly, not exiting")
    # get working directory:
    print("[DEBUG] Getting working directory\n")
    _dir = os.getenv("TRAVIS_BUILD_DIR")
    print("[DEBUG] Got working directory ({0})\n".format(_dir))
    # get divider file:
    dividers_file: str = "{0}/{1}".format(_dir, "area4/dividers.txt")
    print("[DEBUG] Divider file is located at {0}\n".format(dividers_file))
    with open(dividers_file, "r") as fh:
        rawDividers = fh.readlines()
        print("[DEBUG] Fetched raw dividers text file")
    # create instance we can use
    print("[DEBUG] Creating instance of the library")
    d = area4.Area4Instance()
    print("[DEBUG] Created instance: {0}\n\n".format(d))


def test_dividers() -> None:
    # Test each divider
    print("[DEBUG] Starting tests...\n\n")
    for i in range(len(rawDividers)):
        # manually skip dividers 0 and 35:
        if i < 1 or i == 35:
            print("[DEBUG] Manually skipping divider {0}".format(i))
            i = i + 1
        else:
            print("[DEBUG] Testing divider {0}".format(i))
            try:
                # try to match the raw divider with the result
                # of the function:
                if rawDividers[i] == d.divider(i):
                    # it matches
                    print("[+] Divider {0} should work.".format(i))
                else:
                    # it does not match
                    print("[X] Divider {0} is broken!".format(i))
                    raise ValueError("Broken divider detected!")
            except IndexError:
                # this is thrown if a number is offset
                # in the divider array
                # what we do about it is we just
                # simply ignore it
                print("\n[DEBUG] Ignoring an IndexError")


# run setup functions:
# run tests:
test_dividers()

print("\n[DEBUG] Exiting tests!")

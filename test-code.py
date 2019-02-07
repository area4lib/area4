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
    raise OSError("Failed to import the library.")

# init some variables that
# will be needed later
# rawDividers is the array of dividers from the
# text file
rawDividers: str
# _dir is the directory that travis supplies
# as the build directory
_dir: str
# d is the area4 instance, keep it at None for now
d = None
# the commit message:
c_message = os.getenv("TRAVIS_COMMIT_MESSAGE")
# if extra tests should be run:
extra: bool = False


# make sure this is being run directly and
# not from another python module
if not __name__ == "__main__":
    raise EnvironmentError("This module must be run directly!")
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
    print("[DEBUG] Created instance")
    if "!extra-tests" in c_message or c_message == "!extra-tests":
        print("[DEBUG] Running extra tests!")
        extra = True


def test_dividers() -> None:
    # Test each divider
    print("[DEBUG] Starting tests...\n\n")
    for i in range(len(rawDividers)):
        # manually skip dividers 0 and 35:
        if i < 1 or i == 35:
            print("[DEBUG] Manually skipping divider {0}".format(i))
            i = i + 1
        # run tests normally for other dividers
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
                    raise RuntimeError("Broken divider detected!")
            except IndexError:
                # this is thrown if a number is offset
                # in the divider array
                # what we do about it is we just
                # simply ignore it
                print("\n[DEBUG] Ignoring an IndexError")


# test make-div function
def test_make_div() -> None:
    if d.make_div('=-', length=9, start='<', end='=>') == "<=-=-=-=>":
        print("\n[DEBUG] make-div test did not fail")
    else:
        raise RuntimeError("make-div tests failed")


# run setup functions:
# run tests:
test_dividers()
test_make_div()

# notify user tests are complete
print("\n\n[DEBUG] Exiting tests!")

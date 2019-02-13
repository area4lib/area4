"""Runs code tests in a CI environment."""

# import OS module so we can
# get CI build variables
import os
import restructuredtext_lint

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
c_message = os.getenv("CIRRUS_CHANGE_MESSAGE")
if c_message is None:
    raise EnvironmentError("No commit name detected!")
# if extra tests should be run:
extra: bool = False

# make sure this is being run directly and
# not from another python module
if not __name__ == "__main__":
    raise EnvironmentError("This module must be run directly!")
else:
    # if this is being run directly,
    # set up for tests
    print("[DEBUG] Module being run directly, not exiting")
    # get working directory:
    print("[DEBUG] Getting working directory\n")
    _dir = os.getenv("CIRRUS_WORKING_DIR")
    print("[DEBUG] Got working directory ({0})\n".format(_dir))
    # get divider file:
    dividers_file: str = "{0}/{1}".format(_dir, "area4/dividers.txt")
    print("[DEBUG] Divider file is located at {0}\n".format(dividers_file))
    with open(dividers_file, mode="r") as fh:
        rawDividers = fh.readlines()
        print("[DEBUG] Fetched raw dividers text file")
    # create instance we can use
    print("[DEBUG] Creating instance of the library")
    d = area4.Area4Instance()
    print("[DEBUG] Created instance")
    # see if we need to run extra tests
    if "!extra" in c_message or c_message == "!extra":
        print("[DEBUG] Running extra tests!")
        extra = True


# divider tests:
def test_dividers() -> None:
    """
    Test each divider against the raw ones from the text file.

    :return: None
    """
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
                if rawDividers[i].split("\n")[0] == d.divider(i):
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


# make-div tests
def test_make_div() -> None:
    """
    Tests the make-div function.

    :return: None
    """
    if d.make_div('=-', length=9, start='<', end='=>') == "<=-=-=-=>":
        print("\n[DEBUG] make-div test did not fail")
    else:
        raise RuntimeError("make-div tests failed")


# extra test:
# validate info variables
def test_info() -> None:
    """
    Tests the info variables. This is an extra test.

    :return: None
    """
    right_data = [
        "area4",
        "https://github.com/RDIL",
        "me@rdil.rocks",
        "support@rdil.rocks",
        "Dividers in Python, the easy way!"
    ]
    from_class = [
        d.name,
        d.author,
        d.author_email,
        d.support_email,
        d.description
    ]
    print("\n[DEBUG] Running extra test for package info")
    for x in range(
        len(right_data)
    ):
        if not right_data[x] == from_class[x]:
            raise RuntimeError("[X] Failed package info test {0}".format(x))
        else:
            print("[+] Data item {0} works".format(x))


def rst_lint_run() -> None:
    """
    Lints all reStructuredText files. This is an extra check.

    :return: None
    """
    print("\n[DEBUG] Running RST linting")
    files = os.listdir("{0}/docs".format(_dir))
    for name in files:
        restructuredtext_lint.lint_file("{0}/docs/{1}".format(_dir, name))


def travis_config_lint() -> None:
    """
    Lints the Travis CI config file. This is an extra check.

    :return: None
    """
    print("\n[DEBUG] Linting Travis CI config")
    os.system("travislint --verbose .travis.yml")


def extra_tests() -> None:
    """
    Run the extra checks/tests.

    :return: None
    """
    test_info()
    rst_lint_run()
    travis_config_lint()


# run setup functions:
# run tests:
test_dividers()
test_make_div()
if extra:
    # run extra tests if the commit
    # messages match
    extra_tests()

# notify user tests are complete
print("\n[DEBUG] Exiting tests!")

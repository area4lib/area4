"""Runs code tests in a CI environment."""

# Import needed modules
import os
import restructuredtext_lint

# Try to import area4.
# This will fail if it could not be installed or if faulty code is present.
try:
    import area4
except ImportError:
    # At this point, area4 either isn't in site-packages,
    # or not on the system at all.
    raise OSError("Failed to import the library.")

# Create some variables that will be needed later.
# rawDividers is the array of dividers from the text file
rawDividers = None

# _dir is the directory that the CI supplies as the build directory.
_dir = None

# d is the area4 instance
d = None

# Get commit message:
c_message = os.getenv("CIRRUS_CHANGE_MESSAGE")
if c_message is None:
    raise EnvironmentError("No commit name detected!")

# Get the branch:
repo_branch = os.getenv("CIRRUS_BRANCH")
if repo_branch is None:
    raise EnvironmentError("Branch unknown")

# Make the fetched values lowercase:
c_message = c_message.lower()
repo_branch = repo_branch.lower()

# Check if extra tests should be run:
extra = False


# Function to send debug messages to the console:
def debug(message):
    """
    Log a debug message.

    :return: None
    :param message: the message to log
    """
    print("{0}{1}{2}{3}".format("[Verbose]", " ", message, "."))


# Make sure this is being run directly, and
# not from another python module:
if __name__ != "__main__":
    raise EnvironmentError("This module must be run directly!")
else:
    # If this is being run directly, set up for tests:
    debug("Module being run directly, not exiting")
    # Get working directory:
    debug("Getting working directory")
    _dir = os.getenv("CIRRUS_WORKING_DIR")
    debug("Got working directory ({0})".format(_dir))
    # Get divider text file:
    dividers_file = "{0}/{1}".format(_dir, "area4/dividers.txt")
    debug("Divider file is located at {0}".format(dividers_file))
    with open(dividers_file, mode="r") as fh:
        rawDividers = fh.readlines()
        debug("Fetched raw dividers text file")
    # Create instance:
    debug("Creating instance of the library")
    d = area4.Area4Instance()
    debug("Created instance")

    # See if we need to run extra tests:
    if ("!e" in c_message or c_message == "!e") or \
            (repo_branch == "master"):
        debug("Running extra tests")
        extra = True
    else:
        extra = False


def test_dividers():
    """
    Test each divider against the raw ones from the text file.

    :return: None
    """
    for i, item in enumerate(rawDividers):
        if i < 1 or i == 35:
            debug("Manually skipping divider {0}".format(i))
            # Manually skip dividers 0 and 35:
            i = i + 1
        else:
            debug("Testing divider {0}".format(i))
            try:
                # Try to match the raw divider with the result
                # of the function:
                if rawDividers[i].split("\n")[0] == d.divider(i):
                    debug("[+] Divider {0} should work".format(i))
                else:
                    debug("[X] Divider {0} is broken".format(i))
                    raise RuntimeError("Broken divider detected!")
            except IndexError:
                # This is thrown if a number is offset in the divider array.
                # What we do about it is we just simply ignore it
                debug("Ignoring an IndexError")


def test_make_div():
    """
    Tests the make-div function.

    :return: None
    """
    if d.make_div('=-', length=9, start='<', end='=>') == "<=-=-=-=>":
        debug("make-div test did not fail")
    else:
        raise RuntimeError("make-div tests failed")


def test_info():
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
    debug("Running extra test for package info")
    for x, xx in enumerate(right_data):
        if not right_data[x] == from_class[x]:
            raise RuntimeError("[X] Failed package info test {0}".format(x))
        else:
            debug("[+] Data item {0} works".format(x))


def rst_lint_run():
    """
    Lints all reStructuredText files. This is an extra check.

    :return: None
    """
    debug("Running reStructuredText linting.")
    files = os.listdir("{0}/docs".format(_dir))
    for name in files:
        restructuredtext_lint.lint_file("{0}/docs/{1}".format(_dir, name))


# Run tests:
test_dividers()
test_make_div()
if extra:
    # Run extra tests if needed:
    test_info()
    rst_lint_run()

debug("Finished tests")

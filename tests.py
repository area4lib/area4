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

# RAW_DIVIDERS is the array of dividers from the text file
RAW_DIVIDERS = None

# WORKING_DIRECTORY is the place that the tests are running in.
WORKING_DIRECTORY = None

# Determine if this is a tag build:
tag = (os.getenv("CIRRUS_TAG") is not None) and \
      (os.getenv("CIRRUS_TAG") != "")

# Determine if this is a Pull Request build:
pull = (not tag) and \
       (os.getenv("CIRRUS_PR") is not None) and \
       (os.getenv("CIRRUS_PR") != "")

# Get commit message:
COMMIT_MESSAGE = os.getenv("CIRRUS_CHANGE_MESSAGE")
if COMMIT_MESSAGE is None:
    raise EnvironmentError("No commit name detected!")

# Get the branch:
REPO_BRANCH = os.getenv("CIRRUS_BRANCH")
if REPO_BRANCH is None:
    raise EnvironmentError("Branch unknown")

# Get the target:
TARGET = os.getenv("TARGET")

# Make the fetched values lowercase:
COMMIT_MESSAGE = COMMIT_MESSAGE.lower()
REPO_BRANCH = REPO_BRANCH.lower()
if TARGET is not None:
    TARGET = TARGET.lower()

# Check if extra tests should be run:
EXTRA_TESTS = False


# Function to send debug messages to the console:
def debug(message):
    """
    Log a debug message.

    :return: None
    :param message: the message to log
    """
    print("[Verbose] {0}.".format(message))


# Make sure this is being run directly, and
# not from another python module:
if __name__ != "__main__":
    raise EnvironmentError("This module must be run directly!")
else:
    # If this is being run directly, set up for tests:
    debug("Module being run directly, not exiting")
    # Get working directory:
    WORKING_DIRECTORY = os.getenv("CIRRUS_WORKING_DIR")
    if WORKING_DIRECTORY is None:
        WORKING_DIRECTORY = os.path.abspath(
            os.path.dirname(__file__)
        )
        if WORKING_DIRECTORY is None:
            raise EnvironmentError("Could not find working directory!")
    debug("Got working directory ({0})".format(WORKING_DIRECTORY))
    if (TARGET != "safety") and \
       (TARGET != "rst") and \
       (TARGET != "pull_request"):
        # Get divider text file:
        DIVIDERS_FILE = "{0}/{1}".format(
            WORKING_DIRECTORY,
            "area4/dividers.txt"
        )
        debug("Divider file is located at {0}".format(
            DIVIDERS_FILE)
        )
        try:
            with open(file=DIVIDERS_FILE, mode="r") as fh:
                RAW_DIVIDERS = fh.readlines()
                debug("Fetched raw dividers text file")
        except FileNotFoundError:
            raise EnvironmentError("Raw divider file not found!")

        # See if we need to run extra tests:
        if (
            ("!e" in COMMIT_MESSAGE or COMMIT_MESSAGE == "!e") or
                (REPO_BRANCH == "master") or tag
        ) and TARGET != "all":
            debug("Running extra tests")
            EXTRA_TESTS = True
        else:
            EXTRA_TESTS = False


def test_dividers():
    """
    Test each divider against the raw ones from the text file.

    :return: None
    """
    for i, item in enumerate(RAW_DIVIDERS):
        if i < 1 or i == 35:
            debug("Manually skipping divider {0}".format(i))
            # Manually skip dividers 0 and 35:
            i = i + 1
        else:
            try:
                # Try to match the raw divider with the result
                # of the function:
                if RAW_DIVIDERS[i].split("\n")[0] == area4.divider(i):
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
    if area4.make_div('=-', length=9, start='<', end='=>') == "<=-=-=-=>":
        debug("make-div test passed")
    else:
        raise RuntimeError("make-div tests failed")


def test_splitter():
    """
    Test splitter function.

    :return None:
    """
    debug("Running splitter tests")
    if not area4.splitter("---", "Hello") == "Hello":
        raise RuntimeError("splitter test failed")
    else:
        debug("Test of splitter passed")


def test_utilities():
    """
    Test utility module.

    :return: None
    """
    util_module = area4.util_module
    if not util_module.check(__name__) and \
            util_module.get_divider_character(7) == "=" and \
            util_module.redditHorizontal() \
            != "*****":
        raise RuntimeError("Utility module tests failed")
    else:
        debug("Utilities module tests passed")


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
        area4.name,
        area4.author,
        area4.author_email,
        area4.support_email,
        area4.description
    ]
    debug("Running extra test for package info")
    for the_location, place_holder in enumerate(right_data):
        if not right_data[the_location] == from_class[the_location]:
            raise RuntimeError("[X] Failed package info test {0}"
                               .format(the_location)
                               )
        else:
            debug("[+] Data item {0} works".format(the_location))


def rst_lint_run():
    """
    Lints all reStructuredText files. This is an extra check.

    :return: None
    """
    debug("Running reStructuredText linting")
    files = os.listdir("{0}/docs".format(WORKING_DIRECTORY))
    for name in files:
        path = "{0}/docs/{1}".format(WORKING_DIRECTORY, name)
        restructuredtext_lint.lint_file(filepath=path)


def safety_run():
    """
    Run SafetyCI by PyUp.

    :return: None
    """
    results = os.system("make safetyci")
    debug("SafetyCI exited with code {0}".format(results))
    if results == 1 or results == "1":
        raise RuntimeError("SafetyCI failed!")


def pr():
    """
    Check PR for issues.

    :return None:
    """
    if "blocked" in os.getenv("CIRRUS_CHANGE_MESSAGE").lower():
        raise OSError("Pull Request not ready for merge!")


if TARGET == "code":
    # Run tests:
    test_dividers()
    test_make_div()
    test_splitter()
    test_utilities()
    if EXTRA_TESTS:
        # Run extra tests if needed:
        test_info()
elif TARGET == "rst":
    rst_lint_run()
elif TARGET == "safety":
    safety_run()
elif TARGET == "pull_request" and pull:
    pr()
elif TARGET == "all":
    debug("Running ALL tests")
    test_dividers()
    test_make_div()
    test_splitter()
    test_utilities()
    test_info()
    rst_lint_run()
    safety_run()
    if pull:
        pr()
else:
    raise EnvironmentError("No tests specified!")

debug("Finished tests")

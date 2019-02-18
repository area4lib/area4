"""Runs code tests in a CI environment."""

# Import OS module so we can get CI build variables
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
rawDividers: str

# _dir is the directory that the CI supplies as the build directory.
_dir: str

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
extra: bool = False

# Make sure this is being run directly, and
# not from another python module:
if not __name__ == "__main__":
    raise EnvironmentError("This module must be run directly!")
else:
    # If this is being run directly,
    # set up for tests:
    print("[DEBUG] Module being run directly, not exiting")
    # Get working directory:
    print("[DEBUG] Getting working directory\n")
    _dir = os.getenv("CIRRUS_WORKING_DIR")
    print("[DEBUG] Got working directory ({0})\n".format(_dir))
    # Get divider text file:
    dividers_file: str = "{0}/{1}".format(_dir, "area4/dividers.txt")
    print("[DEBUG] Divider file is located at {0}\n".format(dividers_file))
    with open(dividers_file, mode="r") as fh:
        rawDividers = fh.readlines()
        print("[DEBUG] Fetched raw dividers text file")
    # Create instance:
    print("[DEBUG] Creating instance of the library")
    d = area4.Area4Instance()
    print("[DEBUG] Created instance")

    # See if we need to run extra tests:
    if ("!e" in c_message or c_message == "!e") or \
            (repo_branch == "master"):
        print("[DEBUG] Running extra tests!")
        extra = True
    else:
        extra = False


# Divider tests:
def test_dividers() -> None:
    """
    Test each divider against the raw ones from the text file.

    :return: None
    """
    for i in range(len(rawDividers)):
        if i < 1 or i == 35:
            print("[DEBUG] Manually skipping divider {0}".format(i))
            # Manually skip dividers 0 and 35:
            i = i + 1
        else:
            print("[DEBUG] Testing divider {0}".format(i))
            try:
                # Try to match the raw divider with the result
                # of the function:
                if rawDividers[i].split("\n")[0] == d.divider(i):
                    print("[+] Divider {0} should work.".format(i))
                else:
                    print("[X] Divider {0} is broken!".format(i))
                    raise RuntimeError("Broken divider detected!")
            except IndexError:
                # This is thrown if a number is offset in the divider array.
                # What we do about it is we just simply ignore it
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


# Validate info variables
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


def on_start() -> None:
    """
    Run when the test starts.

    :return: None
    """
    print("[DEBUG] Starting tests...\n\n")


def on_finish() -> None:
    """
    Run when the test finishes.

    :return: None
    """
    print("\n[DEBUG] Exiting tests!")


# Run tests:
on_start()

test_dividers()
test_make_div()

if extra:
    # Run extra tests if needed:
    test_info()
    rst_lint_run()

# Notify user tests are complete:
on_finish()

"""Runs code tests in a CI environment."""

# Import needed modules
import unittest
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


class TestCode(unittest.TestCase):
    """The test class."""

    def setUp(self):
        """Prepare for a test."""
        # Get working directory:
        self.working_directory = os.getenv("CIRRUS_WORKING_DIR")
        if self.working_directory is None:
            working_directory = os.path.abspath(
                os.path.dirname(__file__)
            )
            if working_directory is None:
                raise EnvironmentError("Could not find working directory!")
        # Get divider text file:
        self.dividers_file = "{0}/{1}".format(
            self.working_directory,
            "area4/dividers.txt"
        )
        try:
            with open(file=self.dividers_file, mode="r") as fh:
                self.raw_dividers = fh.readlines()
        except FileNotFoundError:
            raise EnvironmentError("Raw divider file not found!")

    def test_dividers(self):
        """Test dividers."""
        for i in range(len(self.raw_dividers)):
            try:
                # Try to match the raw divider with the result
                # of the function:
                if i != 35 and i != 0:
                    self.assertEqual(self.raw_dividers[i], area4.divider(i))
                elif i == 35 and i != 0:
                    self.assertNotEqual(self.raw_dividers[i], area4.divider(i))
            finally:
                print()

    def test_splitter(self):
        """Test splitter."""
        self.assertEqual(area4.splitter("---", "Hello"), "Hello")

    def test_utilities(self):
        """Test util module."""
        module = area4.util
        self.assertEqual(module.get_divider_character(1), "-")
        self.assertEqual(module.get_divider_character(2), "_")
        self.assertEqual(module.get_divider_character(3), ".")
        self.assertEqual(module.get_divider_character(7), "=")
        self.assertEqual(module.get_divider_character(9), "*")
        self.assertEqual(module.get_divider_character(13), "~")
        self.assertEqual(module.get_divider_character(19), "&")
        self.assertNotEqual(module.get_divider_character(21), "¯\\_(ツ)_/¯")
        self.assertEqual(module.get_divider_character(21), None)
        self.assertEqual(module.get_divider_character(216), ";")
        self.assertEqual(module.redditHorizontal(), "*****")

    def test_info(self):
        """Test info."""
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
        for i, e in enumerate(right_data):
            self.assertEqual(right_data[i], from_class[i])

    def test_restructuredtext(self):
        """Test RST file."""
        files = os.listdir("{0}/docs".format(self.working_directory))
        for name in files:
            path = "{0}/docs/{1}".format(self.working_directory, name)
            restructuredtext_lint.lint_file(filepath=path)

    def test_deps(self):
        """Use SafetyCI."""
        self.assertEqual(os.system("make safetyci"), 0)

    def test_make_div(self):
        """Test make_div."""
        self.assertEqual(
            area4.make_div('=-', length=9, start='<', end='=>'),
            "<=-=-=-=>"
        )


if __name__ == '__main__':
    unittest.main()

"""Runs code tests in a CI environment."""

# Import needed modules
import unittest
import os

# Try to import area4.
# This will fail if it could not be installed or if faulty code is present.
try:
    import area4
except Exception:
    # At this point, area4 either isn't in site-packages,
    # or not on the system at all.
    raise OSError("Failed to import the library.")


class Tests(unittest.TestCase):
    """The test class."""

    def setUp(self):
        """Prepare for a test."""
        # Get working directory:
        self.working_directory = os.getenv("CIRRUS_WORKING_DIR")
        # Fallback in case this is being run locally:
        if self.working_directory is None:
            self.working_directory = os.path.abspath(os.path.dirname(__file__))
        # Get divider text file:
        self.dividers_file = "{0}/{1}".format(
            self.working_directory, "area4/dividers.txt"
        )
        with open(file=self.dividers_file, mode="r") as fh:
            self.raw_dividers = fh.readlines()

    def test_dividers(self):
        """Test dividers."""
        try:
            for i in range(len(self.raw_dividers)):
                # Try to match the raw divider with the result
                # of the function:
                if i not in [0, 32, 35, 286]:
                    self.assertEqual(
                        self.raw_dividers[i].replace("\n", ""),
                        area4.divider(i),
                        f"Divider number {i} was not the same in the file and in the code. Please ask a maintainer for help.",
                    )
                elif i in [32, 35, 286] and i != 0:
                    self.assertNotEqual(self.raw_dividers[i], area4.divider(i))
        finally:
            pass

    def test_splitter_1(self):
        """Test splitter function."""
        self.assertEqual(area4.splitter("---", "Hello"), "Hello")

    def test_splitter_2(self):
        """Test splitter function."""
        self.assertEqual(
            area4.splitter("---", "Hello", "world"), "Hello\n---world\n---"
        )

    def test_splitter_3(self):
        """Test splitter function."""
        self.assertEqual(
            area4.splitter(3, "Hello", "world"),
            "Hello\n............\nworld\n............\n",
        )

    def test_splitter_4(self):
        """Test splitter function."""
        self.assertEqual(
            area4.splitter(45, "Hello", "world", "fine"),
            "Hello\neeeeeeeeeeee\nworld\neeeeeeeeeeee\nfine\neeeeeeeeeeee\n",
        )

    def test_splitter_5(self):
        """Test splitter function."""
        self.assertEqual(
            area4.splitter("xyz", "Hello", "world"), "Hello\nxyzworld\nxyz"
        )

    def test_utilities(self):
        """Test util module."""
        module = area4.util
        self.assertEqual(module.get_divider_character(1), "-")
        self.assertEqual(module.get_divider_character(2), "_")
        self.assertEqual(module.get_divider_character(3), ".")
        self.assertEqual(module.get_divider_character(7), "=")
        self.assertEqual(module.get_divider_character(9), "*")
        self.assertEqual(module.get_divider_character(13), "~")
        self.assertNotEqual(module.get_divider_character(21), "¯\\_(ツ)_/¯")
        self.assertEqual(module.get_divider_character(23), "2")
        self.assertEqual(module.get_divider_character(24), "3")
        self.assertEqual(module.get_divider_character(25), "4")
        self.assertEqual(module.get_divider_character(26), "5")
        self.assertEqual(module.get_divider_character(27), "6")
        self.assertEqual(module.get_divider_character(28), "7")
        self.assertEqual(module.get_divider_character(29), "8")
        self.assertEqual(module.get_divider_character(30), "9")
        self.assertEqual(module.get_divider_character(215), ";")
        self.assertEqual(module.reddit_horizontal(), "*****")
        self.assertEqual(module.markdown_horizontal(), "---")

    def test_for_divider_duplicates(self):
        """Checks for any duplicate dividers."""
        for x, z in enumerate(self.raw_dividers):
            # foreach entry, check equality to the parent foreach's current index
            for g, h in enumerate(self.raw_dividers):
                if x == g:
                    # during enumeration, the divider will find itself
                    self.assertEqual(
                        self.raw_dividers[x],
                        self.raw_dividers[g],
                        f"Divider {x} couldn't find itself! This really should not happen.",
                    )
                else:
                    if "Injected" not in self.raw_dividers[x]:
                        # but all the other times it will be another divider
                        # which can NOT be equal!
                        self.assertNotEqual(
                            self.raw_dividers[x],
                            self.raw_dividers[g],
                            f"Dividers {x} and {g} are the same! Duplicates are not allowed.",
                        )

    def test_info(self):
        """Test info."""
        right_data = [
            "area4",
            "RDIL",
            "me@rdil.rocks",
            "Dividers in Python, the easy way!",
        ]
        from_class = [
            area4.name,
            area4.__author__,
            area4.author_email,
            area4.description,
        ]
        for i, e in enumerate(right_data):
            self.assertEqual(right_data[i], from_class[i])
        self.assertEqual(
            area4.area4info(),
            "Name: {0}\nAuthor: {1}\nAuthor Email: {2}\nDescription: {3}".format(
                right_data[0], right_data[1], right_data[2], right_data[3],
            ),
        )

    def test_make_div(self):
        """Test make_div."""
        self.assertEqual(
            area4.make_div("=-", length=9, start="<", end="=>"), "<=-=-=-=>"
        )

    def test_html_horizontal(self):
        """Test html_horizontal divider."""
        self.assertEqual(area4.util.html_horizontal(), "<hr></hr>")
        self.assertEqual(area4.util.html_horizontal(closing_tag=False), "<hr>")


if __name__ == "__main__":
    unittest.main()

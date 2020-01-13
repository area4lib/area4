# Changelog

Key:

* `*` means modification
* `+` means addition
* `-` means deletion

## v3.2.0

```diff
+ Added dividers 245 through 254
* Optimized divider loading
+ Updated setuptools from 44.0.0 to 45.0.0
+ Added tests for HTML horizontal divider
* Combined test and dev requirements
```

## v3.1.0

```diff
+ Update setuptools (42.0.2 -> 44.0.0)
+ Update Sphinx (2.3.0 -> 2.3.1)
+ Added area4.util.html_horizontal
+ Added 1337 divider
+ Enhanced documentation
```

## v3.0.0

```diff

+ Update twine (1.13.0 -> 3.1.1)
+ Update unittest-xml-reporting (2.5.1 -> 2.5.2)
* Converted this changelog to Markdown
* Breaking: changed the output of the splitter function
* Rewrote major parts of the docs
- Removed a divider, see migration guide
+ Optimized some internal code
```

## v2.11.3

```diff
+ Add avocado emoji divider
```

## v2.11.2

```diff
* Improved documentation a lot more
+ Exposed the "blacklisted" dividers list
+ Added maintainer field to setup.py
+ Added Python version constraints to setup.py to prevent unsupported Python version installs
```

## v2.11.1

```diff
+ Added API Refrence documentation page
+ Updated tests to work with new Python version
* Changed copyright header
+ Updated Sphinx version
```

## v2.11.0

```diff
+ Added 14 new dividers
```

## v2.10.0

```diff
+ Added 9 new dividers
+ Made area4.utils.get_raw_file() cache the file contents
* Fixed certain dividers confusing GitHub
+ Added more splitter tests
+ Added test for area4.utils.markdown_horizontal() function
+ Added partially working duplicate divider checking
  (disabled due to failures that would be breaking changes)
```

## v2.9.0

```diff
+ Added markdown horizontal divider
- Removed rdillib dependency
* Updated docs
```

## v2.8.0

```diff
* Updated documentation
* Updated CI to use slim images
- Removed SafetyCI checks, description validation, and old Markdown check
- Removed area4.util_module and area4.theArray aliases
* Renamed area4.author to area4.__author__
+ Added 'text' keyword
- Removed pipenv dependency
```

## v2.7.0

```diff
- Removed util.check function
* Fixed dead links
+ Added integer check
```

## v2.6.0

```diff
+ Added test for area4.area4info
* Refactor and fix area4.area4info (formatting issue and wrong data fixed)
```

## v2.5.9

```diff
- Don't include changelogs in builds
```

## v2.5.8

```diff
* Updated documentation
```

## v2.5.7:

```diff
* Shortened author value
```

## v2.5.6

```diff
- Remove stepped down maintainers
```

## v2.5.5

```diff
+ Improved docs
```

## v2.5.4

```diff
* Built with newer version of setuptools
```

## v2.5.3

```diff
+ Added our first ever runtime dependency - RDILLib (for dynamic emails)
- Removed pycodestyle config from setup.cfg
```

## v2.5.2

```diff
- Removed all dist-info related code
* Updated docs
```

## v2.5.1:

```diff
* Changed Reddit divider function name to match style guide
* Updated tests
```

## v2.5.0

Shoutout to N8python for helping get this release out!

```diff
* Made divider function strip newlines from output
* Made all dividers 12 characters (except for a select few)
```

## v2.4.0

```diff
+ Added a new divider
```

## v2.3.9

```diff
* Updated copyright years in documentation
* Updated Makefile
```

## v2.3.8

```diff
- Removed clone tool as it had no use
* Updated extras
```

## v2.3.7

```diff
- virtualenv is no longer required
```

Version 2.3.6:

```diff
* Updated Sphinx
* Updated contributing guidelines
```

## v2.3.5

```diff
* Packaged with newer version of setuptools
```

## v2.3.4

```diff
+ Added more unit tests
* Updated package info function
```

## v2.3.3

```diff
* Updated setuptools
```

## v2.3.2

```diff
* Moved tests to unittest module
* Fixed bug
```

## v2.3.1

```diff
+ Added Reddit horizontal divider to utilities module
```

## v2.3.0

```diff
- Removed class based system
```

## v2.2.0

```diff
* Code cleanup
```

## v2.1.9

```diff
* Fixed a compatibility issue
```

## v2.1.8

```diff
- Removed BrewMake tool due to lack of use
+ Blacklisted certain dividers from the get_divider_character utility function
```

## v2.1.7

```diff
+ Added get_divider_character utility function
```

## v2.1.6

```diff
+ Added releasing guidelines for maintainers
+ Added tests for utility module
+ Added markdown spellchecking
```

## v2.1.5

```diff
* Made tests way faster
+ Added documentation tests
* Cleaned up documentation
+ Added documentation requirements
```

## v2.1.4

```diff
+ Added BrewMake tool
* Fixed broken links
* Updated contributing guidelines
```

## v2.1.3

This minor release was a continuation of the work done in `v2.1.2`.

## v2.1.2

```diff
* Moved library to area4lib organization!!
```

## v2.1.1

```diff
* Fixed an issue in the code with the splitter function
```

## v2.1.0

```diff
+ Added eye emoji dividers
+ Added splitter function (finally!)
* Moved reduce_to_unit function to utility module
```

## v2.0.9

```diff
+ Added CI auto-deploying
+ Added release schedule
```

## v2.0.8

```diff
+ Added clone tool
* Fixed linting issues
* Updated badges
* Migrated CI tests to macOS
```

## 2.0.7

```diff
* Fixed linting issues
* Moved the utilities module to the main package
* Moved linting tests to Cirrus CI
* Made package info function work on all Python3 versions
```

## v2.0.6

See the changelogs for `v2.0.4`.

## v2.0.5

See the changelogs for `v2.0.4`.

## v2.0.4

```diff
* Fixed Python 3.4 and 3.5 compatibility issues
* Lots of code cleanup
* Moved tests onto GNU make
+ Added semicolon dividers
```

## v2.0.3

```diff
* Updated flake8 to the latest version
* Updated documentation config
+ Added suggested extensions in VSCode
```

## v2.0.2

```diff
* Updated package build tools
* Updated support information
* Updated issue templates
* Updated Probot config
* Updated contributing guidelines
* Updated twine to latest version
```

## v2.0.1

```diff
+ Added new 6 dividers
* Cleaned up docs
- Removed egg building tool
* Updated CodeOwners
* Made code follow PyDocStyle
* Removed Travis CI, moved on to Cirrus CI
* Added dependency bumping bot
```

## v2.0.0

```diff
* Completely changed the divider addition system
* Removed most of the GitHub apps, added new ones
* Redid docs
+ Gave the util module its own package so the import system isn't really odd
* Made the main module class based ( /!\ VERY BREAKING CHANGES ALERT /!\ )
* Made sure the wheel is not built universally
* Added actual code testing with Travis CI
+ Added build tools
- Removed VCS lists
* Updated the contributing guidelines
+ Added markdown linting
```

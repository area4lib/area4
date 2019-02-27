# Releasing

*area4 Releasing Manual - maintainers only.*

## Stable

First, ensure the code is in a stable position.

## Tests

Second, ensure all tests are passing.

## Creating a release

Next, create a release on GitHub. The release information box should have the following put in it:

```
New version now live on PyPI. The tar archive and wheel can be found on the downloads page on PyPI.
```

Make sure to input a version for the tag number and the title should look like:

```
v#.#.#
```

Replace the `#`s with the version number.

## Deploying to PyPI

The CI now deploys whenever a tag is created.

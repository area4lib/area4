# Releasing

*area4 Releasing Manual - [maintainers](https://github.com/area4lib/area4/blob/master/.github/CODEAUTHORS.md#maintainers) only.*

## Timing

For information on when to release, see our [release schedule](https://github.com/area4lib/area4/blob/master/.github/release-schedule.md)

## Stable

First, ensure the [code](https://github.com/area4lib/area4) is in a [stable position](https://github.com/area4lib/area4/blob/master/.github/release-schedule.md#stable-build).

## Tests

Second, ensure all [tests](https://cirrus-ci.com/github/area4lib/area4) are passing.

## Creating a release

Next, create a [release](https://github.com/area4lib/area4/releases) on GitHub. The release information box should have the following put in it:

```none
New version now live on PyPI. The tar archive and wheel can be found on the downloads page on PyPI.
```

Make sure to input a [version](https://semver.org) for the tag number and the title should look like:

```none
v#.#.#
```

Replace the `#`s with the version number.

## Deploying to [PyPI](https://pypi.org)

The CI now deploys whenever a tag is created.

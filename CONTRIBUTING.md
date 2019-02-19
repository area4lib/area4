# area4 Contributing Guidelines

Hello, and welcome to area4. Before you contribute, please read this document to find out the best ways to contribute to this project.

## A few ground rules

There are a few things to keep in mind when contributing:

1. **Be nice**: All of your contributions should be genuine contributions that respect the time of the maintainers and of other contributors. Always be respectful to others who open issues or pull requests. If someone else has a question that you can answer, answer politely and respectfully, and point them in the direction of any other issues or resources if they need help. Make sure you're creating a safe environment for others to contribute!

2. **Follow the [code of conduct](https://github.com/RDIL/area4/blob/master/CODE_OF_CONDUCT.md)**: area4 has a code of conduct that details the kind of behavior you should be demonstrating when using and contributing to this project. Before you contribute, please take a few minutes to read the code of conduct and always follow it when contributing.

## Steps to make changes

1. Fork the repository.
2. Clone it if you are using a git client.
3. Make your changes.
4. Push to your fork.
5. Create a PR.
6. If you need to, push extra commits (or rebase if requested).
7. You should be done!

## What to contribute

There are many ways to contribute to area4! You can help improve the documentation, submit bug reports and feature requests, or write code which can be incorporated into area4. Don't be afraid to contribute to the project--the open source community will be here to help you should you need any!

## Coding

This project code is intended to be...

- Clean. Keep it well formatted and follow your favourite language conventions, so one can understand it.
- Documented. Keep it well documented, so one can learn from it.
- Reusable. Keep it clean and modular, with as little responsibility per programming unit (function, method, class, module, project) as possible, so one can reuse it.
- Testable. Keep it easy to debug and test, so one can be confident that it works properly.  Please keep the [Cirrus CI Build](https://cirrus-ci.com/github/RDIL/area4) at passing if possible.
- Python 3 compatible.  area4 aims to support Python 3 versions (including PyPy3.5), and does not support versions below Python3.  The one thing that does not follow this rule is the package info function, which requires F-strings (which are only supported in Python 3.6 and above).

## Timing

Timing is important, all project staff have lives and don't hang 'round this repository 24/7.
They all are in United States eastern time.

## Work-in-progress pull requests

If you open a pull request that is still a work in progress, please put `[WIP]` or `WIP:` in the title.
You can also use the new GitHub pull request drafting feature.
It will make the work-in-progress bot keep its status check at pending.
This helps us out a ton as we know that a PR is NOT ready for merge.

## Code quality

Please keep your code as readable as possible. We have apps to help out with this such as [CodeFactor](https://codefactor.io) to lint code. Where possible please abide by their feedback.

## Divider style

Please keep dividers at exactly 12 characters.

## Betas

Help us test new code with betas! They are WIP builds that are not finished and may contain bugs, and it helps us to find those before we deploy to PyPI. Betas can be found in issues when we have decided to use them.

## Documentation format

When adding dividers, it must be added to the list of dividers in the docs (`docs/div-looks.rst`).

-------------------

If your pull request is merged your name will be added to the author list (`.github/CODEAUTHORS.md`).

If you have any questions please contact [RDIL](mailto:me@rdil.rocks), but before you do please please review our [documentation](https://area4.readthedocs.io/en/latest/).

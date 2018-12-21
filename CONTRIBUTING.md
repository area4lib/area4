# AREA4 CONTRIBUTING GUIDELINES  

Hello, and welcome to area4.  Before you contribute, please read this document to find out the best ways to contribute to this project.  

## What to contribute  
There are many ways to contribute to area4! You can help improve the documentation, submit bug reports and feature requests, or write code which can be incorporated into area4. Don't be afraid to contribute to the project--the open source community will be here to help you should you need any!  

## A few ground rules  

There are a few things to keep in mind when contributing:  

1. **Be nice**: All of your contributions should be genuine contributions that respect the time of the developers and of other contributers. Always be respectful to others who open issues or pull requests. If someone else has a question that you can answer, answer politely and respectfully, and point them in the direction of any other issues or resources if they need help. Make sure you're creating a safe environment for others to contribute!  

2. **Follow the [code of conduct](https://github.com/RDIL/area4/blob/master/CODE_OF_CONDUCT.md)**: area4 has a code of conduct that details the kind of behavior you should be demonstrating when using and contributing to this project. Before you contribute, please take a few minutes to read the code of conduct and always follow it when contributing.  

## Steps  

1. Fork the repo.  
2. Clone it if you are using a git client.  
3. Make your changes.  
4. Push to your fork.  
5. Create a PR.  
6. If you need to, push extra commits (or rebase if requested).  
7. You should be done!  

## Coding

This project code is intended to be...

* Clean. Keep it well formatted and follow your favourite language conventions, so one can understand it.
Documented. Keep it well documented, so one can learn from it.  
* Reusable. Keep it cohese and modular, with as little responsibility per programming unit (function, method, class, module, project) as possible, so one can reuse it.  
* Testable. Keep it easy to debug and test, so one can be confident that it works properly.  Please keep the [Travis CI build](https://travis-ci.com/RDIL/area4) and [Cirrus CI Build](https://cirrus-ci.com/github/RDIL/area4) at passing if possible.  Travis doesn't directly test the code for errors, rather checks to see if it is safe and ready to deploy to PyPI if needed!  
* Python 3 compatible.  Area4 aims to support Python 3 versions (including PyPy3.5), and does not support versions below Python3.  The one thing that does not follow this rule is the package info function, which requires F-strings (which are only supported in Python 3.6 and above).  

## Timing  
Timing is important, all project staff have lives and don't hang 'round this repository 24/7.  They all are in United States eastern time.  

## Good vs bad contributions  
Please don't spam us with one-liners.  Fixing one typo is fine but fixing five typos each with their own pull request is spammy and will be closed/locked by maintainers.  Big quality changes are fine and encouraged!  

## Work-in-progress pull requests  
If you open a pull request that is still a work in progress, please put `[ WIP ]` in the title.  It will make the work-in-progress bot keep its status check at pending.  This helps us out a ton as we know that a PR is NOT ready for merge.  

## Code quality  
Please keep your code as readable as possible.  We have apps to help out with this such as [CodeFactor](https://codefactor.io) and Codebeat to lint code.  Where possible please abide by their feedback.  

## Divider style  
The divider style can be found in the `info for devs` section of the documentation.  

## Documentation format  
When adding dividers, it must be added to the list of dividers in the docs (`/projectrootfolder/docs/div-looks.rst`) as well as have its own docs in the function in the code.  

-------------------  

If your pull request is merged your name will be added to the author list (`/projectrootfolder/.github/CODEAUTHORS.md`).  

If you have any questions please contact [RDIL](mailto:me@rdil.rocks), but before you do please please review our [documentation](https://area4.readthedocs.io/en/latest/) and [wikis](https://github.com/RDIL/area4/wiki). 

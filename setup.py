"""Builds the package."""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="area4",
    version="2.0.3",
    author="RDIL",
    author_email="me@rdil.rocks",
    description="Dividers in Python, the easy way!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RDIL/area4",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 8",
        "Operating System :: Microsoft :: Windows :: Windows 8.1",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Other OS",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: System",
        "Topic :: Terminals",
        "Topic :: Text Processing",
        "Development Status :: 5 - Production/Stable",
        "Framework :: IDLE",
        "Natural Language :: English",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/RDIL/area4/issues",
        "Documentation": "https://area4.readthedocs.io/en/stable/",
        "Source Code": "https://github.com/RDIL/area4",
    },
    keywords=["area4", "dividers", "python", "utilities", "enhancements"],
    include_package_data=True,
    zip_safe=False
)

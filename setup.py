import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="area4",
    version="1.0.0",
    author="RDIL",
    author_email="contactspaceboom@gmail.com",
    description="Dividers in Python, the easy way! Four different types.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RDIL/area4",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


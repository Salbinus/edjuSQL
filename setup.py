import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="edjuSQL-pkg-Salbinus",
    version="0.0.1",
    author="Alexander Albinus",
    author_email="s_albinus@stud.hwr-berlin.de",
    description="Tool to check your SQL Queries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Salbinus/edjuSQL",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

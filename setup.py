import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "gamelayer",
    version = "0.1.0",
    author = "Kevin Wolff",
    auther_email = "kdrakemagi@gmail.com",
    description = "A pygame toolkit",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Windspar/Gamelayer",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: MIT License",
    ],
    python_requires = ">=3.6",
)

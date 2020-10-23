import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="adam-squared-loose",
    version="0.1.0dev0",
    author="Adam Beecham",
    author_email="adam.beecham@adamsquared.cloud",
    description="service decoupler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adam-squared/loose",
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
)

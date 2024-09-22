from setuptools import find_packages, setup

setup(
    author="n6ck",
    author_email="n@ermm.rest",
    description="An asynchronous API wrapper around cobalt.tools",
    install_requires=["aiohttp", "pydantic"],
    name="cobolt",
    packages=find_packages(),
    python_requires=">=3.12",
    url="https://github.com/n6ck/cobolt",
    version="0.1.0",
)

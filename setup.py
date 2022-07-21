#!/usr/bin/env python3
import pkg_resources
from setuptools import find_packages, setup

from src.pydrs import __author__, __version__


def get_abs_path(relative):
    return pkg_resources.resource_filename(__name__, relative)


def get_long_description() -> str:
    desc = ""
    with open(get_abs_path("README.md"), "r") as _f:
        desc += _f.read().strip()

    desc += "\n\n"

    with open(get_abs_path("CHANGES.md"), "r") as _f:
        desc += _f.read().strip()

    return desc


long_description = get_long_description()


with open(get_abs_path("requirements.txt"), "r") as _f:
    _requirements = _f.read().strip().split("\n")

setup(
    author=__author__,
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Operating System :: OS Independent",
    ],
    description="",
    download_url="https://github.com/lnls-sirius/pydrs",
    include_package_data=True,
    install_requires=_requirements,
    license="MIT License",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="pydrs",
    url="https://github.com/lnls-sirius/pydrs",
    version=__version__,
    packages=find_packages(
        where="src",
        include=["pydrs*"],
    ),
    package_dir={"": "src"},
    python_requires=">=3.6",
    test_suite="tests",
    zip_safe=False,
)

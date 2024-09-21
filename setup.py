from setuptools import setup, find_packages

setup(
    name="aoc22",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Click"],
    entry_points={"console_scripts": ["solve = src.app:cli"]},
)

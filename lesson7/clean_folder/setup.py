from setuptools import setup, find_packages



setup(
    name = "clean_folder",
    version = "1.0",
    entry_points = {
        'console_scripts':['clean_folder=clean_folder.sort:main'],
    },
    packages = find_packages(),
    )

from setuptools import setup

desc = "A Python program that finds files of a certain nature on a certain website. For use in piping magnet links to programs that support them"

setup(
    name = "rahr",
    packages = ["rahr"],
    install_requires = ["requests"],
    entry_points = {
        "console_scripts": ['rahr = rahr.rahr:main']
        },
    version = "1.2.2",
    description = desc,
    long_description = desc,
    author = "Steven Smith",
    author_email = "stevensmith.ome@gmail.com",
    license = "MIT",
    url = "https://github.com/blha303/rahr",
    classifiers = [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "Topic :: Multimedia :: Sound/Audio"
        ],
    )

from setuptools import setup

desc = "A python program to search for torrents via Jackett and provide links to stdout"

setup(
    name = "rahr",
    packages = ["rahr"],
    install_requires = ["requests"],
    entry_points = {
        "console_scripts": ['rahr = rahr.rahr:main']
        },
    version = "2.0.0",
    description = desc,
    long_description = desc,
    author = "Alyssa Smith",
    author_email = "alyssa.dev.smith+rahr@gmail.com",
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

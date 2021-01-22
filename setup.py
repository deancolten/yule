import setuptools
from pathlib import Path

setuptools.setup(
    name="yule",
    version='0.0.3',
    description="A logging package for python",
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Topic :: System :: Logging"
    ],
    url="https://github.com/deancolten/yule",
    author="Colten Dean",
    author_email="coltenrdean@gmail.com",
    install_requires=[
        "colorama"
    ]
)

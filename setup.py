from os.path import abspath, dirname, join
from setuptools import setup, find_packages

CURDIR = dirname(abspath(__file__))

CLASSIFIERS = """
Development Status :: 1 - Production/Stable
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10
Programming Language :: Python :: 3.11
Programming Language :: Python :: 3 :: Only
Topic :: Software Development :: Security
""".strip().splitlines()

with open(join(CURDIR, "README.md")) as f:
    DESCRIPTION = f.read()
with open(join(CURDIR, "requirements.txt")) as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name="pytography",
    version="0.1.0",
    description="A library for password hashing and JWT encoding",
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    author="TalentGate",
    url="https://github.com/TalentGate/pytography",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=CLASSIFIERS,
    python_requires=">=3.6",
    install_requires=REQUIREMENTS,
)
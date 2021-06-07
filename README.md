CodeMelli
=========

[![pypi version](https://img.shields.io/pypi/v/codemelli.svg)](https://pypi.python.org/pypi/codemelli)
[![build status](https://img.shields.io/travis/hanifbirgani/codemelli.svg)](https://travis-ci.com/hanifbirgani/codemelli)
[![docs](https://readthedocs.org/projects/codemelli/badge/?version=latest)](https://codemelli.readthedocs.io/en/latest/?version=latest)
[![code coverage](https://codecov.io/gh/HanifBirgani/codemelli/branch/main/graph/badge.svg?token=NXI0SUQJ0N)](https://codecov.io/gh/HanifBirgani/codemelli)
[![MIT License](https://img.shields.io/github/license/hanifbirgani/codemelli)](https://opensource.org/licenses/MIT)

Python package to validate/generate iranian national ID

Usage
-----
```python
>>> import codemelli

# Validate a real codemelli
>>> codemelli.validator(2833411839)
True

# Validate a fake codemelli
>>> codemelli.validator(3235632189)
False

# Generate a random valid codemelli
>>> codemelli.generator()
6615365987

# Generate a random codemelli with a defined city code
>>> codemelli.generator(223)
2239832630

# Lookup city and state of a valid codemelli
>>> codemelli.lookup(2239832630)
{'city': 'بندرترکمن', 'state': 'گلستان'}
```

-   Free software: MIT license
-   Documentation: <https://codemelli.readthedocs.io>.

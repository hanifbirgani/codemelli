#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = []

test_requirements = ['pytest>=3', ]

setup(
    author="Hanif Birgani",
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="Python package to validate/generate iranian national ID",
    install_requires=requirements,
    long_description_content_type='text/markdown',
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    packages=find_packages(include=['codemelli', 'codemelli.*']),
    package_data={'': ['data/code-city.json']},
    keywords='codemelli',
    name='codemelli',
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/hanifbirgani/codemelli',
    version='0.1.2',
    zip_safe=False,
)

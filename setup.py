from setuptools import setup, find_packages

setup(
    name="sentinel",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'sentinel=sentinel.cli:cli',  
        ],
    },
    author="RykerWilder",
    description="CLI tool for cybersecurity",
)
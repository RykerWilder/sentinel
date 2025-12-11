from setuptools import setup, find_packages

setup(
    name="falcon",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'falcon=falcon.cli:cli',  
        ],
    },
    author="RykerWilder",
    description="CLI multi tool for cybersecurity",
)
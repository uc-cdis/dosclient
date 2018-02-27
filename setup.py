from setuptools import setup

setup(
    name='dosclient',
    version='0.1',
    packages=[
        'dosclient',
    ],
    install_requires=[
        'requests>=2.5.2,<3.0.0',
    ],
)

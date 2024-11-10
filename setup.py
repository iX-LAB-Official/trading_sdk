# sdk/setup.py

from setuptools import setup, find_packages

setup(
    name='trading_sdk',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'aiohttp>=3.7.4'
    ],
    url='https://github.com/iX-LAB-Official/trading_sdk',
    license='MIT',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python SDK for interacting with the trading API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)

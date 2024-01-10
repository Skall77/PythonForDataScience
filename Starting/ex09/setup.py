# ft_package/setup.py

from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[],
    author='aaudevar',
    author_email='aaudevard@gmail.com',
    license='MIT',
    Summary='A small example package',
    description='A small example package',
    long_description='A small example package with a count_in_list function.',
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
    ],
)

from setuptools import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read()

setup(
    name='MediaFileOrganizer',
    version='1.0.0',
    author='Julien Poirou',
    author_email='poiroujulien@gmail.com',
    maintainer='Julien Poirou',
    maintainer_email='poiroujulien@gmail.com',
    url='https://github.com/julienpoirou/media-file-organizer',
    license=license,
    description='A tool to rename and organize your media on your hard drive.',
    long_description=readme,
    requires=requirements
)
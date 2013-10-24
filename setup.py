from distutils.core import setup

setup(
    name='PyTrade',
    version='0.1.0',
    author='Aaron Ash',
    author_email='aaron.ash+pytrade@gmail.com',
    packages=['pytrade'],
    scripts=['bin/moving-average-system.py'],
    url='http://github.com/AshyIsMe/PyTrade',
    license='LICENSE.txt',
    description='Python trading systems',
    long_description=open('README.txt').read(),
    install_requires=[
      "requests",
      "pandas",
    ],
)

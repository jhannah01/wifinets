from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='wifinets',
      version=version,
      description="A tool to convert Android wiglewifi databases to a more usable format",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='wiglewifi wifistumbler',
      author='Jon Hannah',
      author_email='jon@blueodin.com',
      url='https://github.com/jhannah01/wifinets',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

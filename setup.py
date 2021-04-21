from setuptools import setup

setup(
    name='my-simple-cli-python2',    # This is the name of your PyPI-package.
    version='0.1',                          # Update the version number for new releases
    scripts=['myecho.py']                  # The name of your script, and also the command you'll be using for calling it
)
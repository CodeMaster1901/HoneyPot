from setuptools import setup

def readme_file_contents():
    with open('README.rst') as readme_file:
        data = readme_file.read()
    return data


setup(
    name='HoneyPot',
    version='1.0.0',
    description='Simple TCP Honeypot project',
    long_description=readme_file_contents(),
    author='CodeMaster1901',
    license='MIT',
    packages=['HoneyPot'],
    # scripts=['bin/HoneyPot','bin/HoneyPot.bat']
    zip_safe=False,
    install_requires=[
        'docopt'
    ]
)
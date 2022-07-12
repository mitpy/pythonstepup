from setuptools import find_packages, setup
setup(
    name='myarth',
    packages=find_packages(include=['myarth']),
    version='4.0',
    description='My first Python library',
    author='Me',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner', 'wheel'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
from setuptools import setup, find_packages

setup(
    name='pythonpackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Virek000/pythonpackage.git',
    author='Virek Sewchurn',
    author_email='virek999@gmail.com'
)

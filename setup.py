from setuptools import setup, find_packages

setup(
    name='tripy',
    version='0.0.1',
    url='https://github.com/linuxlewis/tripy',
    author='Sam Bolgert',
    author_email='sbolgert@gmail.com',
    description='Simple polygon triangulation',
    license='MIT',
    packages=find_packages(exclude=["tests.*"])
)

from setuptools import find_packages, setup

setup(
    name='tripy',
    version='0.0.3',
    url='https://github.com/linuxlewis/tripy',
    author='Sam Bolgert',
    author_email='sbolgert@gmail.com',
    description='Simple polygon triangulation',
    license='MIT',
    py_modules=['tripy'],
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
)

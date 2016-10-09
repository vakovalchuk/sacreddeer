import setuptools


def readme():
    with open('README.rst') as f:
        return f.read()

setuptools.setup(
    name='sacreddeer',
    version='0.1',
    description='ASk your stupid questions and Deer will answer',
    url='http://github.com/pannkotsky/sacreddeer',
    author='Valerii Kovalchuk',
    author_email='kovvalole@gmail.com',
    license='MIT',
    packages=['sacreddeer'],
    install_requires=[
        'slackclient',
    ],
    zip_safe=False
)

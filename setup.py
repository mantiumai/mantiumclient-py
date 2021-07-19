import os
import setuptools

DEPENDENCIES = open('requirements.txt', 'r').read().split('\n')
with open('README.md', 'r') as fh:
    long_description = fh.read()

build_number = os.getenv('TRAVIS_BUILD_NUMBER', '1')

setuptools.setup(name='mantiumapi',
    version='0.0.' + build_number,
    description='Python Client for the Mantium API',
    long_description='This software is provided as a way to include the Mantium API functionality in your own Python '
                     'software. You can read about the Mantium API at https://developer.mantiumai.com/',
    url='https://github.com/mantiumai/mantiumclient-py',
    author='Mantium',
    author_email='support@mantiumai.com',
    license='Apache 2.0',
    packages=setuptools.find_packages(),
    install_requires=DEPENDENCIES,
    keywords=['security', 'ai', 'nlp'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
        'Operating System :: OS Independent',
    ],
    include_package_data=True,
    zip_safe=False
)

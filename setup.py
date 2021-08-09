# -*- coding: utf-8 -*-
#  Copyright (c) 2021 Mantium, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# Please refer to our terms for more information:
#     https://mantiumai.com/terms-of-use/
#
import os
import setuptools
import pkg_resources


DEPENDENCIES = open('requirements.txt', 'r').read().split('\n')
with open('README.md', 'r') as fh:
    long_description = fh.read()

try:
    build_version=pkg_resources.require("mantiumapi")[0].version
except:
    build_version= '0.1.' + os.getenv('TRAVIS_BUILD_NUMBER', 'unknown')

setuptools.setup(name='mantiumapi',
    version=build_version,
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
        'Development Status :: 4 - Beta',
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
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Operating System :: OS Independent',
    ],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6",
)

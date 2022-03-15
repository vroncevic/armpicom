<img align="right" src="https://raw.githubusercontent.com/vroncevic/armpicom/dev/docs/armpicom_logo.png" width="25%">

# Generate RPI project configuration/build setup

**armpicom** is toolset for generation of RPI project configuration/build setup.

Developed in **[python](https://www.python.org/)** code: **100%**.

[![codecov](https://codecov.io/gh/vroncevic/armpicom/branch/dev/graph/badge.svg?token=4VZJXM0YBA)](https://codecov.io/gh/vroncevic/armpicom)
[![CircleCI](https://circleci.com/gh/vroncevic/armpicom/tree/main.svg?style=svg)](https://circleci.com/gh/vroncevic/armpicom/tree/main)

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![Python package armpicom](https://github.com/vroncevic/armpicom/actions/workflows/armpicom_package.yml/badge.svg)](https://github.com/vroncevic/armpicom/actions/workflows/armpicom_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/armpicom.svg)](https://github.com/vroncevic/armpicom/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/armpicom.svg)](https://github.com/vroncevic/armpicom/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Generation flow of pyp setup](#generation-flow-of-pyp-setup)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![Development environment](https://raw.githubusercontent.com/vroncevic/armpicom/dev/docs/debtux.png)

![Install Python2 Package](https://github.com/vroncevic/armpicom/workflows/Install%20Python2%20Package%20armpicom/badge.svg?branch=main) ![Install Python3 Package](https://github.com/vroncevic/armpicom/workflows/Install%20Python3%20Package%20armpicom/badge.svg?branch=main)

Currently there are three ways to install tool
* Install process based on pip mechanism
* Install process based on build mechanism
* Install process based on docker mechanism

##### Install using pip

Python package is located at **[pypi.org](https://pypi.org/project/armpicom/)**.

You can install by using pip
```
# python2
pip2 install armpicom
# python3
pip3 install armpicom
```

##### Install using build

Navigate to release **[page](https://github.com/vroncevic/armpicom/releases/)** download and extract release archive.

To install **armpicom** type the following
```
tar xvzf armpicom-x.y.z.tar.gz
cd armpicom-x.y.z/
# python2
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
python2 get-pip.py 
python2 -m pip install --upgrade setuptools
python2 -m pip install --upgrade pip
python2 -m pip install --upgrade build
pip2 install -r requirements.txt
python2 -m build --no-isolation --wheel
pip2 install ./dist/armpicom-*-py2-none-any.whl
rm -f get-pip.py
chmod 755 /usr/local/lib/python2.7/dist-packages/usr/local/bin/armpicom_run.py
ln -s /usr/local/lib/python2.7/dist-packages/usr/local/bin/armpicom_run.py /usr/local/bin/armpicom_run.py
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build --no-isolation --wheel
pip3 install ./dist/armpicom-*-py3-none-any.whl
rm -f get-pip.py
chmod 755 /usr/local/lib/python3.9/dist-packages/usr/local/bin/armpicom_run.py
ln -s /usr/local/lib/python3.9/dist-packages/usr/local/bin/armpicom_run.py /usr/local/bin/armpicom_run.py
```

##### Install using docker

You can use Dockerfile to create image/container.

[![armpicom docker checker](https://github.com/vroncevic/armpicom/workflows/armpicom%20docker%20checker/badge.svg)](https://github.com/vroncevic/armpicom/actions?query=workflow%3A%22armpicom+docker+checker%22)

### Dependencies

**armpicom** requires next modules and libraries

* [ats-utilities - Python App/Tool/Script Utilities](https://pypi.org/project/ats-utilities/)

### Generation flow of pyp setup

Base flow of generation process

![Setup generation flow](https://raw.githubusercontent.com/vroncevic/armpicom/dev/docs/python_setup_flow.png)

### Tool structure

**armpicom** is based on OOP.

Tool structure
```
armpicom/
├── conf/
│   ├── armpicom.cfg
│   ├── armpicom.logo
│   ├── armpicom_util.cfg
│   ├── project.yaml
│   └── template/
│       ├── build/
│       │   └── armpicom.md
│       ├── CMakeLists.template
│       ├── pico_sdk_import.template
│       ├── pro_auto_set_url.template
│       └── src/
│           ├── CMakeLists.template
│           └── main.template
├── __init__.py
├── log/
│   └── armpicom.log
├── pro/
│   ├── config/
│   │   ├── __init__.py
│   │   ├── pro_name.py
│   │   └── template_dir.py
│   ├── __init__.py
│   ├── read_template.py
│   └── write_template.py
└── run/
    └── armpicom_run.py

8 directories, 19 files
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/armpicom/badge/?version=latest)](https://armpicom.readthedocs.io/en/latest/?badge=latest)

More documentation and info at
* [armpicom.readthedocs.io](https://armpicom.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2021 by [vroncevic.github.io/armpicom](https://vroncevic.github.io/armpicom)

**armpicom** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/armpicom/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)

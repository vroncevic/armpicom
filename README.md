<img align="right" src="https://raw.githubusercontent.com/vroncevic/armpicom/dev/docs/armpicom_logo.png" width="25%">

# Generate RPI project configuration/build setup

**armpicom** is toolset for generation of RPI project configuration/build setup.

Developed in **[python](https://www.python.org/)** code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/armpicom/workflows/Python%20package/badge.svg?branch=master) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/armpicom.svg)](https://github.com/vroncevic/armpicom/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/armpicom.svg)](https://github.com/vroncevic/armpicom/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using setuptools](#install-using-setuptools)
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

![Install Python2 Package](https://github.com/vroncevic/armpicom/workflows/Install%20Python2%20Package%20armpicom/badge.svg?branch=master) ![Install Python3 Package](https://github.com/vroncevic/armpicom/workflows/Install%20Python3%20Package%20armpicom/badge.svg?branch=master)

Currently there are three ways to install tool:
* Install process based on pip
* Install process based on setup.py (setuptools)
* Install process based on docker mechanism

##### Install using pip

Python package is located at **[pypi.org](https://pypi.org/project/armpicom/)**.

You can install by using pip
```
# python2
pip install armpicom
# python3
pip3 install armpicom
```

##### Install using setuptools

Navigate to release **[page](https://github.com/vroncevic/armpicom/releases/)** download and extract release archive.

To install **armpicom** type the following:
```
tar xvzf armpicom-x.y.z.tar.gz
cd armpicom-x.y.z/
# python2
pip install -r requirements.txt
python setup.py install_lib
python setup.py install_data
python setup.py install_egg_info
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_data
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container.

[![armpicom docker checker](https://github.com/vroncevic/armpicom/workflows/armpicom%20docker%20checker/badge.svg)](https://github.com/vroncevic/armpicom/actions?query=workflow%3A%22armpicom+docker+checker%22)

### Dependencies

**armpicom** requires next modules and libraries:

* [ats-utilities - Python App/Tool/Script Utilities](https://pypi.org/project/ats-utilities/)

### Generation flow of pyp setup

Base flow of generation process:

![Setup generation flow](https://raw.githubusercontent.com/vroncevic/armpicom/dev/docs/python_setup_flow.png)

### Tool structure

**armpicom** is based on OOP.

Generator structure:

```
armpicom/
├── conf/
│   ├── armpicom.cfg
│   ├── armpicom_util.cfg
│   ├── project.yaml
│   └── template/
│       ├── build/
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
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/armpicom/badge/?version=latest)](https://armpicom.readthedocs.io/en/latest/?badge=latest)

More documentation and info at:

* [armpicom.readthedocs.io](https://armpicom.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2018 by [vroncevic.github.io/armpicom](https://vroncevic.github.io/armpicom)

**armpicom** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/armpicom/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)

# Generate RPI project configuration/build setup

<img align="right" src="https://raw.githubusercontent.com/vroncevic/armpicom/dev/docs/armpicom_logo.png" width="25%">

**armpicom** is toolset for generation of RPI PICO project configuration/build setup.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![armpicom python checker](https://github.com/vroncevic/armpicom/actions/workflows/armpicom_python_checker.yml/badge.svg)](https://github.com/vroncevic/armpicom/actions/workflows/armpicom_python_checker.yml) [![armpicom package checker](https://github.com/vroncevic/armpicom/actions/workflows/armpicom_package_checker.yml/badge.svg)](https://github.com/vroncevic/armpicom/actions/workflows/armpicom_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/armpicom.svg)](https://github.com/vroncevic/armpicom/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/armpicom.svg)](https://github.com/vroncevic/armpicom/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/armpicom/dev/docs/debtux.png)

[![armpicom python3 build](https://github.com/vroncevic/armpicom/actions/workflows/armpicom_python3_build.yml/badge.svg)](https://github.com/vroncevic/armpicom/actions/workflows/armpicom_python3_build.yml)

Currently there are three ways to install package
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

**armpicom** is located at **[pypi.org](https://pypi.org/project/armpicom/)**.

You can install by using pip

```bash
# python3
pip3 install armpicom
```

##### Install using build

Navigate to release **[page](https://github.com/vroncevic/armpicom/releases/)** download and extract release archive.

To install **armpicom** type the following

```bash
tar xvzf armpicom-x.y.z.tar.gz
cd armpicom-x.y.z/
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
chmod 755 /usr/local/lib/python3.10/dist-packages/usr/local/bin/armpicom_run.py
ln -s /usr/local/lib/python3.10/dist-packages/usr/local/bin/armpicom_run.py /usr/local/bin/armpicom_run.py
```

##### Install using py setup

Navigate to **[release page](https://github.com/vroncevic/armpicom/releases)** download and extract release archive.

To install **armpicom** locate and run setup.py with arguments

```bash
tar xvzf armpicom-x.y.z.tar.gz
cd armpicom-x.y.z
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container.

### Dependencies

**armpicom** requires next modules and libraries

* [ats-utilities - Python App/Tool/Script Utilities](https://pypi.org/project/ats-utilities/)

### Tool structure

**armpicom** is based on OOP.

Tool structure

```bash
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
        │   ├── __init__.py
        │   ├── read_template.py
        │   └── write_template.py
        ├── py.typed
        └── run/
            └── armpicom_run.py
    
    8 directories, 17 files
```

### Code coverage

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `armpicom/__init__.py` | 71 | 12 | 83% |
| `armpicom/pro/__init__.py` | 59 | 2 | 97% |
| `armpicom/pro/read_template.py` | 53 | 2 | 96% |
| `armpicom/pro/write_template.py` | 58 | 3 | 95% |
| **Total** | 241 | 19 | 92% |

### Docs

[![Documentation Status](https://readthedocs.org/projects/armpicom/badge/?version=latest)](https://armpicom.readthedocs.io/en/latest/?badge=latest)

More documentation and info at

* [armpicom.readthedocs.io](https://armpicom.readthedocs.io)
* [www.python.org](https://www.python.org/)

### Contributing

[Contributing to armpicom](CONTRIBUTING.md)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2021 - 2024 by [vroncevic.github.io/armpicom](https://vroncevic.github.io/armpicom)

**armpicom** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/armpicom/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)

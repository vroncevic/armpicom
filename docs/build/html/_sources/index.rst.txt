Generate RPI project configuration/build setup
-----------------------------------------------

**armpicom** is toolset for generation of of RPI project configuration/build setup.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

|Python package| |GitHub issues| |Documentation Status| |GitHub contributors|

.. |Python package| image:: https://github.com/vroncevic/armpicom/workflows/Python%20package/badge.svg
   :target: https://github.com/vroncevic/armpicom/workflows/Python%20package/badge.svg?branch=main

.. |GitHub issues| image:: https://img.shields.io/github/issues/vroncevic/armpicom.svg
   :target: https://github.com/vroncevic/armpicom/issues

.. |GitHub contributors| image:: https://img.shields.io/github/contributors/vroncevic/armpicom.svg
   :target: https://github.com/vroncevic/armpicom/graphs/contributors

.. |Documentation Status| image:: https://readthedocs.org/projects/armpicom/badge/?version=latest
   :target: https://armpicom.readthedocs.io/projects/armpicom/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   modules
   self

Installation
-------------

|Install Python2 Package| |Install Python3 Package|

.. |Install Python2 Package| image:: https://github.com/vroncevic/armpicom/workflows/Install%20Python2%20Package%20armpicom/badge.svg
   :target: https://github.com/vroncevic/armpicom/workflows/Install%20Python2%20Package%20armpicom/badge.svg?branch=main

.. |Install Python3 Package| image:: https://github.com/vroncevic/armpicom/workflows/Install%20Python3%20Package%20armpicom/badge.svg
   :target: https://github.com/vroncevic/armpicom/workflows/Install%20Python3%20Package%20armpicom/badge.svg?branch=main

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/armpicom/releases

To install **armpicom** type the following:

.. code-block:: bash

    tar xvzf armpicom-x.y.z.tar.gz
    cd armpicom-x.y.z/
    # python2
    pip install -r requirements.txt
    python setup.py install_lib
    python setup.py install_data
    python setup.py install_egg_info
    # pyton3
    pip3 install -r requirements.txt
    python3 setup.py install_lib
    python3 setup.py install_data
    python3 setup.py install_egg_info

You can use Docker to create image/container, or You can use pip to install:

.. code-block:: bash

    # pyton2
    pip install armpicom
    # pyton3
    pip3 install armpicom

|GitHub docker checker|

.. |GitHub docker checker| image:: https://github.com/vroncevic/armpicom/workflows/armpicom%20docker%20checker/badge.svg
   :target: https://github.com/vroncevic/armpicom/actions?query=workflow%3A%22armpicom+docker+checker%22

Dependencies
-------------

**armpicom** requires next modules and libraries:

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Generation flow of project setup
---------------------------------

Base flow of generation process:

.. image:: https://raw.githubusercontent.com/vroncevic/armpicom/dev/docs/python_setup_flow.png

Tool structure
---------------

**armpicom** is based on OOP.

Code structure:

.. code-block:: bash

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

Copyright and licence
-----------------------

|License: GPL v3| |License: Apache 2.0|

.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |License: Apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2021 by `vroncevic.github.io/armpicom <https://vroncevic.github.io/armpicom>`_

**armpicom** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|Python Software Foundation|

.. |Python Software Foundation| image:: https://raw.githubusercontent.com/vroncevic/armpicom/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|Donate|

.. |Donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

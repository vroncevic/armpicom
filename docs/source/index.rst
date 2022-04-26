Generate RPI project configuration/build setup
-----------------------------------------------

☯️ **armpicom** is toolset for generation of of RPI project configuration/build setup.

Developed in 🐍 `python <https://www.python.org/>`_ code.

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

|python package| |github issues| |documentation status| |github contributors|

.. |python package| image:: https://img.shields.io/github/workflow/status/vroncevic/armpicom/armpicom_python_checker?style=flat&label=armpicom%20python%20checker
   :target: https://img.shields.io/github/workflow/status/vroncevic/armpicom/armpicom_python_checker

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/armpicom.svg
   :target: https://github.com/vroncevic/armpicom/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/armpicom.svg
   :target: https://github.com/vroncevic/armpicom/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/armpicom/badge/?version=latest
   :target: https://armpicom.readthedocs.io/projects/armpicom/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   modules
   self

Installation
-------------

|install python2 package| |install python3 package|

.. |install python2 package| image:: https://img.shields.io/github/workflow/status/vroncevic/armpicom/armpicom_python2_build?style=flat&label=armpicom%20python2%20build
   :target: https://img.shields.io/github/workflow/status/vroncevic/armpicom/armpicom_python2_build

.. |install python3 package| image:: https://img.shields.io/github/workflow/status/vroncevic/armpicom/armpicom_python3_build?style=flat&label=armpicom%20python3%20build
   :target: https://img.shields.io/github/workflow/status/vroncevic/armpicom/armpicom_python3_build

|debian linux os|

.. |debian linux os| image:: https://raw.githubusercontent.com/vroncevic/armpicom/dev/docs/debtux.png

Navigate to release `page`_ download and extract release archive 📦.

.. _page: https://github.com/vroncevic/armpicom/releases

To install **armpicom** 📦 type the following

.. code-block:: bash

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

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # pyton2
    pip2 install armpicom
    # pyton3
    pip3 install armpicom

|github docker checker|

.. |github docker checker| image:: https://img.shields.io/github/workflow/status/vroncevic/armpicom/armpicom_docker_checker?style=flat&label=armpicom%20docker%20checker
   :target: https://img.shields.io/github/workflow/status/vroncevic/armpicom/armpicom_docker_checker

Dependencies
-------------

**armpicom** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Generation flow of project setup
---------------------------------

Base flow of generation process

.. image:: https://raw.githubusercontent.com/vroncevic/armpicom/dev/docs/python_setup_flow.png

Tool structure
---------------

**armpicom** is based on OOP.

🧰 Tool structure

.. code-block:: bash

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

Copyright and licence
-----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2021 by `vroncevic.github.io/armpicom <https://vroncevic.github.io/armpicom>`_

**armpicom** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

🌎 🌍 🌏 Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/armpicom/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

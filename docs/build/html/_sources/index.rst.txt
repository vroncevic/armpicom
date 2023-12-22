Generate RPI PICO project configuration/build setup
----------------------------------------------------

**armpicom** is toolset for generation of of RPI PICO project configuration/build setup.

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

|armpicom python checker| |armpicom python package| |github issues| |documentation status| |github contributors|

.. |armpicom python checker| image:: https://github.com/vroncevic/armpicom/actions/workflows/armpicom_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/armpicom/actions/workflows/armpicom_python_checker.yml

.. |armpicom python package| image:: https://github.com/vroncevic/armpicom/actions/workflows/armpicom_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/armpicom/actions/workflows/armpicom_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/armpicom.svg
   :target: https://github.com/vroncevic/armpicom/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/armpicom.svg
   :target: https://github.com/vroncevic/armpicom/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen-avr8/badge/?version=latest
   :target: https://gen-avr8.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   modules
   self

Installation
-------------

|armpicom python3 build|

.. |armpicom python3 build| image:: https://github.com/vroncevic/armpicom/actions/workflows/armpicom_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/armpicom/actions/workflows/armpicom_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/armpicom/releases

To install **armpicom** type the following

.. code-block:: bash

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

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # pyton3
    pip3 install armpicom

Dependencies
-------------

**armpicom** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
---------------

**armpicom** is based on OOP.

Tool structure

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
        │   ├── __init__.py
        │   ├── read_template.py
        │   └── write_template.py
        └── run/
            └── armpicom_run.py

    8 directories, 16 files

Copyright and licence
-----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2021 - 2024 by `vroncevic.github.io/armpicom <https://vroncevic.github.io/armpicom>`_

**armpicom** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/armpicom/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

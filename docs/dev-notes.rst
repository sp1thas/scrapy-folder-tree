Development
===========

Workflow
--------

This project uses the Github Flow.

.. image:: _static/githubflow.png
   :alt: The Github workflow

Dev Environment
---------------

Navigate in the project's root folder and run:

.. code-block:: shell

    poetry install --dev

Make sure that poetry is already installed.

Static analysis
---------------

The project is static analysed using the following tools:


isort
+++++

Make sure that imports are properly formatted using the following command:

.. code-block:: shell

    poetry run isort .

mypy
++++

Make sure that type annotations are properly specified using the following command:

.. code-block:: shell

    poetry run mypy src

black
+++++

Make sure that source code is properly formatted using the following command:

.. code-block:: shell

    poetry run black .

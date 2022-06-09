Introduction
=====================

Everything that can be done using the `ValkyrieManager <https://xenanetworks.com/product/valkyriemanager/>`_ (or `VulcanManager <https://xenanetworks.com/product/vulcanmanager/>`_ ) can also be done through CLI scripting, and in a nearly identical fashion.

.. note::
    
    Please keep this in mind even though most of the examples use the ValkyrieManager for illustration.

Xena chassis can be controlled in the following ways:

1. In a point-and-click interactive style using ValkyrieManager (or VulcanManager).
2. In a command-line-interface style using a text-based scripting interface.
3. In an object-oriented programming style using `Xena OpenAutomation (XOA) Python API <https://github.com/xenadevel/xena-open-automation-python-api>`_.

.. note::
    
    Using XOA Python API to develop test scripts to control Xena testers are out of the scope of this document. 

The CLI commands are simple lines of text exchanged between a client and the Xena chassis. An example of a CLI command to the chassis could be:

.. code-block::
    :linenos:
    
    0/5 PS_RATEPPS [3] 500000

This goes to module 0, port 5, and sets stream 3's rate to 500000 packets per second. The chassis responds with:

.. code-block::
    :linenos:

    <OK>

You would query for the current parameter this way:

.. code-block::
    :linenos:

    0/5 PS_RATEPPS [3] ?

And the chassis would respond in exactly the same way that you set the parameter yourself:

.. code-block::
    :linenos:
    
    0/5 PS_RATEPPS [3] 500000

.. note::
    
    This is exactly the same syntax used when saving and loading port configurations (.xpc file) to files on the client PC. This lets you use saved configurations as a starting point for scripting, and it also allows you to modify the saved files before loading them back into the chassis.


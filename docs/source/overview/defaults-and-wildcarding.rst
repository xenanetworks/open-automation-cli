Defaults and Wildcarding
==========================================

The CLI environment provides you with optional default values for the module index and port index, allowing you to set and get without providing the module and port index explicitly.

Default indices are enabled and disabled using the following short commands:

* ``<module-index>/<port-index>``, set default module and port to the specified values.
* ``<port-index>``, set default port to the specified value, retaining the default module.
* ``-/-``, disable the default module and port.
* ``–``, disable the default port, retaining the default module.
* ``<module-index>/-``, set the default module and disable the default port.
* ``?``, show the current default module and port.

When a default module and port is provided, commands that would otherwise require explicit module and port index values can be written without them, e.g.

.. code-block::
    :linenos:

    PS_RATEPPS [3] 500
    ^---
    #Index error in column 1

    0/5
    PS_RATEPPS [3] 500
    <OK>

Replies from the chassis will also use the current default values to suppress the explicit module and port indices when possible.

The scripting environment also provides wildcarding across modules and ports. Using an asterisk as a module or port index effectively makes the chassis execute the command for each value, e.g.

.. code-block::
    :linenos:

    0/* P_INTERFRAMEGAP 30

This sets the inter-frame gap for every port on module 0. It will generate an individual status response for each operation, and indeed some may succeed while others fail, for instance, due to lack of reservation.

Wildcards also work for queries. This will give you the inter-frame gap for each port of module 0:

.. code-block::
    :linenos:

    0/* P_INTERFRAMEGAP ?

Wildcards cannot be used as default values, but the default and wildcard mechanisms can be combined, for instance, to use a default module together with a wildcarded port:

.. code-block::
    :linenos:

    0/-
    * P_INTERFRAMEGAP 30


Indeed, for chassis with a single module, you will typically set it as the default module and then use only port indices.

.. important:: 
    Wildcard ``*`` is not supported by the ValkyrieManager's integrated Script Client.

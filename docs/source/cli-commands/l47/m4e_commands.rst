L47 Module Packet Engine Commands
-----------------------------------

``M4E_MODE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M4E_MODE <mode>

    # get
    <module-index> M4E_MODE ?

:Description:
    Select resource allocation mode.

:Actions:
    set, get

:Parameter:
    ``mode: <ResourceAllocationMode>``, resource allocation mode

        * ``SIMPLE = 0``
        * ``ADVANCED = 1``

:Example:
    .. code-block::

        # set
        input:  0 M4E_MODE SIMPLE
        output: <OK>

        # get
        input:  0 M4E_MODE ?
        output: 0 M4E_MODE SIMPLE


``M4E_RESERVE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M4E_RESERVE <mask>

    # get
    <module-index> M4E_RESERVE ?

:Description:
    Advanced mode only: Reserve a number of PEs so they later can be assigned to
    specific ports.

:Actions:
    set, get

:Parameter:
    ``mask: <string>``, bitmask of PEs to reserve


:Example:
    .. code-block::

        # set
        input:  0 M4E_RESERVE word
        output: <OK>

        # get
        input:  0 M4E_RESERVE ?
        output: 0 M4E_RESERVE word



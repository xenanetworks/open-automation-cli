Transceiver Commands
---------------------

``PX_RW``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PX_RW [<page_xindex>] <value>

    # get
    <module-index>/<port-index> PX_RW [<page_xindex>] ?

:Description:
    Provides access to the register interface supported by the port transceiver.  It
    is possible to both read and write register values.

:Actions:
    set, get

:Parameter:
    ``value: <string>``, register value of a transceiver


:Example:
    .. code-block::

        # set
        input:  0/1 PX_RW [0] word
        output: <OK>

        # get
        input:  0/1 PX_RW [0] ?
        output: 0/1 PX_RW [0] word


``PX_MII``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PX_MII <value>

    # get
    <module-index>/<port-index> PX_MII ?

:Description:
    Provides access to the register interface supported by the media-independent interface (MII) transceiver.  It
    is possible to both read and write register values.

:Actions:
    set, get

:Parameter:
    ``value: <string>``, register value of a transceiver


:Example:
    .. code-block::

        # set
        input:  0/1 PX_MII word
        output: <OK>

        # get
        input:  0/1 PX_MII ?
        output: 0/1 PX_MII word


``PX_TEMPERATURE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PX_TEMPERATURE ?

:Description:
    Transceiver temperature in degrees Celsius.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PX_TEMPERATURE ?
        output: 0/1 PX_TEMPERATURE



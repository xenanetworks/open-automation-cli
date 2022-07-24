TX Statistics Commands
-----------------------

``PT_TOTAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PT_TOTAL ?

:Description:
    Obtains statistics concerning all the packets transmitted on a port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PT_TOTAL ?
        output: 0/1 PT_TOTAL


``PT_NOTPLD``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PT_NOTPLD ?

:Description:
    Obtains statistics concerning the packets without a test payload transmitted on
    a port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PT_NOTPLD ?
        output: 0/1 PT_NOTPLD


``PT_STREAM``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PT_STREAM [<stream_xindex>] ?

:Description:
    Obtains statistics concerning the packets of a specific stream transmitted on a
    port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PT_STREAM [0] ?
        output: 0/1 PT_STREAM [0]


``PT_CLEAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PT_CLEAR


:Description:
    Clear all the transmit statistics for a port. The byte and packet counts will
    restart at zero.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PT_CLEAR
        output: <OK>



``PT_EXTRA``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PT_EXTRA ?

:Description:
    Obtains additional statistics for packets transmitted on a port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PT_EXTRA ?
        output: 0/1 PT_EXTRA


``PT_FLOWTOTAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PT_FLOWTOTAL [<flow_xindex>] ?

:Description:
    Obtains statistics concerning all the packets transmitted from a between this
    receive port and its partner TX port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PT_FLOWTOTAL [0] ?
        output: 0/1 PT_FLOWTOTAL [0]


``PT_FLOWCLEAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PT_FLOWCLEAR [<flow_xindex>]


:Description:
    Clear all the transmit statistics on a particular flow for a Chimera port. The
    byte and packet counts will restart at zero.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PT_FLOWCLEAR [0]
        output: <OK>




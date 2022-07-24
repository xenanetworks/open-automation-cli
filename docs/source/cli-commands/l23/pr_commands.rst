RX Statistics Commands
-----------------------

``PR_TPLDJITTER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PR_TPLDJITTER [<test_payload_xindex>] ?

:Description:
    Obtains statistics concerning the jitter experienced by the packets with a
    particular test payload id received on a port. The values are the difference in
    packet-to-packet latency, and the minimum will usually be zero.A special value
    of -1 is returned if jitter numbers are not applicable. They are only available
    for TID values 0..31.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PR_TPLDJITTER [0] ?
        output: 0/1 PR_TPLDJITTER [0]


``PR_TOTAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PR_TOTAL ?

:Description:
    Obtains statistics concerning all the packets received on a port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PR_TOTAL ?
        output: 0/1 PR_TOTAL


``PR_NOTPLD``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PR_NOTPLD ?

:Description:
    Obtains statistics concerning the packets without a test payload received on a
    port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PR_NOTPLD ?
        output: 0/1 PR_NOTPLD


``PR_EXTRA``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PR_EXTRA ?

:Description:
    Obtains statistics concerning special errors received on a port since received statistics were cleared.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PR_EXTRA ?
        output: 0/1 PR_EXTRA


``PR_TPLDS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PR_TPLDS ?

:Description:
    Obtain the set of test payload IDs observed among the received packets since
    receive statistics were cleared. Traffic statistics for these test payload
    streams will have non-zero byte and packet count.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PR_TPLDS ?
        output: 0/1 PR_TPLDS


``PR_TPLDTRAFFIC``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PR_TPLDTRAFFIC [<test_payload_xindex>] ?

:Description:
    Obtains traffic statistics concerning the packets with a particular test payload
    identifier received on a port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PR_TPLDTRAFFIC [0] ?
        output: 0/1 PR_TPLDTRAFFIC [0]


``PR_TPLDERRORS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PR_TPLDERRORS [<test_payload_xindex>] ?

:Description:
    Obtains statistics concerning errors in the packets with a particular test
    payload id received on a port. The error information is derived from analysing
    the various fields contained in the embedded test payloads of the received
    packets, independent of which chassis and port may have originated the packets.
    Note that packet-lost statistics involve both a transmitting port and a
    receiving port, and in particular knowing which port originated the packets with
    a particular test payload identifier. This information requires knowledge of the
    global test environment, and is not supported at the port-level.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PR_TPLDERRORS [0] ?
        output: 0/1 PR_TPLDERRORS [0]


``PR_TPLDLATENCY``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PR_TPLDLATENCY [<test_payload_xindex>] ?

:Description:
    Obtains statistics concerning the latency experienced by the packets with a
    particular test payload id received on a port. The values are adjusted by the
    port-level P_LATENCYOFFSET value. A special value of -1 is returned if latency
    numbers are not applicable. Latency is only meaningful when the clocks of the
    transmitter and receiver are synchronized. This requires the two ports to be on
    the same test module, and it requires knowledge of the global test environment
    to ensure that packets are in fact routed between these ports.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PR_TPLDLATENCY [0] ?
        output: 0/1 PR_TPLDLATENCY [0]


``PR_FILTER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PR_FILTER [<filter_xindex>] ?

:Description:
    Obtains statistics concerning the packets satisfying the condition of a
    particular filter for a port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PR_FILTER [0] ?
        output: 0/1 PR_FILTER [0]


``PR_CLEAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PR_CLEAR


:Description:
    Clear all the receive statistics for a port. The byte and packet counts will
    restart at zero.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PR_CLEAR
        output: <OK>



``PR_CALIBRATE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PR_CALIBRATE


:Description:
    Calibrate the latency calculation for packets received on a port. The lowest
    detected latency value (across all Test Payload IDs) will be set as the new
    base.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PR_CALIBRATE
        output: <OK>



``PR_UAT_STATUS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PR_UAT_STATUS ?

:Description:
    This command will show the current UAT (UnAvailable Time) state, which is used
    in Valkyrie1564

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PR_UAT_STATUS ?
        output: 0/1 PR_UAT_STATUS


``PR_UAT_TIME``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PR_UAT_TIME ?

:Description:
    This command will show the current number of unavailable seconds, which is used in Valkyrie1564.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PR_UAT_TIME ?
        output: 0/1 PR_UAT_TIME


``PR_PFCSTATS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PR_PFCSTATS ?

:Description:
    Obtains statistics of received Priority Flow Control (PFC) packets on a port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PR_PFCSTATS ?
        output: 0/1 PR_PFCSTATS


``PR_FLOWTOTAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PR_FLOWTOTAL [<flow_xindex>] ?

:Description:
    Obtains statistics concerning all the packets received from a flow between this
    receive port and its partner TX port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PR_FLOWTOTAL [0] ?
        output: 0/1 PR_FLOWTOTAL [0]


``PR_FLOWCLEAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PR_FLOWCLEAR [<flow_xindex>]


:Description:
    Clear all the receive statistics on a particular flow for a Chimera port. The
    byte and packet counts will restart at zero.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PR_FLOWCLEAR [0]
        output: <OK>




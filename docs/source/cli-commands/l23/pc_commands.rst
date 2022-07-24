Capture Commands
---------------------

``PC_TRIGGER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PC_TRIGGER <start_criteria> <start_criteria_filter> <stop_criteria> <stop_criteria_filter>

    # get
    <module-index>/<port-index> PC_TRIGGER ?

:Description:
    The criteria for when to start and stop the capture process for a port. Even
    when capture is enabled with P_CAPTURE, the actual capturing of packets can be
    delayed until a particular start criteria is met by a received packet.
    Likewise, a stop criteria can be specified, based on a received packet. If no
    explicit stop criteria is specified, capture  stops when the internal buffer
    runs full. In buffer overflow situations, if there is an explicit  stop
    criteria, then the latest packets will be retained (and the early ones
    discarded),  and otherwise, the earliest packets are retained (and the later
    ones discarded).

:Actions:
    set, get

:Parameter:
    ``start_criteria: <StartTrigger>``, the criteria for starting the actual packet capture

        * ``ON = 0``
        * ``FCSERR = 1``
        * ``FILTER = 2``
        * ``PLDERR = 3``

    ``start_criteria_filter: <integer>``, the index of a particular filter for the start criteria

    ``stop_criteria: <StopTrigger>``, the criteria for stopping the actual packet capture

        * ``FULL = 0``
        * ``FCSERR = 1``
        * ``FILTER = 2``
        * ``PLDERR = 3``
        * ``USERSTOP = 4``

    ``stop_criteria_filter: <integer>``, the index of a particular filter for the stop criteria


:Example:
    .. code-block::

        # set
        input:  0/1 PC_TRIGGER ON 1 FULL 1
        output: <OK>

        # get
        input:  0/1 PC_TRIGGER ?
        output: 0/1 PC_TRIGGER ON 1 FULL 1


``PC_KEEP``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PC_KEEP <kind> <index> <byte_count>

    # get
    <module-index>/<port-index> PC_KEEP ?

:Description:
    Which packets to keep once the start criteria has been triggered for a port.
    Also how big a portion of each packet to retain, saving space for more packets
    in the capture buffer.

:Actions:
    set, get

:Parameter:
    ``kind: <PacketType>``, which general kind of packets to keep

        * ``ALL = 0``
        * ``FCSERR = 1``
        * ``NOTPLD = 2``
        * ``TPLD = 3``
        * ``FILTER = 4``
        * ``PLDERR = 5``
        
    ``index: <integer>``, test payload id or filter index for which packets to keep

    ``byte_count: <integer>``, how many bytes to keep in the buffer for of each packet. The value -1 means no limit on packet size.


:Example:
    .. code-block::

        # set
        input:  0/1 PC_KEEP ALL 1 1
        output: <OK>

        # get
        input:  0/1 PC_KEEP ?
        output: 0/1 PC_KEEP ALL 1 1


``PC_STATS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PC_STATS ?

:Description:
    Obtains the number of packets currently in the capture buffer for a port. The
    count is reset to zero when capture is turned on.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PC_STATS ?
        output: 0/1 PC_STATS


``PC_EXTRA``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PC_EXTRA [<apture_packet_xindex>] ?

:Description:
    Obtains extra information about a captured packet for a port. The information
    comprises time of capture, latency, inter-frame gap, and original packet length.
    Latency is only valid for packets with test payloads and where the originating
    port is on the same module and therefore has the same clock.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PC_EXTRA [0] ?
        output: 0/1 PC_EXTRA [0]


``PC_PACKET``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PC_PACKET [<apture_packet_xindex>] ?

:Description:
    Obtains the raw bytes of a captured packet for a port. The packet data may be
    truncated if the PC_KEEP command specified a limit on the number of bytes
    kept.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PC_PACKET [0] ?
        output: 0/1 PC_PACKET [0]



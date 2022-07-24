L47 Connection Group Commands
-----------------------------------

``P4G_INDICES``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_INDICES <group_identifiers>

    # get
    <module-index>/<port-index> P4G_INDICES ?

:Description:
    The full list of Connection Groups on this port. These are the sub-index that
    are used for the parameters that specify TCP connection behavior.

:Actions:
    set, get

:Parameter:
    ``group_identifiers: <integer list>``, list of indices identifying Connection Groups.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_INDICES 0 1
        output: <OK>

        # get
        input:  0/1 P4G_INDICES ?
        output: 0/1 P4G_INDICES 0 1


``P4G_CREATE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_CREATE [<group_xindex>]


:Description:
    Creates an empty Connection Group with the specified sub-index value.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_CREATE [0]
        output: <OK>



``P4G_DELETE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_DELETE [<group_xindex>]


:Description:
    Deletes a Connection Group with the specified sub-index value.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_DELETE [0]
        output: <OK>



``P4G_ENABLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_ENABLE [<group_xindex>] <status>

    # get
    <module-index>/<port-index> P4G_ENABLE [<group_xindex>] ?

:Description:
    Enable/disable/suppress a previously created Connection Group with the specified
    sub-index value.

:Actions:
    set, get

:Parameter:
    ``status: <OnOffWithSuppress>``, specifies the state of the Connection Group.

        * ``OFF = 0``
        * ``ON = 1``
        * ``SUPPRESS = 2``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_ENABLE [0] OFF
        output: <OK>

        # get
        input:  0/1 P4G_ENABLE [0] ?
        output: 0/1 P4G_ENABLE [0] OFF


``P4G_COMMENT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_COMMENT [<group_xindex>] <comment>

    # get
    <module-index>/<port-index> P4G_COMMENT [<group_xindex>] ?

:Description:
    The description of a Connection Group.

:Actions:
    set, get

:Parameter:
    ``comment: <string>``, the description of a Connection Group.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_COMMENT [0] word
        output: <OK>

        # get
        input:  0/1 P4G_COMMENT [0] ?
        output: 0/1 P4G_COMMENT [0] word


``P4G_CLEAR_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_CLEAR_COUNTERS [<group_xindex>]


:Description:
    Clears all run-time statistics for the Connection Group.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_CLEAR_COUNTERS [0]
        output: <OK>



``P4G_ROLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_ROLE [<group_xindex>] <role>

    # get
    <module-index>/<port-index> P4G_ROLE [<group_xindex>] ?

:Description:
    Specifies the client or server role for this Connection Group. A server
    passively waits for the clients to establish connections.

:Actions:
    set, get

:Parameter:
    ``role: <Role>``, the role of the Connection Group.

        * ``CLIENT = 0``
        * ``SERVER = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_ROLE [0] CLIENT
        output: <OK>

        # get
        input:  0/1 P4G_ROLE [0] ?
        output: 0/1 P4G_ROLE [0] CLIENT


``P4G_CLIENT_RANGE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_CLIENT_RANGE [<group_xindex>] <ipv4_address> <address_count> <start_port> <port_count> <max_address_count>

    # get
    <module-index>/<port-index> P4G_CLIENT_RANGE [<group_xindex>] ?

:Description:
    Specifies a number of client sockets (ip address, port number)

:Actions:
    set, get

:Parameter:
    ``ipv4_address: <ipv4_address>``, the start IP address of the address range

    ``address_count: <integer>``, the number of IP addresses

    ``start_port: <integer>``, the starting port number of the port range

    ``port_count: <integer>``, the number of ports

    ``max_address_count: <integer>``, the maximum number of IP addresses that this Connection Group will use, when connection incarnation is set to ``REINCARNATE``


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_CLIENT_RANGE [0] 192.168.1.100 1 1 1 1
        output: <OK>

        # get
        input:  0/1 P4G_CLIENT_RANGE [0] ?
        output: 0/1 P4G_CLIENT_RANGE [0] 192.168.1.100 1 1 1 1


``P4G_SERVER_RANGE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_SERVER_RANGE [<group_xindex>] <ipv4_address> <address_count> <start_port> <port_count>

    # get
    <module-index>/<port-index> P4G_SERVER_RANGE [<group_xindex>] ?

:Description:
    Specifies a number of server sockets (ip address, port number)

:Actions:
    set, get

:Parameter:
    ``ipv4_address: <ipv4_address>``, the start IP address of the address range

    ``address_count: <integer>``, the number of IP addresses

    ``start_port: <integer>``, the starting port number of the port range

    ``port_count: <integer>``, the number of ports


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_SERVER_RANGE [0] 192.168.1.100 1 1 1
        output: <OK>

        # get
        input:  0/1 P4G_SERVER_RANGE [0] ?
        output: 0/1 P4G_SERVER_RANGE [0] 192.168.1.100 1 1 1


``P4G_LP_TIME_SCALE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_LP_TIME_SCALE [<group_xindex>] <timescale>

    # get
    <module-index>/<port-index> P4G_LP_TIME_SCALE [<group_xindex>] ?

:Description:
    Specifies the time scale of the load profile.

:Actions:
    set, get

:Parameter:
    ``timescale: <Timescale>``, specifying the time scale.

        * ``MSECS = 0``
        * ``SECONDS = 1``
        * ``MINUTES = 2``
        * ``HOURS = 3``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_LP_TIME_SCALE [0] MSECS
        output: <OK>

        # get
        input:  0/1 P4G_LP_TIME_SCALE [0] ?
        output: 0/1 P4G_LP_TIME_SCALE [0] MSECS


``P4G_LP_SHAPE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_LP_SHAPE [<group_xindex>] <star_time> <rampup_duration> <steady_duration> <rampdown_duration>

    # get
    <module-index>/<port-index> P4G_LP_SHAPE [<group_xindex>] ?

:Description:
    Specifies a load profile time duration. Time is measured from the beginning of
    the test when ``P€G_TRAFFIC`` is set to ``ON``.

:Actions:
    set, get

:Parameter:
    ``star_time: <integer>``, ramp-up start time

    ``rampup_duration: <integer>``, ramp-up phase duration

    ``steady_duration: <integer>``, steady phase duration

    ``rampdown_duration: <integer>``, ramp-down phase duration


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_LP_SHAPE [0] 1 1 1 1
        output: <OK>

        # get
        input:  0/1 P4G_LP_SHAPE [0] ?
        output: 0/1 P4G_LP_SHAPE [0] 1 1 1 1


``P4G_NAT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_NAT [<group_xindex>] <on_off>

    # get
    <module-index>/<port-index> P4G_NAT [<group_xindex>] ?

:Description:
    Specify whether to support DUT Source NAT functionality. NAT should be enabled on both Client and Server ports that belong to the same Connection Group.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, specifying whether to enable Source NAT support

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_NAT [0] OFF
        output: <OK>

        # get
        input:  0/1 P4G_NAT [0] ?
        output: 0/1 P4G_NAT [0] OFF


``P4G_TCP_RTT_VALUE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TCP_RTT_VALUE [<group_xindex>] ?

:Description:
    Returns values that can be used to calculate the RTT value of all connections in
    a Connection Group.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TCP_RTT_VALUE [0] ?
        output: 0/1 P4G_TCP_RTT_VALUE [0]


``P4G_TCP_STATE_CURRENT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TCP_STATE_CURRENT [<group_xindex>] ?

:Description:
    Returns a list of the current TCP state counters. The counters returned
    corresponds the the following TCP states:
    
    * CLOSED
    * LISTEN
    * SYN_SENT
    * TCP_SYN_RCVD
    * ESTABLISHED
    * FIN_WAIT_1
    * FIN_WAIT_2
    * CLOSE_WAIT
    * CLOSING
    * LAST_ACK
    * TIME_WAIT

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TCP_STATE_CURRENT [0] ?
        output: 0/1 P4G_TCP_STATE_CURRENT [0]


``P4G_TCP_STATE_TOTAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TCP_STATE_TOTAL [<group_xindex>] ?

:Description:
    Returns a list of the total TCP state counters. The counters returned
    corresponds the the following TCP states:

    * CLOSED
    * LISTEN
    * SYN_SENT
    * TCP_SYN_RCVD
    * ESTABLISHED
    * FIN_WAIT_1
    * FIN_WAIT_2
    * CLOSE_WAIT
    * CLOSING
    * LAST_ACK
    * TIME_WAIT

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TCP_STATE_TOTAL [0] ?
        output: 0/1 P4G_TCP_STATE_TOTAL [0]


``P4G_TCP_STATE_RATE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TCP_STATE_RATE [<group_xindex>] ?

:Description:
    Returns a list of the TCP state rates measured in connections/second. The
    counters returned corresponds the the following TCP state rates:

    * CLOSED
    * LISTEN
    * SYN_SENT
    * TCP_SYN_RCVD
    * ESTABLISHED
    * FIN_WAIT_1
    * FIN_WAIT_2
    * CLOSE_WAIT
    * CLOSING
    * LAST_ACK
    * TIME_WAIT

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TCP_STATE_RATE [0] ?
        output: 0/1 P4G_TCP_STATE_RATE [0]


``P4G_TCP_RX_PAYLOAD_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TCP_RX_PAYLOAD_COUNTERS [<group_xindex>] ?

:Description:
    Returns a list of the TCP Rx payload counters.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TCP_RX_PAYLOAD_COUNTERS [0] ?
        output: 0/1 P4G_TCP_RX_PAYLOAD_COUNTERS [0]


``P4G_TCP_TX_PAYLOAD_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TCP_TX_PAYLOAD_COUNTERS [<group_xindex>] ?

:Description:
    Returns a list of the TCP Tx payload counters.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TCP_TX_PAYLOAD_COUNTERS [0] ?
        output: 0/1 P4G_TCP_TX_PAYLOAD_COUNTERS [0]


``P4G_TCP_RETRANSMIT_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TCP_RETRANSMIT_COUNTERS [<group_xindex>] ?

:Description:
    Returns a list of TCP retransmission counters.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TCP_RETRANSMIT_COUNTERS [0] ?
        output: 0/1 P4G_TCP_RETRANSMIT_COUNTERS [0]


``P4G_TCP_ERROR_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TCP_ERROR_COUNTERS [<group_xindex>] ?

:Description:
    Returns a list of TCP error counters.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TCP_ERROR_COUNTERS [0] ?
        output: 0/1 P4G_TCP_ERROR_COUNTERS [0]


``P4G_IP_DS_TYPE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_IP_DS_TYPE [<group_xindex>] <ds_type>

    # get
    <module-index>/<port-index> P4G_IP_DS_TYPE [<group_xindex>] ?

:Description:
    Configure the mode of the DS field of the IP header of this Connection Group.

:Actions:
    set, get

:Parameter:
    ``ds_type: <MSSType>``, specifying how to fill out the DS field

        * ``FIXED = 0``
        * ``INCREMENT = 1``
        * ``RANDOM = 2``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_IP_DS_TYPE [0] FIXED
        output: <OK>

        # get
        input:  0/1 P4G_IP_DS_TYPE [0] ?
        output: 0/1 P4G_IP_DS_TYPE [0] FIXED


``P4G_IP_DS_VALUE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_IP_DS_VALUE [<group_xindex>] <ds_value>

    # get
    <module-index>/<port-index> P4G_IP_DS_VALUE [<group_xindex>] ?

:Description:
    Specify the (FIXED) value used for DS.

:Actions:
    set, get

:Parameter:
    ``ds_value: <string>``, the fixed DS value to be used


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_IP_DS_VALUE [0] word
        output: <OK>

        # get
        input:  0/1 P4G_IP_DS_VALUE [0] ?
        output: 0/1 P4G_IP_DS_VALUE [0] word


``P4G_IP_DS_MASK``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_IP_DS_MASK [<group_xindex>] <ds_mask>

    # get
    <module-index>/<port-index> P4G_IP_DS_MASK [<group_xindex>] ?

:Description:
    Specify a bit mask to be applied to the DS field. If the fixed value is fixed,
    the current (calculated) value is curr, and the mask is mask, then the effective
    DS will be calculated as follows: (fixed AND (NOT mask)) OR (curr AND mask) or
    in C syntax (fixed & (~mask)) | (curr & mask)

:Actions:
    set, get

:Parameter:
    ``ds_mask: <string>``, the DS mask to be used.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_IP_DS_MASK [0] word
        output: <OK>

        # get
        input:  0/1 P4G_IP_DS_MASK [0] ?
        output: 0/1 P4G_IP_DS_MASK [0] word


``P4G_IP_DS_MINMAX``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_IP_DS_MINMAX [<group_xindex>] <ds_min> <ds_max>

    # get
    <module-index>/<port-index> P4G_IP_DS_MINMAX [<group_xindex>] ?

:Description:
    Configure the min and max values of the range for the calculated part of the DS
    value. Both values are included in the range. Relevant when :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_IP_DS_TYPE` is set to ``INCREMENT`` or ``RANDOM``.

:Actions:
    set, get

:Parameter:
    ``ds_min: <string>``, minimum value for the calculated part of DS

    ``ds_max: <string>``, maximum value for the calculated part of DS


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_IP_DS_MINMAX [0] word word
        output: <OK>

        # get
        input:  0/1 P4G_IP_DS_MINMAX [0] ?
        output: 0/1 P4G_IP_DS_MINMAX [0] word word


``P4G_IP_DS_STEP``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_IP_DS_STEP [<group_xindex>] <ds_step>

    # get
    <module-index>/<port-index> P4G_IP_DS_STEP [<group_xindex>] ?

:Description:
    Specifies the incrementing step size for the calculated part of the DS value.
    Relevant when :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_IP_DS_TYPE` is set to ``INCREMENT``.

:Actions:
    set, get

:Parameter:
    ``ds_step: <string>``, the incrementing step size for DS.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_IP_DS_STEP [0] word
        output: <OK>

        # get
        input:  0/1 P4G_IP_DS_STEP [0] ?
        output: 0/1 P4G_IP_DS_STEP [0] word


``P4G_TCP_MSS_TYPE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TCP_MSS_TYPE [<group_xindex>] <mss_type>

    # get
    <module-index>/<port-index> P4G_TCP_MSS_TYPE [<group_xindex>] ?

:Description:
    Specifies the Maximum Segment size (MSS) type for a Connection Group. The MSS can
    either be fixed size identical for all connections in the Connection Group,
    incrementing or random. The individual MSS for a specific connection is always
    constant once the incrementing or random value has been created. Refer to
    :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_MSS_MINMAX` 
    command for information on how to configure min and max values.

:Actions:
    set, get

:Parameter:
    ``mss_type: <MSSType>``, specifying how MSS is set

        * ``FIXED = 0``
        * ``INCREMENT = 1``
        * ``RANDOM = 2``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TCP_MSS_TYPE [0] FIXED
        output: <OK>

        # get
        input:  0/1 P4G_TCP_MSS_TYPE [0] ?
        output: 0/1 P4G_TCP_MSS_TYPE [0] FIXED


``P4G_TCP_MSS_MINMAX``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TCP_MSS_MINMAX [<group_xindex>] <mss_min> <mss_max>

    # get
    <module-index>/<port-index> P4G_TCP_MSS_MINMAX [<group_xindex>] ?

:Description:
    Configure the min and max values of the range for MSS. Both values are
    included in the range. Relevant when P4G_TCP_MSS_TYPE is set to INCREMENT or
    RANDOM.

:Actions:
    set, get

:Parameter:
    ``mss_min: <integer>``, minimum value of MSS

    ``mss_max: <integer>``, maximum value of MSS


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TCP_MSS_MINMAX [0] 1 1
        output: <OK>

        # get
        input:  0/1 P4G_TCP_MSS_MINMAX [0] ?
        output: 0/1 P4G_TCP_MSS_MINMAX [0] 1 1


``P4G_TCP_MSS_VALUE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TCP_MSS_VALUE [<group_xindex>] <mss>

    # get
    <module-index>/<port-index> P4G_TCP_MSS_VALUE [<group_xindex>] ?

:Description:
    Configure the fixed MSS value. Relevant when P4G_TCP_MSS_TYPE is set to FIXED.

:Actions:
    set, get

:Parameter:
    ``mss: <integer>``, the fixed value of MSS (in bytes)


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TCP_MSS_VALUE [0] 1
        output: <OK>

        # get
        input:  0/1 P4G_TCP_MSS_VALUE [0] ?
        output: 0/1 P4G_TCP_MSS_VALUE [0] 1


``P4G_TCP_WINDOW_SIZE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TCP_WINDOW_SIZE [<group_xindex>] <window_size>

    # get
    <module-index>/<port-index> P4G_TCP_WINDOW_SIZE [<group_xindex>] ?

:Description:
    Configure the value of the TCP RWND.

:Actions:
    set, get

:Parameter:
    ``window_size: <integer>``, RWND size in bytes


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TCP_WINDOW_SIZE [0] 1
        output: <OK>

        # get
        input:  0/1 P4G_TCP_WINDOW_SIZE [0] ?
        output: 0/1 P4G_TCP_WINDOW_SIZE [0] 1


``P4G_TCP_DUP_THRES``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TCP_DUP_THRES [<group_xindex>] <threshold>

    # get
    <module-index>/<port-index> P4G_TCP_DUP_THRES [<group_xindex>] ?

:Description:
    Configure the value of the TCP duplicate ACK threshold.

:Actions:
    set, get

:Parameter:
    ``threshold: <integer>``, duplicate ACK threshold - must be larger than 0


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TCP_DUP_THRES [0] 1
        output: <OK>

        # get
        input:  0/1 P4G_TCP_DUP_THRES [0] ?
        output: 0/1 P4G_TCP_DUP_THRES [0] 1


``P4G_TCP_SYN_RTO``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TCP_SYN_RTO [<group_xindex>] <retrans_timeout> <retry_count> <backoff>

    # get
    <module-index>/<port-index> P4G_TCP_SYN_RTO [<group_xindex>] ?

:Description:
    Configure the value of the TCP SYN retransmission timeout, max retries and max backoff.

:Actions:
    set, get

:Parameter:
    ``retrans_timeout: <integer>``, SYN retransmission timeout [milliseconds] - must be larger than 0

    ``retry_count: <integer>``, maximum SYN retransmission retries - must be larger than 0

    ``backoff: <integer>``, maximum SYN retransmission backoff


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TCP_SYN_RTO [0] 1 1 1
        output: <OK>

        # get
        input:  0/1 P4G_TCP_SYN_RTO [0] ?
        output: 0/1 P4G_TCP_SYN_RTO [0] 1 1 1


``P4G_TCP_RTO``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TCP_RTO [<group_xindex>] <rto_type> <retrans_timeout> <retry_count> <backoff>

    # get
    <module-index>/<port-index> P4G_TCP_RTO [<group_xindex>] ?

:Description:
    Configure the value of the TCP retransmission timeout, max retries and max backoff.

:Actions:
    set, get

:Parameter:
    ``rto_type: <RTOType>``, specifying RTO type

        * ``STATIC = 0``
        * ``DYNAMIC = 1``

    ``retrans_timeout: <integer>``, retransmission timeout [milliseconds] - must be larger than 0

    ``retry_count: <integer>``, maximum retransmission retries - must be larger than 0

    ``backoff: <integer>``, maximum retransmission backoff


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TCP_RTO [0] STATIC 1 1 1
        output: <OK>

        # get
        input:  0/1 P4G_TCP_RTO [0] ?
        output: 0/1 P4G_TCP_RTO [0] STATIC 1 1 1


``P4G_UDP_PACKET_SIZE_TYPE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_UDP_PACKET_SIZE_TYPE [<group_xindex>] <packet_size_type>

    # get
    <module-index>/<port-index> P4G_UDP_PACKET_SIZE_TYPE [<group_xindex>] ?

:Description:
    Specifies the UDP packet size type for a Connection Group. The packet size can either
    be fixed size identical for all connections in the Connection Group,
    incrementing or random. The individual packet size for a specific connection is
    always constant once the incrementing or random value has been created. Refer to
    :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_UDP_PACKET_SIZE_MINMAX` command for information on how to configure min and max values.

:Actions:
    set, get

:Parameter:
    ``packet_size_type: <MSSType>``, specifying how UDP packet size is set

        * ``FIXED = 0``
        * ``INCREMENT = 1``
        * ``RANDOM = 2``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_UDP_PACKET_SIZE_TYPE [0] FIXED
        output: <OK>

        # get
        input:  0/1 P4G_UDP_PACKET_SIZE_TYPE [0] ?
        output: 0/1 P4G_UDP_PACKET_SIZE_TYPE [0] FIXED


``P4G_UDP_PACKET_SIZE_MINMAX``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_UDP_PACKET_SIZE_MINMAX [<group_xindex>] <size_min> <size_max>

    # get
    <module-index>/<port-index> P4G_UDP_PACKET_SIZE_MINMAX [<group_xindex>] ?

:Description:
    Configure the minimum and maximum values of the range for UDP packet size. Both
    values are included in the range. Relevant when P4G_UDP_PACKET_SIZE_TYPE is set
    to INCREMENT or RANDOM.

:Actions:
    set, get

:Parameter:
    ``size_min: <integer>``, the minimum value of UDP packet size

    ``size_max: <integer>``, the maximum value of UDP packet size


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_UDP_PACKET_SIZE_MINMAX [0] 1 1
        output: <OK>

        # get
        input:  0/1 P4G_UDP_PACKET_SIZE_MINMAX [0] ?
        output: 0/1 P4G_UDP_PACKET_SIZE_MINMAX [0] 1 1


``P4G_UDP_PACKET_SIZE_VALUE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_UDP_PACKET_SIZE_VALUE [<group_xindex>] <size>

    # get
    <module-index>/<port-index> P4G_UDP_PACKET_SIZE_VALUE [<group_xindex>] ?

:Description:
    Configure the fixed UDP packet size value. Relevant when
    P4G_UDP_PACKET_SIZE_TYPE is set to FIXED.

:Actions:
    set, get

:Parameter:
    ``size: <integer>``, the fixed value of UDP packet size


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_UDP_PACKET_SIZE_VALUE [0] 1
        output: <OK>

        # get
        input:  0/1 P4G_UDP_PACKET_SIZE_VALUE [0] ?
        output: 0/1 P4G_UDP_PACKET_SIZE_VALUE [0] 1


``P4G_TCP_CONGESTION_MODE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TCP_CONGESTION_MODE [<group_xindex>] <congestion_type>

    # get
    <module-index>/<port-index> P4G_TCP_CONGESTION_MODE [<group_xindex>] ?

:Description:
    Configure the TCP congestion control algorithm.

:Actions:
    set, get

:Parameter:
    ``congestion_type: <CongestionType>``, specifying congestion algorithm type

        * ``NONE = 0``
        * ``RENO = 1``
        * ``NEW_RENO = 2``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TCP_CONGESTION_MODE [0] NONE
        output: <OK>

        # get
        input:  0/1 P4G_TCP_CONGESTION_MODE [0] ?
        output: 0/1 P4G_TCP_CONGESTION_MODE [0] NONE


``P4G_TCP_WINDOW_SCALING``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TCP_WINDOW_SCALING [<group_xindex>] <on_off> <factor>

    # get
    <module-index>/<port-index> P4G_TCP_WINDOW_SCALING [<group_xindex>] ?

:Description:
    Enable window scaling for the Connection Group. Note to use windows scaling it
    need to be enabled in both the client and server Connection Group. .

:Actions:
    set, get

:Parameter:
    ``on_off: <YesNo>``, specifying whether to enable window scaling or not

        * ``NO = 0``
        * ``YES = 1``

    ``factor: <integer>``, default value is 0 and maximum value is 14 - ignored if window scaling is not enabled


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TCP_WINDOW_SCALING [0] NO 1
        output: <OK>

        # get
        input:  0/1 P4G_TCP_WINDOW_SCALING [0] ?
        output: 0/1 P4G_TCP_WINDOW_SCALING [0] NO 1


``P4G_TCP_RTO_MINMAX``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TCP_RTO_MINMAX [<group_xindex>] <rto_min> <rto_max>

    # get
    <module-index>/<port-index> P4G_TCP_RTO_MINMAX [<group_xindex>] ?

:Description:
    Configure the min and max values of the TCP retransmission timeout, when rto type
    is set to dynamic. If the calculated rto fall outside the interval, the value is
    clamped to the min or max value.

:Actions:
    set, get

:Parameter:
    ``rto_min: <integer>``, min retransmission timeout [us] - must be larger than 0 and less than max.

    ``rto_max: <integer>``, max retransmission timeout [us] - must be larger than 0 and greater than min.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TCP_RTO_MINMAX [0] 1 1
        output: <OK>

        # get
        input:  0/1 P4G_TCP_RTO_MINMAX [0] ?
        output: 0/1 P4G_TCP_RTO_MINMAX [0] 1 1


``P4G_TCP_RTO_PROLONGED_MODE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TCP_RTO_PROLONGED_MODE [<group_xindex>] <mode> <timeout>

    # get
    <module-index>/<port-index> P4G_TCP_RTO_PROLONGED_MODE [<group_xindex>] ?

:Description:
    Configure TCP retransmission prolonged mode. When enabled, TCP will, after
    exceeding max number of retransmission retries, continue trying retransmit until
    success, whereafter it will operate normally.

:Actions:
    set, get

:Parameter:
    ``mode: <IsEnabled>``, specifying whether to enable/disable prolonged retransmission mode

        * ``DISABLE = 0``
        * ``ENABLE = 1``

    ``timeout: <integer>``, retransmission timeout in milliseconds, when prolonged mode is enabled. When ``mode`` is set to 0, the value of the timeout is ignored. When ``mode`` is set to 1, the value of the timeout may not be 0.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TCP_RTO_PROLONGED_MODE [0] DISABLE 1
        output: <OK>

        # get
        input:  0/1 P4G_TCP_RTO_PROLONGED_MODE [0] ?
        output: 0/1 P4G_TCP_RTO_PROLONGED_MODE [0] DISABLE 1


``P4G_TCP_ICWND_CALC_METHOD``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TCP_ICWND_CALC_METHOD [<group_xindex>] <method> <factor>

    # get
    <module-index>/<port-index> P4G_TCP_ICWND_CALC_METHOD [<group_xindex>] ?

:Description:
    Select the algorithm to calculate the TCP initial congestion window (ICWND).

:Actions:
    set, get

:Parameter:
    ``method: <AlgorithmMethod>``, specifying the algorithm

        * ``RFC5681 = 0``
        * ``RFC2581 = 1``
        * ``FIXED_FACTOR = 2``

    ``factor: <integer>``, factor to multiply the senders MSS with, when method is set to ``FIXED_FACTOR``. Otherwise the value is ignored.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TCP_ICWND_CALC_METHOD [0] RFC5681 1
        output: <OK>

        # get
        input:  0/1 P4G_TCP_ICWND_CALC_METHOD [0] ?
        output: 0/1 P4G_TCP_ICWND_CALC_METHOD [0] RFC5681 1


``P4G_TCP_ISSTHRESH``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TCP_ISSTHRESH [<group_xindex>] <mode> <threshold>

    # get
    <module-index>/<port-index> P4G_TCP_ISSTHRESH [<group_xindex>] ?

:Description:
    Configure the TCP initial slow start threshold (ISSTHRESH).

:Actions:
    set, get

:Parameter:
    ``mode: <AutoOrManual>``, specifying TCP initial slow start mode

        * ``AUTOMATIC = 0``
        * ``MANUAL = 1``
        
    ``threshold: <integer>``, number of bytes, value ignored when mode is set to ``MANUAL``


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TCP_ISSTHRESH [0] AUTOMATIC 1
        output: <OK>

        # get
        input:  0/1 P4G_TCP_ISSTHRESH [0] ?
        output: 0/1 P4G_TCP_ISSTHRESH [0] AUTOMATIC 1


``P4G_TCP_ACK_FREQUENCY``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TCP_ACK_FREQUENCY [<group_xindex>] <packets_before_ack>

    # get
    <module-index>/<port-index> P4G_TCP_ACK_FREQUENCY [<group_xindex>] ?

:Description:
    Number of received packets before a pure-ACK is sent.

:Actions:
    set, get

:Parameter:
    ``packets_before_ack: <integer>``, number of received packets before an ACK is sent, range between 1 and 255, default 1. When set to 1, every packet is ACKed.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TCP_ACK_FREQUENCY [0] 1
        output: <OK>

        # get
        input:  0/1 P4G_TCP_ACK_FREQUENCY [0] ?
        output: 0/1 P4G_TCP_ACK_FREQUENCY [0] 1


``P4G_TCP_ACK_TIMEOUT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TCP_ACK_TIMEOUT [<group_xindex>] <ack_timeout>

    # get
    <module-index>/<port-index> P4G_TCP_ACK_TIMEOUT [<group_xindex>] ?

:Description:
    Delayed ACK timeout in microsecondsA pure ACK for the last RX packet will be
    sent after :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_ACK_TIMEOUT` microseconds in case it cannot be sent by other means, ie. a number of packets received since last ACK is less than :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_ACK_FREQUENCY` and there is no TX packets to sent (to piggy-back an ACK)

:Actions:
    set, get

:Parameter:
    ``ack_timeout: <integer>``, timeout value in microseconds, default 200000.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TCP_ACK_TIMEOUT [0] 1
        output: <OK>

        # get
        input:  0/1 P4G_TCP_ACK_TIMEOUT [0] ?
        output: 0/1 P4G_TCP_ACK_TIMEOUT [0] 1


``P4G_L2_CLIENT_MAC``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_L2_CLIENT_MAC [<group_xindex>] <mac_address> <mode>

    # get
    <module-index>/<port-index> P4G_L2_CLIENT_MAC [<group_xindex>] ?

:Description:
    Configure the client MAC address. This is either a single static MAC
    address or an embedding of the four byte IPv4 address into the lower 4 bytes of
    the 6 byte MAC address.

:Actions:
    set, get

:Parameter:
    ``mac_address: <string>``, the MAC address specified as hexadecimal

    ``mode: <EmbedIP>``, whether to embed the IP address in MAC

        * ``DONT_EMBED_IP = 0``
        * ``EMBED_IP = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_L2_CLIENT_MAC [0] word DONT_EMBED_IP
        output: <OK>

        # get
        input:  0/1 P4G_L2_CLIENT_MAC [0] ?
        output: 0/1 P4G_L2_CLIENT_MAC [0] word DONT_EMBED_IP


``P4G_L2_SERVER_MAC``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_L2_SERVER_MAC [<group_xindex>] <mac_address> <mode>

    # get
    <module-index>/<port-index> P4G_L2_SERVER_MAC [<group_xindex>] ?

:Description:
    Configure the server MAC address. This is either a single static MAC
    address or an embedding of the four byte IPv4 address into the lower 4 bytes of
    the 6 byte MAC address.

:Actions:
    set, get

:Parameter:
    ``mac_address: <string>``, the MAC address specified as hexadecimal

    ``mode: <EmbedIP>``, whether to embed the IP address in MAC

        * ``DONT_EMBED_IP = 0``
        * ``EMBED_IP = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_L2_SERVER_MAC [0] word DONT_EMBED_IP
        output: <OK>

        # get
        input:  0/1 P4G_L2_SERVER_MAC [0] ?
        output: 0/1 P4G_L2_SERVER_MAC [0] word DONT_EMBED_IP


``P4G_L2_USE_ADDRESS_RES``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_L2_USE_ADDRESS_RES [<group_xindex>] <is_enabled>

    # get
    <module-index>/<port-index> P4G_L2_USE_ADDRESS_RES [<group_xindex>] ?

:Description:
    Specify whether to use ARP and NDP to resolve hardware (MAC) addresses in the
    ``pre_run`` phase.

:Actions:
    set, get

:Parameter:
    ``is_enabled: <YesNo>``, specifying whether to use ARP and NDP to resolve hardware (MAC) addresses.

        * ``NO = 0``
        * ``YES = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_L2_USE_ADDRESS_RES [0] NO
        output: <OK>

        # get
        input:  0/1 P4G_L2_USE_ADDRESS_RES [0] ?
        output: 0/1 P4G_L2_USE_ADDRESS_RES [0] NO


``P4G_L2_USE_GW``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_L2_USE_GW [<group_xindex>] <is_enabled>

    # get
    <module-index>/<port-index> P4G_L2_USE_GW [<group_xindex>] ?

:Description:
    Specify whether to use the resolved default gateway's MAC address as the destination MAC address in the packets.

:Actions:
    set, get

:Parameter:
    ``is_enabled: <YesNo>``, specifying whether to use gateway's MAC address as the destination MAC address in the packets.

        * ``NO = 0``
        * ``YES = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_L2_USE_GW [0] NO
        output: <OK>

        # get
        input:  0/1 P4G_L2_USE_GW [0] ?
        output: 0/1 P4G_L2_USE_GW [0] NO


``P4G_L2_GW``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_L2_GW [<group_xindex>] <ipv4_address> <mac_address>

    # get
    <module-index>/<port-index> P4G_L2_GW [<group_xindex>] ?

:Description:
    Specify a default gateway for IPv4.

:Actions:
    set, get

:Parameter:
    ``ipv4_address: <ipv4_address>``, IPv5 address of the gateway

    ``mac_address: <string>``, the MAC address of the gateway


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_L2_GW [0] 192.168.1.100 word
        output: <OK>

        # get
        input:  0/1 P4G_L2_GW [0] ?
        output: 0/1 P4G_L2_GW [0] 192.168.1.100 word


``P4G_L2_IPV6_GW``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_L2_IPV6_GW [<group_xindex>] <ipv6_address> <mac_address>

    # get
    <module-index>/<port-index> P4G_L2_IPV6_GW [<group_xindex>] ?

:Description:
    Specify a default gateway for IPv6.

:Actions:
    set, get

:Parameter:
    ``ipv6_address: <ipv6_address>``, the 16 bytes of IPv6 address of gateway

    ``mac_address: <string>``, the MAC address of the gateway


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_L2_IPV6_GW [0] ::1 word
        output: <OK>

        # get
        input:  0/1 P4G_L2_IPV6_GW [0] ?
        output: 0/1 P4G_L2_IPV6_GW [0] ::1 word


``P4G_TEST_APPLICATION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TEST_APPLICATION [<group_xindex>] <behavior>

    # get
    <module-index>/<port-index> P4G_TEST_APPLICATION [<group_xindex>] ?

:Description:
    Configure the application layer mode. This command affects whether TCP payload is generated.
    
    * ``NONE`` means that TCP connections are created according to the client and server ranges, and ramped up/down as specified in the load profile. But no payload is transmitted.
    
    * ``RAW`` differs from ``NONE`` in that it transmits payload when the TCP connection is established.

    * ``REPLAY`` refers to PCAP replay.

:Actions:
    set, get

:Parameter:
    ``behavior: <ApplicationLayerBehavior>``, the application layer mode

        * ``NONE = 0``
        * ``RAW = 1``
        * ``REPLAY = 2``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TEST_APPLICATION [0] NONE
        output: <OK>

        # get
        input:  0/1 P4G_TEST_APPLICATION [0] ?
        output: 0/1 P4G_TEST_APPLICATION [0] NONE


``P4G_RAW_TEST_SCENARIO``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_RAW_TEST_SCENARIO [<group_xindex>] <scenario>

    # get
    <module-index>/<port-index> P4G_RAW_TEST_SCENARIO [<group_xindex>] ?

:Description:
    Configure the traffic direction scenario for RAW mode.

:Actions:
    set, get

:Parameter:
    ``scenario: <TrafficScenario>``, traffic scenario

        * ``DOWNLOAD = 0``
        * ``UPLOAD = 1``
        * ``BOTH = 2``
        * ``ECHO = 3``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_RAW_TEST_SCENARIO [0] DOWNLOAD
        output: <OK>

        # get
        input:  0/1 P4G_RAW_TEST_SCENARIO [0] ?
        output: 0/1 P4G_RAW_TEST_SCENARIO [0] DOWNLOAD


``P4G_RAW_PAYLOAD_TYPE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_RAW_PAYLOAD_TYPE [<group_xindex>] <gen_method>

    # get
    <module-index>/<port-index> P4G_RAW_PAYLOAD_TYPE [<group_xindex>] ?

:Description:
    Specify the payload generation method.

:Actions:
    set, get

:Parameter:
    ``gen_method: <PayloadGenerationMethod>``, payload generation method

        * ``FIXED = 0``
        * ``INCREMENT = 1``
        * ``RANDOM = 2``
        * ``LONGRANDOM = 3``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_RAW_PAYLOAD_TYPE [0] FIXED
        output: <OK>

        # get
        input:  0/1 P4G_RAW_PAYLOAD_TYPE [0] ?
        output: 0/1 P4G_RAW_PAYLOAD_TYPE [0] FIXED


``P4G_RAW_PAYLOAD_TOTAL_LEN``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_RAW_PAYLOAD_TOTAL_LEN [<group_xindex>] <mode> <length>

    # get
    <module-index>/<port-index> P4G_RAW_PAYLOAD_TOTAL_LEN [<group_xindex>] ?

:Description:
    Configure the total amount of payload to transmit on one connection.

:Actions:
    set, get

:Parameter:
    ``mode: <InfiniteOrFinite>``, generation mode.

        * ``INFINITE = 0``
        * ``FINITE = 1``

    ``length: <integer>``, size of the payload


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_RAW_PAYLOAD_TOTAL_LEN [0] INFINITE 1
        output: <OK>

        # get
        input:  0/1 P4G_RAW_PAYLOAD_TOTAL_LEN [0] ?
        output: 0/1 P4G_RAW_PAYLOAD_TOTAL_LEN [0] INFINITE 1


``P4G_RAW_PAYLOAD``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_RAW_PAYLOAD [<group_xindex>] <offset> <length> <content>

    # get
    <module-index>/<port-index> P4G_RAW_PAYLOAD [<group_xindex>] ?

:Description:
    Specify raw payload as hex bytes. This command can be called several times to build
    a custom payload.

:Actions:
    set, get

:Parameter:
    ``offset: <integer>``, the offset in the payload buffer where data is to be written

    ``length: <integer>``, number of bytes to write

    ``content: <string>``, specifying the payload


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_RAW_PAYLOAD [0] 1 1 word
        output: <OK>

        # get
        input:  0/1 P4G_RAW_PAYLOAD [0] ?
        output: 0/1 P4G_RAW_PAYLOAD [0] 1 1 word


``P4G_RAW_PAYLOAD_REPEAT_LEN``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_RAW_PAYLOAD_REPEAT_LEN [<group_xindex>] <length>

    # get
    <module-index>/<port-index> P4G_RAW_PAYLOAD_REPEAT_LEN [<group_xindex>] ?

:Description:
    Specify the length of the raw payload, which is defined by one or more :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_PAYLOAD` commands, to repeat.
    
    :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_PAYLOAD_REPEAT_LEN` number of bytes will be repeated until :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_PAYLOAD_TOTAL_LEN` bytes are transmitted on the connection.

:Actions:
    set, get

:Parameter:
    ``length: <integer>``, the length of the raw payload to repeat


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_RAW_PAYLOAD_REPEAT_LEN [0] 1
        output: <OK>

        # get
        input:  0/1 P4G_RAW_PAYLOAD_REPEAT_LEN [0] ?
        output: 0/1 P4G_RAW_PAYLOAD_REPEAT_LEN [0] 1


``P4G_RAW_HAS_DOWNLOAD_REQ``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_RAW_HAS_DOWNLOAD_REQ [<group_xindex>] <on_off>

    # get
    <module-index>/<port-index> P4G_RAW_HAS_DOWNLOAD_REQ [<group_xindex>] ?

:Description:
    Specify whether the server waits for a request from the client before it starts transmitting.
    
    .. note::
    
        This parameter is N/A when :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_L4_PROTOCOL` is configured as UDP.

:Actions:
    set, get

:Parameter:
    ``on_off: <YesNo>``, whether the server waits for a request from the client before it starts transmitting.

        * ``NO = 0``
        * ``YES = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_RAW_HAS_DOWNLOAD_REQ [0] NO
        output: <OK>

        # get
        input:  0/1 P4G_RAW_HAS_DOWNLOAD_REQ [0] ?
        output: 0/1 P4G_RAW_HAS_DOWNLOAD_REQ [0] NO


``P4G_RAW_CLOSE_CONN``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_RAW_CLOSE_CONN [<group_xindex>] <who_close>

    # get
    <module-index>/<port-index> P4G_RAW_CLOSE_CONN [<group_xindex>] ?

:Description:
    Specify how to close TCP connection when all payload has been transmitted.
    
    In raw test scenario ``DOWNLOAD``, the server can close the connection, when all payload has been transmitted.
    
    In raw test scenario ``UPLOAD``, the client can close the connection, when all payload has been transmitted. In any case, both server and client Connection Groups must be configured with the same value of this parameter.
    
    In raw test scenario ``BOTH`` (bidirectional), this parameter is N/A and will be ignored.
    
    In a transaction scenario, where :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_HAS_DOWNLOAD_REQ` is set to ``YES``, both client and server can close the connection, when the last transaction has been completed.
    
    When :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_CONN_INCARNATION` is set to ``IMMORTAL`` or ``REINCARNATE``, and this command is set to ``NONE``, connections will be closed after 'connection lifetime', set by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_CONN_LIFETIME`.
    
    .. note::
    
        This parameter is N/A when :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_L4_PROTOCOL` is configured as UDP.

:Actions:
    set, get

:Parameter:
    ``who_close: <WhoClose>``, specifying how to close TCP connection

        * ``NONE = 0``
        * ``CLIENT = 1``
        * ``SERVER = 2``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_RAW_CLOSE_CONN [0] NONE
        output: <OK>

        # get
        input:  0/1 P4G_RAW_CLOSE_CONN [0] ?
        output: 0/1 P4G_RAW_CLOSE_CONN [0] NONE


``P4G_RAW_UTILIZATION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_RAW_UTILIZATION [<group_xindex>] <utilization>

    # get
    <module-index>/<port-index> P4G_RAW_UTILIZATION [<group_xindex>] ?

:Description:
    Specify the link layer bandwidth utilization for all the generated traffic from
    the specified Raw Connection Group.

:Actions:
    set, get

:Parameter:
    ``utilization: <integer>``, utilization specified in ppm.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_RAW_UTILIZATION [0] 1
        output: <OK>

        # get
        input:  0/1 P4G_RAW_UTILIZATION [0] ?
        output: 0/1 P4G_RAW_UTILIZATION [0] 1


``P4G_RAW_DOWNLOAD_REQUEST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_RAW_DOWNLOAD_REQUEST [<group_xindex>] <length> <content>

    # get
    <module-index>/<port-index> P4G_RAW_DOWNLOAD_REQUEST [<group_xindex>] ?

:Description:
    Specify the content of the download request sent by the client and expected by the server as hex bytes.
    
    .. note::
    
        This parameter is N/A when P4G_L4_PROTOCOL is configured as UDP.

:Actions:
    set, get

:Parameter:
    ``length: <integer>``, specifying the number of bytes to write. Maximum request length is 1024 bytes.

    ``content: <string>``, specifying the request content.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_RAW_DOWNLOAD_REQUEST [0] 1 word
        output: <OK>

        # get
        input:  0/1 P4G_RAW_DOWNLOAD_REQUEST [0] ?
        output: 0/1 P4G_RAW_DOWNLOAD_REQUEST [0] 1 word


``P4G_RAW_TX_DURING_RAMP``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_RAW_TX_DURING_RAMP [<group_xindex>] <should_close_conn_ramp_up> <should_close_conn_ramp_down>

    # get
    <module-index>/<port-index> P4G_RAW_TX_DURING_RAMP [<group_xindex>] ?

:Description:
    Specify if TCP payload transmission should take place during ramp-up and ramp-down. 
    
    .. note::
    
        For UDP connections payload transmission will always take place during ramp-up and ramp-down, and this parameter is therefore N/A.

:Actions:
    set, get

:Parameter:
    ``should_close_conn_ramp_up: <YesNo>``, whether TCP payload transmission should take place during ramp-up.

        * ``NO = 0``
        * ``YES = 1``

    ``should_close_conn_ramp_down: <YesNo>``, whether TCP payload transmission should take place during ramp-down.

        * ``NO = 0``
        * ``YES = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_RAW_TX_DURING_RAMP [0] NO NO
        output: <OK>

        # get
        input:  0/1 P4G_RAW_TX_DURING_RAMP [0] ?
        output: 0/1 P4G_RAW_TX_DURING_RAMP [0] NO NO


``P4G_RAW_TX_TIME_OFFSET``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_RAW_TX_TIME_OFFSET [<group_xindex>] <start_offset> <stop_offset>

    # get
    <module-index>/<port-index> P4G_RAW_TX_TIME_OFFSET [<group_xindex>] ?

:Description:
    Specify a time offset to the transmit start and stop time, if :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TX_DURING_RAMP` is set to ``NO`` for ramp-up and ramp-down respectively.

:Actions:
    set, get

:Parameter:
    ``start_offset: <integer>``, specify time in milliseconds from ramp-up has completed to start of payload transmit.

    ``stop_offset: <integer>``, specify time in milliseconds from stop of payload transmit to start of ramp-down.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_RAW_TX_TIME_OFFSET [0] 1 1
        output: <OK>

        # get
        input:  0/1 P4G_RAW_TX_TIME_OFFSET [0] ?
        output: 0/1 P4G_RAW_TX_TIME_OFFSET [0] 1 1


``P4G_RAW_BURSTY_TX``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_RAW_BURSTY_TX [<group_xindex>] <bursty>

    # get
    <module-index>/<port-index> P4G_RAW_BURSTY_TX [<group_xindex>] ?

:Description:
    Enables or disables bursty transmission.

:Actions:
    set, get

:Parameter:
    ``bursty: <OnOff>``, whether bursty transmission is on or off.

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_RAW_BURSTY_TX [0] OFF
        output: <OK>

        # get
        input:  0/1 P4G_RAW_BURSTY_TX [0] ?
        output: 0/1 P4G_RAW_BURSTY_TX [0] OFF


``P4G_RAW_BURSTY_CONF``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_RAW_BURSTY_CONF [<group_xindex>] <active_duration> <inactive_duration>

    # get
    <module-index>/<port-index> P4G_RAW_BURSTY_CONF [<group_xindex>] ?

:Description:
    Specifies active and inactive periods of bursty transmission in milliseconds. The burst period starts with the active part.

:Actions:
    set, get

:Parameter:
    ``active_duration: <integer>``, specifies the duration in milliseconds of the active part of the burst period.

    ``inactive_duration: <integer>``, specifies the duration in milliseconds of the inactive part of the burst period.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_RAW_BURSTY_CONF [0] 1 1
        output: <OK>

        # get
        input:  0/1 P4G_RAW_BURSTY_CONF [0] ?
        output: 0/1 P4G_RAW_BURSTY_CONF [0] 1 1


``P4G_VLAN_ENABLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_VLAN_ENABLE [<group_xindex>] <on_off>

    # get
    <module-index>/<port-index> P4G_VLAN_ENABLE [<group_xindex>] ?

:Description:
    Specify whether to insert a VLAN tag header upon transmit.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, specifying whether to enable VLAN tag

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_VLAN_ENABLE [0] OFF
        output: <OK>

        # get
        input:  0/1 P4G_VLAN_ENABLE [0] ?
        output: 0/1 P4G_VLAN_ENABLE [0] OFF


``P4G_VLAN_TCI``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_VLAN_TCI [<group_xindex>] <tci>

    # get
    <module-index>/<port-index> P4G_VLAN_TCI [<group_xindex>] ?

:Description:
    Specify the VLAN TCI.

:Actions:
    set, get

:Parameter:
    ``tci: <string>``, specifying the 16 bit TCI


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_VLAN_TCI [0] word
        output: <OK>

        # get
        input:  0/1 P4G_VLAN_TCI [0] ?
        output: 0/1 P4G_VLAN_TCI [0] word


``P4G_TIME_HIST_CONF``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TIME_HIST_CONF [<group_xindex>] <start> <interval>

    # get
    <module-index>/<port-index> P4G_TIME_HIST_CONF [<group_xindex>] ?

:Description:
    Sets the start value and the interval size for the time histograms (:class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_ESTABLISH_HIST` and :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_CLOSE_HIST`).

:Actions:
    set, get

:Parameter:
    ``start: <integer>``, start value of first histogram interval in microseconds

    ``interval: <integer>``, histogram interval size in microseconds


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TIME_HIST_CONF [0] 1 1
        output: <OK>

        # get
        input:  0/1 P4G_TIME_HIST_CONF [0] ?
        output: 0/1 P4G_TIME_HIST_CONF [0] 1 1


``P4G_PAYLOAD_HIST_CONF``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_PAYLOAD_HIST_CONF [<group_xindex>] <start> <interval>

    # get
    <module-index>/<port-index> P4G_PAYLOAD_HIST_CONF [<group_xindex>] ?

:Description:
    Sets the start value and the interval size for the payload histograms.

:Actions:
    set, get

:Parameter:
    ``start: <integer>``, start value of first histogram interval in bytes

    ``interval: <integer>``, histogram interval size in bytes


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_PAYLOAD_HIST_CONF [0] 1 1
        output: <OK>

        # get
        input:  0/1 P4G_PAYLOAD_HIST_CONF [0] ?
        output: 0/1 P4G_PAYLOAD_HIST_CONF [0] 1 1


``P4G_TRANSACTION_HIST_CONF``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TRANSACTION_HIST_CONF [<group_xindex>] <start> <interval>

    # get
    <module-index>/<port-index> P4G_TRANSACTION_HIST_CONF [<group_xindex>] ?

:Description:
    Sets the start value and the interval size for the transaction histogram (:class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_APP_TRANSACTION_HIST`).

:Actions:
    set, get

:Parameter:
    ``start: <integer>``, tart value of first histogram interval

    ``interval: <integer>``, histogram interval size


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TRANSACTION_HIST_CONF [0] 1 1
        output: <OK>

        # get
        input:  0/1 P4G_TRANSACTION_HIST_CONF [0] ?
        output: 0/1 P4G_TRANSACTION_HIST_CONF [0] 1 1


``P4G_RAW_RX_PAYLOAD_LEN``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_RAW_RX_PAYLOAD_LEN [<group_xindex>] <mode> <length>

    # get
    <module-index>/<port-index> P4G_RAW_RX_PAYLOAD_LEN [<group_xindex>] ?

:Description:
    Specify the length of the payload the Client should expect to receive before sending the next download request to the Server. Should be configured identical to the :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_PAYLOAD_TOTAL_LEN` for the Server. If mode is set to INFINITE, effectively no request/response repetitions will be performed.
    
    .. note::
    
        This parameter is N/A when :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_L4_PROTOCOL` is configured as UDP.

:Actions:
    set, get

:Parameter:
    ``mode: <InfiniteOrFinite>``, specifying the payload length mode

        * ``INFINITE = 0``
        * ``FINITE = 1``

    ``length: <integer>``, number of payload bytes the client should receive before sending the next request, if mode is ``FINITE``.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_RAW_RX_PAYLOAD_LEN [0] INFINITE 1
        output: <OK>

        # get
        input:  0/1 P4G_RAW_RX_PAYLOAD_LEN [0] ?
        output: 0/1 P4G_RAW_RX_PAYLOAD_LEN [0] INFINITE 1


``P4G_RAW_REQUEST_REPEAT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_RAW_REQUEST_REPEAT [<group_xindex>] <mode> <repeat>

    # get
    <module-index>/<port-index> P4G_RAW_REQUEST_REPEAT [<group_xindex>] ?

:Description:
    Specify the number of request/response transactions to perform - if :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_HAS_DOWNLOAD_REQ` is set to ``YES``.
    
    .. note::
        
        This parameter is N/A when :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_L4_PROTOCOL` is configured as UDP.

:Actions:
    set, get

:Parameter:
    ``mode: <InfiniteOrFinite>``, specifying the transaction mode.

        * ``INFINITE = 0``
        * ``FINITE = 1``

    ``repeat: <integer>``, number of request/response transactions to perform , if mode is ``FINITE``.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_RAW_REQUEST_REPEAT [0] INFINITE 1
        output: <OK>

        # get
        input:  0/1 P4G_RAW_REQUEST_REPEAT [0] ?
        output: 0/1 P4G_RAW_REQUEST_REPEAT [0] INFINITE 1


``P4G_RAW_CONN_INCARNATION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_RAW_CONN_INCARNATION [<group_xindex>] <mode>

    # get
    <module-index>/<port-index> P4G_RAW_CONN_INCARNATION [<group_xindex>] ?

:Description:
    Defines the lifecycle of a connection and how new connections should be established as old connections are closed.

:Actions:
    set, get

:Parameter:
    ``mode: <LifecycleMode>``, connection lifecycle mode

        * ``ONCE = 0``
        * ``IMMORTAL = 1``
        * ``REINCARNATE = 2``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_RAW_CONN_INCARNATION [0] ONCE
        output: <OK>

        # get
        input:  0/1 P4G_RAW_CONN_INCARNATION [0] ?
        output: 0/1 P4G_RAW_CONN_INCARNATION [0] ONCE


``P4G_RAW_CONN_REPETITIONS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_RAW_CONN_REPETITIONS [<group_xindex>] <mode> <repetition_count>

    # get
    <module-index>/<port-index> P4G_RAW_CONN_REPETITIONS [<group_xindex>] ?

:Description:
    Defines how many times a new connection should be created, after an old
    connection has been closed, when :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_CONN_INCARNATION` is set to ``IMMORTAL`` or
    ``REINCARNATE``.

:Actions:
    set, get

:Parameter:
    ``mode: <InfiniteOrFinite>``, repetition mode.

        * ``INFINITE = 0``
        * ``FINITE = 1``

    ``repetition_count: <integer>``, number of repetitions


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_RAW_CONN_REPETITIONS [0] INFINITE 1
        output: <OK>

        # get
        input:  0/1 P4G_RAW_CONN_REPETITIONS [0] ?
        output: 0/1 P4G_RAW_CONN_REPETITIONS [0] INFINITE 1


``P4G_RAW_CONN_LIFETIME``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_RAW_CONN_LIFETIME [<group_xindex>] <timescale> <lifetime>

    # get
    <module-index>/<port-index> P4G_RAW_CONN_LIFETIME [<group_xindex>] ?

:Description:
    Defines the lifetime of a connection, when :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_CONN_INCARNATION` is set to ``IMMORTAL`` or ``REINCARNATE``.

:Actions:
    set, get

:Parameter:
    ``timescale: <Timescale>``, specifying the time scale

        * ``MSECS = 0``
        * ``SECONDS = 1``
        * ``MINUTES = 2``
        * ``HOURS = 3``

    ``lifetime: <integer>``, time from a connection is established until it will be closed.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_RAW_CONN_LIFETIME [0] MSECS 1
        output: <OK>

        # get
        input:  0/1 P4G_RAW_CONN_LIFETIME [0] ?
        output: 0/1 P4G_RAW_CONN_LIFETIME [0] MSECS 1


``P4G_IP_VERSION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_IP_VERSION [<group_xindex>] <version_number>

    # get
    <module-index>/<port-index> P4G_IP_VERSION [<group_xindex>] ?

:Description:
    Specifies either IPv4 or IPv6.

:Actions:
    set, get

:Parameter:
    ``version_number: <L47IPVersion>``, IP version

        * ``IPV4 = 4``
        * ``IPV6 = 6``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_IP_VERSION [0] IPV4
        output: <OK>

        # get
        input:  0/1 P4G_IP_VERSION [0] ?
        output: 0/1 P4G_IP_VERSION [0] IPV4


``P4G_IPV6_CLIENT_RANGE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_IPV6_CLIENT_RANGE [<group_xindex>] <ipv6_address> <address_count> <start_port> <port_count> <max_address_count>

    # get
    <module-index>/<port-index> P4G_IPV6_CLIENT_RANGE [<group_xindex>] ?

:Description:
    Specifies the number of client sockets (IPv6 address, port number).

:Actions:
    set, get

:Parameter:
    ``ipv6_address: <ipv6_address>``, the start ip address of the address range

    ``address_count: <integer>``, the number of IPv6 addresses

    ``start_port: <integer>``, the start port number of the port range

    ``port_count: <integer>``, the number of ports

    ``max_address_count: <integer>``, the maximum number of IPv6 addresses that this Connection Group will use, when connection incarnation is set to ``REINCARNATE``


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_IPV6_CLIENT_RANGE [0] ::1 1 1 1 1
        output: <OK>

        # get
        input:  0/1 P4G_IPV6_CLIENT_RANGE [0] ?
        output: 0/1 P4G_IPV6_CLIENT_RANGE [0] ::1 1 1 1 1


``P4G_IPV6_SERVER_RANGE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_IPV6_SERVER_RANGE [<group_xindex>] <ipv6_address> <address_count> <start_port> <port_count>

    # get
    <module-index>/<port-index> P4G_IPV6_SERVER_RANGE [<group_xindex>] ?

:Description:
    Specifies the number of server sockets (IPv6 address, port number)

:Actions:
    set, get

:Parameter:
    ``ipv6_address: <ipv6_address>``, the start IPv6 address of the address range

    ``address_count: <integer>``, the number of IPv6 addresses

    ``start_port: <integer>``, the start port number of the port range

    ``port_count: <integer>``, the number of ports


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_IPV6_SERVER_RANGE [0] ::1 1 1 1
        output: <OK>

        # get
        input:  0/1 P4G_IPV6_SERVER_RANGE [0] ?
        output: 0/1 P4G_IPV6_SERVER_RANGE [0] ::1 1 1 1


``P4G_IPV6_TRAFFIC_CLASS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_IPV6_TRAFFIC_CLASS [<group_xindex>] <traffic_class>

    # get
    <module-index>/<port-index> P4G_IPV6_TRAFFIC_CLASS [<group_xindex>] ?

:Description:
    Configure the value of the traffic class field of the IPv6 header.

:Actions:
    set, get

:Parameter:
    ``traffic_class: <string>``, value of the traffic class field


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_IPV6_TRAFFIC_CLASS [0] word
        output: <OK>

        # get
        input:  0/1 P4G_IPV6_TRAFFIC_CLASS [0] ?
        output: 0/1 P4G_IPV6_TRAFFIC_CLASS [0] word


``P4G_IPV6_FLOW_LABEL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_IPV6_FLOW_LABEL [<group_xindex>] <flow_label>

    # get
    <module-index>/<port-index> P4G_IPV6_FLOW_LABEL [<group_xindex>] ?

:Description:
    Configure the value of the flow label field of the IPv6 header.

:Actions:
    set, get

:Parameter:
    ``flow_label: <string>``, value of the traffic class field (only lowest 20 bits are valid)


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_IPV6_FLOW_LABEL [0] word
        output: <OK>

        # get
        input:  0/1 P4G_IPV6_FLOW_LABEL [0] ?
        output: 0/1 P4G_IPV6_FLOW_LABEL [0] word


``P4G_L4_PROTOCOL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_L4_PROTOCOL [<group_xindex>] <protocol_type>

    # get
    <module-index>/<port-index> P4G_L4_PROTOCOL [<group_xindex>] ?

:Description:
    Specifies either TCP or UDP as Layer 4 protocol.

:Actions:
    set, get

:Parameter:
    ``protocol_type: <L47ProtocolType>``, the Layer 4 protocol

        * ``TCP = 0``
        * ``UDP = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_L4_PROTOCOL [0] TCP
        output: <OK>

        # get
        input:  0/1 P4G_L4_PROTOCOL [0] ?
        output: 0/1 P4G_L4_PROTOCOL [0] TCP


``P4G_TCP_ESTABLISH_HIST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TCP_ESTABLISH_HIST [<group_xindex>] ?

:Description:
    Returns a histogram over TCP connection establish times, with start and interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TIME_HIST_CONF`.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TCP_ESTABLISH_HIST [0] ?
        output: 0/1 P4G_TCP_ESTABLISH_HIST [0]


``P4G_TCP_CLOSE_HIST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TCP_CLOSE_HIST [<group_xindex>] ?

:Description:
    Returns a histogram over TCP connection close times, with start and interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TIME_HIST_CONF`.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TCP_CLOSE_HIST [0] ?
        output: 0/1 P4G_TCP_CLOSE_HIST [0]


``P4G_TCP_RX_TOTAL_BYTES_HIST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TCP_RX_TOTAL_BYTES_HIST [<group_xindex>] ?

:Description:
    Returns a histogram over number of total TCP bytes received, with start and interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_PAYLOAD_HIST_CONF`.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TCP_RX_TOTAL_BYTES_HIST [0] ?
        output: 0/1 P4G_TCP_RX_TOTAL_BYTES_HIST [0]


``P4G_TCP_RX_GOOD_BYTES_HIST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TCP_RX_GOOD_BYTES_HIST [<group_xindex>] ?

:Description:
    Returns a histogram over number of good TCP bytes received, with start and interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_PAYLOAD_HIST_CONF`.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TCP_RX_GOOD_BYTES_HIST [0] ?
        output: 0/1 P4G_TCP_RX_GOOD_BYTES_HIST [0]


``P4G_TCP_TX_TOTAL_BYTES_HIST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TCP_TX_TOTAL_BYTES_HIST [<group_xindex>] ?

:Description:
    Returns a histogram over number of total TCP bytes transmitted, with start and interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_PAYLOAD_HIST_CONF`.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TCP_TX_TOTAL_BYTES_HIST [0] ?
        output: 0/1 P4G_TCP_TX_TOTAL_BYTES_HIST [0]


``P4G_TCP_TX_GOOD_BYTES_HIST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TCP_TX_GOOD_BYTES_HIST [<group_xindex>] ?

:Description:
    Returns a histogram over number of good TCP bytes transmitted, with start and interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_PAYLOAD_HIST_CONF`.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TCP_TX_GOOD_BYTES_HIST [0] ?
        output: 0/1 P4G_TCP_TX_GOOD_BYTES_HIST [0]


``P4G_APP_REPLAY_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_APP_REPLAY_COUNTERS [<group_xindex>] ?

:Description:
    Returns NAT collisions of a replay application.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_APP_REPLAY_COUNTERS [0] ?
        output: 0/1 P4G_APP_REPLAY_COUNTERS [0]


``P4G_APP_TRANSACTION_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_APP_TRANSACTION_COUNTERS [<group_xindex>] ?

:Description:
    Returns request/response transaction statistics.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_APP_TRANSACTION_COUNTERS [0] ?
        output: 0/1 P4G_APP_TRANSACTION_COUNTERS [0]


``P4G_APP_TRANSACTION_HIST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_APP_TRANSACTION_HIST [<group_xindex>] ?

:Description:
    Returns a histogram over completed request/response transactions per connection,
    with start and interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TRANSACTION_HIST_CONF`.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_APP_TRANSACTION_HIST [0] ?
        output: 0/1 P4G_APP_TRANSACTION_HIST [0]


``P4G_UDP_STATE_CURRENT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_UDP_STATE_CURRENT [<group_xindex>] ?

:Description:
    Returns a list of the current UDP state counters. The counters returned
    corresponds the the following UDP states:
    
    * ``CLOSED`` The connection structure has been created, but has not been 'ramped up' yet.    
    * ``OPEN`` The connection has been 'ramped up', and is ready to transmit or receive data.    
    * ``ACTIVE``. The connection is actively transmitting data.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_UDP_STATE_CURRENT [0] ?
        output: 0/1 P4G_UDP_STATE_CURRENT [0]


``P4G_UDP_STATE_TOTAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_UDP_STATE_TOTAL [<group_xindex>] ?

:Description:
    Returns a list of the total UDP state counters. The counters returned
    corresponds the the following UDP states:
    
    * ``CLOSED`` The connection structure has been created, but has not been 'ramped up' yet.    
    * ``OPEN`` The connection has been 'ramped up', and is ready to transmit or receive data.    
    * ``ACTIVE`` The connection is actively transmitting data.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_UDP_STATE_TOTAL [0] ?
        output: 0/1 P4G_UDP_STATE_TOTAL [0]


``P4G_UDP_STATE_RATE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_UDP_STATE_RATE [<group_xindex>] ?

:Description:
    Returns a list of the UDP state rates measured in connections/second. The
    counters returned corresponds the the following UDP state rates:
    
    * ``CLOSED`` The connection structure has been created, but has not been 'ramped up' yet.    
    * ``OPEN`` The connection has been 'ramped up', and is ready to transmit or receive data.    
    * ``ACTIVE`` The connection is actively transmitting data.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_UDP_STATE_RATE [0] ?
        output: 0/1 P4G_UDP_STATE_RATE [0]


``P4G_UDP_RX_PAYLOAD_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_UDP_RX_PAYLOAD_COUNTERS [<group_xindex>] ?

:Description:
    Returns a list of the UDP RX payload counters.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_UDP_RX_PAYLOAD_COUNTERS [0] ?
        output: 0/1 P4G_UDP_RX_PAYLOAD_COUNTERS [0]


``P4G_UDP_TX_PAYLOAD_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_UDP_TX_PAYLOAD_COUNTERS [<group_xindex>] ?

:Description:
    Returns a list of the UDP TX payload counters.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_UDP_TX_PAYLOAD_COUNTERS [0] ?
        output: 0/1 P4G_UDP_TX_PAYLOAD_COUNTERS [0]


``P4G_UDP_RX_BYTES_HIST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_UDP_RX_BYTES_HIST [<group_xindex>] ?

:Description:
    Returns a histogram over number of UDP bytes received, with start and interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_PAYLOAD_HIST_CONF`.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_UDP_RX_BYTES_HIST [0] ?
        output: 0/1 P4G_UDP_RX_BYTES_HIST [0]


``P4G_UDP_TX_BYTES_HIST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_UDP_TX_BYTES_HIST [<group_xindex>] ?

:Description:
    Returns a histogram over number of UDP bytes transmitted, with start and interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_PAYLOAD_HIST_CONF`.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_UDP_TX_BYTES_HIST [0] ?
        output: 0/1 P4G_UDP_TX_BYTES_HIST [0]


``P4G_TCP_RX_PACKET_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TCP_RX_PACKET_COUNTERS [<group_xindex>] ?

:Description:
    Returns a list of the TCP RX packet counters.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TCP_RX_PACKET_COUNTERS [0] ?
        output: 0/1 P4G_TCP_RX_PACKET_COUNTERS [0]


``P4G_TCP_TX_PACKET_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TCP_TX_PACKET_COUNTERS [<group_xindex>] ?

:Description:
    Returns a list of the TCP TX packet counters.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TCP_TX_PACKET_COUNTERS [0] ?
        output: 0/1 P4G_TCP_TX_PACKET_COUNTERS [0]


``P4G_UDP_RX_PACKET_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_UDP_RX_PACKET_COUNTERS [<group_xindex>] ?

:Description:
    Returns a list of the UDP RX packet counters.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_UDP_RX_PACKET_COUNTERS [0] ?
        output: 0/1 P4G_UDP_RX_PACKET_COUNTERS [0]


``P4G_UDP_TX_PACKET_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_UDP_TX_PACKET_COUNTERS [<group_xindex>] ?

:Description:
    Returns a list of the UDP TX packet counters.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_UDP_TX_PACKET_COUNTERS [0] ?
        output: 0/1 P4G_UDP_TX_PACKET_COUNTERS [0]


``P4G_CLEAR_POST_STAT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_CLEAR_POST_STAT [<group_xindex>]


:Description:
    Clears all TCP Connection Group post-test statistics.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_CLEAR_POST_STAT [0]
        output: <OK>



``P4G_RECALC_TIME_HIST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_RECALC_TIME_HIST [<group_xindex>]


:Description:
    Recalculates connection time histograms (retrieved with: :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_ESTABLISH_HIST` and :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_CLOSE_HIST`). Used in case time histogram configuration has been changed (using :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TIME_HIST_CONF`).

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_RECALC_TIME_HIST [0]
        output: <OK>



``P4G_RECALC_PAYLOAD_HIST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_RECALC_PAYLOAD_HIST [<group_xindex>]


:Description:
    Recalculates connection payload histograms (retrieved with: :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_RX_TOTAL_BYTES_HIST`, :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_RX_GOOD_BYTES_HIST`, :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_TX_TOTAL_BYTES_HIST` and :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_TX_GOOD_BYTES_HIST`). Used in case
    payload histogram configuration has been changed (using :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_PAYLOAD_HIST_CONF`)

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_RECALC_PAYLOAD_HIST [0]
        output: <OK>



``P4G_RECALC_TRANSACTION_HIST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_RECALC_TRANSACTION_HIST [<group_xindex>]


:Description:
    Recalculates transaction histograms (retrieved with: :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_APP_TRANSACTION_HIST`).
    Used in case transaction histogram configuration has been changed (using :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TRANSACTION_HIST_CONF`)

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_RECALC_TRANSACTION_HIST [0]
        output: <OK>



``P4G_REPLAY_FILE_INDICES``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_REPLAY_FILE_INDICES [<group_xindex>] ?

:Description:
    Returns an index list of configured Replay Files for this Connection Group.
    These are the Replay File Index that are used for :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_REPLAY_FILE_NAME` and :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_REPLAY_FILE_CLEAR` commands.  More than one Replay File can be configured for a Connection Group. When configuring a Replay File for a Connection Group, it must have an index.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_REPLAY_FILE_INDICES [0] ?
        output: 0/1 P4G_REPLAY_FILE_INDICES [0]


``P4G_REPLAY_FILE_NAME``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_REPLAY_FILE_NAME [<group_xindex>, <replay_file_xindex>] <file_name>

    # get
    <module-index>/<port-index> P4G_REPLAY_FILE_NAME [<group_xindex>, <replay_file_xindex>] ?

:Description:
    More than one Replay File can be configured for a Connection Group. When
    configuring a Replay File for a Connection Group, it must have an index. The
    indices at which Replay Files are configured does not have to be continuous.

:Actions:
    set, get

:Parameter:
    ``file_name: <string>``, file name (including relative path and excluding the ``.bson`` extension).


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_REPLAY_FILE_NAME [0, 0] word
        output: <OK>

        # get
        input:  0/1 P4G_REPLAY_FILE_NAME [0, 0] ?
        output: 0/1 P4G_REPLAY_FILE_NAME [0, 0] word


``P4G_REPLAY_FILE_CLEAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_REPLAY_FILE_CLEAR [<replay_file_xindex>]


:Description:
    Clears a Replay File index, so no Replay File is configured for that index.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_REPLAY_FILE_CLEAR [0]
        output: <OK>



``P4G_REPLAY_UTILIZATION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_REPLAY_UTILIZATION [<group_xindex>] <utilization>

    # get
    <module-index>/<port-index> P4G_REPLAY_UTILIZATION [<group_xindex>] ?

:Description:
    Specify the link layer bandwidth utilization for all the generated traffic from
    the specified Replay Connection Group.

:Actions:
    set, get

:Parameter:
    ``utilization: <integer>``, utilization specified in ppm.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_REPLAY_UTILIZATION [0] 1
        output: <OK>

        # get
        input:  0/1 P4G_REPLAY_UTILIZATION [0] ?
        output: 0/1 P4G_REPLAY_UTILIZATION [0] 1


``P4G_REPLAY_USER_INCARNATION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_REPLAY_USER_INCARNATION [<group_xindex>] <mode>

    # get
    <module-index>/<port-index> P4G_REPLAY_USER_INCARNATION [<group_xindex>] ?

:Description:
    Defines the lifecycle mode of a user and its connections, and how new users should be
    established as old connections are closed.

:Actions:
    set, get

:Parameter:
    ``mode: <LifecycleMode>``, defines the lifecycle mode of connections.

        * ``ONCE = 0``
        * ``IMMORTAL = 1``
        * ``REINCARNATE = 2``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_REPLAY_USER_INCARNATION [0] ONCE
        output: <OK>

        # get
        input:  0/1 P4G_REPLAY_USER_INCARNATION [0] ?
        output: 0/1 P4G_REPLAY_USER_INCARNATION [0] ONCE


``P4G_REPLAY_USER_REPETITIONS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_REPLAY_USER_REPETITIONS [<group_xindex>] <mode> <repetition_count>

    # get
    <module-index>/<port-index> P4G_REPLAY_USER_REPETITIONS [<group_xindex>] ?

:Description:
    Defines how many times a new user should be created after an old user has been destroyed, when :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_REPLAY_USER_INCARNATION` is set to ``IMMORTAL`` or ``REINCARNATE``.

:Actions:
    set, get

:Parameter:
    ``mode: <InfiniteOrFinite>``, the repetition mode

        * ``INFINITE = 0``
        * ``FINITE = 1``
        
    ``repetition_count: <integer>``, number of repetitions


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_REPLAY_USER_REPETITIONS [0] INFINITE 1
        output: <OK>

        # get
        input:  0/1 P4G_REPLAY_USER_REPETITIONS [0] ?
        output: 0/1 P4G_REPLAY_USER_REPETITIONS [0] INFINITE 1


``P4G_USER_STATE_CURRENT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_USER_STATE_CURRENT [<group_xindex>] ?

:Description:
    Returns a list of the current user state counters. A user is identified by a
    Client IP address. The counters returned corresponds the the following user
    states:
    
    * ``INIT`` The user has been created,  but has no open connections yet.
    
    * ``ACTIVE``  The user has at least one open connection.
    
    * ``SUCCESS`` The user has successfully transmitted and received all payload.
    
    * ``FAILED`` The user has failed in transmitting or receiving all payload.  STOPPED The user has been stopped due to ramp-down.
    
    * ``INACTIVE`` All the users connection is closed, but the user has not been destroyed yet.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_USER_STATE_CURRENT [0] ?
        output: 0/1 P4G_USER_STATE_CURRENT [0]


``P4G_USER_STATE_TOTAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_USER_STATE_TOTAL [<group_xindex>] ?

:Description:
    Returns a list of the total user state counters. A user is identified by a
    Client IP address. The counters returned corresponds the the following user
    states:
    
    * ``INIT`` The user has been created, but has no open connections yet.
    
    * ``ACTIVE`` The user has at least one open connection.
    
    * ``SUCCESS`` The user has successfully transmitted and received all payload.
    
    * ``FAILED`` The user has failed in transmitting or receiving all payload.
    
    * ``STOPPED`` The user has been stopped due to ramp-down.
    
    * ``INACTIVE`` All the users connection is closed, but the user has not been destroyed yet.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_USER_STATE_TOTAL [0] ?
        output: 0/1 P4G_USER_STATE_TOTAL [0]


``P4G_USER_STATE_RATE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_USER_STATE_RATE [<group_xindex>] ?

:Description:
    Returns a list of the user state rates measured in users/second. A user is
    identified by a Client IP address. The counters returned  corresponds the the
    following user states:
    
    * ``INIT`` The user has been created, but has no open connections yet.
    
    * ``ACTIVE`` The user has at least one open connection.
    
    * ``SUCCESS`` The user has successfully transmitted and received all payload.
    
    * ``FAILED`` The user has failed in transmitting or receiving all payload.
    
    * ``STOPPED`` The user has been stopped due to ramp-down.
    
    * ``INACTIVE`` All the users connection is closed, but the user has not been destroyed yet.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_USER_STATE_RATE [0] ?
        output: 0/1 P4G_USER_STATE_RATE [0]


``P4G_TLS_ENABLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TLS_ENABLE [<group_xindex>] <on_off>

    # get
    <module-index>/<port-index> P4G_TLS_ENABLE [<group_xindex>] ?

:Description:
    Enable/Disable TLS.

:Actions:
    set, get

:Parameter:
    ``on_off: <YesNo>``, specifying whether to enable TLS

        * ``NO = 0``
        * ``YES = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TLS_ENABLE [0] NO
        output: <OK>

        # get
        input:  0/1 P4G_TLS_ENABLE [0] ?
        output: 0/1 P4G_TLS_ENABLE [0] NO


``P4G_TLS_CIPHER_SUITES``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TLS_CIPHER_SUITES [<group_xindex>] <ciphers>

    # get
    <module-index>/<port-index> P4G_TLS_CIPHER_SUITES [<group_xindex>] ?

:Description:
    Configure the list of ciphers to announce in order of priorities.

:Actions:
    set, get

:Parameter:
    ``ciphers: <string>``, sequence of ciphers identified by theirs IANA number in order of priority.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TLS_CIPHER_SUITES [0] word
        output: <OK>

        # get
        input:  0/1 P4G_TLS_CIPHER_SUITES [0] ?
        output: 0/1 P4G_TLS_CIPHER_SUITES [0] word


``P4G_TLS_MAX_RECORD_SIZE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TLS_MAX_RECORD_SIZE [<group_xindex>] <size>

    # get
    <module-index>/<port-index> P4G_TLS_MAX_RECORD_SIZE [<group_xindex>] ?

:Description:
    Configure the maximum outgoing TLS record size.

:Actions:
    set, get

:Parameter:
    ``size: <integer>``, maximum outgoing record size in the interval (0, 16384], default value 8087.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TLS_MAX_RECORD_SIZE [0] 1
        output: <OK>

        # get
        input:  0/1 P4G_TLS_MAX_RECORD_SIZE [0] ?
        output: 0/1 P4G_TLS_MAX_RECORD_SIZE [0] 1


``P4G_TLS_CERTIFICATE_FILENAME``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TLS_CERTIFICATE_FILENAME [<group_xindex>] <filename>


:Description:
    Configure the TLS certificate.

:Actions:
    set

:Parameter:
    ``filename: <string>``, the filename of the certificate relative to the FTP TLS folder on the tester.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TLS_CERTIFICATE_FILENAME [0] word
        output: <OK>



``P4G_TLS_PRIVATE_KEY_FILENAME``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TLS_PRIVATE_KEY_FILENAME [<group_xindex>] <filename>


:Description:
    Configure the private key matching the TLS certificate.

:Actions:
    set

:Parameter:
    ``filename: <string>``, the filename of the private key relative to the FTP TLS folder on the tester.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TLS_PRIVATE_KEY_FILENAME [0] word
        output: <OK>



``P4G_TLS_DHPARAMS_FILENAME``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TLS_DHPARAMS_FILENAME [<group_xindex>] <filename>


:Description:
    Configure TLS DH parameters, if not set a default set will be used.

:Actions:
    set

:Parameter:
    ``filename: <string>``, the filename of the TLS DH parameters relative to the FTP TLS folder on the tester.


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TLS_DHPARAMS_FILENAME [0] word
        output: <OK>



``P4G_TLS_CLOSE_NOTIFY``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TLS_CLOSE_NOTIFY [<group_xindex>] <on_off>

    # get
    <module-index>/<port-index> P4G_TLS_CLOSE_NOTIFY [<group_xindex>] ?

:Description:
    Enable/Disable TLS sending close notify alert on connection tear-down.

:Actions:
    set, get

:Parameter:
    ``on_off: <YesNo>``, whether TLS sends close notify alert on connection tear-down.

        * ``NO = 0``
        * ``YES = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TLS_CLOSE_NOTIFY [0] NO
        output: <OK>

        # get
        input:  0/1 P4G_TLS_CLOSE_NOTIFY [0] ?
        output: 0/1 P4G_TLS_CLOSE_NOTIFY [0] NO


``P4G_TLS_ALERT_WARNING_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TLS_ALERT_WARNING_COUNTERS [<group_xindex>] ?

:Description:
    Returns a list of TLS warning counters.  The counters returned corresponds the
    the following TLS warnings:

    * close_notify
    * unexpected_message
    * bad_record_mac
    * record_overflow
    * decompression_failure
    * handshake_failure
    * bad_certificate
    * unsupported_certificate
    * certificate_revoked
    * certificate_expired
    * certificate_unknown
    * illegal_parameter
    * unknown_ca
    * access_denied
    * decode_error
    * decrypt_error
    * protocol_version
    * insufficient_security
    * internal_error
    * user_canceled
    * no_renegotiation
    * unsupported_extension
    * unknown.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TLS_ALERT_WARNING_COUNTERS [0] ?
        output: 0/1 P4G_TLS_ALERT_WARNING_COUNTERS [0]


``P4G_TLS_ALERT_FATAL_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TLS_ALERT_FATAL_COUNTERS [<group_xindex>] ?

:Description:
    Returns a list of TLS error counters. The counters returned corresponds the the
    following TLS warnings:

    * close_notify
    * unexpected_message
    * bad_record_mac
    * record_overflow
    * decompression_failure
    * handshake_failure
    * bad_certificate
    * unsupported_certificate
    * certificate_revoked
    * certificate_expired
    * certificate_unknown
    * illegal_parameter
    * unknown_ca
    * access_denied
    * decode_error
    * decrypt_error
    * protocol_version
    * insufficient_security
    * internal_error
    * user_canceled
    * no_renegotiation
    * unsupported_extension
    * unknown.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TLS_ALERT_FATAL_COUNTERS [0] ?
        output: 0/1 P4G_TLS_ALERT_FATAL_COUNTERS [0]


``P4G_TLS_STATE_CURRENT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TLS_STATE_CURRENT [<group_xindex>] ?

:Description:
    Returns a list of the current TLS state counters. The counters returned
    corresponds the the following TLS states:
    
    * TLS_INACTIVE
    * TLS_HANDSHAKING
    * TLS_HANDSHAKE_DONE
    * TLS_HANDSHAKE_FAILED
    * TLS_FAILED
    * TLS_INTERNAL_FAILED
    * TLS_CLOSE_NOTIFY
    * TLS_DONE

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TLS_STATE_CURRENT [0] ?
        output: 0/1 P4G_TLS_STATE_CURRENT [0]


``P4G_TLS_STATE_TOTAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TLS_STATE_TOTAL [<group_xindex>] ?

:Description:
    Returns a list of the total TLS state counters. The counters returned
    corresponds the the following TLS states:

    * TLS_INACTIVE
    * TLS_HANDSHAKING
    * TLS_HANDSHAKE_DONE
    * TLS_HANDSHAKE_FAILED
    * TLS_FAILED
    * TLS_INTERNAL_FAILED
    * TLS_CLOSE_NOTIFY
    * TLS_DONE

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TLS_STATE_TOTAL [0] ?
        output: 0/1 P4G_TLS_STATE_TOTAL [0]


``P4G_TLS_STATE_RATE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TLS_STATE_RATE [<group_xindex>] ?

:Description:
    Returns a list of the TLS state rates measured in per second. The
    counters returned corresponds the the following TLS states:

    * TLS_INACTIVE
    * TLS_HANDSHAKING
    * TLS_HANDSHAKE_DONE
    * TLS_HANDSHAKE_FAILED
    * TLS_FAILED
    * TLS_INTERNAL_FAILED
    * TLS_CLOSE_NOTIFY
    * TLS_DONE

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TLS_STATE_RATE [0] ?
        output: 0/1 P4G_TLS_STATE_RATE [0]


``P4G_TLS_RX_PAYLOAD_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TLS_RX_PAYLOAD_COUNTERS [<group_xindex>] ?

:Description:
    Returns a list of the TLS Rx payload counters.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TLS_RX_PAYLOAD_COUNTERS [0] ?
        output: 0/1 P4G_TLS_RX_PAYLOAD_COUNTERS [0]


``P4G_TLS_TX_PAYLOAD_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TLS_TX_PAYLOAD_COUNTERS [<group_xindex>] ?

:Description:
    Returns a list of the TLS Tx payload counters.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TLS_TX_PAYLOAD_COUNTERS [0] ?
        output: 0/1 P4G_TLS_TX_PAYLOAD_COUNTERS [0]


``P4G_TLS_RX_PAYLOAD_BYTES_HIST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TLS_RX_PAYLOAD_BYTES_HIST [<group_xindex>] ?

:Description:
    Returns a histogram over number of TLS Payload bytes received, with start and
    interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_PAYLOAD_HIST_CONF`.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TLS_RX_PAYLOAD_BYTES_HIST [0] ?
        output: 0/1 P4G_TLS_RX_PAYLOAD_BYTES_HIST [0]


``P4G_TLS_TX_PAYLOAD_BYTES_HIST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TLS_TX_PAYLOAD_BYTES_HIST [<group_xindex>] ?

:Description:
    Returns a histogram over number of TLS Payload bytes transmitted, with start and
    interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_PAYLOAD_HIST_CONF`.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TLS_TX_PAYLOAD_BYTES_HIST [0] ?
        output: 0/1 P4G_TLS_TX_PAYLOAD_BYTES_HIST [0]


``P4G_TLS_HANDSHAKE_HIST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TLS_HANDSHAKE_HIST [<group_xindex>] ?

:Description:
    Returns a histogram over TLS connection handshake times, with start and interval
    values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_PAYLOAD_HIST_CONF`.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TLS_HANDSHAKE_HIST [0] ?
        output: 0/1 P4G_TLS_HANDSHAKE_HIST [0]


``P4G_TLS_SERVER_NAME``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TLS_SERVER_NAME [<group_xindex>] <server_name>

    # get
    <module-index>/<port-index> P4G_TLS_SERVER_NAME [<group_xindex>] ?

:Description:
    Configure the server name advertised by the client in the TLS SNI (Server Name
    Indication) extension. Both the client and server must be configured with the
    same server_name, as the server will check the server name in Client Hello
    message. If server name is not configured (or configured blank), the SNI
    extension will not be inserted in the Client Hello message.

:Actions:
    set, get

:Parameter:
    ``server_name: <string>``, server name inserted in the SNI TLS extension


:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TLS_SERVER_NAME [0] word
        output: <OK>

        # get
        input:  0/1 P4G_TLS_SERVER_NAME [0] ?
        output: 0/1 P4G_TLS_SERVER_NAME [0] word


``P4G_TLS_PROTOCOL_VER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4G_TLS_PROTOCOL_VER [<group_xindex>] <tls_version>

    # get
    <module-index>/<port-index> P4G_TLS_PROTOCOL_VER [<group_xindex>] ?

:Description:
    Configures the desired TLS protocol version. More specifically the TLS version
    configured is the protocol version advertised by the client in the Client Hello
    message, and the highest TLS protocol version accepted by the server. If the
    protocol_version in the Client Hello message is higher than the highest protocol
    version accepted by the server, the TLS Handshake will fail.

:Actions:
    set, get

:Parameter:
    ``tls_version: <TLSVersion>``, the highest supported TLS protocol version

        * ``SSLV3 = 0``
        * ``TLS10 = 1``
        * ``TLS11 = 2``
        * ``TLS12 = 3``

:Example:
    .. code-block::

        # set
        input:  0/1 P4G_TLS_PROTOCOL_VER [0] SSLV3
        output: <OK>

        # get
        input:  0/1 P4G_TLS_PROTOCOL_VER [0] ?
        output: 0/1 P4G_TLS_PROTOCOL_VER [0] SSLV3


``P4G_TLS_MIN_REQ_PROTOCOL_VER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4G_TLS_MIN_REQ_PROTOCOL_VER [<group_xindex>] ?

:Description:
    Returns the minimum TLS protocol version required by the configured list of
    cipher suites. Each cipher suite has a minimum required TLS protocol version
    that will support the cipher suite. The minimum required TLS protocol version
    for a list of cipher suites is the lowest minimum required TLS protocol version
    of all the cipher suites in the list.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4G_TLS_MIN_REQ_PROTOCOL_VER [0] ?
        output: 0/1 P4G_TLS_MIN_REQ_PROTOCOL_VER [0]



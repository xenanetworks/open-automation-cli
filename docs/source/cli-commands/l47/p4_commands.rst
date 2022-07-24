L47 Port Commands
-----------------------------------

``P4_TRAFFIC``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4_TRAFFIC <traffic_state>


:Description:
    Gives a traffic state command to a L47 port.

:Actions:
    set

:Parameter:
    ``traffic_state: <L47TrafficState>``, the traffic state command issued to the port

        * ``OFF = 0``
        * ``ON = 1``
        * ``STOP = 2``
        * ``PREPARE = 3``
        * ``PRERUN = 4``

:Example:
    .. code-block::

        # set
        input:  0/1 P4_TRAFFIC OFF
        output: <OK>



``P4_STATE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_STATE ?

:Description:
    Display the current state of the L47 port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_STATE ?
        output: 0/1 P4_STATE


``P4_CAPABILITIES``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_CAPABILITIES ?

:Description:
    Report the speeds supported by the L47 port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_CAPABILITIES ?
        output: 0/1 P4_CAPABILITIES


``P4_STATE_STATUS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_STATE_STATUS ?

:Description:
    Returns status of the last port state change. If the port state has changed to
    PREPARE_FAIL, the status contains information about the reason for the fail.
    Currently the status will be "OK"in all other states.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_STATE_STATUS ?
        output: 0/1 P4_STATE_STATUS


``P4_VLAN_OFFLOAD``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4_VLAN_OFFLOAD <offload>

    # get
    <module-index>/<port-index> P4_VLAN_OFFLOAD ?

:Description:
    Specifies if 802.1Q VLAN tag should be inserted and stripped by the Ethernet
    device. If VLAN Offload is switched ON, VLAN tags will not be present in frames
    captured by the L47 Server.

:Actions:
    set, get

:Parameter:
    ``offload: <OnOff>``, specifies if VLAN Offload is enabled

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P4_VLAN_OFFLOAD OFF
        output: <OK>

        # get
        input:  0/1 P4_VLAN_OFFLOAD ?
        output: 0/1 P4_VLAN_OFFLOAD OFF


``P4_ARP_CONFIG``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4_ARP_CONFIG <rate> <retrans_timeout> <retries>

    # get
    <module-index>/<port-index> P4_ARP_CONFIG ?

:Description:
    Configure the value of the ARP request transmission rate, retransmission timeout
    and max. retries.

:Actions:
    set, get

:Parameter:
    ``rate: <integer>``, ARP Request transmission rate (requests/sec) - must be larger than 0

    ``retrans_timeout: <integer>``, ARP Request retransmission timeout [ms] - must be larger than 0

    ``retries: <integer>``, maximum ARP Request retransmission retries


:Example:
    .. code-block::

        # set
        input:  0/1 P4_ARP_CONFIG 1 1 1
        output: <OK>

        # get
        input:  0/1 P4_ARP_CONFIG ?
        output: 0/1 P4_ARP_CONFIG 1 1 1


``P4_NDP_CONFIG``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4_NDP_CONFIG <rate> <retrans_timeout> <retries>

    # get
    <module-index>/<port-index> P4_NDP_CONFIG ?

:Description:
    Configure the value of the NDP Neighbor Solicitation transmission rate,
    retransmission timeout and max. retries.

:Actions:
    set, get

:Parameter:
    ``rate: <integer>``, NDP Neighbor Solicitation transmission rate (requests/sec) - must be larger than 0

    ``retrans_timeout: <integer>``, NDP Neighbor Solicitation retransmission timeout [ms] - must be larger than 0

    ``retries: <integer>``, maximum NDP Neighbor Solicitation retransmission retries


:Example:
    .. code-block::

        # set
        input:  0/1 P4_NDP_CONFIG 1 1 1
        output: <OK>

        # get
        input:  0/1 P4_NDP_CONFIG ?
        output: 0/1 P4_NDP_CONFIG 1 1 1


``P4_CAPTURE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4_CAPTURE <on_off>

    # get
    <module-index>/<port-index> P4_CAPTURE ?

:Description:
    Starts or stops packet capture on this port.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, specifying whether to capture traffic on this port

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P4_CAPTURE OFF
        output: <OK>

        # get
        input:  0/1 P4_CAPTURE ?
        output: 0/1 P4_CAPTURE OFF


``P4_CAPTURE_GET_FIRST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_CAPTURE_GET_FIRST ?

:Description:
    Returns the first captured frame on the port. Command is only valid when port is
    in state STOPPED

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_CAPTURE_GET_FIRST ?
        output: 0/1 P4_CAPTURE_GET_FIRST


``P4_CAPTURE_GET_NEXT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_CAPTURE_GET_NEXT ?

:Description:
    Returns the next captured frame on the port. Command is only valid when port is
    in state STOPPED

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_CAPTURE_GET_NEXT ?
        output: 0/1 P4_CAPTURE_GET_NEXT


``P4_ETH_TX_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_ETH_TX_COUNTERS ?

:Description:
    Return total port Ethernet transmit statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_ETH_TX_COUNTERS ?
        output: 0/1 P4_ETH_TX_COUNTERS


``P4_ETH_RX_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_ETH_RX_COUNTERS ?

:Description:
    Return total port Ethernet receive statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_ETH_RX_COUNTERS ?
        output: 0/1 P4_ETH_RX_COUNTERS


``P4_PORT_TX_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_PORT_TX_COUNTERS ?

:Description:
    Return total port transmit statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_PORT_TX_COUNTERS ?
        output: 0/1 P4_PORT_TX_COUNTERS


``P4_PORT_RX_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_PORT_RX_COUNTERS ?

:Description:
    Return total port receive statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_PORT_RX_COUNTERS ?
        output: 0/1 P4_PORT_RX_COUNTERS


``P4_PORT_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_PORT_COUNTERS ?

:Description:
    Return total port transmit error statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_PORT_COUNTERS ?
        output: 0/1 P4_PORT_COUNTERS


``P4_TX_PACKET_SIZE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_TX_PACKET_SIZE ?

:Description:
    Return histogram over transmitted (layer 2) packets sizes in 100 bytes intervals.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_TX_PACKET_SIZE ?
        output: 0/1 P4_TX_PACKET_SIZE


``P4_RX_PACKET_SIZE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_RX_PACKET_SIZE ?

:Description:
    Return a histogram over received (layer 2) packets sizes in 100 bytes intervals.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_RX_PACKET_SIZE ?
        output: 0/1 P4_RX_PACKET_SIZE


``P4_TX_MTU``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_TX_MTU ?

:Description:
    Return histogram over transmitted (layer 3) packets sizes in 1 byte intervals.
    Each bin represents a packet size in the interval [576..1500] bytes.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_TX_MTU ?
        output: 0/1 P4_TX_MTU


``P4_RX_MTU``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_RX_MTU ?

:Description:
    Return histogram over received (layer 3) packets sizes in 1 byte intervals. Each
    bin represents a packet size in the interval [576..1500] bytes.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_RX_MTU ?
        output: 0/1 P4_RX_MTU


``P4_IPV4_RX_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_IPV4_RX_COUNTERS ?

:Description:
    Return total Port IPv4 protocol receive statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_IPV4_RX_COUNTERS ?
        output: 0/1 P4_IPV4_RX_COUNTERS


``P4_IPV4_TX_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_IPV4_TX_COUNTERS ?

:Description:
    Return total Port IPv4 protocol transmit statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_IPV4_TX_COUNTERS ?
        output: 0/1 P4_IPV4_TX_COUNTERS


``P4_IPV4_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_IPV4_COUNTERS ?

:Description:
    Return total Port IPv4 protocol error statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_IPV4_COUNTERS ?
        output: 0/1 P4_IPV4_COUNTERS


``P4_IPV6_RX_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_IPV6_RX_COUNTERS ?

:Description:
    Return total Port IPv6 protocol receive statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_IPV6_RX_COUNTERS ?
        output: 0/1 P4_IPV6_RX_COUNTERS


``P4_IPV6_TX_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_IPV6_TX_COUNTERS ?

:Description:
    Return total Port IPv6 protocol transmit statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_IPV6_TX_COUNTERS ?
        output: 0/1 P4_IPV6_TX_COUNTERS


``P4_IPV6_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_IPV6_COUNTERS ?

:Description:
    Return total Port IPv6 protocol error statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_IPV6_COUNTERS ?
        output: 0/1 P4_IPV6_COUNTERS


``P4_ARP_RX_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_ARP_RX_COUNTERS ?

:Description:
    Return total Port ARP protocol receive statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_ARP_RX_COUNTERS ?
        output: 0/1 P4_ARP_RX_COUNTERS


``P4_ARP_TX_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_ARP_TX_COUNTERS ?

:Description:
    Return total Port ARP protocol transmit statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_ARP_TX_COUNTERS ?
        output: 0/1 P4_ARP_TX_COUNTERS


``P4_ARP_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_ARP_COUNTERS ?

:Description:
    Return total Port ARP protocol error statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_ARP_COUNTERS ?
        output: 0/1 P4_ARP_COUNTERS


``P4_NDP_RX_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_NDP_RX_COUNTERS ?

:Description:
    Return total Port NDP protocol receive statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_NDP_RX_COUNTERS ?
        output: 0/1 P4_NDP_RX_COUNTERS


``P4_NDP_TX_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_NDP_TX_COUNTERS ?

:Description:
    Return total Port NDP protocol transmit statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_NDP_TX_COUNTERS ?
        output: 0/1 P4_NDP_TX_COUNTERS


``P4_NDP_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_NDP_COUNTERS ?

:Description:
    Return total Port NDP protocol error statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_NDP_COUNTERS ?
        output: 0/1 P4_NDP_COUNTERS


``P4_ICMP_RX_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_ICMP_RX_COUNTERS ?

:Description:
    Return total Port ICMP protocol receive statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_ICMP_RX_COUNTERS ?
        output: 0/1 P4_ICMP_RX_COUNTERS


``P4_ICMP_TX_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_ICMP_TX_COUNTERS ?

:Description:
    Return total Port ICMP protocol transmit statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_ICMP_TX_COUNTERS ?
        output: 0/1 P4_ICMP_TX_COUNTERS


``P4_ICMP_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_ICMP_COUNTERS ?

:Description:
    Return total Port ICMP protocol error statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_ICMP_COUNTERS ?
        output: 0/1 P4_ICMP_COUNTERS


``P4_TCP_RX_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_TCP_RX_COUNTERS ?

:Description:
    Return total Port TCP protocol receive statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_TCP_RX_COUNTERS ?
        output: 0/1 P4_TCP_RX_COUNTERS


``P4_TCP_TX_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_TCP_TX_COUNTERS ?

:Description:
    Return total Port TCP protocol transmit statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_TCP_TX_COUNTERS ?
        output: 0/1 P4_TCP_TX_COUNTERS


``P4_TCP_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_TCP_COUNTERS ?

:Description:
    Return total Port TCP protocol error statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_TCP_COUNTERS ?
        output: 0/1 P4_TCP_COUNTERS


``P4_UDP_RX_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_UDP_RX_COUNTERS ?

:Description:
    Return total Port UDP protocol receive statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_UDP_RX_COUNTERS ?
        output: 0/1 P4_UDP_RX_COUNTERS


``P4_UDP_TX_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_UDP_TX_COUNTERS ?

:Description:
    Return total Port UDP protocol transmit statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_UDP_TX_COUNTERS ?
        output: 0/1 P4_UDP_TX_COUNTERS


``P4_UDP_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_UDP_COUNTERS ?

:Description:
    Return total Port UDP protocol error statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_UDP_COUNTERS ?
        output: 0/1 P4_UDP_COUNTERS


``P4_CLEAR_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4_CLEAR_COUNTERS


:Description:
    Clears all run-time port counters.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 P4_CLEAR_COUNTERS
        output: <OK>



``P4_ETH_COUNTERS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_ETH_COUNTERS ?

:Description:
    Return total port Ethernet statistics since last clear.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_ETH_COUNTERS ?
        output: 0/1 P4_ETH_COUNTERS


``P4_CLEAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4_CLEAR


:Description:
    Set the Port State to OFF and delete all configured Connection Groups for the port.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 P4_CLEAR
        output: <OK>



``P4_SPEEDSELECTION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4_SPEEDSELECTION <speed>

    # get
    <module-index>/<port-index> P4_SPEEDSELECTION ?

:Description:
    Sets the port speed. The selected speed must be one of the speeds supported by
    the port, which can be retrieved with :class:`~xoa_driver.internals.core.commands.p4_commands.P4_CAPABILITIES`.

:Actions:
    set, get

:Parameter:
    ``speed: <L47PortSpeed>``, specifies the speed mode of the port

        * ``AUTO = 0``
        * ``F100M = 1``
        * ``F1G = 2``
        * ``F2_5G = 3``
        * ``F5G = 4``
        * ``F10G = 5``
        * ``F25G = 6``
        * ``F40G = 7``
        * ``F50G = 8``
        * ``F100G = 9``

:Example:
    .. code-block::

        # set
        input:  0/1 P4_SPEEDSELECTION AUTO
        output: <OK>

        # get
        input:  0/1 P4_SPEEDSELECTION ?
        output: 0/1 P4_SPEEDSELECTION AUTO


``P4_MAX_PACKET_RATE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P4_MAX_PACKET_RATE <mode> <rate> <time_window>

    # get
    <module-index>/<port-index> P4_MAX_PACKET_RATE ?

:Description:
    Specifies the maximum number of packets per second allowed to be transmitted on the port.

:Actions:
    set, get

:Parameter:
    ``mode: <AutoOrManual>``, specifies the mode of the max. pps mechanism

        * ``AUTOMATIC = 0``
        * ``MANUAL = 1``
    ``rate: <integer>``, maximum number of packets per second to transmit on this port

    ``time_window: <integer>``, time window [us] to measure the pps rate


:Example:
    .. code-block::

        # set
        input:  0/1 P4_MAX_PACKET_RATE AUTOMATIC 1 1
        output: <OK>

        # get
        input:  0/1 P4_MAX_PACKET_RATE ?
        output: 0/1 P4_MAX_PACKET_RATE AUTOMATIC 1 1


``P4_PCI_INFO``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_PCI_INFO ?

:Description:
    Report the port PCI info.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_PCI_INFO ?
        output: 0/1 P4_PCI_INFO


``P4_FW_VER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_FW_VER ?

:Description:
    Report the firmware version of the port (NIC).

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_FW_VER ?
        output: 0/1 P4_FW_VER


``P4_DEV_NAME``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_DEV_NAME ?

:Description:
    Report the name of the device (NIC) on which the port is located.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_DEV_NAME ?
        output: 0/1 P4_DEV_NAME


``P4_PORT_TYPE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_PORT_TYPE ?

:Description:
    Report the port type. The different possible ports are divided into types.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_PORT_TYPE ?
        output: 0/1 P4_PORT_TYPE


``P4_LICENSE_INFO``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_LICENSE_INFO ?

:Description:
    Returns the information on the license assigned to the port - if any.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_LICENSE_INFO ?
        output: 0/1 P4_LICENSE_INFO


``P4_APTITUDES``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P4_APTITUDES ?

:Description:
    Returns the ports aptitudes - i.e. what is possible to configure on the port in
    terms of features and performance.
    
    Current schema of the BSON document:
    
    .. code-block::

        schema = {
            'chassis': {
                'type': 'int32',
                'required': True,
                'enum': ['CHASSIS_TYPE_UNKNOWN',
                        'CHASSIS_TYPE_APPLIANCE',
                        'CHASSIS_TYPE_BAY',
                        'CHASSIS_TYPE_COMPACT',
                        'CHASSIS_TYPE_SAFIRE']
            },
            'tcp_udp': {
                'type': 'document',
                'required': True,
                'properties': {
                    'cc': {
                        'type': 'int32',
                        'required': True,
                    },
                }
            },
            'tls': {
                'type': 'document',
                'required': True,
                'properties': {
                    'supported': {
                        'type': 'bool',
                        'required': True,
                    },
                    'cc': {
                        'type': 'int32',
                        'required': True,
                    }
                }
            }
        }

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P4_APTITUDES ?
        output: 0/1 P4_APTITUDES



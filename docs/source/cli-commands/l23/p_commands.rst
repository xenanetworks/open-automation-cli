Port Commands
---------------------

``P_RESERVATION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_RESERVATION <operation>

    # get
    <module-index>/<port-index> P_RESERVATION ?

:Description:
    You set this command to reserve, release, or relinquish a port. The port must
    be reserved before any of its configuration can be changed, including streams,
    filters, capture, and datasets.The owner of the session must already have been
    specified. Reservation will fail if the chassis or module is reserved to other
    users.

:Actions:
    set, get

:Parameter:
    ``operation: <ReservedAction>``, the reservation of the test port, i.e., reserve, release, or relinquish.

        * ``RELEASE = 0``
        * ``RESERVE = 1``
        * ``RELINQUISH = 2``

:Example:
    .. code-block::

        # set
        input:  0/1 P_RESERVATION RELEASE
        output: <OK>

        # get
        input:  0/1 P_RESERVATION ?
        output: 0/1 P_RESERVATION RELEASE


``P_RESERVEDBY``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P_RESERVEDBY ?

:Description:
    Identify the user who has a port reserved. The empty string if the port is not
    currently reserved. Note that multiple connections can specify the same name
    with C_OWNER, but a resource can only be reserved to one connection. Therefore
    you cannot count on having the port just because it is reserved in your name.
    The port is reserved to this connection only if P_RESERVATION returns
    RESERVED_BY_YOU.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P_RESERVEDBY ?
        output: 0/1 P_RESERVEDBY


``P_RESET``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_RESET


:Description:
    Reset port-level parameters to standard values, and delete all streams, filters,
    capture, and dataset definitions.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 P_RESET
        output: <OK>



``P_CAPABILITIES``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P_CAPABILITIES ?

:Description:
    A series of integer values specifying various internal limits of a port.
    integer: integer, internally defined limit values.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P_CAPABILITIES ?
        output: 0/1 P_CAPABILITIES


``P_INTERFACE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P_INTERFACE ?

:Description:
    Obtains the name of the physical interface type of a port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P_INTERFACE ?
        output: 0/1 P_INTERFACE


``P_SPEEDSELECTION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_SPEEDSELECTION <mode>

    # get
    <module-index>/<port-index> P_SPEEDSELECTION ?

:Description:
    The speed mode of an autoneg port with an interface type supporting multiple speeds.

    .. note::

        This is only a settable command when speed is selected at the port level. Use the :class:`~xoa_driver.internals.core.commands.m_commands.M_CFPCONFIG` command when speed is selected at the module level.

:Actions:
    set, get

:Parameter:
    ``mode: <PortSpeedMode>``, the speed mode of the port with an interface type supporting multiple speeds

        * ``AUTO = 0``
        * ``F10M = 1``
        * ``F100M = 2``
        * ``F1G = 3``
        * ``F10G = 4``
        * ``F40G = 5``
        * ``F100G = 6``
        * ``F10MHDX = 7``
        * ``F100MHDX = 8``
        * ``F10M100M = 9``
        * ``F100M1G = 10``
        * ``F100M1G10G = 11``
        * ``F2500M = 12``
        * ``F5G = 13``
        * ``F100M1G2500M = 14``
        * ``F25G = 15``
        * ``F50G = 16``
        * ``F200G = 17``
        * ``F400G = 18``
        * ``F800G = 19``
        * ``F1600G = 20``
        * ``UNKNOWN = 255``

:Example:
    .. code-block::

        # set
        input:  0/1 P_SPEEDSELECTION AUTO
        output: <OK>

        # get
        input:  0/1 P_SPEEDSELECTION ?
        output: 0/1 P_SPEEDSELECTION AUTO


``P_SPEED``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P_SPEED ?

:Description:
    Obtains the current physical speed of a port's interface.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P_SPEED ?
        output: 0/1 P_SPEED


``P_RECEIVESYNC``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P_RECEIVESYNC ?

:Description:
    Obtains the current in-sync status of a port's receive interface.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P_RECEIVESYNC ?
        output: 0/1 P_RECEIVESYNC


``P_COMMENT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_COMMENT <comment>

    # get
    <module-index>/<port-index> P_COMMENT ?

:Description:
    The description of a port.

:Actions:
    set, get

:Parameter:
    ``comment: <string>``, the description of the port


:Example:
    .. code-block::

        # set
        input:  0/1 P_COMMENT word
        output: <OK>

        # get
        input:  0/1 P_COMMENT ?
        output: 0/1 P_COMMENT word


``P_SPEEDREDUCTION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_SPEEDREDUCTION <ppm>

    # get
    <module-index>/<port-index> P_SPEEDREDUCTION ?

:Description:
    A speed reduction applied to the transmitting side of a port, resulting in an
    effective traffic rate that is slightly lower than the rate of the physical
    interface. Speed reduction is effectuated by inserting short idle periods in the
    generated traffic pattern to consume part of the port's physical bandwidth. The
    port's clock speed is not altered.

:Actions:
    set, get

:Parameter:
    ``ppm: <integer>``, the speed reduction ppm value of the test port


:Example:
    .. code-block::

        # set
        input:  0/1 P_SPEEDREDUCTION 1
        output: <OK>

        # get
        input:  0/1 P_SPEEDREDUCTION ?
        output: 0/1 P_SPEEDREDUCTION 1


``P_INTERFRAMEGAP``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_INTERFRAMEGAP <min_byte_count>

    # get
    <module-index>/<port-index> P_INTERFRAMEGAP ?

:Description:
    The mimimum gap between packets in the traffic generated for a port. The gap
    includes the Ethernet preamble.

:Actions:
    set, get

:Parameter:
    ``min_byte_count: <integer>``, the mimimum gap between packets in the traffic generated for a port. The gap includes the Ethernet preamble.


:Example:
    .. code-block::

        # set
        input:  0/1 P_INTERFRAMEGAP 1
        output: <OK>

        # get
        input:  0/1 P_INTERFRAMEGAP ?
        output: 0/1 P_INTERFRAMEGAP 1


``P_MACADDRESS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_MACADDRESS <mac_address>

    # get
    <module-index>/<port-index> P_MACADDRESS ?

:Description:
    A 48-bit Ethernet MAC address specified for a port. This address is used as the
    default source MAC field in the header of generated traffic for the port, and is
    also used for support of the ARP protocol.

:Actions:
    set, get

:Parameter:
    ``mac_address: <string>``, the MAC address of the port


:Example:
    .. code-block::

        # set
        input:  0/1 P_MACADDRESS word
        output: <OK>

        # get
        input:  0/1 P_MACADDRESS ?
        output: 0/1 P_MACADDRESS word


``P_IPADDRESS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_IPADDRESS <ipv4_address> <subnet_mask> <gateway> <wild>

    # get
    <module-index>/<port-index> P_IPADDRESS ?

:Description:
    An IPv4 network configuration specified for a port. The address is used as the
    default source address field in the IP header of generated traffic, and the
    configuration is also used for support of the ARP and PING protocols.

:Actions:
    set, get

:Parameter:
    ``ipv4_address: <ipv4_address>``, the IPv4 address of the port

    ``subnet_mask: <ipv4_address>``, the subnet mask of the local network segment for the port

    ``gateway: <ipv4_address>``, he gateway of the local network segment for the port

    ``wild: <ipv4_address>``, wildcards used for ARP and PING replies, and each byte must be 255 (0xFF) or 0 (0x00)


:Example:
    .. code-block::

        # set
        input:  0/1 P_IPADDRESS 192.168.1.100 255.255.255.0 192.168.1.1 192.168.1.100
        output: <OK>

        # get
        input:  0/1 P_IPADDRESS ?
        output: 0/1 P_IPADDRESS 192.168.1.100 255.255.255.0 192.168.1.1 192.168.1.100


``P_ARPREPLY``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_ARPREPLY <on_off>

    # get
    <module-index>/<port-index> P_ARPREPLY ?

:Description:
    Whether the port replies to ARP requests. The
    port can reply to incoming ARP requests by mapping the IP address specified for
    the port to the MAC address specified for the port. ARP/NDP reply generation is
    independent of whether traffic and capture is on for the port.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, whether the port replies to ARP requests

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_ARPREPLY OFF
        output: <OK>

        # get
        input:  0/1 P_ARPREPLY ?
        output: 0/1 P_ARPREPLY OFF


``P_PINGREPLY``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_PINGREPLY <on_off>

    # get
    <module-index>/<port-index> P_PINGREPLY ?

:Description:
    Whether the port replies to IPv4/IPv6 PING. The port can
    reply to incoming IPv4/IPv6 PING requests to the IP address specified for the port. IPv4/IPv6 PING
    reply generation is independent of whether traffic and capture is on for the
    port.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, whether the port replies to IPv4/IPv6 PING requests

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_PINGREPLY OFF
        output: <OK>

        # get
        input:  0/1 P_PINGREPLY ?
        output: 0/1 P_PINGREPLY OFF


``P_PAUSE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_PAUSE <on_off>

    # get
    <module-index>/<port-index> P_PAUSE ?

:Description:
    Whether a port responds to incoming Ethernet PAUSE frames by holding back outgoing traffic.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, the status of whether the port responds to incoming Ethernet PAUSE frames by holding back outgoing traffic.

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_PAUSE OFF
        output: <OK>

        # get
        input:  0/1 P_PAUSE ?
        output: 0/1 P_PAUSE OFF


``P_RANDOMSEED``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_RANDOMSEED <seed>

    # get
    <module-index>/<port-index> P_RANDOMSEED ?

:Description:
    A fixed seed value specified for a port. This value is used for a pseudo-random
    number generator used when generating traffic that requires random variation in
    packet length, payload, or modified fields. As long as no part of the port
    configuration is changed, the generated traffic patterns are reproducible when
    restarting traffic for the port. A specified seed value of -1 instead creates
    variation by using a new time-based seed value each time traffic generation is
    restarted.

:Actions:
    set, get

:Parameter:
    ``seed: <integer>``, the seed value for the port


:Example:
    .. code-block::

        # set
        input:  0/1 P_RANDOMSEED 1
        output: <OK>

        # get
        input:  0/1 P_RANDOMSEED ?
        output: 0/1 P_RANDOMSEED 1


``P_LOOPBACK``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_LOOPBACK <mode>

    # get
    <module-index>/<port-index> P_LOOPBACK ?

:Description:
    The loopback mode for a port. Ports can be configured to perform two different
    kinds of loopback: 1) External RX-to-TX loopback, where the received packets
    are re-transmitted immediately. The packets are still processed by the receive
    logic, and can be captured and analysed. 2) Internal TX-to-RX loopback, where
    the transmitted packets are received directly by the port itself. This is mainly
    useful for testing the generated traffic patterns before actual use.

:Actions:
    set, get

:Parameter:
    ``mode: <LoopbackMode>``, the loop back mode of the port

        * ``NONE = 0``
        * ``L1RX2TX = 1``
        * ``L2RX2TX = 2``
        * ``L3RX2TX = 3``
        * ``TXON2RX = 4``
        * ``TXOFF2RX = 5``
        * ``PORT2PORT = 6``

:Example:
    .. code-block::

        # set
        input:  0/1 P_LOOPBACK NONE
        output: <OK>

        # get
        input:  0/1 P_LOOPBACK ?
        output: 0/1 P_LOOPBACK NONE


``P_FLASH``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_FLASH <on_off>

    # get
    <module-index>/<port-index> P_FLASH ?

:Description:
    Make the test port LED for a particular port flash on and off with a 1-second
    interval. This is helpful when you need to identify a specific port within a
    chassis.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, the status of the LED flashing status of the port.

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_FLASH OFF
        output: <OK>

        # get
        input:  0/1 P_FLASH ?
        output: 0/1 P_FLASH OFF


``P_TRAFFIC``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_TRAFFIC <on_off>

    # get
    <module-index>/<port-index> P_TRAFFIC ?

:Description:
    Whether a port is transmitting packets. When on, the port generates a sequence
    of packets with contributions from each stream that is enabled. The streams are
    configured using the PS_xxx parameters.

    .. note::

        From Release 57.1, if any of the specified packet sizes cannot fit into the packet generator, this command will return FAILED and not start the traffic. While traffic is on the streams for this port cannot be enabled or disabled, and the configuration of those streams that are enabled cannot be changed.

:Actions:
    set, get

:Parameter:
    ``on_off: <StartOrStop>``, the traffic generation status of the port.

        * ``STOP = 0``
        * ``START = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_TRAFFIC STOP
        output: <OK>

        # get
        input:  0/1 P_TRAFFIC ?
        output: 0/1 P_TRAFFIC STOP


``P_CAPTURE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_CAPTURE <on_off>

    # get
    <module-index>/<port-index> P_CAPTURE ?

:Description:
    Whether a port is capturing packets. When on, the port retains the received
    packets and makes them available for inspection. The capture criteria are
    configured using the PC_xxx parameters. While capture is on the capture
    parameters cannot be changed.

:Actions:
    set, get

:Parameter:
    ``on_off: <StartOrStop>``, whether the port is capturing packets.

        * ``STOP = 0``
        * ``START = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_CAPTURE STOP
        output: <OK>

        # get
        input:  0/1 P_CAPTURE ?
        output: 0/1 P_CAPTURE STOP


``P_XMITONE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_XMITONE <hex_data>


:Description:
    Transmits a single packet from a port, independent of the stream definitions,
    and independent of whether traffic is on. A valid Frame Check Sum is written
    into the final four bytes.

:Actions:
    set

:Parameter:
    ``hex_data: <string>``, raw bytes of the packet in hex to transmit


:Example:
    .. code-block::

        # set
        input:  0/1 P_XMITONE word
        output: <OK>



``P_LATENCYOFFSET``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_LATENCYOFFSET <offset>

    # get
    <module-index>/<port-index> P_LATENCYOFFSET ?

:Description:
    An offset applied to the latency measurements performed for received traffic
    containing test payloads. This value affects the minimum, average, and maximum
    latency values obtained through the PR_TPLDLATENCY command.

:Actions:
    set, get

:Parameter:
    ``offset: <integer>``, the port latency offset value in nanoseconds


:Example:
    .. code-block::

        # set
        input:  0/1 P_LATENCYOFFSET 1
        output: <OK>

        # get
        input:  0/1 P_LATENCYOFFSET ?
        output: 0/1 P_LATENCYOFFSET 1


``P_LATENCYMODE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_LATENCYMODE <mode>

    # get
    <module-index>/<port-index> P_LATENCYMODE ?

:Description:
    Latency is measured by inserting a time-stamp in each packet when it is
    transmitted, and relating it to the time when the packet is received. There are
    four separate modes for calculating the latency:

        1)  Last-bit-out to last-bit-in, which measures basic bit-transit time,
            independent of packet length.
        2)  First-bit-out to last-bit-in, which adds the time taken to transmit the
            packet itself.
        3)  Last-bit-out to first-bit-in, which subtracts the time taken to transmit the
            packet itself. The same latency mode must be configured for the transmitting
            port and the receiving port; otherwise invalid measurements will occur.
        4)  First-bit-out to first-bit-in, which adds the time taken to transmit the
            packet itself, and subtracts the time taken to transmit the packet itself.
            The same latency mode must be configured for the transmitting
            port and the receiving port; otherwise invalid measurements will occur.

:Actions:
    set, get

:Parameter:
    ``mode: <LatencyMode>``, the latency measurement mode of the port

        * ``LAST2LAST = 0``
        * ``FIRST2LAST = 1``
        * ``LAST2FIRST = 2``
        * ``FIRST2FIRST = 3``

:Example:
    .. code-block::

        # set
        input:  0/1 P_LATENCYMODE LAST2LAST
        output: <OK>

        # get
        input:  0/1 P_LATENCYMODE ?
        output: 0/1 P_LATENCYMODE LAST2LAST


``P_AUTOTRAIN``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_AUTOTRAIN <interval>

    # get
    <module-index>/<port-index> P_AUTOTRAIN ?

:Description:
    The interval between sending out training packets, allowing a switch to learn
    the port's MAC address. Layer-2 switches configure themselves automatically by
    detecting the source MAC addresses of packets received on each port. If a port
    only receives, and does not itself transmit test traffic, then the switch will
    never learn its MAC address. Also, if transmission is very rare the switch will
    age-out the learned MAC address. By setting the auto-train interval you instruct
    the port to send switch training packets, independent of whether the port is
    transmitting test traffic.

:Actions:
    set, get

:Parameter:
    ``interval: <integer>``, the interval between sending out training packets of the port


:Example:
    .. code-block::

        # set
        input:  0/1 P_AUTOTRAIN 1
        output: <OK>

        # get
        input:  0/1 P_AUTOTRAIN ?
        output: 0/1 P_AUTOTRAIN 1


``P_UAT_MODE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_UAT_MODE <mode> <delay>

    # get
    <module-index>/<port-index> P_UAT_MODE ?

:Description:
    This command defines if a port is currently used by test suite Valkyrie1564, which
    means that UAT (UnAvailable Time) will be detected for the port.

:Actions:
    set, get

:Parameter:
    ``mode: <OnOff>``, the state of the affected stream counters

        * ``OFF = 0``
        * ``ON = 1``
    ``delay: <integer>``, time in milliseconds to wait before detection of UAT is started. Default value: 500. This command is ignored when state is set to OFF


:Example:
    .. code-block::

        # set
        input:  0/1 P_UAT_MODE OFF 1
        output: <OK>

        # get
        input:  0/1 P_UAT_MODE ?
        output: 0/1 P_UAT_MODE OFF 1


``P_UAT_FLR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_UAT_FLR <frame_loss_ratio>

    # get
    <module-index>/<port-index> P_UAT_FLR ?

:Description:
    This command defines the threshold for the Frame Loss Ratio, where a second is
    declared as a Severely Errored Second (SES). In Valkyrie1564 UnAvailable Time
    (UAT) is declared after 10 consecutive SES has been detected

:Actions:
    set, get

:Parameter:
    ``frame_loss_ratio: <integer>``, Frame Loss Ratio specified as a number times 1/100, 0..100


:Example:
    .. code-block::

        # set
        input:  0/1 P_UAT_FLR 1
        output: <OK>

        # get
        input:  0/1 P_UAT_FLR ?
        output: 0/1 P_UAT_FLR 1


``P_MIXWEIGHTS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_MIXWEIGHTS <weight_56_bytes> <weight_60_bytes> <weight_64_bytes> <weight_70_bytes> <weight_78_bytes> <weight_92_bytes> <weight_256_bytes> <weight_496_bytes> <weight_512_bytes> <weight_570_bytes> <weight_576_bytes> <weight_594_bytes> <weight_1438_bytes> <weight_1518_bytes> <weight_9216_bytes> <weight_16360_bytes>

    # get
    <module-index>/<port-index> P_MIXWEIGHTS ?

:Description:
    Allow changing the distribution of the MIX packet length by specifying the
    percentage of each of the 16 possible frame sizes used in the MIX.  The sum of
    the percentage values specified must be 100. The command will affect the mix-
    distribution for all streams on the port. The possible 16 frame sizes are: 56
    (not valid for 40G/100G), 60, 64, 70, 78, 92, 256, 496, 512, 570, 576, 594,
    1438, 1518, 9216, and 16360.

    .. note::

        This command requires Xena server version 375 or higher.

:Actions:
    set, get

:Parameter:
    ``weight_56_bytes: <integer>``, specifying the percentage of 56-byte frame sizes

    ``weight_60_bytes: <integer>``, specifying the percentage of 60-byte frame sizes

    ``weight_64_bytes: <integer>``, specifying the percentage of 64-byte frame sizes

    ``weight_70_bytes: <integer>``, specifying the percentage of 70-byte frame sizes

    ``weight_78_bytes: <integer>``, specifying the percentage of 78-byte frame sizes

    ``weight_92_bytes: <integer>``, specifying the percentage of 92-byte frame sizes

    ``weight_256_bytes: <integer>``, specifying the percentage of 256-byte frame sizes

    ``weight_496_bytes: <integer>``, specifying the percentage of 496-byte frame sizes

    ``weight_512_bytes: <integer>``, specifying the percentage of 512-byte frame sizes

    ``weight_570_bytes: <integer>``, specifying the percentage of 570-byte frame sizes

    ``weight_576_bytes: <integer>``, weight_576_bytes

    ``weight_594_bytes: <integer>``, specifying the percentage of 594-byte frame sizes

    ``weight_1438_bytes: <integer>``, specifying the percentage of 1438-byte frame sizes

    ``weight_1518_bytes: <integer>``, specifying the percentage of 1518-byte frame sizes

    ``weight_9216_bytes: <integer>``, specifying the percentage of 9216-byte frame sizes

    ``weight_16360_bytes: <integer>``, specifying the percentage of 16360-byte frame sizes


:Example:
    .. code-block::

        # set
        input:  0/1 P_MIXWEIGHTS 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
        output: <OK>

        # get
        input:  0/1 P_MIXWEIGHTS ?
        output: 0/1 P_MIXWEIGHTS 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1


``P_MDIXMODE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_MDIXMODE <mode>

    # get
    <module-index>/<port-index> P_MDIXMODE ?

:Description:
    Selects the MDI/MDIX behaviour of copper interfaces (Currently supported on
    M6SFP and M2SFPT).

:Actions:
    set, get

:Parameter:
    ``mode: <MDIXMode>``, the MDI/MDIX mode of the port.

        * ``AUTO = 0``
        * ``MDI = 1``
        * ``MDIX = 2``

:Example:
    .. code-block::

        # set
        input:  0/1 P_MDIXMODE AUTO
        output: <OK>

        # get
        input:  0/1 P_MDIXMODE ?
        output: 0/1 P_MDIXMODE AUTO


``P_TRAFFICERR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P_TRAFFICERR ?

:Description:
    Obtain the traffic error which has occurred in the last ``*_TRAFFIC`` or ``C_TRAFFICSYNC`` command.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P_TRAFFICERR ?
        output: 0/1 P_TRAFFICERR


``P_GAPMONITOR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_GAPMONITOR <start> <stop>

    # get
    <module-index>/<port-index> P_GAPMONITOR ?

:Description:
    The gap-start and gap-stop criteria for the port's gap monitor. The gap monitor
    expects a steady stream of incoming packets, and detects larger-than-allowed
    gaps between them. Once a gap event is encountered it requires a certain number
    of consecutive packets below the threshold to end the event.

:Actions:
    set, get

:Parameter:
    ``start: <integer>``, the maximum allowed gap between packets, in microseconds. (0 to 134.000 microseconds) 0 = disable gap monitor

    ``stop: <integer>``, the minimum number of good packets required. (0 to 1024 packets) 0 = disable gap monitor


:Example:
    .. code-block::

        # set
        input:  0/1 P_GAPMONITOR 1 1
        output: <OK>

        # get
        input:  0/1 P_GAPMONITOR ?
        output: 0/1 P_GAPMONITOR 1 1


``P_CHECKSUM``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_CHECKSUM <offset>

    # get
    <module-index>/<port-index> P_CHECKSUM ?

:Description:
    Controls an extra payload integrity checksum, which also covers the header
    protocols following the Ethernet header. It will therefore catch any
    modifications to the protocol fields (which should therefore not have modifiers
    on them).

:Actions:
    set, get

:Parameter:
    ``offset: <integer>``, the offset in the packet where the calculation of the extra checksum is started from


:Example:
    .. code-block::

        # set
        input:  0/1 P_CHECKSUM 1
        output: <OK>

        # get
        input:  0/1 P_CHECKSUM ?
        output: 0/1 P_CHECKSUM 1


``P_STATUS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P_STATUS ?

:Description:
    Get the received signal level for optical ports.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P_STATUS ?
        output: 0/1 P_STATUS


``P_AUTONEGSELECTION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_AUTONEGSELECTION <on_off>

    # get
    <module-index>/<port-index> P_AUTONEGSELECTION ?

:Description:
    Whether the port responds to incoming auto-negotiation requests. Only applicable
    to electrical ports (RJ45).

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, whether the port responds to incoming auto-negotiation requests

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_AUTONEGSELECTION OFF
        output: <OK>

        # get
        input:  0/1 P_AUTONEGSELECTION ?
        output: 0/1 P_AUTONEGSELECTION OFF


``P_MIXLENGTH``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_MIXLENGTH [<osition_xindex>] <frame_size>

    # get
    <module-index>/<port-index> P_MIXLENGTH [<osition_xindex>] ?

:Description:
    Allows inspecting the frame sizes defined for each position of the P_MIXWEIGHTS
    command.  By default, the 16 frame sizes are: 56 (not valid for 40G/100G), 60,
    64, 70, 78, 92, 256, 496, 512, 570, 576, 594, 1438, 1518, 9216, and 16360.  In
    addition to inspecting these sizes one by one, it also allows changing frame
    size for positions 0, 1, 14 and 15 (default values 56, 60, 9216 and 16360).
    Supported by the following modules: Thor-400G-7S-1P, Thor-100G-5S-4P and
    Loki-100G-5S-2P.

    .. note::

        This command requires release 84 or higher.

:Actions:
    set, get

:Parameter:
    ``frame_size: <integer>``, the frame size for the position.


:Example:
    .. code-block::

        # set
        input:  0/1 P_MIXLENGTH [0] 1
        output: <OK>

        # get
        input:  0/1 P_MIXLENGTH [0] ?
        output: 0/1 P_MIXLENGTH [0] 1


``P_ARPRXTABLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_ARPRXTABLE <chunks>

    # get
    <module-index>/<port-index> P_ARPRXTABLE ?

:Description:
    Port ARP table used to reply to incoming ARP requests.

:Actions:
    set, get

:Parameter:
    ``chunks: <ArpChunk>``, * IP address to match to the Target IP address in the ARP requests
* The prefix used for address matching
* Whether the target MAC address will be patched with the part of the IP address that is not masked by the prefix
* The target MAC address to return in the ARP reply


:Example:
    .. code-block::

        # set
        input:  0/1 P_ARPRXTABLE ?L
        output: <OK>

        # get
        input:  0/1 P_ARPRXTABLE ?
        output: 0/1 P_ARPRXTABLE ?L


``P_NDPRXTABLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_NDPRXTABLE <chunks>

    # get
    <module-index>/<port-index> P_NDPRXTABLE ?

:Description:
    Port NDP table used to reply to incoming NDP Neighbor Solicitation.

:Actions:
    set, get

:Parameter:
    ``chunks: <NdpChunk>``, * IP address to match to the Target IP address in the NDP Neighbor Solication
* The prefix used for address matching
* Whether the target MAC address will be patched with the part of the IP address that is not masked by the prefix
* The target MAC address to return in the NDP Neighbor Advertisement


:Example:
    .. code-block::

        # set
        input:  0/1 P_NDPRXTABLE ?L
        output: <OK>

        # get
        input:  0/1 P_NDPRXTABLE ?
        output: 0/1 P_NDPRXTABLE ?L


``P_MULTICAST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_MULTICAST <ipv4_multicast_addresses> <operation> <second_count>

    # get
    <module-index>/<port-index> P_MULTICAST ?

:Description:
    A multicast mode for a port. Ports can use the IGMPv2 protocol to join or leave
    multicast groups, either on an on-off basis or repeatedly.

:Actions:
    set, get

:Parameter:
    ``ipv4_multicast_addresses: <>``, a multicast group address to join or leave

    ``operation: <MulticastOperation>``, the operation

        * ``OFF = 0``
        * ``ON = 1``
        * ``JOIN = 2``
        * ``LEAVE = 3``
    ``second_count: <integer>``, the interval between repeated joins in seconds.


:Example:
    .. code-block::

        # set
        input:  0/1 P_MULTICAST 192.168.1.100 OFF 1
        output: <OK>

        # get
        input:  0/1 P_MULTICAST ?
        output: 0/1 P_MULTICAST 192.168.1.100 OFF 1


``P_MULTICASTEXT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_MULTICASTEXT <ipv4_multicast_addresses> <operation> <second_count> <igmp_version>

    # get
    <module-index>/<port-index> P_MULTICASTEXT ?

:Description:
    A multicast mode for a port. Ports can use the IGMPv2/IGMPv3 protocol to join or
    leave multicast groups, either on an on-off basis or repeatedly. ** Requires
    software release 83.2 or higher

:Actions:
    set, get

:Parameter:
    ``ipv4_multicast_addresses: <>``, a multicast group address to join or leave

    ``operation: <MulticastExtOperation>``, the operation

        * ``OFF = 0``
        * ``ON = 1``
        * ``JOIN = 2``
        * ``LEAVE = 3``
        * ``INCLUDE = 4``
        * ``EXCLUDE = 5``
        * ``LEAVE_TO_ALL = 6``
        * ``GENERAL_QUERY = 7``
        * ``GROUP_QUERY = 8``
    ``second_count: <integer>``, the interval between repeated joins in seconds.

    ``igmp_version: <IGMPVersion>``, IGMP version

        * ``IGMPV2 = 0``
        * ``IGMPV3 = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_MULTICASTEXT 192.168.1.100 OFF 1 IGMPV2
        output: <OK>

        # get
        input:  0/1 P_MULTICASTEXT ?
        output: 0/1 P_MULTICASTEXT 192.168.1.100 OFF 1 IGMPV2


``P_MCSRCLIST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_MCSRCLIST <ipv4_addresses>

    # get
    <module-index>/<port-index> P_MCSRCLIST ?

:Description:
    Multicast source list of the port. Only valid if the IGMP protocol version is
    IGMPv3 set by P_MULTICASTEXT.

:Actions:
    set, get

:Parameter:
    ``ipv4_addresses: <>``, the multicast source list of the port


:Example:
    .. code-block::

        # set
        input:  0/1 P_MCSRCLIST 192.168.1.100
        output: <OK>

        # get
        input:  0/1 P_MCSRCLIST ?
        output: 0/1 P_MCSRCLIST 192.168.1.100


``P_TXMODE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_TXMODE <mode>

    # get
    <module-index>/<port-index> P_TXMODE ?

:Description:
    The scheduling mode for outgoing traffic from the port, specifying how multiple
    logical streams are merged onto one physical port. There are four primary modes:
    Normal Interleaved: The streams are treated independently, and are merged into a
    combined traffic pattern for the port, which honors each stream's ideal packet
    placements as well as possible. This is the default mode. Strict Uniform: This
    is a slight variation of normal interleaved scheduling, which emphasizes strict
    uniformity of the inter-packet-gaps as more important than hitting the stream
    rates absolutely precisely. Sequential: Each stream in turn contribute one or
    more packets, before continuing to the next stream, in a cyclical pattern. The
    count of packets for each stream is obtained from the PS_PACKETLIMIT command
    value for the stream. The individual rates for each stream are ignored, and
    instead the overall rate is determined at the port-level. This in turn determines
    the rates for each stream, taking into account their packet lengths and counts.
    The maximum number of packets in a cycle (i.e. the sum of PS_PACKETLIMIT for all
    enabled streams) is 500. If the packet number is larger than 500,  will be returned
    when attempting to start the traffic (P_TRAFFIC ON). Burst*: When this mode is selected,
    frames from the streams on a port are sent as bursts as depicted below:
    The Burst Period is defined in the P_TXBURSTPERIOD command. For the individual streams
    the number of packets in a burst is defined by the PS_BURST command, while the Inter
    Packet Gap and the Inter Burst Gap are defined by the PS_BURSTGAP command.

:Actions:
    set, get

:Parameter:
    ``mode: <TXMode>``, the scheduling mode for outgoing traffic from the port, containing the loopback mode for the port: NORMAL (interleaved packet scheduling), STRICTUNIFORM (strict uniform mode), SEQUENTIAL (sequential packet scheduling), BURST (burst mode).

        * ``NORMAL = 0``
        * ``STRICTUNIFORM = 1``
        * ``SEQUENTIAL = 2``
        * ``BURST = 3``

:Example:
    .. code-block::

        # set
        input:  0/1 P_TXMODE NORMAL
        output: <OK>

        # get
        input:  0/1 P_TXMODE ?
        output: 0/1 P_TXMODE NORMAL


``P_MULTICASTHDR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_MULTICASTHDR <header_count> <header_format> <tag> <pcp> <dei>

    # get
    <module-index>/<port-index> P_MULTICASTHDR ?

:Description:
    Allows addition of a VLAN tag to IGMPv2 and IGPMv3 packets. This command
    requires software release 83.2 or higher.

:Actions:
    set, get

:Parameter:
    ``header_count: <integer>``, number of additional headers. Currently only 0 or 1 supported

    ``header_format: <MulticastHeaderFormat>``, indicates the header format

        * ``NOHDR = 0``
        * ``VLAN = 1``
    ``tag: <integer>``, VLAN tag (VID)

    ``pcp: <integer>``, VLAN Priority code point

    ``dei: <OnOff>``, drop-eligible indicator

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_MULTICASTHDR 1 NOHDR 1 1 OFF
        output: <OK>

        # get
        input:  0/1 P_MULTICASTHDR ?
        output: 0/1 P_MULTICASTHDR 1 NOHDR 1 1 OFF


``P_RATEFRACTION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_RATEFRACTION <port_rate_ppm>

    # get
    <module-index>/<port-index> P_RATEFRACTION ?

:Description:
    The port-level rate of the traffic transmitted for a port in sequential tx mode,
    expressed in millionths of the effective rate for the port. The bandwidth
    consumption includes the inter-frame gaps, and does not depend on the length of
    the packets for the streams.

:Actions:
    set, get

:Parameter:
    ``port_rate_ppm: <integer>``, the port-level rate of the traffic transmitted for a port in sequential tx mode, expressed in millionths of the effective rate for the port


:Example:
    .. code-block::

        # set
        input:  0/1 P_RATEFRACTION 1
        output: <OK>

        # get
        input:  0/1 P_RATEFRACTION ?
        output: 0/1 P_RATEFRACTION 1


``P_RATEPPS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_RATEPPS <port_rate_pps>

    # get
    <module-index>/<port-index> P_RATEPPS ?

:Description:
    The port-level rate of the traffic transmitted for a port in sequential tx mode,
    expressed in packets per second. The bandwidth consumption is heavily dependent
    on the length of the packets generated for the streams, and also on the inter-
    frame gap for the port.

:Actions:
    set, get

:Parameter:
    ``port_rate_pps: <integer>``, the port-level rate of the traffic transmitted for a port in sequential tx mode, expressed in packets per second


:Example:
    .. code-block::

        # set
        input:  0/1 P_RATEPPS 1
        output: <OK>

        # get
        input:  0/1 P_RATEPPS ?
        output: 0/1 P_RATEPPS 1


``P_RATEL2BPS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_RATEL2BPS <port_rate_bps>

    # get
    <module-index>/<port-index> P_RATEL2BPS ?

:Description:
    The port-level rate of the traffic transmitted for a port in sequential tx mode,
    expressed in units of bits per-second at layer-2, thus including the Ethernet
    header but excluding the inter-frame gap. The bandwidth consumption is somewhat
    dependent on the length of the packets generated for the stream, and also on the
    inter-frame gap for the port.

:Actions:
    set, get

:Parameter:
    ``port_rate_bps: <integer>``, the port-level rate of the traffic transmitted for a port in sequential tx mode, expressed in units of bits per-second at layer-2, thus including the Ethernet header but excluding the inter-frame gap


:Example:
    .. code-block::

        # set
        input:  0/1 P_RATEL2BPS 1
        output: <OK>

        # get
        input:  0/1 P_RATEL2BPS ?
        output: 0/1 P_RATEL2BPS 1


``P_PAYLOADMODE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_PAYLOADMODE <mode>

    # get
    <module-index>/<port-index> P_PAYLOADMODE ?

:Description:
    Set this command to configure the port to use different payload modes, i.e.
    normal, extend payload, and custom payload field, for ALL streams on this port.
    The extended payload feature allows the definition of a much larger (up to MTU)
    payload buffer for each stream. The custom payload field feature allows you to
    define a sequence of custom data fields for each stream. The data fields will
    then be used in a round robin fashion when packets are sent based on the stream
    definition.

:Actions:
    set, get

:Parameter:
    ``mode: <PayloadMode>``, the port's payload mode, i.e. normal, extend payload, and custom payload field, for ALL streams on this port

        * ``NORMAL = 0``
        * ``EXTPL = 1``
        * ``CDF = 2``

:Example:
    .. code-block::

        # set
        input:  0/1 P_PAYLOADMODE NORMAL
        output: <OK>

        # get
        input:  0/1 P_PAYLOADMODE ?
        output: 0/1 P_PAYLOADMODE NORMAL


``P_BRRMODE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_BRRMODE <mode>

    # get
    <module-index>/<port-index> P_BRRMODE ?

:Description:
    Selects the Master/Slave setting of 100 Mbit/s (requires Valkyrie release 76.1 or higher) and 1000 Mbit/s (requires Valkyrie release 76.2 or higher) BroadR-Reach copper interfaces.

:Actions:
    set, get

:Parameter:
    ``mode: <BRRMode>``, the port's BroadR-Reach mode

        * ``SLAVE = 0``
        * ``MASTER = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_BRRMODE SLAVE
        output: <OK>

        # get
        input:  0/1 P_BRRMODE ?
        output: 0/1 P_BRRMODE SLAVE


``P_TXENABLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_TXENABLE <on_off>

    # get
    <module-index>/<port-index> P_TXENABLE ?

:Description:
    Whether a port should enable its transmitter, or keep the outgoing link down.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, the port's transmiter status

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_TXENABLE OFF
        output: <OK>

        # get
        input:  0/1 P_TXENABLE ?
        output: 0/1 P_TXENABLE OFF


``P_MAXHEADERLENGTH``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_MAXHEADERLENGTH <max_header_length>

    # get
    <module-index>/<port-index> P_MAXHEADERLENGTH ?

:Description:
    The maximum number of header content bytes that can be freely specified for each
    generated stream. The remaining payload bytes of the packet are auto-
    generated.The default is 128 bytes. When a larger number is select there is a
    corresponding proportional reduction in the number of stream definitions that
    are available for the port. Possible values: 128 (default), 256, 512, 1024,
    2048.

:Actions:
    set, get

:Parameter:
    ``max_header_length: <integer>``, the maximum number of header content bytes that can be freely specified for each generated stream on the port


:Example:
    .. code-block::

        # set
        input:  0/1 P_MAXHEADERLENGTH 1
        output: <OK>

        # get
        input:  0/1 P_MAXHEADERLENGTH ?
        output: 0/1 P_MAXHEADERLENGTH 1


``P_TXTIMELIMIT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_TXTIMELIMIT <microseconds>

    # get
    <module-index>/<port-index> P_TXTIMELIMIT ?

:Description:
    A port-level time-limit on how long it keeps transmitting when started. After
    the elapsed time traffic must be stopped and restarted. This complements the
    stream-level PS_PACKETLIMIT function.

:Actions:
    set, get

:Parameter:
    ``microseconds: <integer>``, the port-level time-limit on how long it keeps transmitting when started in microseconds. Maximum can be 2^63


:Example:
    .. code-block::

        # set
        input:  0/1 P_TXTIMELIMIT 1
        output: <OK>

        # get
        input:  0/1 P_TXTIMELIMIT ?
        output: 0/1 P_TXTIMELIMIT 1


``P_TXTIME``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P_TXTIME ?

:Description:
    How long the port has been transmitting, the elapsed time since traffic was
    started.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P_TXTIME ?
        output: 0/1 P_TXTIME


``P_XMITONETIME``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P_XMITONETIME ?

:Description:
    The time at which the latest packet was transmitted using the P_XMITONE command.
    The time reference is the same used by the time stamps of captured packets.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P_XMITONETIME ?
        output: 0/1 P_XMITONETIME


``P_IPV6ADDRESS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_IPV6ADDRESS <ipv6_address> <gateway> <subnet_prefix> <wildcard_prefix>

    # get
    <module-index>/<port-index> P_IPV6ADDRESS ?

:Description:
    An IPv6 network configuration specified for a port. The address is used as the
    default source address field in the IP header of generated traffic, and the
    configuration is also used for support of the NDP and PINGv6 protocols.

:Actions:
    set, get

:Parameter:
    ``ipv6_address: <ipv6_address>``, the IPv6 address of the port

    ``gateway: <ipv4_address>``, the gateway of the local network segment for the port

    ``subnet_prefix: <integer>``, the subnet prefix of the local network segment for the port

    ``wildcard_prefix: <integer>``, a prefix that makes the port replies to NDP/PING for the masked addresses, valid value 0-255


:Example:
    .. code-block::

        # set
        input:  0/1 P_IPV6ADDRESS ::1 192.168.1.1 1 1
        output: <OK>

        # get
        input:  0/1 P_IPV6ADDRESS ?
        output: 0/1 P_IPV6ADDRESS ::1 192.168.1.1 1 1


``P_ARPV6REPLY``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_ARPV6REPLY <on_off>

    # get
    <module-index>/<port-index> P_ARPV6REPLY ?

:Description:
    Whether the port generates replies using the IPv6 Network Discovery Protocol.
    The port can reply to incoming NDP Neighbort Solications by mapping the IPv6 address
    specified for the port to the MAC address specified for the port. NDP reply
    generation is independent of whether traffic and capture is on for the port.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, whether the port replies to NDP Neighbor Solicitations.

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_ARPV6REPLY OFF
        output: <OK>

        # get
        input:  0/1 P_ARPV6REPLY ?
        output: 0/1 P_ARPV6REPLY OFF


``P_PINGV6REPLY``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_PINGV6REPLY <on_off>

    # get
    <module-index>/<port-index> P_PINGV6REPLY ?

:Description:
    Whether the port generates PINGv6 replies using the ICMP protocol received over
    IPv6. The port can reply to incoming PINGv6 requests to the IPv6 address
    specified for the port. PINGv6 reply generation is independent of whether
    traffic and capture is on for the port.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, whether the port replies to incoming PINGv6.

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_PINGV6REPLY OFF
        output: <OK>

        # get
        input:  0/1 P_PINGV6REPLY ?
        output: 0/1 P_PINGV6REPLY OFF


``P_ERRORS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P_ERRORS ?

:Description:
    Obtains the total number of errors detected across all streams on the port,
    including lost packets, misorder events, and payload errors.

    .. note::

        FCS errors are included, which will typically lead to double-counting of lost packets.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P_ERRORS ?
        output: 0/1 P_ERRORS


``P_TXPREPARE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_TXPREPARE


:Description:
    Prepare port for transmission

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 P_TXPREPARE
        output: <OK>



``P_TXDELAY``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_TXDELAY <delay_val>

    # get
    <module-index>/<port-index> P_TXDELAY ?

:Description:
    Sets a variable delay from a traffic start command received by the port until
    it starts transmitting. The delay is specified in multiples of 64 microseconds.
    Valid values are 0-31250 (0 to 2.000.000 microseconds).

    .. note::

        You must use :class:`~xoa_driver.internals.core.commands.c_commands.C_TRAFFIC` instead of :class:`~xoa_driver.internals.core.commands.p_commands.P_TRAFFIC` to start traffic for :class:`~xoa_driver.internals.core.commands.p_commands.P_TXDELAY` to have this effect.

:Actions:
    set, get

:Parameter:
    ``delay_val: <integer>``, the delay specified in multiples of 64 microseconds.


:Example:
    .. code-block::

        # set
        input:  0/1 P_TXDELAY 1
        output: <OK>

        # get
        input:  0/1 P_TXDELAY ?
        output: 0/1 P_TXDELAY 1


``P_LPENABLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_LPENABLE <on_off>

    # get
    <module-index>/<port-index> P_LPENABLE ?

:Description:
    Enables/disables Energy Efficient Ethernet (EEE) on the port.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, whether Energy Efficient Ethernet (EEE) is enabled on the port

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_LPENABLE OFF
        output: <OK>

        # get
        input:  0/1 P_LPENABLE ?
        output: 0/1 P_LPENABLE OFF


``P_LPTXMODE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_LPTXMODE <on_off>

    # get
    <module-index>/<port-index> P_LPTXMODE ?

:Description:
    Enables/disables the transmission of Low Power Idles (LPIs) on the port. When
    enabled, the transmit side of the port will automatically enter low-power mode
    (and leave) low-power mode in periods of low or no traffic. LPIs will only be
    transmitted if the Link Partner (receiving port) has advertised EEE capability
    for the selected port speed during EEE auto-negotiation.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, whether the transmission of Low Power Idles (LPIs) is enabeld on the port

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_LPTXMODE OFF
        output: <OK>

        # get
        input:  0/1 P_LPTXMODE ?
        output: 0/1 P_LPTXMODE OFF


``P_LPSTATUS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P_LPSTATUS ?

:Description:
    Displays the Energy Efficient Ethernet (EEE) status as reported by the PHY.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P_LPSTATUS ?
        output: 0/1 P_LPSTATUS


``P_LPPARTNERAUTONEG``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P_LPPARTNERAUTONEG ?

:Description:
    Displays the EEE capabilities advertised during autonegotiation by the far side
    (link partner).

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P_LPPARTNERAUTONEG ?
        output: 0/1 P_LPPARTNERAUTONEG


``P_LPSNRMARGIN``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P_LPSNRMARGIN ?

:Description:
    Displays the SNR margin on the four link channels (Channel A-D) as reported by
    the PHY. It is displayed in units of 0.1dB.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P_LPSNRMARGIN ?
        output: 0/1 P_LPSNRMARGIN


``P_LPRXPOWER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P_LPRXPOWER ?

:Description:
    Obtain the RX power recorded during training for the four channels.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P_LPRXPOWER ?
        output: 0/1 P_LPRXPOWER


``P_FAULTSIGNALING``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_FAULTSIGNALING <fault_signaling>

    # get
    <module-index>/<port-index> P_FAULTSIGNALING ?

:Description:
    Sets the remote/local fault signaling behavior of the port (performed by the
    Reconciliation Sub-layer). By default, the port acts according to the standard,
    i.e. when receiving a bad signal, it transmits "Remote Fault indications"on the
    output and when receiving a "Remote Fault indication"from the far-side it will
    transmit IDLE sequences.

:Actions:
    set, get

:Parameter:
    ``fault_signaling: <FaultSignaling>``, remote/local fault signaling behavior of the port

        * ``NORMAL = 0``
        * ``FORCE_LOCAL = 1``
        * ``FORCE_REMOTE = 2``
        * ``DISABLED = 3``

:Example:
    .. code-block::

        # set
        input:  0/1 P_FAULTSIGNALING NORMAL
        output: <OK>

        # get
        input:  0/1 P_FAULTSIGNALING ?
        output: 0/1 P_FAULTSIGNALING NORMAL


``P_FAULTSTATUS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P_FAULTSTATUS ?

:Description:
    Shows if a local or remote fault is currently being detected by the
    Reconciliation Sub-layer of the port.

    .. note::

        Currently only available on M1CFP100, M2CFP40, M2QSFP+ and M1CFP4QSFP28CXP.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P_FAULTSTATUS ?
        output: 0/1 P_FAULTSTATUS


``P_TPLDMODE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_TPLDMODE <mode>

    # get
    <module-index>/<port-index> P_TPLDMODE ?

:Description:
    Sets the size of the Xena Test Payload (TPLD) used to track streams, perform
    latency measurements etc. Default is "Normal", which is a 20 byte TPLD. "Micro"
    is a condensed version, which is useful when generating very small packets with
    relatively long headers (like IPv6). It has the following characteristics
    compared to the "normal" TPLD. When the TPLDMODE is changed, it will affect ALL
    streams on the port. 1) Only 6 byte long. 2) Less accurate mechanism to separate
    Xena-generated packets from other packets is the network - it is recommended not
    to have too much other traffic going into the receive Xena port, when micro TPLD
    is used. 3) No sequence checking (packet loss or packet misordering). The number
    of received packets for each stream can still be compared to the number of
    transmitted packets to detect packet loss once traffic has been stopped. Note:
    Currently not available on M6SFP, M2SFPT, M6RJ45+/M2RJ45+, M2CFP40, M1CFP100,
    M2SFP+4SFP

:Actions:
    set, get

:Parameter:
    ``mode: <TPLDMode>``, the Test Payload mode of the port.

        * ``NORMAL = 0``
        * ``MICRO = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_TPLDMODE NORMAL
        output: <OK>

        # get
        input:  0/1 P_TPLDMODE ?
        output: 0/1 P_TPLDMODE NORMAL


``P_LPSUPPORT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P_LPSUPPORT ?

:Description:
    Read EEE capabilities of the port (variable size, one for each supported speed,
    returns 0s if no EEE).

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P_LPSUPPORT ?
        output: 0/1 P_LPSUPPORT


``P_TXPACKETLIMIT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_TXPACKETLIMIT <packet_count_limit>

    # get
    <module-index>/<port-index> P_TXPACKETLIMIT ?

:Description:
    The number of packets that will be transmitted from a port when traffic is
    started on the port. A value of 0 or -1 makes the port transmit continuously.
    Traffic from the streams on the port can however also be set to stop after
    transmitting a number of packets.

:Actions:
    set, get

:Parameter:
    ``packet_count_limit: <integer>``, the number of packets that will be transmitted from the port when traffic is started on the port


:Example:
    .. code-block::

        # set
        input:  0/1 P_TXPACKETLIMIT 1
        output: <OK>

        # get
        input:  0/1 P_TXPACKETLIMIT ?
        output: 0/1 P_TXPACKETLIMIT 1


``P_TCVRSTATUS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P_TCVRSTATUS ?

:Description:
    Get various tcvr status information. RX loss status of the individual RX optical
    lanes (only 4 lanes are supported currently).

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P_TCVRSTATUS ?
        output: 0/1 P_TCVRSTATUS


``P_DYNAMIC``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_DYNAMIC <on_off>

    # get
    <module-index>/<port-index> P_DYNAMIC ?

:Description:
    Controls if a >10G port supports dynamic changes when the traffic is
    running. This command is only supported by ports >10G.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, whether the port should support dynamic changes when the traffic is running

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_DYNAMIC OFF
        output: <OK>

        # get
        input:  0/1 P_DYNAMIC ?
        output: 0/1 P_DYNAMIC OFF


``P_PFCENABLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_PFCENABLE <cos_0> <cos_1> <cos_2> <cos_3> <cos_4> <cos_5> <cos_6> <cos_7>

    # get
    <module-index>/<port-index> P_PFCENABLE ?

:Description:
    This setting control whether a port responds to incoming Ethernet Priority Flow
    Control (PFC) frames, by holding back outgoing traffic for that priority.

:Actions:
    set, get

:Parameter:
    ``cos_0: <OnOff>``, whether PFC response is enabled for CoS 0

        * ``OFF = 0``
        * ``ON = 1``
    ``cos_1: <OnOff>``, whether PFC response is enabled for CoS 1

        * ``OFF = 0``
        * ``ON = 1``
    ``cos_2: <OnOff>``, whether PFC response is enabled for CoS 2

        * ``OFF = 0``
        * ``ON = 1``
    ``cos_3: <OnOff>``, whether PFC response is enabled for CoS 3

        * ``OFF = 0``
        * ``ON = 1``
    ``cos_4: <OnOff>``, whether PFC response is enabled for CoS 4

        * ``OFF = 0``
        * ``ON = 1``
    ``cos_5: <OnOff>``, whether PFC response is enabled for CoS 5

        * ``OFF = 0``
        * ``ON = 1``
    ``cos_6: <OnOff>``, whether PFC response is enabled for CoS 6

        * ``OFF = 0``
        * ``ON = 1``
    ``cos_7: <OnOff>``, whether PFC response is enabled for CoS 7

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_PFCENABLE OFF OFF OFF OFF OFF OFF OFF OFF
        output: <OK>

        # get
        input:  0/1 P_PFCENABLE ?
        output: 0/1 P_PFCENABLE OFF OFF OFF OFF OFF OFF OFF OFF


``P_TXBURSTPERIOD``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_TXBURSTPERIOD <burst_period>

    # get
    <module-index>/<port-index> P_TXBURSTPERIOD ?

:Description:
    In Burst TX mode this command defines the time from the start of one sequence of
    bursts (from a number of streams) to the start of next sequence of bursts. NB:
    Only used when Port TX Mode is "BURST".

:Actions:
    set, get

:Parameter:
    ``burst_period: <integer>``, the duration in microseconds from the start of one sequence of bursts (from a number of streams) to the start of next sequence of bursts in Burst TX mode


:Example:
    .. code-block::

        # set
        input:  0/1 P_TXBURSTPERIOD 1
        output: <OK>

        # get
        input:  0/1 P_TXBURSTPERIOD ?
        output: 0/1 P_TXBURSTPERIOD 1


``P_TXRUNTLENGTH``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_TXRUNTLENGTH <runt_length>

    # get
    <module-index>/<port-index> P_TXRUNTLENGTH ?

:Description:
    Enable TX runt feature to cut all packets to a number of bytes.

:Actions:
    set, get

:Parameter:
    ``runt_length: <integer>``, enable TX runt feature to cut all packets to I bytes. Set to -1 to disable.


:Example:
    .. code-block::

        # set
        input:  0/1 P_TXRUNTLENGTH 1
        output: <OK>

        # get
        input:  0/1 P_TXRUNTLENGTH ?
        output: 0/1 P_TXRUNTLENGTH 1


``P_RXRUNTLENGTH``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_RXRUNTLENGTH <runt_length>

    # get
    <module-index>/<port-index> P_RXRUNTLENGTH ?

:Description:
    Enable RX runt length detection to flag if packets are seen with length not
    being I bytes.

:Actions:
    set, get

:Parameter:
    ``runt_length: <integer>``, RX runt length detection to flag if packets are seen with length not being I bytes. Set to -1 to disabled.


:Example:
    .. code-block::

        # set
        input:  0/1 P_RXRUNTLENGTH 1
        output: <OK>

        # get
        input:  0/1 P_RXRUNTLENGTH ?
        output: 0/1 P_RXRUNTLENGTH 1


``P_RXRUNTLEN_ERRS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P_RXRUNTLEN_ERRS ?

:Description:
    Sticky clear on read: Have packets with wrong runt length been detected since last read?

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P_RXRUNTLEN_ERRS ?
        output: 0/1 P_RXRUNTLEN_ERRS


``P_TXPREAMBLE_REMOVE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_TXPREAMBLE_REMOVE <on_off>

    # get
    <module-index>/<port-index> P_TXPREAMBLE_REMOVE ?

:Description:
    Remove preamble from outgoing frames.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, whether the preambles from outgoing frames are to be removed by the port

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_TXPREAMBLE_REMOVE OFF
        output: <OK>

        # get
        input:  0/1 P_TXPREAMBLE_REMOVE ?
        output: 0/1 P_TXPREAMBLE_REMOVE OFF


``P_RXPREAMBLE_INSERT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_RXPREAMBLE_INSERT <on_off>

    # get
    <module-index>/<port-index> P_RXPREAMBLE_INSERT ?

:Description:
    Insert preambles to the incoming frames.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, whether the port should insert preambles to the incoming frames

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_RXPREAMBLE_INSERT OFF
        output: <OK>

        # get
        input:  0/1 P_RXPREAMBLE_INSERT ?
        output: 0/1 P_RXPREAMBLE_INSERT OFF


``P_LOADMODE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_LOADMODE <on_off>

    # get
    <module-index>/<port-index> P_LOADMODE ?

:Description:
    The action determines if config load mode is enabled or disabled for the Chimera port.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, whether config load is enabled on the Chimera port

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_LOADMODE OFF
        output: <OK>

        # get
        input:  0/1 P_LOADMODE ?
        output: 0/1 P_LOADMODE OFF


``P_SPEEDS_SUPPORTED``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> P_SPEEDS_SUPPORTED ?

:Description:
    Read the speeds supported by the port. The speeds supported by a port depends on
    the transceiver inserted into the port. A series of 0/1 values, identifying
    which speeds are supported by the port.

    .. note::

        Ports can support zero (in case of e.g. empty cage), one, or multiple speeds.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 P_SPEEDS_SUPPORTED ?
        output: 0/1 P_SPEEDS_SUPPORTED


``P_EMULATE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> P_EMULATE <action>

    # get
    <module-index>/<port-index> P_EMULATE ?

:Description:
    The action determines if emulation functionality is enabled or disabled

:Actions:
    set, get

:Parameter:
    ``action: <OnOff>``, whether the Chimera port's emulation functionality is enabled

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 P_EMULATE OFF
        output: <OK>

        # get
        input:  0/1 P_EMULATE ?
        output: 0/1 P_EMULATE OFF



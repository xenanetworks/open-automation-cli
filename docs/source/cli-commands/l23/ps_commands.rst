Stream Commands
---------------------

``PS_INDICES``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_INDICES <stream_indices>

    # get
    <module-index>/<port-index> PS_INDICES ?

:Description:
    The full list of which streams are defined for a port. These are the sub-index
    values that are used for the parameters defining the traffic patterns
    transmitted for the port. Setting the value of this command creates a new
    empty stream for each value that is not already in use, and deletes each stream
    that is not mentioned in the list. The same can be accomplished one-stream-at-a-
    time using the PS_CREATE and PS_DELETE commands.

:Actions:
    set, get

:Parameter:
    ``stream_indices: <indices>``, the sub-indices of streams on the port


:Example:
    .. code-block::

        # set
        input:  0/1 PS_INDICES 0 1
        output: <OK>

        # get
        input:  0/1 PS_INDICES ?
        output: 0/1 PS_INDICES 0 1


``PS_CREATE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_CREATE [<stream_xindex>]


:Description:
    Creates an empty stream definition with the specified sub-index value.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PS_CREATE [0]
        output: <OK>



``PS_DELETE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_DELETE [<stream_xindex>]


:Description:
    Deletes the stream definition with the specified sub-index value.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PS_DELETE [0]
        output: <OK>



``PS_ENABLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_ENABLE [<stream_xindex>] <state>

    # get
    <module-index>/<port-index> PS_ENABLE [<stream_xindex>] ?

:Description:
    This property determines if a stream contributes outgoing packets for a port.
    The value can be toggled between ON and SUPPRESS while traffic is enabled at the
    port level. Streams in the OFF state cannot be set to any other value while
    traffic is enabled. The sum of the rates of all enabled or suppressed streams
    must not exceed the effective port rate.

:Actions:
    set, get

:Parameter:
    ``state: <OnOffWithSuppress>``, a stream state

        * ``OFF = 0``
        * ``ON = 1``
        * ``SUPPRESS = 2``

:Example:
    .. code-block::

        # set
        input:  0/1 PS_ENABLE [0] OFF
        output: <OK>

        # get
        input:  0/1 PS_ENABLE [0] ?
        output: 0/1 PS_ENABLE [0] OFF


``PS_PACKETLIMIT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_PACKETLIMIT [<stream_xindex>] <packet_count>

    # get
    <module-index>/<port-index> PS_PACKETLIMIT [<stream_xindex>] ?

:Description:
    Based on different port transmission mode, the meaning of this API is different.
    When Port TX Mode is set to NORMAL, STRICT UNIFORM or BURST: The number of
    packets that will be transmitted when traffic is started on a port. A value of 0
    or -1 makes the stream transmit continuously. When Port TX Mode is set to
    SEQUENTIAL: The number of sequential packets sent before switching to the next
    stream. The minimum value is 1. The port will transmit continuously until the
    user stops the traffic.

:Actions:
    set, get

:Parameter:
    ``packet_count: <integer>``, the number of packets


:Example:
    .. code-block::

        # set
        input:  0/1 PS_PACKETLIMIT [0] 1
        output: <OK>

        # get
        input:  0/1 PS_PACKETLIMIT [0] ?
        output: 0/1 PS_PACKETLIMIT [0] 1


``PS_COMMENT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_COMMENT [<stream_xindex>] <comment>

    # get
    <module-index>/<port-index> PS_COMMENT [<stream_xindex>] ?

:Description:
    The description of a stream.

:Actions:
    set, get

:Parameter:
    ``comment: <string>``, the description of the stream


:Example:
    .. code-block::

        # set
        input:  0/1 PS_COMMENT [0] word
        output: <OK>

        # get
        input:  0/1 PS_COMMENT [0] ?
        output: 0/1 PS_COMMENT [0] word


``PS_TPLDID``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_TPLDID [<stream_xindex>] <test_payload_identifier>

    # get
    <module-index>/<port-index> PS_TPLDID [<stream_xindex>] ?

:Description:
    The identifier of the test payloads inserted into packets transmitted for a
    stream. A value of -1 disables test payloads for the stream. Test payloads are
    inserted at the end of each packet, and contains time-stamp and sequence-number
    information. This allows the receiving port to provide error-checking and
    latency measurements, in addition to the basic counts and rate measurements
    provided for all traffic. The test payload identifier furthermore allows the
    receiving port to distinguish multiple different streams, which may originate
    from multiple different chassis. Since test payloads are an inter-port and
    inter-chassis mechanism, the test payload identifier assignments should be
    planned globally across all the chassis and ports of the testbed.

:Actions:
    set, get

:Parameter:
    ``test_payload_identifier: <integer>``, the test payload identifier value. -1 = disable test payloads


:Example:
    .. code-block::

        # set
        input:  0/1 PS_TPLDID [0] 1
        output: <OK>

        # get
        input:  0/1 PS_TPLDID [0] ?
        output: 0/1 PS_TPLDID [0] 1


``PS_INSERTFCS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_INSERTFCS [<stream_xindex>] <on_off>

    # get
    <module-index>/<port-index> PS_INSERTFCS [<stream_xindex>] ?

:Description:
    Whether a valid frame checksum is added to the packets of a stream.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, whether frame checksums are inserted

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PS_INSERTFCS [0] OFF
        output: <OK>

        # get
        input:  0/1 PS_INSERTFCS [0] ?
        output: 0/1 PS_INSERTFCS [0] OFF


``PS_ARPREQUEST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PS_ARPREQUEST [<stream_xindex>] ?

:Description:
    Generates an outgoing ARP request on the test port. The packet header for the
    stream must contain an IP protocol segment, and the destination IP address is
    used in the ARP request. If there is a gateway IP address specified for the port
    and it is on a different subnet than the destination IP address in the packet
    header, then the gateway IP address is used instead. The framing of the ARP
    request matches the packet header, including any VLAN protocol segments. This
    command does not generate an immediate result, but waits until an ARP
    reply is received on the test port. If no reply is received within 500
    milliseconds, it returns.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PS_ARPREQUEST [0] ?
        output: 0/1 PS_ARPREQUEST [0]


``PS_PINGREQUEST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PS_PINGREQUEST [<stream_xindex>] ?

:Description:
    Generates an outgoing ping request using the ICMP protocol on the test port. The
    packet header for the stream must contain an IP protocol segment, with valid
    source and destination IP addresses. The framing of the ping request matches the
    packet header, including any VLAN protocol segments, and the destination MAC
    address must also be valid, possibly containing a value obtained with
    PS_ARPREQUEST. This command does not generate an immediate result, but
    waits until a ping reply is received on the test port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PS_PINGREQUEST [0] ?
        output: 0/1 PS_PINGREQUEST [0]


``PS_MODIFIEREXTRANGE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_MODIFIEREXTRANGE [<stream_xindex>, <odifier_xindex>] <min_val> <step> <max_val>

    # get
    <module-index>/<port-index> PS_MODIFIEREXTRANGE [<stream_xindex>, <odifier_xindex>] ?

:Description:
    Range specification for an extended packet modifier for a stream header,
    specifying which values the modifier should take on. This applies only to
    incrementing and decrementing modifiers; random modifiers always produce every
    possible bit pattern. The range is specified as a three values: mix, step, and
    max, where max must be equal to min plus a multiple of step. Note that when
    "decrement" is specified in PS_MODIFIEREXT as the action, the value sequence
    will begin with the max value instead of the min value and decrement from there:
    {max, max-1, max-2, ...., min, max, max-1...}.

:Actions:
    set, get

:Parameter:
    ``min_val: <integer>``, the minimum modifier value

    ``step: <integer>``, the increment between modifier values

    ``max_val: <integer>``, the maximum modifier value


:Example:
    .. code-block::

        # set
        input:  0/1 PS_MODIFIEREXTRANGE [0, 0] 1 1 1
        output: <OK>

        # get
        input:  0/1 PS_MODIFIEREXTRANGE [0, 0] ?
        output: 0/1 PS_MODIFIEREXTRANGE [0, 0] 1 1 1


``PS_MODIFIERRANGE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_MODIFIERRANGE [<stream_xindex>, <odifier_xindex>] <min_val> <step> <max_val>

    # get
    <module-index>/<port-index> PS_MODIFIERRANGE [<stream_xindex>, <odifier_xindex>] ?

:Description:
    Range specification for a packet modifier for a stream header, specifying which
    values the modifier should take on. This applies only to incrementing and
    decrementing modifiers; random modifiers always produce every possible bit
    pattern. The range is specified as three values: mix, step, and max, where max
    must be equal to min plus a multiple of step. Note that when "decrement" is
    specified in PS_MODIFIER as the action, the value sequence will begin with the
    max value instead of the min value and decrement from there: {max, max-1, max-2,
    ...., min, max, max-1...}.

:Actions:
    set, get

:Parameter:
    ``min_val: <integer>``, the minimum modifier value

    ``step: <integer>``, the increment between modifier values

    ``max_val: <integer>``, the maximum modifier value


:Example:
    .. code-block::

        # set
        input:  0/1 PS_MODIFIERRANGE [0, 0] 1 1 1
        output: <OK>

        # get
        input:  0/1 PS_MODIFIERRANGE [0, 0] ?
        output: 0/1 PS_MODIFIERRANGE [0, 0] 1 1 1


``PS_RATEFRACTION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_RATEFRACTION [<stream_xindex>] <stream_rate_ppm>

    # get
    <module-index>/<port-index> PS_RATEFRACTION [<stream_xindex>] ?

:Description:
    The rate of the traffic transmitted for a stream expressed in millionths of the
    effective rate for the port. The bandwidth consumption includes the inter-frame
    gap and is independent of the length of the packets generated for the stream.
    The sum of the bandwidth consumption for all the enabled streams must not exceed
    the effective rate for the port. Setting this command also instructs the
    Manager to attempt to keep the rate-percentage unchanged in case it has to cap
    stream rates. Get value is only valid if the rate was last set using this
    command.

:Actions:
    set, get

:Parameter:
    ``stream_rate_ppm: <integer>``, stream rate expressed as a ppm value between 0 and 1,000,000.


:Example:
    .. code-block::

        # set
        input:  0/1 PS_RATEFRACTION [0] 1
        output: <OK>

        # get
        input:  0/1 PS_RATEFRACTION [0] ?
        output: 0/1 PS_RATEFRACTION [0] 1


``PS_RATEPPS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_RATEPPS [<stream_xindex>] <stream_rate_pps>

    # get
    <module-index>/<port-index> PS_RATEPPS [<stream_xindex>] ?

:Description:
    The rate of the traffic transmitted for a stream expressed in packets per
    second. The bandwidth consumption is heavily dependent on the length of the
    packets generated for the stream, and also on the inter-frame gap for the port.
    The sum of the bandwidth consumption for all the enabled streams must not exceed
    the effective rate for the port. Setting this command also instructs the
    Manager to attempt to keep the packets-per-second unchanged in case it has to
    cap stream rates. Get value is only valid if the rate was the last set using
    this command.

:Actions:
    set, get

:Parameter:
    ``stream_rate_pps: <integer>``, stream rate expressed in packets per second


:Example:
    .. code-block::

        # set
        input:  0/1 PS_RATEPPS [0] 1
        output: <OK>

        # get
        input:  0/1 PS_RATEPPS [0] ?
        output: 0/1 PS_RATEPPS [0] 1


``PS_RATEL2BPS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_RATEL2BPS [<stream_xindex>] <l2_bps>

    # get
    <module-index>/<port-index> PS_RATEL2BPS [<stream_xindex>] ?

:Description:
    The rate of the traffic transmitted for a stream, expressed in units of bits-
    per-second at layer-2, thus including the Ethernet header but excluding the
    inter-frame gap. The bandwidth consumption is somewhat dependent on the length
    of the packets generated for the stream, and also on the inter-frame gap for the
    port. The sum of the bandwidth consumption for all the enabled streams must not
    exceed the effective rate for the port. Setting this command also instructs
    the Manager to attempt to keep the layer-2 bps rate unchanged in case it has to
    cap stream rates. Get value is only valid if the rate was the last set using
    this command.

:Actions:
    set, get

:Parameter:
    ``l2_bps: <integer>``, stream rate expressed in bits per second


:Example:
    .. code-block::

        # set
        input:  0/1 PS_RATEL2BPS [0] 1
        output: <OK>

        # get
        input:  0/1 PS_RATEL2BPS [0] ?
        output: 0/1 PS_RATEL2BPS [0] 1


``PS_BURST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_BURST [<stream_xindex>] <size> <density>

    # get
    <module-index>/<port-index> PS_BURST [<stream_xindex>] ?

:Description:
    The burstiness of the traffic transmitted for a stream, expressed in terms of
    the number of packets in each burst, and how densely they are packed together.
    The burstiness does not affect the bandwidth consumed by the stream, only the
    spacing between the packets. A density value of 100 means that the packets are
    packed tightly together, only spaced by the minimum inter-frame gap. A value of
    0 means even, non-bursty, spacing. The exact spacing achieved depends on the
    other enabled streams of the port.

:Actions:
    set, get

:Parameter:
    ``size: <integer>``, the number of packets lumped together in a burst

    ``density: <integer>``, the percentage of the available spacing that is inserted between bursts


:Example:
    .. code-block::

        # set
        input:  0/1 PS_BURST [0] 1 1
        output: <OK>

        # get
        input:  0/1 PS_BURST [0] ?
        output: 0/1 PS_BURST [0] 1 1


``PS_PACKETHEADER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_PACKETHEADER [<stream_xindex>] <hex_data>

    # get
    <module-index>/<port-index> PS_PACKETHEADER [<stream_xindex>] ?

:Description:
    The first portion of the packet bytes that are transmitted for a stream. This
    starts with the 14 bytes of the Ethernet header, followed by any contained
    protocol segments. All packets transmitted for the stream start with this fixed
    header. Individual byte positions of the packet header may be varied on a
    packet-to-packet basis using modifiers. The full packet comprises the header,
    the payload, an optional test payload, and the frame checksum. The header data
    is specified as raw bytes, since the script environment does not know the field-
    by-field layout of the various protocol segments.

:Actions:
    set, get

:Parameter:
    ``hex_data: <string>``, the raw bytes comprising the packet header


:Example:
    .. code-block::

        # set
        input:  0/1 PS_PACKETHEADER [0] word
        output: <OK>

        # get
        input:  0/1 PS_PACKETHEADER [0] ?
        output: 0/1 PS_PACKETHEADER [0] word


``PS_HEADERPROTOCOL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_HEADERPROTOCOL [<stream_xindex>] <segments>

    # get
    <module-index>/<port-index> PS_HEADERPROTOCOL [<stream_xindex>] ?

:Description:
    This command will inform the Xena tester how to interpret the packet header
    byte sequence specified with PS_PACKETHEADER.  This is mainly for information
    purposes, and the stream will transmit the packet header bytes even if no
    protocol segments are specified.  The Xena tester however support calculation of
    certain field values in hardware, such as the IP, TCP and UDP length and
    checksum fields.  This allow the use of hardware modifiers for these protocol
    segments.  In order for this function to work the Xena tester needs to know the
    type of each segment that precedes the segment where the hardware calculation is
    to be performed.

:Actions:
    set, get

:Parameter:
    ``segments: <List[ProtocolOption]>``, a number specifying a built-in protocol segment


:Example:
    .. code-block::

        # set
        input:  0/1 PS_HEADERPROTOCOL [0] 0 1 2
        output: <OK>

        # get
        input:  0/1 PS_HEADERPROTOCOL [0] ?
        output: 0/1 PS_HEADERPROTOCOL [0] 0 1 2


``PS_MODIFIERCOUNT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_MODIFIERCOUNT [<stream_xindex>] <modifier_count>

    # get
    <module-index>/<port-index> PS_MODIFIERCOUNT [<stream_xindex>] ?

:Description:
    The number of standard 16-bit modifiers active on the packet header of a stream.
    Each modifier is specified using PS_MODIFIER.

:Actions:
    set, get

:Parameter:
    ``modifier_count: <integer>``, the number of modifiers for the stream


:Example:
    .. code-block::

        # set
        input:  0/1 PS_MODIFIERCOUNT [0] 1
        output: <OK>

        # get
        input:  0/1 PS_MODIFIERCOUNT [0] ?
        output: 0/1 PS_MODIFIERCOUNT [0] 1


``PS_MODIFIER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_MODIFIER [<stream_xindex>, <odifier_xindex>] <position> <mask> <action> <repetition>

    # get
    <module-index>/<port-index> PS_MODIFIER [<stream_xindex>, <odifier_xindex>] ?

:Description:
    A packet modifier for a stream header. The headers of each packet transmitted
    for the stream will be varied according to the modifier specification. This
    command requires two sub-indices, one for the stream and one for the modifier.
    A modifier is positioned at a fixed place in the header, selects a number of
    consecutive bits starting from that position, and applies an action to those
    bits in each packet. Packets can be repeated so that a certain number of
    identical packets are transmitted before applying the next modification.

:Actions:
    set, get

:Parameter:
    ``position: <integer>``, the byte position from the start of the packet

    ``mask: <string>``, the mask specifying which bits to affect

    ``action: <ModifierAction>``, which action to perform on the affected bits

        * ``INC = 0``
        * ``DEC = 1``
        * ``RANDOM = 2``

    ``repetition: <integer>``, how many times to repeat on each packet


:Example:
    .. code-block::

        # set
        input:  0/1 PS_MODIFIER [0, 0] 1 word INC 1
        output: <OK>

        # get
        input:  0/1 PS_MODIFIER [0, 0] ?
        output: 0/1 PS_MODIFIER [0, 0] 1 word INC 1


``PS_PACKETLENGTH``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_PACKETLENGTH [<stream_xindex>] <length_type> <min_val> <max_val>

    # get
    <module-index>/<port-index> PS_PACKETLENGTH [<stream_xindex>] ?

:Description:
    The length distribution of the packets transmitted for a stream. The length of
    the packets transmitted for a stream can be varied from packet to packet,
    according to a choice of distributions within a specified min...max range. The
    length of each packet is reflected in the size of the payload portion of the
    packet, whereas the header has constant length. Length variation complements,
    and is independent of, the content variation produced by header modifiers.

:Actions:
    set, get

:Parameter:
    ``length_type: <LengthType>``, the kind of distribution of packet length

        * ``FIXED = 0``
        * ``INCREMENTING = 1``
        * ``BUTTERFLY = 2``
        * ``RANDOM = 3``
        * ``MIX = 4``

    ``min_val: <integer>``, lower limit on the packet length

    ``max_val: <integer>``, upper limit on the packet length


:Example:
    .. code-block::

        # set
        input:  0/1 PS_PACKETLENGTH [0] FIXED 1 1
        output: <OK>

        # get
        input:  0/1 PS_PACKETLENGTH [0] ?
        output: 0/1 PS_PACKETLENGTH [0] FIXED 1 1


``PS_PAYLOAD``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_PAYLOAD [<stream_xindex>] <payload_type> <hex_data>

    # get
    <module-index>/<port-index> PS_PAYLOAD [<stream_xindex>] ?

:Description:
    The payload content of the packets transmitted for a stream. The payload portion
    of a packet starts after the header and continues up until the test payload or
    the frame checksum. The payload may vary in length and is filled with either an
    incrementing sequence of byte values or a repeated multi-byte pattern. Length
    variation complements and is independent of the content variation produced by
    header modifiers.

:Actions:
    set, get

:Parameter:
    ``payload_type: <PayloadType>``, the kind of payload content

        * ``PATTERN = 0``
        * ``INCREMENTING = 1``
        * ``PRBS = 2``
        * ``RANDOM = 3``

    ``hex_data: <string>``, a pattern of bytes to be repeated. The maximum length of the pattern is 18 bytes. Only used if the type is set to PATTERN.


:Example:
    .. code-block::

        # set
        input:  0/1 PS_PAYLOAD [0] PATTERN word
        output: <OK>

        # get
        input:  0/1 PS_PAYLOAD [0] ?
        output: 0/1 PS_PAYLOAD [0] PATTERN word


``PS_IPV4GATEWAY``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_IPV4GATEWAY [<stream_xindex>] <gateway>

    # get
    <module-index>/<port-index> PS_IPV4GATEWAY [<stream_xindex>] ?

:Description:
    An IPv4 gateway configuration specified for a stream.

:Actions:
    set, get

:Parameter:
    ``gateway: <ipv4_address>``, the IPv4 gateway address of the stream


:Example:
    .. code-block::

        # set
        input:  0/1 PS_IPV4GATEWAY [0] 192.168.1.1
        output: <OK>

        # get
        input:  0/1 PS_IPV4GATEWAY [0] ?
        output: 0/1 PS_IPV4GATEWAY [0] 192.168.1.1


``PS_IPV6GATEWAY``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_IPV6GATEWAY [<stream_xindex>] <gateway>

    # get
    <module-index>/<port-index> PS_IPV6GATEWAY [<stream_xindex>] ?

:Description:
    An IPv6 gateway configuration specified for a stream.

:Actions:
    set, get

:Parameter:
    ``gateway: <ipv4_address>``, the IPv6 gateway address of the stream


:Example:
    .. code-block::

        # set
        input:  0/1 PS_IPV6GATEWAY [0] 192.168.1.1
        output: <OK>

        # get
        input:  0/1 PS_IPV6GATEWAY [0] ?
        output: 0/1 PS_IPV6GATEWAY [0] 192.168.1.1


``PS_BURSTGAP``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_BURSTGAP [<stream_xindex>] <inter_packet_gap> <inter_burst_gap>

    # get
    <module-index>/<port-index> PS_BURSTGAP [<stream_xindex>] ?

:Description:
    When the port is in in Burst TX mode, this command defines the gap between packets in a burst
    (inter-packet gap) and the gap after a burst defined in one stream stops until a
    burst defined in the next stream starts (inter-burst gap).

:Actions:
    set, get

:Parameter:
    ``inter_packet_gap: <integer>``, Burst Inter Packet Gap (in bytes).

    ``inter_burst_gap: <integer>``, Inter Burst Gap (in bytes).


:Example:
    .. code-block::

        # set
        input:  0/1 PS_BURSTGAP [0] 1 1
        output: <OK>

        # get
        input:  0/1 PS_BURSTGAP [0] ?
        output: 0/1 PS_BURSTGAP [0] 1 1


``PS_INJECTFCSERR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_INJECTFCSERR [<stream_xindex>]


:Description:
    Force a frame checksum error in one of the packets currently being transmitted
    from a stream. This can aid in analyzing the error-detection functionality of
    the system under test. Traffic must be on for the port, and the stream must be
    enabled.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PS_INJECTFCSERR [0]
        output: <OK>



``PS_INJECTSEQERR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_INJECTSEQERR [<stream_xindex>]


:Description:
    Force a sequence error by skipping a test payload sequence number in one of the
    packets currently being transmitted from a stream. This can aid in analyzing the
    error-detection functionality of the system under test. Traffic must be on for
    the port, and the stream must be enabled and include test payloads.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PS_INJECTSEQERR [0]
        output: <OK>



``PS_INJECTMISERR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_INJECTMISERR [<stream_xindex>]


:Description:
    Force a misorder error by swapping the test payload sequence numbers in two of
    the packets currently being transmitted from a stream. This can aid in analysing
    the error-detection functionality of the system under test. Traffic must be on
    for the port, and the stream must be enabled and include test payloads.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PS_INJECTMISERR [0]
        output: <OK>



``PS_INJECTPLDERR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_INJECTPLDERR [<stream_xindex>]


:Description:
    Force a payload integrity error in one of the packets currently being
    transmitted from a stream. Payload integrity validation is only available for
    incrementing payloads, and the error is created by changing a byte from the
    incrementing sequence. The packet will have a correct frame checksum, but the
    receiving Xena chassis will detect the invalid payload based on information in
    the test payload. Traffic must be on for the port, and the stream must be
    enabled and include test payloads.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PS_INJECTPLDERR [0]
        output: <OK>



``PS_INJECTTPLDERR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_INJECTTPLDERR [<stream_xindex>]


:Description:
    Force a test payload error in one of the packets currently being transmitted
    from a stream. This means that the test payload will not be recognized at the
    receiving port, so it will be counted as a no-test-payload packet, and there
    will be a lost packet for the stream. Traffic must be on for the port, and the
    stream must be enabled and include test payloads.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PS_INJECTTPLDERR [0]
        output: <OK>



``PS_MODIFIEREXT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_MODIFIEREXT [<stream_xindex>, <modifier_xindex>] <position> <mask> <action> <repetition>

    # get
    <module-index>/<port-index> PS_MODIFIEREXT [<stream_xindex>, <modifier_xindex>] ?

:Description:
    An extended packet modifier for a stream header. The headers of each packet
    transmitted for the stream will be varied according to the modifier
    specification. The modifier acts on 24 bits and takes up the space for two
    16-bit modifiers to do this. This command requires two sub-indices, one for
    the stream and one for the modifier. A modifier is positioned at a fixed place
    in the header, selects a number of consecutive bits starting from that position,
    and applies an action to those bits in each packet. Packets can be repeated so
    that a certain number of identical packets are transmitted before applying the
    next modification.

:Actions:
    set, get

:Parameter:
    ``position: <integer>``, the byte position from the start of the packet. Cannot be < 1!

    ``mask: <string>``, the mask specifying which bits to affect

    ``action: <ModifierAction>``, which action to perform on the affected bits,

        * ``INC = 0``
        * ``DEC = 1``
        * ``RANDOM = 2``
        
    ``repetition: <integer>``, how many times to repeat on each packet. Note: For now the only value supported is 1.


:Example:
    .. code-block::

        # set
        input:  0/1 PS_MODIFIEREXT [0, 0] 1 word INC 1
        output: <OK>

        # get
        input:  0/1 PS_MODIFIEREXT [0, 0] ?
        output: 0/1 PS_MODIFIEREXT [0, 0] 1 word INC 1


``PS_MODIFIEREXTCOUNT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_MODIFIEREXTCOUNT [<stream_xindex>] <ext_modifier_count>

    # get
    <module-index>/<port-index> PS_MODIFIEREXTCOUNT [<stream_xindex>] ?

:Description:
    The number of extended 24-bit modifiers active on the packet header of a stream.
    Each modifier is specified using PS_MODIFIEREXT.

:Actions:
    set, get

:Parameter:
    ``ext_modifier_count: <integer>``, the number of extended 24-bit modifiers for the stream


:Example:
    .. code-block::

        # set
        input:  0/1 PS_MODIFIEREXTCOUNT [0] 1
        output: <OK>

        # get
        input:  0/1 PS_MODIFIEREXTCOUNT [0] ?
        output: 0/1 PS_MODIFIEREXTCOUNT [0] 1


``PS_CDFOFFSET``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_CDFOFFSET [<stream_xindex>] <offset>

    # get
    <module-index>/<port-index> PS_CDFOFFSET [<stream_xindex>] ?

:Description:
    This command is part of the Custom Data Field (CDF) feature. The CDF offset
    for the stream is the location in the stream data packets where the various CDF
    data will be inserted. All fields for a given stream uses the same offset
    value. The default value is zero (0) which means that the CDF data  will be
    inserted at the very start of the packet, thus overwriting the packet protocol
    headers.  If you want the CDF data to start immediately after the end of the
    packet protocol headers you will have to set the CDF field offset manually. The
    feature requires that the P_PAYLOADMODE command on the parent port has been
    set to CDF. This enables the feature for all streams on this port.

:Actions:
    set, get

:Parameter:
    ``offset: <integer>``, the location where the CDF data will be inserted


:Example:
    .. code-block::

        # set
        input:  0/1 PS_CDFOFFSET [0] 1
        output: <OK>

        # get
        input:  0/1 PS_CDFOFFSET [0] ?
        output: 0/1 PS_CDFOFFSET [0] 1


``PS_CDFCOUNT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_CDFCOUNT [<stream_xindex>] <cdf_count>

    # get
    <module-index>/<port-index> PS_CDFCOUNT [<stream_xindex>] ?

:Description:
    This command is part of the Custom Data Field (CDF) feature. It controls the
    number of custom data fields available for each stream. You can set a different number
    of fields for each stream. Changing the field count value to a larger value will
    leave all existing fields intact. Changing the field count value to a smaller
    value will remove all existing fields with an index larger than or equal to the
    new count. The feature requires that the P_PAYLOADMODE command on the parent
    port has been set to CDF. This enables the feature for all streams on this port.

:Actions:
    set, get

:Parameter:
    ``cdf_count: <integer>``, the number of CDF data fields to allocate for the stream


:Example:
    .. code-block::

        # set
        input:  0/1 PS_CDFCOUNT [0] 1
        output: <OK>

        # get
        input:  0/1 PS_CDFCOUNT [0] ?
        output: 0/1 PS_CDFCOUNT [0] 1


``PS_CDFDATA``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_CDFDATA [<stream_xindex>, <custom_data_field_xindex>] <hex_data>

    # get
    <module-index>/<port-index> PS_CDFDATA [<stream_xindex>, <custom_data_field_xindex>] ?

:Description:
    This command is part of the Custom Data Field (CDF) feature. It controls the
    actual field data for a single field. It is possible to define fields with
    different data lengths for each stream. If the length of a data field exceeds
    (packet length - CDF offset) defined for the stream the field data will be
    truncated when transmitted. The feature requires that the P_PAYLOADMODE
    command on the parent port has been set to CDF. This enables the feature for
    all streams on this port.

:Actions:
    set, get

:Parameter:
    ``hex_data: <string>``, a pattern of bytes to be used


:Example:
    .. code-block::

        # set
        input:  0/1 PS_CDFDATA [0, 0] word
        output: <OK>

        # get
        input:  0/1 PS_CDFDATA [0, 0] ?
        output: 0/1 PS_CDFDATA [0, 0] word


``PS_EXTPAYLOAD``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_EXTPAYLOAD [<stream_xindex>] <hex_data>

    # get
    <module-index>/<port-index> PS_EXTPAYLOAD [<stream_xindex>] ?

:Description:
    This command controls the extended payload feature. The PS_PAYLOAD command
    described above only allow the user to specify an 18-byte pattern (when
    PS_PAYLOAD is set to PATTERN). The PS_EXTPAYLOAD command allow the definition
    of a much larger (up to MTU) payload buffer for each stream. The extended
    payload will be inserted immediately after the end of the protocol segment area.
    The feature requires the P_PAYLOADMODE command on the parent port being set to
    EXTPL. This enables the feature for all streams on this port.

:Actions:
    set, get

:Parameter:
    ``hex_data: <string>``, the extended payload in bytes of a stream


:Example:
    .. code-block::

        # set
        input:  0/1 PS_EXTPAYLOAD [0] word
        output: <OK>

        # get
        input:  0/1 PS_EXTPAYLOAD [0] ?
        output: 0/1 PS_EXTPAYLOAD [0] word


``PS_PFCPRIORITY``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PS_PFCPRIORITY [<stream_xindex>] <pcp>

    # get
    <module-index>/<port-index> PS_PFCPRIORITY [<stream_xindex>] ?

:Description:
    Set and get the Priority Flow Control (PFC) mode.

:Actions:
    set, get

:Parameter:
    ``pcp: <PFCMode>``, pcp

        * ``VLAN_PCP = 128``

:Example:
    .. code-block::

        # set
        input:  0/1 PS_PFCPRIORITY [0] VLAN_PCP
        output: <OK>

        # get
        input:  0/1 PS_PFCPRIORITY [0] ?
        output: 0/1 PS_PFCPRIORITY [0] VLAN_PCP



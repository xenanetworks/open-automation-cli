Impairment Flow Filter Commands
----------------------------------------

``PEF_INIT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_INIT [<flow_xindex>]


:Description:
    Prepares for setting up a filter definition.  When called, all filter
    definitions in the shadow-set which are not applied are discarded and replaced
    with the default values (DEFAULT).  NOTE: There are 2 register copies used to
    configure the filters:      (1) Shadow copy (type = 0), temporary copy
    configured by SW.          Values stored in "shadow registers" have no immediate
    effect on the flow filters.          "PEF_APPLY" API will pass the values from
    the "shadow copy" to the "working copy".      (2) Working registers (type = 1),
    reflects what is currently used for filtering in the FPGA. Working registers
    cannot be written directly C only using the "shadow copy".      (3) All SETs are
    performed on shadow registers ONLY.      (4) Only when PEF_APPLY is called,
    working registers and FPGA are updated with values from the "shadow copy".

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PEF_INIT [0]
        output: <OK>



``PEF_APPLY``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_APPLY [<flow_xindex>]


:Description:
    Applies filter definitions from "shadow-registers" to "working-registers". This
    also pushes these settings to the FPGA.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PEF_APPLY [0]
        output: <OK>



``PEF_ENABLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_ENABLE [<flow_xindex>] <state>

    # get
    <module-index>/<port-index> PEF_ENABLE [<flow_xindex>] ?

:Description:
    Defines if filtering is enabled for the flow.

:Actions:
    set, get

:Parameter:
    ``state: <OnOff>``, state of the filter

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PEF_ENABLE [0] OFF
        output: <OK>

        # get
        input:  0/1 PEF_ENABLE [0] ?
        output: 0/1 PEF_ENABLE [0] OFF


``PEF_ETHSETTINGS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_ETHSETTINGS [<flow_xindex>] <use> <action>

    # get
    <module-index>/<port-index> PEF_ETHSETTINGS [<flow_xindex>] ?

:Description:
    Defines what filter action is performed on the Ethernet header.

:Actions:
    set, get

:Parameter:
    ``use: <FilterUse>``, specifies if Ethernet information is expected

        * ``OFF = 0``
        * ``AND = 1``

    ``action: <InfoAction>``, specifies the use of Ethernet information.

        * ``EXCLUDE = 0``
        * ``INCLUDE = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PEF_ETHSETTINGS [0] OFF EXCLUDE
        output: <OK>

        # get
        input:  0/1 PEF_ETHSETTINGS [0] ?
        output: 0/1 PEF_ETHSETTINGS [0] OFF EXCLUDE


``PEF_ETHSRCADDR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_ETHSRCADDR [<flow_xindex>] <use> <value> <mask>

    # get
    <module-index>/<port-index> PEF_ETHSRCADDR [<flow_xindex>] ?

:Description:
    Defines the Ethernet Source Address settings for the Ethernet filter.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``

:Actions:
    set, get

:Parameter:
    ``use: <OnOff>``, specifies the use of Ethernet Source Address information

        * ``OFF = 0``
        * ``ON = 1``

    ``value: <string>``, specifying the six bytes of the address. Default value: 0x000000000000.

    ``mask: <string>``, specifying the mask corresponding to the address. Default value: 0xFFFFFFFFFFFF.


:Example:
    .. code-block::

        # set
        input:  0/1 PEF_ETHSRCADDR [0] OFF word word
        output: <OK>

        # get
        input:  0/1 PEF_ETHSRCADDR [0] ?
        output: 0/1 PEF_ETHSRCADDR [0] OFF word word


``PEF_ETHDESTADDR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_ETHDESTADDR [<flow_xindex>] <use> <value> <mask>

    # get
    <module-index>/<port-index> PEF_ETHDESTADDR [<flow_xindex>] ?

:Description:
    Defines the Ethernet Destination Address settings for the Ethernet filter.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``

:Actions:
    set, get

:Parameter:
    ``use: <OnOff>``, specifies the use of Ethernet Destination Address information

        * ``OFF = 0``
        * ``ON = 1``

    ``value: <string>``, specifying the six bytes of the address. Default value: 0x000000000000

    ``mask: <string>``, specifying the mask corresponding to the address. Default value: 0xFFFFFFFFFFFF


:Example:
    .. code-block::

        # set
        input:  0/1 PEF_ETHDESTADDR [0] OFF word word
        output: <OK>

        # get
        input:  0/1 PEF_ETHDESTADDR [0] ?
        output: 0/1 PEF_ETHDESTADDR [0] OFF word word


``PEF_L2PUSE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_L2PUSE [<flow_xindex>] <use>

    # get
    <module-index>/<port-index> PEF_L2PUSE [<flow_xindex>] ?

:Description:
    Defines what Layer 2+ protocols that are present and may be used for the filter.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``

:Actions:
    set, get

:Parameter:
    ``use: <L2PlusPresent>``, specifies the presence of Layer 2+ protocols.

        * ``NA = 0``
        * ``VLAN1 = 1``
        * ``VLAN2 = 2``
        * ``MPLS = 3``

:Example:
    .. code-block::

        # set
        input:  0/1 PEF_L2PUSE [0] NA
        output: <OK>

        # get
        input:  0/1 PEF_L2PUSE [0] ?
        output: 0/1 PEF_L2PUSE [0] NA


``PEF_VLANSETTINGS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_VLANSETTINGS [<flow_xindex>] <use> <action>

    # get
    <module-index>/<port-index> PEF_VLANSETTINGS [<flow_xindex>] ?

:Description:
    Defines what filter action is performed on the VLAN header.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``

:Actions:
    set, get

:Parameter:
    ``use: <FilterUse>``, specifies if VLAN information is expected

        * ``OFF = 0``
        * ``AND = 1``

    ``action: <InfoAction>``, specifies the action of VLAN information

        * ``EXCLUDE = 0``
        * ``INCLUDE = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PEF_VLANSETTINGS [0] OFF EXCLUDE
        output: <OK>

        # get
        input:  0/1 PEF_VLANSETTINGS [0] ?
        output: 0/1 PEF_VLANSETTINGS [0] OFF EXCLUDE


``PEF_VLANTAG``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_VLANTAG [<flow_xindex>] <use> <value> <mask>

    # get
    <module-index>/<port-index> PEF_VLANTAG [<flow_xindex>] ?

:Description:
    Basic mode only. Defines the VLAN TAG settings for the VLAN filter.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``

:Actions:
    set, get

:Parameter:
    ``use: <OnOff>``, specifies the use of VLAN TAG information

        * ``OFF = 0``
        * ``ON = 1``

    ``value: <integer>``, specifying the 12 bit value of the tag. Default value: 0.

    ``mask: <string>``, specifying the 12 bit value of the tag. Default value: 0x0FFF


:Example:
    .. code-block::

        # set
        input:  0/1 PEF_VLANTAG [0] OFF 1 word
        output: <OK>

        # get
        input:  0/1 PEF_VLANTAG [0] ?
        output: 0/1 PEF_VLANTAG [0] OFF 1 word


``PEF_VLANPCP``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_VLANPCP [<flow_xindex>] <use> <value> <mask>

    # get
    <module-index>/<port-index> PEF_VLANPCP [<flow_xindex>] ?

:Description:
    Basic mode only. Defines the VLAN PCP settings for the VLAN filter.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``

:Actions:
    set, get

:Parameter:
    ``use: <OnOff>``, specifies the use of VLAN PCP information

        * ``OFF = 0``
        * ``ON = 1``

    ``value: <integer>``, specifying the value of the PCP. Default value: 0 (Range: 0 to 7)

    ``mask: <string>``, specifying the 8 bit value mask. Default value: 0x07


:Example:
    .. code-block::

        # set
        input:  0/1 PEF_VLANPCP [0] OFF 1 word
        output: <OK>

        # get
        input:  0/1 PEF_VLANPCP [0] ?
        output: 0/1 PEF_VLANPCP [0] OFF 1 word


``PEF_MPLSSETTINGS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_MPLSSETTINGS [<flow_xindex>] <use> <action>

    # get
    <module-index>/<port-index> PEF_MPLSSETTINGS [<flow_xindex>] ?

:Description:
    Basic mode only. Defines what filter action is performed on the MPLS header.

:Actions:
    set, get

:Parameter:
    ``use: <FilterUse>``, specifies the use of MPLS information

        * ``OFF = 0``
        * ``AND = 1``

    ``action: <InfoAction>``, specifies specifies if MPLS information is expected

        * ``EXCLUDE = 0``
        * ``INCLUDE = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PEF_MPLSSETTINGS [0] OFF EXCLUDE
        output: <OK>

        # get
        input:  0/1 PEF_MPLSSETTINGS [0] ?
        output: 0/1 PEF_MPLSSETTINGS [0] OFF EXCLUDE


``PEF_MPLSLABEL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_MPLSLABEL [<flow_xindex>] <use> <value> <mask>

    # get
    <module-index>/<port-index> PEF_MPLSLABEL [<flow_xindex>] ?

:Description:
    Basic mode only. Defines the MPLS label settings for the filter.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``

:Actions:
    set, get

:Parameter:
    ``use: <OnOff>``, specifies the use of MPLS label information.

        * ``OFF = 0``
        * ``ON = 1``

    ``value: <integer>``, specifying the 20-bit value of the label. Default value: 0.

    ``mask: <string>``, specifying the 20-bit value of the label. Default value: 0x0FFFFF,


:Example:
    .. code-block::

        # set
        input:  0/1 PEF_MPLSLABEL [0] OFF 1 word
        output: <OK>

        # get
        input:  0/1 PEF_MPLSLABEL [0] ?
        output: 0/1 PEF_MPLSLABEL [0] OFF 1 word


``PEF_MPLSTOC``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_MPLSTOC [<flow_xindex>] <use> <value> <mask>

    # get
    <module-index>/<port-index> PEF_MPLSTOC [<flow_xindex>] ?

:Description:
    Basic mode only. Defines the MPLS TOC settings for the filter.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``

:Actions:
    set, get

:Parameter:
    ``use: <OnOff>``, specifies the use of MPLS TOC information

        * ``OFF = 0``
        * ``ON = 1``

    ``value: <integer>``, specifying the value of the MPLS TOC. Default value: 0 (Range: 0 to 7).

    ``mask: <string>``, specifying the filter mask for the value of the MPLS TOC. Default value: 0x07


:Example:
    .. code-block::

        # set
        input:  0/1 PEF_MPLSTOC [0] OFF 1 word
        output: <OK>

        # get
        input:  0/1 PEF_MPLSTOC [0] ?
        output: 0/1 PEF_MPLSTOC [0] OFF 1 word


``PEF_L3USE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_L3USE [<flow_xindex>] <use>

    # get
    <module-index>/<port-index> PEF_L3USE [<flow_xindex>] ?

:Description:
    Basic mode only. Defines what Layer 3 protocols that are present and may be used
    for the filter.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``

:Actions:
    set, get

:Parameter:
    ``use: <L3PlusPresent>``, specifies the presence of Layer 3 protocols

        * ``NA = 0``
        * ``IP4 = 1``
        * ``IP6 = 2``

:Example:
    .. code-block::

        # set
        input:  0/1 PEF_L3USE [0] NA
        output: <OK>

        # get
        input:  0/1 PEF_L3USE [0] ?
        output: 0/1 PEF_L3USE [0] NA


``PEF_IPV4SETTINGS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_IPV4SETTINGS [<flow_xindex>] <use> <action>

    # get
    <module-index>/<port-index> PEF_IPV4SETTINGS [<flow_xindex>] ?

:Description:
    Basic mode only. Defines what filter action is performed on the IPv4 header.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``

:Actions:
    set, get

:Parameter:
    ``use: <FilterUse>``, specifies the use of IPv4 information

        * ``OFF = 0``
        * ``AND = 1``

    ``action: <InfoAction>``, specifies the action of IPv4 information

        * ``EXCLUDE = 0``
        * ``INCLUDE = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PEF_IPV4SETTINGS [0] OFF EXCLUDE
        output: <OK>

        # get
        input:  0/1 PEF_IPV4SETTINGS [0] ?
        output: 0/1 PEF_IPV4SETTINGS [0] OFF EXCLUDE


``PEF_IPV4SRCADDR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_IPV4SRCADDR [<flow_xindex>] <use> <value> <mask>

    # get
    <module-index>/<port-index> PEF_IPV4SRCADDR [<flow_xindex>] ?

:Description:
    Basic mode only. Defines the IPv4 Source Address settings for the IPv4 filter.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``

:Actions:
    set, get

:Parameter:
    ``use: <OnOff>``, specifies the use of IPv4 Source Address information

        * ``OFF = 0``
        * ``ON = 1``

    ``value: <ipv4_address>``, specifying the four bytes of the address. Default value: 0.0.0.0

    ``mask: <string>``, specifying the filter mask of the value. Default value: 0xFFFFFFFF


:Example:
    .. code-block::

        # set
        input:  0/1 PEF_IPV4SRCADDR [0] OFF 192.168.1.100 word
        output: <OK>

        # get
        input:  0/1 PEF_IPV4SRCADDR [0] ?
        output: 0/1 PEF_IPV4SRCADDR [0] OFF 192.168.1.100 word


``PEF_IPV4DESTADDR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_IPV4DESTADDR [<flow_xindex>] <use> <value> <mask>

    # get
    <module-index>/<port-index> PEF_IPV4DESTADDR [<flow_xindex>] ?

:Description:
    Basic mode only. Defines the IPv4 Destination Address settings for the IPv4 filter.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``

:Actions:
    set, get

:Parameter:
    ``use: <OnOff>``, specifies the use of IPv4 Destination Address information

        * ``OFF = 0``
        * ``ON = 1``

    ``value: <ipv4_address>``, specifying the four bytes of the address. Default value: 0.0.0.0

    ``mask: <string>``, specifying the filter mask of the value. Default value: 0xFFFFFFFF


:Example:
    .. code-block::

        # set
        input:  0/1 PEF_IPV4DESTADDR [0] OFF 192.168.1.100 word
        output: <OK>

        # get
        input:  0/1 PEF_IPV4DESTADDR [0] ?
        output: 0/1 PEF_IPV4DESTADDR [0] OFF 192.168.1.100 word


``PEF_IPV4DSCP``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_IPV4DSCP [<flow_xindex>] <use> <value> <mask>

    # get
    <module-index>/<port-index> PEF_IPV4DSCP [<flow_xindex>] ?

:Description:
    Basic mode only. Defines if IPv4 DSCP/TOS settings used for the IPv4 filter.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``

:Actions:
    set, get

:Parameter:
    ``use: <OnOff>``, specifies the use of IPv4 DSCP/TOS information.

        * ``OFF = 0``
        * ``ON = 1``

    ``value: <integer>``, specifying the value of the IPv4 DSCP/TOS in the upper 6 bits. value[7:2] = DSCP/TOS, value[1:0] = reserved (must be zero). Default vaule: 0

    ``mask: <string>``, specifying the filter mask of the value in the upper 6 bits. mask[7:2] = DSCP/TOS mask, mask[1:0] = reserved (must be zero). Default value: 0xFC


:Example:
    .. code-block::

        # set
        input:  0/1 PEF_IPV4DSCP [0] OFF 1 word
        output: <OK>

        # get
        input:  0/1 PEF_IPV4DSCP [0] ?
        output: 0/1 PEF_IPV4DSCP [0] OFF 1 word


``PEF_IPV6SETTINGS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_IPV6SETTINGS [<flow_xindex>] <use> <action>

    # get
    <module-index>/<port-index> PEF_IPV6SETTINGS [<flow_xindex>] ?

:Description:
    Basic mode only. Defines what filter action is performed on the IPv6 header.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``

:Actions:
    set, get

:Parameter:
    ``use: <FilterUse>``, specifies the use of IPv6 header

        * ``OFF = 0``
        * ``AND = 1``

    ``action: <InfoAction>``, specifies the action of IPv6 header

        * ``EXCLUDE = 0``
        * ``INCLUDE = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PEF_IPV6SETTINGS [0] OFF EXCLUDE
        output: <OK>

        # get
        input:  0/1 PEF_IPV6SETTINGS [0] ?
        output: 0/1 PEF_IPV6SETTINGS [0] OFF EXCLUDE


``PEF_IPV6SRCADDR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_IPV6SRCADDR [<flow_xindex>] <use> <value> <mask>

    # get
    <module-index>/<port-index> PEF_IPV6SRCADDR [<flow_xindex>] ?

:Description:
    Basic mode only. Defines the IPv6 Source Address settings for the IPv6 filter.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``

:Actions:
    set, get

:Parameter:
    ``use: <OnOff>``, specifies the use of IPv6 Source Address information

        * ``OFF = 0``
        * ``ON = 1``

    ``value: <string>``, specifying the address. Default : 0x00000000000000000000000000000000

    ``mask: <string>``, specifying the six first bytes of the address. Default value: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF


:Example:
    .. code-block::

        # set
        input:  0/1 PEF_IPV6SRCADDR [0] OFF word word
        output: <OK>

        # get
        input:  0/1 PEF_IPV6SRCADDR [0] ?
        output: 0/1 PEF_IPV6SRCADDR [0] OFF word word


``PEF_IPV6DESTADDR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_IPV6DESTADDR [<flow_xindex>] <use> <value> <mask>

    # get
    <module-index>/<port-index> PEF_IPV6DESTADDR [<flow_xindex>] ?

:Description:
    Basic mode only. Defines the IPv6 Destination Address settings for the IPv6 filter.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``

:Actions:
    set, get

:Parameter:
    ``use: <OnOff>``, specifies the use of IPv6 Destination Address information

        * ``OFF = 0``
        * ``ON = 1``

    ``value: <string>``, specifying the address. Default : 0x00000000000000000000000000000000

    ``mask: <string>``, specifying the six first bytes of the address. Default value: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF


:Example:
    .. code-block::

        # set
        input:  0/1 PEF_IPV6DESTADDR [0] OFF word word
        output: <OK>

        # get
        input:  0/1 PEF_IPV6DESTADDR [0] ?
        output: 0/1 PEF_IPV6DESTADDR [0] OFF word word


``PEF_IPV6TC``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_IPV6TC [<flow_xindex>] <use> <value> <mask>

    # get
    <module-index>/<port-index> PEF_IPV6TC [<flow_xindex>] ?

:Description:
    Basic mode only. Defines the IPv6 Traffic Class settings used for the filter.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``

:Actions:
    set, get

:Parameter:
    ``use: <OnOff>``, specifies the use of the IPv6 Traffic Class information.

        * ``OFF = 0``
        * ``ON = 1``

    ``value: <integer>``, specifying the value of the IPv6 Traffic Class in the upper 6 bits. value[7:2] = IPv6 Traffic Class. value[1:0] = reserved (must be zero). Default value: 0

    ``mask: <string>``, specifying the filter mask for the value in the upper 6 bits. mask[7:2] = IPv6 Traffic Class mask. mask[1:0] = reserved (must be zero). Default value: 0xFC


:Example:
    .. code-block::

        # set
        input:  0/1 PEF_IPV6TC [0] OFF 1 word
        output: <OK>

        # get
        input:  0/1 PEF_IPV6TC [0] ?
        output: 0/1 PEF_IPV6TC [0] OFF 1 word


``PEF_UDPSETTINGS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_UDPSETTINGS [<flow_xindex>] <use> <action>

    # get
    <module-index>/<port-index> PEF_UDPSETTINGS [<flow_xindex>] ?

:Description:
    Basic mode only. Controls if UDP packet information is used for flow filtering.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``

:Actions:
    set, get

:Parameter:
    ``use: <FilterUse>``, specifies the use of UDP information.

        * ``OFF = 0``
        * ``AND = 1``

    ``action: <InfoAction>``, specifies the action of UDP information.

        * ``EXCLUDE = 0``
        * ``INCLUDE = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PEF_UDPSETTINGS [0] OFF EXCLUDE
        output: <OK>

        # get
        input:  0/1 PEF_UDPSETTINGS [0] ?
        output: 0/1 PEF_UDPSETTINGS [0] OFF EXCLUDE


``PEF_UDPSRCPORT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_UDPSRCPORT [<flow_xindex>] <use> <value> <mask>

    # get
    <module-index>/<port-index> PEF_UDPSRCPORT [<flow_xindex>] ?

:Description:
    Basic mode only. Defines UDP Source Port settings used for the filter.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``

:Actions:
    set, get

:Parameter:
    ``use: <OnOff>``, specifies the use of UDP Source Port information

        * ``OFF = 0``
        * ``ON = 1``

    ``value: <integer>``, specifying the value of the UDP Source Port. Default value: 0

    ``mask: <string>``, specifying the filter mask for the value. Default value: 0xFFFF


:Example:
    .. code-block::

        # set
        input:  0/1 PEF_UDPSRCPORT [0] OFF 1 word
        output: <OK>

        # get
        input:  0/1 PEF_UDPSRCPORT [0] ?
        output: 0/1 PEF_UDPSRCPORT [0] OFF 1 word


``PEF_UDPDESTPORT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_UDPDESTPORT [<flow_xindex>] <use> <value> <mask>

    # get
    <module-index>/<port-index> PEF_UDPDESTPORT [<flow_xindex>] ?

:Description:
    Basic mode only. Defines UDP Destination Port settings used for the filter.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``.

:Actions:
    set, get

:Parameter:
    ``use: <OnOff>``, specifies the use of UDP Destination Port information

        * ``OFF = 0``
        * ``ON = 1``

    ``value: <integer>``, specifying the value of the UDP Destination Port. Default value: 0

    ``mask: <string>``, specifying the filter mask for the value. Default value: 0xFFFF


:Example:
    .. code-block::

        # set
        input:  0/1 PEF_UDPDESTPORT [0] OFF 1 word
        output: <OK>

        # get
        input:  0/1 PEF_UDPDESTPORT [0] ?
        output: 0/1 PEF_UDPDESTPORT [0] OFF 1 word


``PEF_TCPSETTINGS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_TCPSETTINGS [<flow_xindex>] <use> <action>

    # get
    <module-index>/<port-index> PEF_TCPSETTINGS [<flow_xindex>] ?

:Description:
    Basic mode only. Defines if filtering on TCP information is used for flow
    filtering.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``.

:Actions:
    set, get

:Parameter:
    ``use: <FilterUse>``, specifies the use of TCP information.

        * ``OFF = 0``
        * ``AND = 1``

    ``action: <InfoAction>``, specifies the action of TCP information.

        * ``EXCLUDE = 0``
        * ``INCLUDE = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PEF_TCPSETTINGS [0] OFF EXCLUDE
        output: <OK>

        # get
        input:  0/1 PEF_TCPSETTINGS [0] ?
        output: 0/1 PEF_TCPSETTINGS [0] OFF EXCLUDE


``PEF_TCPSRCPORT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_TCPSRCPORT [<flow_xindex>] <use> <value> <mask>

    # get
    <module-index>/<port-index> PEF_TCPSRCPORT [<flow_xindex>] ?

:Description:
    Basic mode only. Defines TCP Source Port settings used for the filter.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``.

:Actions:
    set, get

:Parameter:
    ``use: <OnOff>``, specifies the use of TCP Source Port information

        * ``OFF = 0``
        * ``ON = 1``

    ``value: <integer>``, specifies the value of the TCP Source Port. Default value: 0

    ``mask: <string>``, specifies the filter mask for the value. Default value: 0xFFFF


:Example:
    .. code-block::

        # set
        input:  0/1 PEF_TCPSRCPORT [0] OFF 1 word
        output: <OK>

        # get
        input:  0/1 PEF_TCPSRCPORT [0] ?
        output: 0/1 PEF_TCPSRCPORT [0] OFF 1 word


``PEF_TCPDESTPORT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_TCPDESTPORT [<flow_xindex>] <use> <value> <mask>

    # get
    <module-index>/<port-index> PEF_TCPDESTPORT [<flow_xindex>] ?

:Description:
    Basic mode only. Defines TCP Destination Port settings used for the filter.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``.

:Actions:
    set, get

:Parameter:
    ``use: <OnOff>``, specifies the use of TCP Destination Port information

        * ``OFF = 0``
        * ``ON = 1``

    ``value: <integer>``, specifies the value of the TCP Destination Port. Default value: 0

    ``mask: <string>``, specifies the filter mask for the value. Default value: 0xFFFF


:Example:
    .. code-block::

        # set
        input:  0/1 PEF_TCPDESTPORT [0] OFF 1 word
        output: <OK>

        # get
        input:  0/1 PEF_TCPDESTPORT [0] ?
        output: 0/1 PEF_TCPDESTPORT [0] OFF 1 word


``PEF_ANYSETTINGS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_ANYSETTINGS [<flow_xindex>] <use> <action>

    # get
    <module-index>/<port-index> PEF_ANYSETTINGS [<flow_xindex>] ?

:Description:
    Basic mode only. Defines if filtering on ANY field in a packet is used for flow filtering.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``.

:Actions:
    set, get

:Parameter:
    ``use: <FilterUse>``, specifies the use of ANY field information.

        * ``OFF = 0``
        * ``AND = 1``

    ``action: <InfoAction>``, specifies the action of ANY field information.

        * ``EXCLUDE = 0``
        * ``INCLUDE = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PEF_ANYSETTINGS [0] OFF EXCLUDE
        output: <OK>

        # get
        input:  0/1 PEF_ANYSETTINGS [0] ?
        output: 0/1 PEF_ANYSETTINGS [0] OFF EXCLUDE


``PEF_ANYCONFIG``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_ANYCONFIG [<flow_xindex>] <position> <value> <mask>

    # get
    <module-index>/<port-index> PEF_ANYCONFIG [<flow_xindex>] ?

:Description:
    Basic mode only. Defines the ANY field filter configuration. The "ANY field"
    filter will match 6 consecutive bytes in the incoming packets at a programmable
    offset. Applying a mask, allows to only filter based on selected bits within the
    6 bytes.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``.

:Actions:
    set, get

:Parameter:
    ``position: <integer>``, specifies the start position of the ANY field. Default value: 0, Range:0-127

    ``value: <string>``, specifying the six bytes of the field. Default value: 0x000000000000

    ``mask: <string>``, specifying the six bytes of the field. Default value: 0xFFFFFFFFFFFF


:Example:
    .. code-block::

        # set
        input:  0/1 PEF_ANYCONFIG [0] 1 word word
        output: <OK>

        # get
        input:  0/1 PEF_ANYCONFIG [0] ?
        output: 0/1 PEF_ANYCONFIG [0] 1 word word


``PEF_TPLDSETTINGS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_TPLDSETTINGS [<flow_xindex>] <use> <action>

    # get
    <module-index>/<port-index> PEF_TPLDSETTINGS [<flow_xindex>] ?

:Description:
    Defines if filtering on TPLD field in a packet is used for flow filtering. The
    TPLD filter allows filtering based on the Xena Testpayload ID. The Testpayload
    ID is meta data, which can be inserted into the Ethernet packets by Xena traffic
    generators. For each flow filter, can the filter be based on 16 TPLD ID values.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``.

:Actions:
    set, get

:Parameter:
    ``use: <FilterUse>``, specifies the use of TPLD information.

        * ``OFF = 0``
        * ``AND = 1``

    ``action: <InfoAction>``, specifies the action of TPLD information.

        * ``EXCLUDE = 0``
        * ``INCLUDE = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PEF_TPLDSETTINGS [0] OFF EXCLUDE
        output: <OK>

        # get
        input:  0/1 PEF_TPLDSETTINGS [0] ?
        output: 0/1 PEF_TPLDSETTINGS [0] OFF EXCLUDE


``PEF_TPLDCONFIG``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_TPLDCONFIG [<flow_xindex>] <use> <id>

    # get
    <module-index>/<port-index> PEF_TPLDCONFIG [<flow_xindex>] ?

:Description:
    Defines the TPLD filter configuration. There are only 16 TPLD filter, thus the index values are from 0 to 15.

    .. note::

        For SET, the only allowed ``filter_type`` is ``shadow-copy``.

:Actions:
    set, get

:Parameter:
    ``use: <OnOff>``, specifies the use of TPLD field information

        * ``OFF = 0``
        * ``ON = 1``
        
    ``id: <integer>``, specifies the TPLD ID. Range: 0-2015, Default value: 0


:Example:
    .. code-block::

        # set
        input:  0/1 PEF_TPLDCONFIG [0] OFF 1
        output: <OK>

        # get
        input:  0/1 PEF_TPLDCONFIG [0] ?
        output: 0/1 PEF_TPLDCONFIG [0] OFF 1


``PEF_VALUE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_VALUE [<flow_xindex>] <pid> <value>

    # get
    <module-index>/<port-index> PEF_VALUE [<flow_xindex>] ?

:Description:
    Extended mode only. Defines the byte values that can be matched if selected by :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_MASK`.

    If segment_index is zero, the maximum number of match value
    bytes that can be set is determined by the total length of the segments
    specified with :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_PROTOCOL`.
    E.g. if :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_PROTOCOL` is set to ETHERNET then only
    12 bytes can be set. In order to set the full 128 bytes, either specify a
    detailed segment list, or use the raw segment type. This specifies 12 + 116 = 128 bytes.

    If segment_index is non-zero, only the bytes covered by that segment are manipulated, so if :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_PROTOCOL` is set to ``ETHERNET VLAN ETHERTYPE eCPRI``, then segment_index = 4 selects the 8
    bytes of the eCPRI header starting at byte position (12 + 2 + 4) = 18. For ``set``
    commands where fewer value bytes are provided than specified by the protocol
    segment, those unspecified bytes are set to zero. The ``get`` commands always returns
    the number of bytes specified by the segment.

:Actions:
    set, get

:Parameter:
    ``pid: <integer>``, pid

    ``value: <string>``, the raw bytes comprising the packet header


:Example:
    .. code-block::

        # set
        input:  0/1 PEF_VALUE [0] 1 word
        output: <OK>

        # get
        input:  0/1 PEF_VALUE [0] ?
        output: 0/1 PEF_VALUE [0] 1 word


``PEF_MASK``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_MASK [<flow_xindex>] <masks>

    # get
    <module-index>/<port-index> PEF_MASK [<flow_xindex>] ?

:Description:
    Extended mode only. Defines the mask byte values that select the values specified by :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_VALUE`. For a chosen ``segment_index`` the first byte in the value masks the
    first byte of the corresponding :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_VALUE`, and so on.

    ``get/set`` semantics are similar to :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_VALUE`.

:Actions:
    set, get

:Parameter:
    ``masks: <string>``, mask byte values


:Example:
    .. code-block::

        # set
        input:  0/1 PEF_MASK [0] word
        output: <OK>

        # get
        input:  0/1 PEF_MASK [0] ?
        output: 0/1 PEF_MASK [0] word


``PEF_PROTOCOL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_PROTOCOL [<flow_xindex>] <segment_list>

    # get
    <module-index>/<port-index> PEF_PROTOCOL [<flow_xindex>] ?

:Description:
    Extended mode only. Defines the sequence of protocol segments that can be
    matched. The total length of the specified segments cannot exceed 128 bytes. If
    an existing sequence of segments is changed (using PEF_PROTOCOL) the underlying
    value and mask bytes remain unchanged, even though the semantics of those bytes
    may have changed. However, if the total length, in bytes, of the segments is
    reduced, then the excess bytes of value and mask are set to zero. I.e. to update
    an existing filter, you must first correct the list of segments (using
    PEF_PROTOCOL) and subsequently update the filtering value (using :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_VALUE`) and filtering mask (:class:`~xoa_driver.internals.core.commands.pef_commands.PEF_MASK`).

:Actions:
    set, get

:Parameter:
    ``segment_list: <List[ProtocolOption]>``, specifying the list of protocol segment types in the order they are expected in a frame. First segment type must be ``ETHERNET``; the following can be chosen freely.


:Example:
    .. code-block::

        # set
        input:  0/1 PEF_PROTOCOL [0] 0 1 2
        output: <OK>

        # get
        input:  0/1 PEF_PROTOCOL [0] ?
        output: 0/1 PEF_PROTOCOL [0] 0 1 2


``PEF_MODE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEF_MODE [<flow_xindex>] <mode>

    # get
    <module-index>/<port-index> PEF_MODE [<flow_xindex>] ?

:Description:
    Control the filter mode.

:Actions:
    set, get

:Parameter:
    ``mode: <FilterMode>``, the mode of the filter.

        * ``BASIC = 0``
        * ``EXTENDED = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PEF_MODE [0] BASIC
        output: <OK>

        # get
        input:  0/1 PEF_MODE [0] ?
        output: 0/1 PEF_MODE [0] BASIC



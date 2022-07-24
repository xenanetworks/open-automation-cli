Impairment Flow Commands
--------------------------

``PE_FCSDROP``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PE_FCSDROP <on_off>

    # get
    <module-index>/<port-index> PE_FCSDROP ?

:Description:
    The action on packets with FCS errors on a port.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, whether the action on packets with FCS errors on a port is enabled

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PE_FCSDROP OFF
        output: <OK>

        # get
        input:  0/1 PE_FCSDROP ?
        output: 0/1 PE_FCSDROP OFF


``PE_TPLDMODE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PE_TPLDMODE <mode>

    # get
    <module-index>/<port-index> PE_TPLDMODE ?

:Description:
    The action indicates the TPLD mode to be used per port.

:Actions:
    set, get

:Parameter:
    ``mode: <TPLDMode>``, indicating the TPLD mode

        * ``NORMAL = 0``
        * ``MICRO = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PE_TPLDMODE NORMAL
        output: <OK>

        # get
        input:  0/1 PE_TPLDMODE ?
        output: 0/1 PE_TPLDMODE NORMAL


``PE_COMMENT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PE_COMMENT [<flow_xindex>] <comment>

    # get
    <module-index>/<port-index> PE_COMMENT [<flow_xindex>] ?

:Description:
    Flow description.

:Actions:
    set, get

:Parameter:
    ``comment: <string>``, the description of the flow


:Example:
    .. code-block::

        # set
        input:  0/1 PE_COMMENT [0] word
        output: <OK>

        # get
        input:  0/1 PE_COMMENT [0] ?
        output: 0/1 PE_COMMENT [0] word


``PE_INDICES``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PE_INDICES ?

:Description:
    Get the flow indices. Currently the number of flows is 8.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PE_INDICES ?
        output: 0/1 PE_INDICES


``PE_LATENCYRANGE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PE_LATENCYRANGE [<flow_xindex>] ?

:Description:
    Retrieve minimum and maximum configurable latency per flow in nanoseconds.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PE_LATENCYRANGE [0] ?
        output: 0/1 PE_LATENCYRANGE [0]


``PE_CORRUPT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PE_CORRUPT [<flow_xindex>] <corruption_type>

    # get
    <module-index>/<port-index> PE_CORRUPT [<flow_xindex>] ?

:Description:
    Configures impairment corruption type.
    
    .. note::
        
        IP / TCP / UDP corruption modes are not supported on default flow (0)

:Actions:
    set, get

:Parameter:
    ``corruption_type: <CorruptionType>``, corruption type

        * ``OFF = 0``
        * ``ETH = 1``
        * ``IP = 2``
        * ``UDP = 3``
        * ``TCP = 4``
        * ``BER = 5``

:Example:
    .. code-block::

        # set
        input:  0/1 PE_CORRUPT [0] OFF
        output: <OK>

        # get
        input:  0/1 PE_CORRUPT [0] ?
        output: 0/1 PE_CORRUPT [0] OFF


``PE_MISORDER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PE_MISORDER [<flow_xindex>] <depth>

    # get
    <module-index>/<port-index> PE_MISORDER [<flow_xindex>] ?

:Description:
    Configures the misordering depth in number of packets.
    
    .. note::
        probability [see :class:`~xoa_driver.internals.core.commands.ped_commands.PED_FIXED`] * (depth + 1) should be less than 1,000,000.

:Actions:
    set, get

:Parameter:
    ``depth: <integer>``, the misordering depth (Range 1 - 32). Default value.


:Example:
    .. code-block::

        # set
        input:  0/1 PE_MISORDER [0] 1
        output: <OK>

        # get
        input:  0/1 PE_MISORDER [0] ?
        output: 0/1 PE_MISORDER [0] 1


``PE_BANDPOLICER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PE_BANDPOLICER [<flow_xindex>] <on_off> <mode> <cir> <cbs>

    # get
    <module-index>/<port-index> PE_BANDPOLICER [<flow_xindex>] ?

:Description:
    Configures the bandwidth policer.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, enables/disables policer. Note: PED_ENABLE is not supported for the policer.

        * ``OFF = 0``
        * ``ON = 1``

    ``mode: <PolicerMode>``, policer mode

        * ``L1 = 0``
        * ``L2 = 1``

    ``cir: <integer>``, policer committed information rate in units of 100 kbps (range 0 to 1000000), default is 0.

    ``cbs: <integer>``, policer committed burst burst in bytes (range 0 to 4194304), default is 0.


:Example:
    .. code-block::

        # set
        input:  0/1 PE_BANDPOLICER [0] OFF L1 1 1
        output: <OK>

        # get
        input:  0/1 PE_BANDPOLICER [0] ?
        output: 0/1 PE_BANDPOLICER [0] OFF L1 1 1


``PE_BANDSHAPER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PE_BANDSHAPER [<flow_xindex>] <on_off> <mode> <cir> <cbs> <buffer_size>

    # get
    <module-index>/<port-index> PE_BANDSHAPER [<flow_xindex>] ?

:Description:
    Configures the bandwidth shaper. L1 (0) (Shaper performed at Layer 1 level. I.e. including
    the preamble and min interpacket gap) L2 (1) (Shaper performed at Layer 2 level. I.e. excluding the preamble and min interpacket gap) Default value: L2 (0)

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, enables/disables shaper

        * ``OFF = 0``
        * ``ON = 1``

    ``mode: <PolicerMode>``, shaper mode

        * ``L1 = 0``
        * ``L2 = 1``
        
    ``cir: <integer>``, shaper committed information rate in units of 100 kbps (range 0 to 1000000), default is 0.

    ``cbs: <integer>``, shaper committed burst size in bytes (range 0 to 4194304), default is 0.

    ``buffer_size: <integer>``, shaper buffer size in bytes (range 0 to 2097152), default is 0.


:Example:
    .. code-block::

        # set
        input:  0/1 PE_BANDSHAPER [0] OFF L1 1 1 1
        output: <OK>

        # get
        input:  0/1 PE_BANDSHAPER [0] ?
        output: 0/1 PE_BANDSHAPER [0] OFF L1 1 1 1


``PE_DROPTOTAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PE_DROPTOTAL ?

:Description:
    Obtains statistics concerning all the packets dropped between this receive port and its partner TX port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PE_DROPTOTAL ?
        output: 0/1 PE_DROPTOTAL


``PE_LATENCYTOTAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PE_LATENCYTOTAL ?

:Description:
    Obtains statistics concerning all the packets delayed this receive port and its partner TX port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PE_LATENCYTOTAL ?
        output: 0/1 PE_LATENCYTOTAL


``PE_DUPTOTAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PE_DUPTOTAL ?

:Description:
    Obtains statistics concerning all the packets duplicated between this receive port and its partner TX port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PE_DUPTOTAL ?
        output: 0/1 PE_DUPTOTAL


``PE_MISTOTAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PE_MISTOTAL ?

:Description:
    Obtains statistics concerning all the packets mis-ordered between this receive
    port and its partner TX port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PE_MISTOTAL ?
        output: 0/1 PE_MISTOTAL


``PE_CORTOTAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PE_CORTOTAL ?

:Description:
    Obtains statistics concerning all the packets corrupted on between this receive port and its partner TX port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PE_CORTOTAL ?
        output: 0/1 PE_CORTOTAL


``PE_JITTERTOTAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PE_JITTERTOTAL ?

:Description:
    Obtains statistics concerning all the packets jittered between this receive port
    and its partner TX port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PE_JITTERTOTAL ?
        output: 0/1 PE_JITTERTOTAL


``PE_CLEAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PE_CLEAR


:Description:
    Clear all the impairment (duplicate, drop, mis-ordered, corrupted, latency and
    jitter) statistics for a Chimera port and flows on the port. The byte and packet
    counts will restart at zero.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PE_CLEAR
        output: <OK>



``PE_FLOWDROPTOTAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PE_FLOWDROPTOTAL [<flow_xindex>] ?

:Description:
    Obtains statistics concerning all the packets dropped in a flow between this receive port and its partner TX port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PE_FLOWDROPTOTAL [0] ?
        output: 0/1 PE_FLOWDROPTOTAL [0]


``PE_FLOWLATENCYTOTAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PE_FLOWLATENCYTOTAL [<flow_xindex>] ?

:Description:
    Obtains statistics concerning all the packets delayed between this receive port and its partner TX port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PE_FLOWLATENCYTOTAL [0] ?
        output: 0/1 PE_FLOWLATENCYTOTAL [0]


``PE_FLOWDUPTOTAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PE_FLOWDUPTOTAL [<flow_xindex>] ?

:Description:
    Obtains statistics concerning all the packets duplicated in a flow between this receive port and its partner TX port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PE_FLOWDUPTOTAL [0] ?
        output: 0/1 PE_FLOWDUPTOTAL [0]


``PE_FLOWMISTOTAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PE_FLOWMISTOTAL [<flow_xindex>] ?

:Description:
    Obtains statistics concerning all the packets mis-ordered in a flow between this receive port and its partner TX port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PE_FLOWMISTOTAL [0] ?
        output: 0/1 PE_FLOWMISTOTAL [0]


``PE_FLOWCORTOTAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PE_FLOWCORTOTAL [<flow_xindex>] ?

:Description:
    Obtains statistics concerning all the packets corrupted in a flow between this receive port and its partner TX port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PE_FLOWCORTOTAL [0] ?
        output: 0/1 PE_FLOWCORTOTAL [0]


``PE_FLOWJITTERTOTAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PE_FLOWJITTERTOTAL [<flow_xindex>] ?

:Description:
    Obtains statistics concerning all the packets jittered in a flow between this receive port and its partner TX port.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PE_FLOWJITTERTOTAL [0] ?
        output: 0/1 PE_FLOWJITTERTOTAL [0]


``PE_FLOWCLEAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PE_FLOWCLEAR [<flow_xindex>]


:Description:
    Clear all the impairment (duplicate, drop, mis-ordered, corrupted, latency and
    jitter) statistics on a particular flow on the port. The byte and packet counts
    will restart at zero.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PE_FLOWCLEAR [0]
        output: <OK>




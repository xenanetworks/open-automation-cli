Module Commands
---------------------

``M_RESERVATION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M_RESERVATION <operation>

    # get
    <module-index> M_RESERVATION ?

:Description:
    Set this command to reserve, release, or relinquish a module itself (as
    opposed to its ports). The module must be reserved before its hardware image can
    be upgraded. The owner of the session must already have been specified.
    Reservation will fail if the chassis or any ports are reserved for other users.

    .. note::

        The reservation parameters are slightly asymmetric with respect to set/get. When querying for the current reservation state, the chassis will use these values.

:Actions:
    set, get

:Parameter:
    ``operation: <ReservedAction>``, reservation operation to perform

        * ``RELEASE = 0``
        * ``RESERVE = 1``
        * ``RELINQUISH = 2``

:Example:
    .. code-block::

        # set
        input:  0 M_RESERVATION RELEASE
        output: <OK>

        # get
        input:  0 M_RESERVATION ?
        output: 0 M_RESERVATION RELEASE


``M_RESERVEDBY``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M_RESERVEDBY ?

:Description:
    Identify the user who has a module reserved. Returns an empty string if the
    module is not currently reserved by anyone.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M_RESERVEDBY ?
        output: 0 M_RESERVEDBY


``M_MODEL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M_MODEL ?

:Description:
    Gets the legacy model P/N name of a Xena test module.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M_MODEL ?
        output: 0 M_MODEL


``M_SERIALNO``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M_SERIALNO ?

:Description:
    Gets the unique serial number of a module.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M_SERIALNO ?
        output: 0 M_SERIALNO


``M_VERSIONNO``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M_VERSIONNO ?

:Description:
    Gets the version number of the hardware image installed on a module.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M_VERSIONNO ?
        output: 0 M_VERSIONNO


``M_STATUS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M_STATUS ?

:Description:
    Get status readings for the test module itself.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M_STATUS ?
        output: 0 M_STATUS


``M_PORTCOUNT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M_PORTCOUNT ?

:Description:
    Gets the maximum number of ports on a module.

    .. note::

        For a CFP-type module this number refers to the maximum number of ports possible on the module regardless of the media configuration. So if a CFP-type module can be set in for instance either 1x100G mode or 8x10G mode then this command will always return 8. If you want the current number of ports for a CFP-type module you need to read the :class:`~xoa_driver.internals.core.commands.m_commands.M_CFPCONFIG` command which returns the number of current ports.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M_PORTCOUNT ?
        output: 0 M_PORTCOUNT


``M_UPGRADE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M_UPGRADE <image_name>


:Description:
    Transfers a hardware image file from the chassis to a module. This image will
    take effect when the chassis is powered-on the next time. The transfer takes
    approximately 3 minutes, but no further action is required by the client.

:Actions:
    set

:Parameter:
    ``image_name: <string>``, the fully qualified name of a file previously uploaded to the chassis


:Example:
    .. code-block::

        # set
        input:  0 M_UPGRADE word
        output: <OK>



``M_UPGRADEPROGRESS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M_UPGRADEPROGRESS ?

:Description:
    Provides a value indicating the current stage of an ongoing hardware image
    upgrade operation. This is for information only; the upgrade operation runs to
    completion by itself. The progress values are pushed to the client without it
    having to request them.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M_UPGRADEPROGRESS ?
        output: 0 M_UPGRADEPROGRESS


``M_TIMESYNC``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M_TIMESYNC <mode>

    # get
    <module-index> M_TIMESYNC ?

:Description:
    Control how the test module timestamp clock is running, either freely in the
    chassis or locked to an external system time. Running with free chassis time
    allows nano-second precision measurements of latencies, but only when the
    transmitting and receiving ports are in the same chassis. Running with locked
    external time enables inter-chassis latency measurements, but can introduce
    small time discontinuities as the test module time is adjusted.

:Actions:
    set, get

:Parameter:
    ``mode: <TimeSyncMode>``, the time sync mode of the test module timestamp clock

        * ``CHASSIS = 0``
        * ``EXTERNAL = 1``
        * ``MODULE = 2``

:Example:
    .. code-block::

        # set
        input:  0 M_TIMESYNC CHASSIS
        output: <OK>

        # get
        input:  0 M_TIMESYNC ?
        output: 0 M_TIMESYNC CHASSIS


``M_CFPTYPE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M_CFPTYPE ?

:Description:
    Get information about the transceiver currently inserted into the cages.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M_CFPTYPE ?
        output: 0 M_CFPTYPE


``M_CFPCONFIG``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M_CFPCONFIG <port_count> <port_speed>

    # get
    <module-index> M_CFPCONFIG ?

:Description:
    The current number of ports and their speed of a CFP test module. If the CFP
    type is NOTFLEXIBLE then it reflects the transceiver currently in the CFP cage.
    If the CFP type is FLEXIBLE (or NOTPRESENT) then the configuration can be changed
    explicitly. The following combinations are possible: 4x10G, 8x10G, 1x40G, 2x40G,
    and 1x100G. (replaced by ``M_CFPCONFIGEXT``)

:Actions:
    set, get

:Parameter:
    ``port_count: <integer>``, number of ports

    ``port_speed: <integer>``, port speed, in Gbps


:Example:
    .. code-block::

        # set
        input:  0 M_CFPCONFIG 1 1
        output: <OK>

        # get
        input:  0 M_CFPCONFIG ?
        output: 0 M_CFPCONFIG 1 1


``M_COMMENT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M_COMMENT <comment>

    # get
    <module-index> M_COMMENT ?

:Description:
    Gets the user-defined description string of a module.

:Actions:
    set, get

:Parameter:
    ``comment: <string>``, the user-specified comment/description for the module


:Example:
    .. code-block::

        # set
        input:  0 M_COMMENT word
        output: <OK>

        # get
        input:  0 M_COMMENT ?
        output: 0 M_COMMENT word


``M_TIMEADJUSTMENT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M_TIMEADJUSTMENT <adjust>

    # get
    <module-index> M_TIMEADJUSTMENT ?

:Description:
    Control time adjustment for module wall clock.

:Actions:
    set, get

:Parameter:
    ``adjust: <integer>``, the time adjustment value for the module clock


:Example:
    .. code-block::

        # set
        input:  0 M_TIMEADJUSTMENT 1
        output: <OK>

        # get
        input:  0 M_TIMEADJUSTMENT ?
        output: 0 M_TIMEADJUSTMENT 1


``M_CAPABILITIES``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M_CAPABILITIES ?

:Description:
    Gets the module capabilities.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M_CAPABILITIES ?
        output: 0 M_CAPABILITIES


``M_MEDIASUPPORT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M_MEDIASUPPORT ?

:Description:
    This command shows the available speeds on a module. The structure of the returned value is
    [<cage_type> <available_speed_count> [<ports_per_speed> <speed>] ].
    [<ports_per_speed> <speed>] are repeated until all speeds supported by the <cage_type> has been listed.
    [<cage_type> <available_speed_count>] are repeated for all cage types on the module
    including the related <ports_per_speed> <speed> information.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M_MEDIASUPPORT ?
        output: 0 M_MEDIASUPPORT


``M_FPGAREIMAGE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M_FPGAREIMAGE


:Description:
    Reload FPGA image.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0 M_FPGAREIMAGE
        output: <OK>



``M_MULTIUSER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M_MULTIUSER <on_off>

    # get
    <module-index> M_MULTIUSER ?

:Description:
    Enable or disable multiple sessions to control the same module.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, Enable or disable multiple sessions to control the same module

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0 M_MULTIUSER OFF
        output: <OK>

        # get
        input:  0 M_MULTIUSER ?
        output: 0 M_MULTIUSER OFF


``M_CFPCONFIGEXT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M_CFPCONFIGEXT <port_count>

    # get
    <module-index> M_CFPCONFIGEXT ?

:Description:
    This property defines the current number of ports and the speed of each of them
    on a CFP test module. If the CFP type is NOTFLEXIBLE then it reflects the
    transceiver currently in the CFP cage. If the CFP type is FLEXIBLE(or
    NOTPRESENT) then the configuration can be changed explicitly. The following
    combinations are possible: 2x10G, 4x10G, 8x10G, 2x25G, 4x25G, 8x25G, 1x40G,
    2x40G, 2x50G, 4x50G, 8x50G, 1x100G, 2x100G, 4x100G, 2x200G, and 1x400G.
    (replaces M_CFPCONFIG)

:Actions:
    set, get

:Parameter:
    ``port_count: <integer list>``, port_count


:Example:
    .. code-block::

        # set
        input:  0 M_CFPCONFIGEXT 0 1
        output: <OK>

        # get
        input:  0 M_CFPCONFIGEXT ?
        output: 0 M_CFPCONFIGEXT 0 1


``M_CLOCKPPB``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M_CLOCKPPB <ppb>

    # get
    <module-index> M_CLOCKPPB ?

:Description:
    Makes small adjustments to the local clock of the test module, which drives the
    TX rate of the test ports.

:Actions:
    set, get

:Parameter:
    ``ppb: <integer>``, adjustment from nominal value, in parts-per-billion, positive or negative


:Example:
    .. code-block::

        # set
        input:  0 M_CLOCKPPB 1
        output: <OK>

        # get
        input:  0 M_CLOCKPPB ?
        output: 0 M_CLOCKPPB 1


``M_SMAINPUT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M_SMAINPUT <sma_in>

    # get
    <module-index> M_SMAINPUT ?

:Description:
    For test modules with SMA (SubMiniature version A) connectors, selects the function of the SMA input.

:Actions:
    set, get

:Parameter:
    ``sma_in: <SMAInputFunction>``, the function of the SMA (SubMiniature version A) input of the module

        * ``NOTUSED = 0``
        * ``TX2MHZ = 1``
        * ``TX10MHZ = 2``

:Example:
    .. code-block::

        # set
        input:  0 M_SMAINPUT NOTUSED
        output: <OK>

        # get
        input:  0 M_SMAINPUT ?
        output: 0 M_SMAINPUT NOTUSED


``M_SMAOUTPUT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M_SMAOUTPUT <sma_out>

    # get
    <module-index> M_SMAOUTPUT ?

:Description:
    For test modules with SMA (SubMiniature version A) connectors, selects the function of the SMA output.

:Actions:
    set, get

:Parameter:
    ``sma_out: <SMAOutputFunction>``, sma_out

        * ``DISABLED = 0``
        * ``PASSTHROUGH = 1``
        * ``P0SOF = 2``
        * ``P1SOF = 3``
        * ``REF2MHZ = 4``
        * ``REF10MHZ = 5``
        * ``REF125MHZ = 6``
        * ``REF156MHZ = 7``
        * ``P0RXCLK = 8``
        * ``P1RXCLK = 9``
        * ``P0RXCLK2MHZ = 10``
        * ``P1RXCLK2MHZ = 11``
        * ``TS_PPS = 12``

:Example:
    .. code-block::

        # set
        input:  0 M_SMAOUTPUT DISABLED
        output: <OK>

        # get
        input:  0 M_SMAOUTPUT ?
        output: 0 M_SMAOUTPUT DISABLED


``M_SMASTATUS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M_SMASTATUS ?

:Description:
    For test modules with SMA connectors, this returns the status of the SMA input.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M_SMASTATUS ?
        output: 0 M_SMASTATUS


``M_NAME``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M_NAME ?

:Description:
    Gets the name of a module.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M_NAME ?
        output: 0 M_NAME


``M_REVISION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M_REVISION ?

:Description:
    Gets the model P/N name of a Xena test module.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M_REVISION ?
        output: 0 M_REVISION


``M_MEDIA``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M_MEDIA <media_type>

    # get
    <module-index> M_MEDIA ?

:Description:
    For the test modules that support media configuration (check M_CAPABILITIES), this command sets the desired media
    type (front port).

:Actions:
    set, get

:Parameter:
    ``media_type: <MediaType>``, the media type of the test module

        * ``CFP4 = 0``
        * ``QSFP28 = 1``
        * ``CXP = 2``
        * ``SFP28 = 3``
        * ``QSFP56 = 4``
        * ``QSFP_DD = 5``
        * ``SFP56 = 6``
        * ``SFP_DD = 7``
        * ``QSFP_DD_NRZ = 9``
        * ``QSFP28_PAM4 = 10``
        * ``CFP = 99``
        * ``BASE_T1 = 100``
        * ``BASE_T1S = 101``

:Example:
    .. code-block::

        # set
        input:  0 M_MEDIA CFP4
        output: <OK>

        # get
        input:  0 M_MEDIA ?
        output: 0 M_MEDIA CFP4


``M_CLOCKSYNCSTATUS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M_CLOCKSYNCSTATUS ?

:Description:
    Get module's clock sync status.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M_CLOCKSYNCSTATUS ?
        output: 0 M_CLOCKSYNCSTATUS


``M_LICENSE_DEMO_INFO``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M_LICENSE_DEMO_INFO ?

:Description:
    Returns info about the demo status of the module. Only applicable to L47 test module.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M_LICENSE_DEMO_INFO ?
        output: 0 M_LICENSE_DEMO_INFO


``M_LICENSE_MAINTENANCE_INFO``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M_LICENSE_MAINTENANCE_INFO ?

:Description:
    Returns info about the maintenance license status for the module. Only applicable to L47 test module.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M_LICENSE_MAINTENANCE_INFO ?
        output: 0 M_LICENSE_MAINTENANCE_INFO


``M_LICENSE_CWB_DETECTED``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M_LICENSE_CWB_DETECTED ?

:Description:
    Returns if clock-windback is detected. If clock-windback has been detected the
    chassis is locked and no reservations of ports can be performed. To recover from
    clock-windback, set the system time correct (via the M4_SYSTEM_TIME command) and
    perform a license update (via the M_LICENSE_UPDATE command). Only applicable to L47 test module.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M_LICENSE_CWB_DETECTED ?
        output: 0 M_LICENSE_CWB_DETECTED


``M_LICENSE_UPDATE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M_LICENSE_UPDATE


:Description:
    This command instructs the chassis to update its local license information from
    FlexNet Operations. The chassis can be configured in on-line and off-line mode
    (by the M_LICENSE_ONLINE command). In on-line mode, the chassis sends a
    capability request to FlexNet Operations and receives a capability response. In
    offline mode a capability response (bin file) must be downloaded from FlexNet
    Operations and uploaded to the chassis. The capability response (bin file) is
    parsed and the license info is stored locally in trusted storage. A capability
    response (bin file) has a lifetime of one day (24 hours). The result of the
    license update operation can be retrieved by M_LICENSE_UPDATE_STATUS.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0 M_LICENSE_UPDATE
        output: <OK>



``M_LICENSE_UPDATE_STATUS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M_LICENSE_UPDATE_STATUS ?

:Description:
    Returns the status of the latest license update operations.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M_LICENSE_UPDATE_STATUS ?
        output: 0 M_LICENSE_UPDATE_STATUS


``M_LICENSE_LIST_BSON``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M_LICENSE_LIST_BSON ?

:Description:
    Returns a list of locally stored licenses - formatted as a BSON document.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M_LICENSE_LIST_BSON ?
        output: 0 M_LICENSE_LIST_BSON


``M_LICENSE_ONLINE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M_LICENSE_ONLINE <mode>

    # get
    <module-index> M_LICENSE_ONLINE ?

:Description:
    Configures the chassis in online or offline mode. The online mode configuration
    defines two different license update procedures as described for the
    M_LICENSE_UPDATE command. In online mode the license update procedure requires
    access to the Internet. In offline mode the license update procedure can be
    performed without access to the Internet.

:Actions:
    set, get

:Parameter:
    ``mode: <IsOnline>``, the current online/offline mode of the L47 tester

        * ``OFFLINE = 0``
        * ``ONLINE = 1``

:Example:
    .. code-block::

        # set
        input:  0 M_LICENSE_ONLINE OFFLINE
        output: <OK>

        # get
        input:  0 M_LICENSE_ONLINE ?
        output: 0 M_LICENSE_ONLINE OFFLINE


``M_TXCLOCKSOURCE_NEW``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M_TXCLOCKSOURCE_NEW <tx_clock>

    # get
    <module-index> M_TXCLOCKSOURCE_NEW ?

:Description:
    For test modules with advanced timing features, select what clock drives the port TX
    rates.

:Actions:
    set, get

:Parameter:
    ``tx_clock: <TXClockSource>``, the test module's TX clock source settings

        * ``MODULELOCALCLOCK = 0``
        * ``SMAINPUT = 1``
        * ``P0RXCLK = 2``
        * ``P1RXCLK = 3``
        * ``P2RXCLK = 4``
        * ``P3RXCLK = 5``
        * ``P4RXCLK = 6``
        * ``P5RXCLK = 7``
        * ``P6RXCLK = 8``
        * ``P7RXCLK = 9``

:Example:
    .. code-block::

        # set
        input:  0 M_TXCLOCKSOURCE_NEW MODULELOCALCLOCK
        output: <OK>

        # get
        input:  0 M_TXCLOCKSOURCE_NEW ?
        output: 0 M_TXCLOCKSOURCE_NEW MODULELOCALCLOCK


``M_TXCLOCKSTATUS_NEW``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M_TXCLOCKSTATUS_NEW ?

:Description:
    For test modules with advanced timing features, check whether a valid clock is
    present.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M_TXCLOCKSTATUS_NEW ?
        output: 0 M_TXCLOCKSTATUS_NEW


``M_TXCLOCKFILTER_NEW``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M_TXCLOCKFILTER_NEW <filter_bandwidth>

    # get
    <module-index> M_TXCLOCKFILTER_NEW ?

:Description:
    For test modules with advanced timing features, the loop bandwidth on the TX
    clock filter.

:Actions:
    set, get

:Parameter:
    ``filter_bandwidth: <LoopBandwidth>``, the setting of the loop bandwidth on the TX clock filter

        * ``BW103HZ = 1``
        * ``BW207HZ = 2``
        * ``BW416HZ = 3``
        * ``BW1683HZ = 4``
        * ``BW7019HZ = 5``

:Example:
    .. code-block::

        # set
        input:  0 M_TXCLOCKFILTER_NEW BW103HZ
        output: <OK>

        # get
        input:  0 M_TXCLOCKFILTER_NEW ?
        output: 0 M_TXCLOCKFILTER_NEW BW103HZ


``M_EMULBYPASS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M_EMULBYPASS <on_off>

    # get
    <module-index> M_EMULBYPASS ?

:Description:
    Set emulator bypass mode. Emulator bypass mode will bypass the entire emulator
    for minimum latency.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, the bypass mode of the impairment emulator.

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0 M_EMULBYPASS OFF
        output: <OK>

        # get
        input:  0 M_EMULBYPASS ?
        output: 0 M_EMULBYPASS OFF



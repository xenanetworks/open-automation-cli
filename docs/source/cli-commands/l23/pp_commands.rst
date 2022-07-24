High-Speed Port Commands
--------------------------

``PP_ALARMS_ERRORS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PP_ALARMS_ERRORS ?

:Description:
    Obtain the error count of each alarm, PCS Error, FEC Error, Header Error, Align
    Error, BIP Error, and High BER Error.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PP_ALARMS_ERRORS ?
        output: 0/1 PP_ALARMS_ERRORS


``PP_ALARMS_ERRORS_CLEAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_ALARMS_ERRORS_CLEAR <dummy>


:Description:
    Clear all PCS/PMA alarms.

:Actions:
    set

:Parameter:
    ``dummy: <integer>``, dummy


:Example:
    .. code-block::

        # set
        input:  0/1 PP_ALARMS_ERRORS_CLEAR 1
        output: <OK>



``PP_TXLANECONFIG``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_TXLANECONFIG [<lane_xindex>] <virt_lane_index> <skew>

    # get
    <module-index>/<port-index> PP_TXLANECONFIG [<lane_xindex>] ?

:Description:
    The virtual lane index and artificial skew for data transmitted on a specified
    physical lane.

:Actions:
    set, get

:Parameter:
    ``virt_lane_index: <integer>``, virtual lane index

    ``skew: <integer>``, the inserted skew on the lane, in bit units


:Example:
    .. code-block::

        # set
        input:  0/1 PP_TXLANECONFIG [0] 1 1
        output: <OK>

        # get
        input:  0/1 PP_TXLANECONFIG [0] ?
        output: 0/1 PP_TXLANECONFIG [0] 1 1


``PP_TXLANEINJECT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_TXLANEINJECT [<lane_xindex>] <inject_error_type>


:Description:
    Inject a particular kind of CAUI error into a specific physical lane.

:Actions:
    set

:Parameter:
    ``inject_error_type: <InjectErrorType>``, specifying what kind of error to inject

        * ``HEADERERROR = 1``
        * ``ALIGNERROR = 2``
        * ``BIP8ERROR = 3``

:Example:
    .. code-block::

        # set
        input:  0/1 PP_TXLANEINJECT [0] HEADERERROR
        output: <OK>



``PP_TXPRBSCONFIG``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_TXPRBSCONFIG [<serdes_xindex>] <prbs_seed> <prbs_on_off> <error_on_off>

    # get
    <module-index>/<port-index> PP_TXPRBSCONFIG [<serdes_xindex>] ?

:Description:
    The PRBS configuration for a particular SerDes. When PRBS is enabled for any SerDes
    then the overall link is compromised and drops out of sync.

:Actions:
    set, get

:Parameter:
    ``prbs_seed: <integer>``, not used, set to 0.

    ``prbs_on_off: <PRBSOnOff>``, whether this SerDes is transmitting PRBS data.

        * ``PRBSOFF = 0``
        * ``PRBSON = 1``
        
    ``error_on_off: <ErrorOnOff>``, whether bit-level errors are injected into this SerDes

        * ``ERRORSOFF = 0``
        * ``ERRORSON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PP_TXPRBSCONFIG [0] 1 PRBSOFF ERRORSOFF
        output: <OK>

        # get
        input:  0/1 PP_TXPRBSCONFIG [0] ?
        output: 0/1 PP_TXPRBSCONFIG [0] 1 PRBSOFF ERRORSOFF


``PP_TXERRORRATE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_TXERRORRATE <rate>

    # get
    <module-index>/<port-index> PP_TXERRORRATE ?

:Description:
    The rate of continuous bit-level error injection. Errors are injected evenly
    across the SerDes where injection is enabled.

:Actions:
    set, get

:Parameter:
    ``rate: <integer>``, the number of bits between each error. 0, no error injection


:Example:
    .. code-block::

        # set
        input:  0/1 PP_TXERRORRATE 1
        output: <OK>

        # get
        input:  0/1 PP_TXERRORRATE ?
        output: 0/1 PP_TXERRORRATE 1


``PP_TXINJECTONE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_TXINJECTONE


:Description:
    Inject a single bit-level error into the SerDes where injection has been enabled.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PP_TXINJECTONE
        output: <OK>



``PP_RXTOTALSTATS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PP_RXTOTALSTATS ?

:Description:
    Provides FEC Total counters.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PP_RXTOTALSTATS ?
        output: 0/1 PP_RXTOTALSTATS


``PP_RXFECSTATS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PP_RXFECSTATS ?

:Description:
    Provides statistics on how many FEC blocks have been seen with a given number of symbol errors.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PP_RXFECSTATS ?
        output: 0/1 PP_RXFECSTATS


``PP_LINKFLAP_PARAMS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_LINKFLAP_PARAMS <duration> <period> <repetition>

    # get
    <module-index>/<port-index> PP_LINKFLAP_PARAMS ?

:Description:
    Set port 'link flap' parameters. Notice: Period must be larger than duration.

:Actions:
    set, get

:Parameter:
    ``duration: <integer>``, 0 ms - 1000 ms; increments of 1 ms; 0 = permanently link down.

    ``period: <integer>``, 10 ms - 50000 ms; number of ms - must be multiple of 10 ms.

    ``repetition: <integer>``, 1 - 64K; 0 = continuous.


:Example:
    .. code-block::

        # set
        input:  0/1 PP_LINKFLAP_PARAMS 1 1 1
        output: <OK>

        # get
        input:  0/1 PP_LINKFLAP_PARAMS ?
        output: 0/1 PP_LINKFLAP_PARAMS 1 1 1


``PP_LINKFLAP_ENABLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_LINKFLAP_ENABLE <on_off>

    # get
    <module-index>/<port-index> PP_LINKFLAP_ENABLE ?

:Description:
    Enable / disable port 'link flap'.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, whether link flap is enabled

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PP_LINKFLAP_ENABLE OFF
        output: <OK>

        # get
        input:  0/1 PP_LINKFLAP_ENABLE ?
        output: 0/1 PP_LINKFLAP_ENABLE OFF


``PP_PMAERRPUL_PARAMS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_PMAERRPUL_PARAMS <duration> <period> <repetition> <coeff> <exp>

    # get
    <module-index>/<port-index> PP_PMAERRPUL_PARAMS ?

:Description:
    The 'PMA pulse error inject'.

    .. note::

        Period must be > duration. BER will be: coeff * 10exp

:Actions:
    set, get

:Parameter:
    ``duration: <integer>``, 0 ms - 5000m s; increments of 1 ms; 0 = constant BER

    ``period: <integer>``, 10 ms - 50000 ms; number of ms - must be multiple of 10 ms

    ``repetition: <integer>``, 1 - 64K; 0 = continuous

    ``coeff: <integer>``, (0.01 < coeff < 9.99) * 100

    ``exp: <integer>``, -3 < exp < -17


:Example:
    .. code-block::

        # set
        input:  0/1 PP_PMAERRPUL_PARAMS 1 1 1 1 1
        output: <OK>

        # get
        input:  0/1 PP_PMAERRPUL_PARAMS ?
        output: 0/1 PP_PMAERRPUL_PARAMS 1 1 1 1 1


``PP_RXLANELOCK``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PP_RXLANELOCK [<lane_xindex>] ?

:Description:
    Whether the receiver has achieved header lock and alignment lock on the data
    received on a specified physical lane.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PP_RXLANELOCK [0] ?
        output: 0/1 PP_RXLANELOCK [0]


``PP_RXLANESTATUS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PP_RXLANESTATUS [<lane_xindex>] ?

:Description:
    The virtual lane index and actual skew for data received on a specified physical
    lane. This is only meaningful when the lane is in header lock and alignment
    lock.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PP_RXLANESTATUS [0] ?
        output: 0/1 PP_RXLANESTATUS [0]


``PP_RXLANEERRORS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PP_RXLANEERRORS [<lane_xindex>] ?

:Description:
    Statistics about errors detected at the physical coding sub-layer on the data
    received on a specified physical lane.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PP_RXLANEERRORS [0] ?
        output: 0/1 PP_RXLANEERRORS [0]


``PP_RXPRBSSTATUS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PP_RXPRBSSTATUS [<serdes_xindex>] ?

:Description:
    Statistics about PRBS pattern detection on the data received on a specified
    SerDes.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PP_RXPRBSSTATUS [0] ?
        output: 0/1 PP_RXPRBSSTATUS [0]


``PP_RXCLEAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_RXCLEAR


:Description:
    Clear all the PCS/PMA receiver statistics for a port.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PP_RXCLEAR
        output: <OK>



``PP_RXLASERPOWER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PP_RXLASERPOWER ?

:Description:
    Reading of the optical power level of the received signal. There is one value
    for each laser/wavelength, and the number of these depends on the kind of CFP
    transceiver used. The list is empty if the CFP transceiver does not support
    optical power read-out.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PP_RXLASERPOWER ?
        output: 0/1 PP_RXLASERPOWER


``PP_TXLASERPOWER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PP_TXLASERPOWER ?

:Description:
    Reading of the optical power level of the transmission signal. There is one
    value for each laser/wavelength, and the number of these depends on the kind of
    CFP transceiver used. The list is empty if the CFP transceiver does not support
    optical power read-out.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PP_TXLASERPOWER ?
        output: 0/1 PP_TXLASERPOWER


``PP_PMAERRPUL_ENABLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_PMAERRPUL_ENABLE <on_off>

    # get
    <module-index>/<port-index> PP_PMAERRPUL_ENABLE ?

:Description:
    Enable / disable 'PMA pulse error inject'.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, whether PMA pulse error inject is enabled

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PP_PMAERRPUL_ENABLE OFF
        output: <OK>

        # get
        input:  0/1 PP_PMAERRPUL_ENABLE ?
        output: 0/1 PP_PMAERRPUL_ENABLE OFF


``PP_EYEMEASURE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_EYEMEASURE [<serdes_xindex>] <status> <dummy>

    # get
    <module-index>/<port-index> PP_EYEMEASURE [<serdes_xindex>] ?

:Description:
    Start/stop a new BER eye-measure on a 25G serdes. Use "get" to see the status of
    the data gathering process.

:Actions:
    set, get

:Parameter:
    ``status: <StartOrStop>``, status of the serdes

        * ``STOP = 0``
        * ``START = 1``

    ``dummy: <integer list>``, reserved for future expansion


:Example:
    .. code-block::

        # set
        input:  0/1 PP_EYEMEASURE [0] STOP 0 1
        output: <OK>

        # get
        input:  0/1 PP_EYEMEASURE [0] ?
        output: 0/1 PP_EYEMEASURE [0] STOP 0 1


``PP_EYERESOLUTION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_EYERESOLUTION [<serdes_xindex>] <x_resolution> <y_resolution>

    # get
    <module-index>/<port-index> PP_EYERESOLUTION [<serdes_xindex>] ?

:Description:
    Set or get the resolution used for the next BER eye-measurement.

:Actions:
    set, get

:Parameter:
    ``x_resolution: <integer>``, number of columns, must be between 9 and 65 and be in the form 2^n+1

    ``y_resolution: <integer>``, number of columns, must be between 7 and 255 and be in the form 2^n-1


:Example:
    .. code-block::

        # set
        input:  0/1 PP_EYERESOLUTION [0] 1 1
        output: <OK>

        # get
        input:  0/1 PP_EYERESOLUTION [0] ?
        output: 0/1 PP_EYERESOLUTION [0] 1 1


``PP_EYEREAD``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PP_EYEREAD [<serdes_xindex>, <olum_xindex>] ?

:Description:
    Read a single column of a measured BER eye on a 25G serdes. Every readout also
    returns the resolution (x,y) and the number of valid columns (used to facilitate
    reading out the eye while it is being measured).  Note that the columns of the
    eye-data will be measured in the order: xres-1, xres-2, xres-3, ... 0.  The
    values show the number of bit errors measured out of a total of 1M bits at each
    of the individual sampling points (x=timeaxis, y = 0/1 threshold).

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PP_EYEREAD [0, 0] ?
        output: 0/1 PP_EYEREAD [0, 0]


``PP_EYEINFO``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PP_EYEINFO [<serdes_xindex>] ?

:Description:
    Read out BER eye-measurement information such as the vertical and horizontal
    bathtub curve information on a 25G serdes. This must be called after "PP_EYEMEASURE"
    has run to return valid results.  Use "get" to see the status of the data
    gathering process.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PP_EYEINFO [0] ?
        output: 0/1 PP_EYEINFO [0]


``PP_PHYTXEQ``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_PHYTXEQ [<serdes_xindex>] <pre1>

    # get
    <module-index>/<port-index> PP_PHYTXEQ [<serdes_xindex>] ?

:Description:
    Control and monitor the equalizer settings of the on-board PHY in the
    transmission direction (towards the transceiver cage) on Thor and Loki modules.

:Actions:
    set, get

:Parameter:
    ``pre1: <integer list>``, preemphasis, (range: Module dependent), default = 0 (neutral)


:Example:
    .. code-block::

        # set
        input:  0/1 PP_PHYTXEQ [0] 0 1
        output: <OK>

        # get
        input:  0/1 PP_PHYTXEQ [0] ?
        output: 0/1 PP_PHYTXEQ [0] 0 1


``PP_PHYRETUNE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_PHYRETUNE [<serdes_xindex>] <dummy>


:Description:
    Trigger a new retuning of the receive equalizer on the PHY for one of the 25G
    serdes. Useful if e.g. a direct attached copper cable or loop transceiver does
    not go into sync after insertion. Note that the retuning will cause disruption
    of the traffic on all serdes.

:Actions:
    set

:Parameter:
    ``dummy: <integer>``, reserved for future improvements, always set to 1


:Example:
    .. code-block::

        # set
        input:  0/1 PP_PHYRETUNE [0] 1
        output: <OK>



``PP_PHYAUTOTUNE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_PHYAUTOTUNE [<serdes_xindex>] <on_off>

    # get
    <module-index>/<port-index> PP_PHYAUTOTUNE [<serdes_xindex>] ?

:Description:
    Enable or disable the automatic receiving of PHY retuning (see PP_PHYRETUNE), which
    is performed on the 25G interfaces as soon as a signal is detected by the
    transceiver. Useful if a bad signal causes the PHY to continuously retune or if
    for some other reason it is preferable to use manual retuning (PP_PHYRETUNE).

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, Enable/disable automatic receiving PHY retuning. Default is enabled

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PP_PHYAUTOTUNE [0] OFF
        output: <OK>

        # get
        input:  0/1 PP_PHYAUTOTUNE [0] ?
        output: 0/1 PP_PHYAUTOTUNE [0] OFF


``PP_EYEBER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PP_EYEBER [<serdes_xindex>] ?

:Description:
    Obtain BER estimations of an eye diagram.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PP_EYEBER [0] ?
        output: 0/1 PP_EYEBER [0]


``PP_PHYAUTONEG``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_PHYAUTONEG <fec_mode> <reserved_1> <reserved_2> <reserved_3> <reserved_4>

    # get
    <module-index>/<port-index> PP_PHYAUTONEG ?

:Description:
    Autonegotiation settings of the PHY.

:Actions:
    set, get

:Parameter:
    ``fec_mode: <OnOff>``, FEC mode ON or OFF

        * ``OFF = 0``
        * ``ON = 1``

    ``reserved_1: <integer>``, reserved for future use.

    ``reserved_2: <integer>``, reserved for future use.

    ``reserved_3: <integer>``, reserved for future use.

    ``reserved_4: <integer>``, reserved for future use.


:Example:
    .. code-block::

        # set
        input:  0/1 PP_PHYAUTONEG OFF 1 1 1 1
        output: <OK>

        # get
        input:  0/1 PP_PHYAUTONEG ?
        output: 0/1 PP_PHYAUTONEG OFF 1 1 1 1


``PP_TXPRBSTYPE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_TXPRBSTYPE <prbs_inserted_type> <prbs_pattern> <invert>

    # get
    <module-index>/<port-index> PP_TXPRBSTYPE ?

:Description:
    The TX PRBS type used when the interface is in PRBS mode.

:Actions:
    set, get

:Parameter:
    ``prbs_inserted_type: <PRBSInsertedType>``, PRBS inserted type

        * ``CAUI_VIRTUAL = 0``
        * ``PHY_LINE = 1``
        * ``PHY_HOST = 2``
        * ``TCVR = 3``

    ``prbs_pattern: <PRBSPattern>``, PRBS pattern

        * ``PRBS7 = 0``
        * ``PRBS9 = 1``
        * ``PRBS11 = 2``
        * ``PRBS15 = 3``
        * ``PRBS23 = 4``
        * ``PRBS31 = 5``

    ``invert: <PRBSInvertState>``, PRBS invert state

        * ``NON_INVERTED = 0``
        * ``INVERTED = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PP_TXPRBSTYPE CAUI_VIRTUAL PRBS7 NON_INVERTED
        output: <OK>

        # get
        input:  0/1 PP_TXPRBSTYPE ?
        output: 0/1 PP_TXPRBSTYPE CAUI_VIRTUAL PRBS7 NON_INVERTED


``PP_RXPRBSTYPE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_RXPRBSTYPE <prbs_inserted_type> <prbs_pattern> <invert> <statistics_mode>

    # get
    <module-index>/<port-index> PP_RXPRBSTYPE ?

:Description:
    The RX PRBS type used when the interface is in PRBS mode.

:Actions:
    set, get

:Parameter:
    ``prbs_inserted_type: <PRBSInsertedType>``, PRBS inserted type

        * ``CAUI_VIRTUAL = 0``
        * ``PHY_LINE = 1``
        * ``PHY_HOST = 2``
        * ``TCVR = 3``

    ``prbs_pattern: <PRBSPattern>``, PRBS pattern

        * ``PRBS7 = 0``
        * ``PRBS9 = 1``
        * ``PRBS11 = 2``
        * ``PRBS15 = 3``
        * ``PRBS23 = 4``
        * ``PRBS31 = 5``

    ``invert: <PRBSInvertState>``, PRBS invert state

        * ``NON_INVERTED = 0``
        * ``INVERTED = 1``

    ``statistics_mode: <PRBSStatisticsMode>``, PRBS statistics mode

        * ``ACCUMULATIVE = 0``
        * ``PERSECOND = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PP_RXPRBSTYPE CAUI_VIRTUAL PRBS7 NON_INVERTED ACCUMULATIVE
        output: <OK>

        # get
        input:  0/1 PP_RXPRBSTYPE ?
        output: 0/1 PP_RXPRBSTYPE CAUI_VIRTUAL PRBS7 NON_INVERTED ACCUMULATIVE


``PP_FECMODE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_FECMODE <mode>

    # get
    <module-index>/<port-index> PP_FECMODE ?

:Description:
    FEC mode for port that supports FEC.

:Actions:
    set, get

:Parameter:
    ``mode: <FECMode>``, FEC mode for port

        * ``OFF = 0``
        * ``ON = 1``
        * ``RS_FEC = 2``
        * ``FC_FEC = 3``
        * ``RS_FEC_KR = 4``
        * ``RS_FEC_KP = 5``

:Example:
    .. code-block::

        # set
        input:  0/1 PP_FECMODE OFF
        output: <OK>

        # get
        input:  0/1 PP_FECMODE ?
        output: 0/1 PP_FECMODE OFF


``PP_EYEDWELLBITS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_EYEDWELLBITS [<serdes_xindex>] <min_dwell_bit_count> <max_dwell_bit_count>

    # get
    <module-index>/<port-index> PP_EYEDWELLBITS [<serdes_xindex>] ?

:Description:
    Min and max dwell bits for an eye capture.

:Actions:
    set, get

:Parameter:
    ``min_dwell_bit_count: <integer>``, minimum dwell bits for an eye capture

    ``max_dwell_bit_count: <integer>``, maximum dwell bits for an eye capture


:Example:
    .. code-block::

        # set
        input:  0/1 PP_EYEDWELLBITS [0] 1 1
        output: <OK>

        # get
        input:  0/1 PP_EYEDWELLBITS [0] ?
        output: 0/1 PP_EYEDWELLBITS [0] 1 1


``PP_PHYSIGNALSTATUS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PP_PHYSIGNALSTATUS ?

:Description:
    Obtain the PHY signal status.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PP_PHYSIGNALSTATUS ?
        output: 0/1 PP_PHYSIGNALSTATUS


``PP_PRBSTYPE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_PRBSTYPE <prbs_inserted_type> <polynomial> <invert> <statistics_mode>

    # get
    <module-index>/<port-index> PP_PRBSTYPE ?

:Description:
    Defines the PRBS type used when the interface is in PRBS mode.

:Actions:
    set, get

:Parameter:
    ``prbs_inserted_type: <PRBSInsertedType>``, specifying where the PRBS is inserted

        * ``CAUI_VIRTUAL = 0``
        * ``PHY_LINE = 1``
        * ``PHY_HOST = 2``
        * ``TCVR = 3``

    ``polynomial: <PRBSPolynomial>``, specifying which PRBS that is used

        * ``PRBS7 = 0``
        * ``PRBS9 = 1``
        * ``PRBS11 = 2``
        * ``PRBS15 = 3``
        * ``PRBS23 = 4``
        * ``PRBS31 = 5``
        * ``PRBS58 = 6``
        * ``PRBS49 = 7``
        * ``PRBS10 = 8``
        * ``PRBS20 = 9``
        * ``PRBS13 = 10``

    ``invert: <PRBSInvertState>``, specifying if the PRBS is inverted

        * ``NON_INVERTED = 0``
        * ``INVERTED = 1``

    ``statistics_mode: <PRBSStatisticsMode>``, specifying PRBS statistics mode, accumulative or for last second

        * ``ACCUMULATIVE = 0``
        * ``PERSECOND = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PP_PRBSTYPE CAUI_VIRTUAL PRBS7 NON_INVERTED ACCUMULATIVE
        output: <OK>

        # get
        input:  0/1 PP_PRBSTYPE ?
        output: 0/1 PP_PRBSTYPE CAUI_VIRTUAL PRBS7 NON_INVERTED ACCUMULATIVE


``PP_PHYSETTINGS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_PHYSETTINGS <link_training_on_off> <precode_on_off> <graycode_on_off> <pam4_msb_lsb_swap>

    # get
    <module-index>/<port-index> PP_PHYSETTINGS ?

:Description:
    Get/Set low-level PHY settings.

:Actions:
    set, get

:Parameter:
    ``link_training_on_off: <OnOff>``, enabling/disabling link training

        * ``OFF = 0``
        * ``ON = 1``

    ``precode_on_off: <OnOffDefault>``, enabling/disabling link precode

        * ``OFF = 0``
        * ``ON = 1``
        * ``DEFAULT = 2``

    ``graycode_on_off: <OnOff>``, enabling/disabling link graycode.

        * ``OFF = 0``
        * ``ON = 1``

    ``pam4_msb_lsb_swap: <OnOff>``, enabling/disabling PAM4 MSB/LSB swap.

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PP_PHYSETTINGS OFF OFF OFF OFF
        output: <OK>

        # get
        input:  0/1 PP_PHYSETTINGS ?
        output: 0/1 PP_PHYSETTINGS OFF OFF OFF OFF


``PP_PHYRXEQ``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_PHYRXEQ [<serdes_xindex>] <auto> <ctle> <reserved>

    # get
    <module-index>/<port-index> PP_PHYRXEQ [<serdes_xindex>] ?

:Description:
    RX EQ parameters.

:Actions:
    set, get

:Parameter:
    ``auto: <integer>``, auto on or off

    ``ctle: <integer>``, Continuous Time Linear equalization

    ``reserved: <integer>``, reserved


:Example:
    .. code-block::

        # set
        input:  0/1 PP_PHYRXEQ [0] 1 1 1
        output: <OK>

        # get
        input:  0/1 PP_PHYRXEQ [0] ?
        output: 0/1 PP_PHYRXEQ [0] 1 1 1


``PP_AUTONEG``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_AUTONEG <mode> <tec_ability> <fec_capable> <fec_requested> <pause_mode>

    # get
    <module-index>/<port-index> PP_AUTONEG ?

:Description:
    Auto-negotiation settings of the PHY - for Thor-400G-7S-1P Thor-400G-7S-1P[b]
    and [c]

:Actions:
    set, get

:Parameter:
    ``mode: <AutoNegMode>``, auto neg mode

        * ``ANEG_OFF = 0``
        * ``ANEG_ON = 1``

    ``tec_ability: <AutoNegTecAbility>``, technical ability

        * ``DEFAULT_TECH_MODE = 0``
        * ``IEEE_10G_KR = 4``
        * ``IEEE_40G_CR4 = 16``
        * ``IEEE_100G_KR4 = 128``
        * ``IEEE_100G_CR4 = 256``
        * ``IEEE_25GBASE_CRS_KRS = 512``
        * ``IEEE_25GBASE_CR_KR = 1024``
        * ``IEEE_50GBASE_CR_KR = 8192``
        * ``IEEE_100GBASE_CR2_KR2 = 16384``
        * ``IEEE_200GBASE_CR4_KR4 = 32768``
        * ``EC_25GBASE_KR1 = 16777216``
        * ``EC_25GBASE_CR1 = 33554432``
        * ``EC_50GBASE_KR2 = 67108864``
        * ``EC_50GBASE_CR2 = 134217728``
        * ``EC_400GGBASE_KR8 = 268435456``
        * ``EC_50G_CR1_KR1 = 503``
        * ``BAM_50G_CR1_KR1 = 504``
        * ``BAM_50G_CR2_KR2 = 505``
        * ``BAM_100G_CR2_KR2 = 1002``
        * ``BAM_100G_CR4_KR4 = 1003``
        * ``BAM_200G_CR2_KR2 = 2002``
        * ``BAM_400G_CR8_KR8 = 4001``

    ``fec_capable: <AutoNegFECOption>``, FEC capable

        * ``DEFAULT_FEC = 0``
        * ``NO_FEC = 1``
        * ``FCFEC = 2``
        * ``RSFEC_CL91 = 4``
        * ``RS528 = 256``
        * ``RS544 = 512``
        * ``RS272 = 1024``

    ``fec_requested: <AutoNegFECOption>``, FEC requested

        * ``DEFAULT_FEC = 0``
        * ``NO_FEC = 1``
        * ``FCFEC = 2``
        * ``RSFEC_CL91 = 4``
        * ``RS528 = 256``
        * ``RS544 = 512``
        * ``RS272 = 1024``

    ``pause_mode: <PauseMode>``, pause mode

        * ``NO_PAUSE = 0``
        * ``SYM_PAUSE = 1``
        * ``ASYM_PAUSE = 2``

:Example:
    .. code-block::

        # set
        input:  0/1 PP_AUTONEG ANEG_OFF DEFAULT_TECH_MODE DEFAULT_FEC DEFAULT_FEC NO_PAUSE
        output: <OK>

        # get
        input:  0/1 PP_AUTONEG ?
        output: 0/1 PP_AUTONEG ANEG_OFF DEFAULT_TECH_MODE DEFAULT_FEC DEFAULT_FEC NO_PAUSE


``PP_AUTONEGSTATUS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PP_AUTONEGSTATUS ?

:Description:
    Status of auto-negotiation settings of the PHY - for Thor-400G-7S-1P[b] and [c]

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PP_AUTONEGSTATUS ?
        output: 0/1 PP_AUTONEGSTATUS


``PP_LINKTRAIN``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PP_LINKTRAIN <mode> <pam4_frame_size> <nrz_pam4_init_cond> <nrz_preset> <timeout_mode>

    # get
    <module-index>/<port-index> PP_LINKTRAIN ?

:Description:
    Link training settings - for Thor-400G-7S-1P rev.B. The PP_LINKTRAIN command is
    per port.

:Actions:
    set, get

:Parameter:
    ``mode: <LinkTrainingMode>``, link training mode

        * ``AUTO = 0``
        * ``FORCE_ENABLE = 1``

    ``pam4_frame_size: <PAM4FrameSize>``, PAM4 frame size

        * ``N16K_FRAME = 0``
        * ``N4K_FRAME = 1``

    ``nrz_pam4_init_cond: <LinkTrainingInitCondition>``, link training init condition

        * ``NO_INIT = 0``
        * ``INIT_ENABLED = 1``

    ``nrz_preset: <NRZPreset>``, NRZ preset

        * ``NRZ_NO_PRESET = 0``
        * ``NRZ_WITH_PRESET = 1``
        
    ``timeout_mode: <TimeoutMode>``, timeout mode

        * ``DEFAULT_TIMEOUT = 0``
        * ``TIMEOUT_DISABLED = 255``

:Example:
    .. code-block::

        # set
        input:  0/1 PP_LINKTRAIN AUTO N16K_FRAME NO_INIT NRZ_NO_PRESET DEFAULT_TIMEOUT
        output: <OK>

        # get
        input:  0/1 PP_LINKTRAIN ?
        output: 0/1 PP_LINKTRAIN AUTO N16K_FRAME NO_INIT NRZ_NO_PRESET DEFAULT_TIMEOUT


``PP_LINKTRAINSTATUS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PP_LINKTRAINSTATUS [<lane_xindex>] ?

:Description:
    Link training status - for Thor-400G-7S-1P rev.B. The PP_LINKTRAINSTATUS command
    is per lane.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PP_LINKTRAINSTATUS [0] ?
        output: 0/1 PP_LINKTRAINSTATUS [0]



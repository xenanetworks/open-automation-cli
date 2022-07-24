Impairment Distribution Commands
----------------------------------------

``PED_SCHEDULE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PED_SCHEDULE [<flow_xindex>, <impairment_type_xindex>] <duration> <period>

    # get
    <module-index>/<port-index> PED_SCHEDULE [<flow_xindex>, <impairment_type_xindex>] ?

:Description:
    Configure the impairment scheduler function.  The configuration of the scheduler
    depends on the kind of distribution to schedule:      (1) Burst distributions:
    "Fixed Burst" and "Accumulate and Burst".      (2) Non-Burst distributions: All
    others.  For burst distributions, the scheduler can be configured for "One-shot"
    operation or "Repeat Operation".  When running in "Repeat Operation" the "Repeat
    Period" must be configured. For non-burst distributions,  the scheduler can be
    configured operate in either "Continuous" or "Repeat Period" modes.  When
    running in "Repeat Period" configuration of "Duration" and "Repeat Period" is
    required.

:Actions:
    set, get

:Parameter:
    ``duration: <integer>``, specifies the "on" period. Units = multiples of 10 ms (range 1 to 65535), default is 1

    ``period: <integer>``, specifies the "total" period. Units = multiples of 10 ms (range 0 to 65535), default is 0


:Example:
    .. code-block::

        # set
        input:  0/1 PED_SCHEDULE [0, 0] 1 1
        output: <OK>

        # get
        input:  0/1 PED_SCHEDULE [0, 0] ?
        output: 0/1 PED_SCHEDULE [0, 0] 1 1


``PED_ONESHOTSTATUS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PED_ONESHOTSTATUS [<flow_xindex>, <impairment_type_xindex>] ?

:Description:
    Retrieves the one-shot completion status.
    
    .. note::
    
        The return value is only valid, if the configured distribution is either accumulate & burst (DELAY) or fixed burst (non-DELAY).

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PED_ONESHOTSTATUS [0, 0] ?
        output: 0/1 PED_ONESHOTSTATUS [0, 0]


``PED_OFF``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PED_OFF [<flow_xindex>, <impairment_type_xindex>]


:Description:
    Configure Impairments Distribution to OFF. Assigning a different distribution than OFF to an impairment
    will activate the impairment. To de-activate the impairment assign distribution OFF.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PED_OFF [0, 0]
        output: <OK>



``PED_FIXED``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PED_FIXED [<flow_xindex>, <impairment_type_xindex>] <probability>

    # get
    <module-index>/<port-index> PED_FIXED [<flow_xindex>, <impairment_type_xindex>] ?

:Description:
    Configuration of Fixed Rate distribution. This is predictable distribution with
    nearly equal distance between impairments, to match the configured probability.

    .. note::
    
        In case of misordering, a special limit applies, probability * (depth + 1) should be less than 1000000.

:Actions:
    set, get

:Parameter:
    ``probability: <integer>``, the fixed probability in ppm. Default value is 0.


:Example:
    .. code-block::

        # set
        input:  0/1 PED_FIXED [0, 0] 1
        output: <OK>

        # get
        input:  0/1 PED_FIXED [0, 0] ?
        output: 0/1 PED_FIXED [0, 0] 1


``PED_RANDOM``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PED_RANDOM [<flow_xindex>, <impairment_type_xindex>] <probability>

    # get
    <module-index>/<port-index> PED_RANDOM [<flow_xindex>, <impairment_type_xindex>] ?

:Description:
    Configuration of Random Rate distribution. Packets are impaired randomly based
    on a per packet probability. This way the impaired fraction of packets will be
    equal to the configured probability over time. Random probability in ppm (i.e. 1
    means 0.0001%)

:Actions:
    set, get

:Parameter:
    ``probability: <integer>``, specifies the random probability in ppm. Default value is 0.


:Example:
    .. code-block::

        # set
        input:  0/1 PED_RANDOM [0, 0] 1
        output: <OK>

        # get
        input:  0/1 PED_RANDOM [0, 0] ?
        output: 0/1 PED_RANDOM [0, 0] 1


``PED_BER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PED_BER [<flow_xindex>, <impairment_type_xindex>] <coef> <exp>

    # get
    <module-index>/<port-index> PED_BER [<flow_xindex>, <impairment_type_xindex>] ?

:Description:
    Configuration of Bit Error Rate distribution.

:Actions:
    set, get

:Parameter:
    ``coef: <integer>``, specifies the coefficient for BER. Default value: 1 (Range is 1 to 9).

    ``exp: <integer>``, specifies the exponent for BER. Default value: -10 (Range is -18 to -1).


:Example:
    .. code-block::

        # set
        input:  0/1 PED_BER [0, 0] 1 1
        output: <OK>

        # get
        input:  0/1 PED_BER [0, 0] ?
        output: 0/1 PED_BER [0, 0] 1 1


``PED_FIXEDBURST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PED_FIXEDBURST [<flow_xindex>, <impairment_type_xindex>] <burst_size>

    # get
    <module-index>/<port-index> PED_FIXEDBURST [<flow_xindex>, <impairment_type_xindex>] ?

:Description:
    Configuration of Fixed Burst distribution.
    
    .. note::
    
        In case of ``_impairment_type_xindex`` = ``MISO``, burstsize is fixed to 1.

:Actions:
    set, get

:Parameter:
    ``burst_size: <integer>``, specifies the burst size (Range 1 - 16383). Default value = 1.


:Example:
    .. code-block::

        # set
        input:  0/1 PED_FIXEDBURST [0, 0] 1
        output: <OK>

        # get
        input:  0/1 PED_FIXEDBURST [0, 0] ?
        output: 0/1 PED_FIXEDBURST [0, 0] 1


``PED_RANDOMBURST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PED_RANDOMBURST [<flow_xindex>, <impairment_type_xindex>] <minimum> <maximum> <probability>

    # get
    <module-index>/<port-index> PED_RANDOMBURST [<flow_xindex>, <impairment_type_xindex>] ?

:Description:
    Configuration of Random Burst distribution.

:Actions:
    set, get

:Parameter:
    ``minimum: <integer>``, specifies minimum burst size. Default value: 0 (Range 0 to 65535)

    ``maximum: <integer>``, specifies maximum burst size. Default value: 0 (Range 0 to 65535)

    ``probability: <integer>``, specifies the per packet probability of initiating a burst in ppm. Default value: 0.


:Example:
    .. code-block::

        # set
        input:  0/1 PED_RANDOMBURST [0, 0] 1 1 1
        output: <OK>

        # get
        input:  0/1 PED_RANDOMBURST [0, 0] ?
        output: 0/1 PED_RANDOMBURST [0, 0] 1 1 1


``PED_GE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PED_GE [<flow_xindex>, <impairment_type_xindex>] <goodprob> <goodtransprob> <badprob> <badtransprob>

    # get
    <module-index>/<port-index> PED_GE [<flow_xindex>, <impairment_type_xindex>] ?

:Description:
    Configuration of Gilbert-Elliot distribution.

:Actions:
    set, get

:Parameter:
    ``goodprob: <integer>``, specifies the good state probability in ppm. Default value: 0.

    ``goodtransprob: <integer>``, specifies the good state transition probability in ppm. Default value: 0.

    ``badprob: <integer>``, specifies the bad state probability in ppm. Default value: 0.

    ``badtransprob: <integer>``, specifies the bad state transition probability in ppm. Default value: 0.


:Example:
    .. code-block::

        # set
        input:  0/1 PED_GE [0, 0] 1 1 1 1
        output: <OK>

        # get
        input:  0/1 PED_GE [0, 0] ?
        output: 0/1 PED_GE [0, 0] 1 1 1 1


``PED_UNI``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PED_UNI [<flow_xindex>, <impairment_type_xindex>] <minimum> <maximum>

    # get
    <module-index>/<port-index> PED_UNI [<flow_xindex>, <impairment_type_xindex>] ?

:Description:
    Configuration of Uniform distribution.
    
    .. note::
    
        If minimum is less than minimum latency, value is set to minimum latency. If minimum is greater than maximum latency, value is set to maximum latency.

:Actions:
    set, get

:Parameter:
    ``minimum: <integer>``, in case of iid != DELAY, specifies the minimum no. of packets. Default value: 0 (Range 0 to 4194288). In case of iid = DELAY, specifies the minimum latency limit. Unit is nanosecond (must be multiples of 100 ns). Default value: minimum latency.

    ``maximum: <integer>``, in case of iid != DELAY, specifies the maximum no. of packets. Default value: 0 (Range 0 to 4194288). In case of iid = DELAY, specifies the maximum latency limit. Unit is nanosecond (must be multiples of 100 ns). Default value: minimum latency.


:Example:
    .. code-block::

        # set
        input:  0/1 PED_UNI [0, 0] 1 1
        output: <OK>

        # get
        input:  0/1 PED_UNI [0, 0] ?
        output: 0/1 PED_UNI [0, 0] 1 1


``PED_GAUSS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PED_GAUSS [<flow_xindex>, <impairment_type_xindex>] <mean> <std_deviation>

    # get
    <module-index>/<port-index> PED_GAUSS [<flow_xindex>, <impairment_type_xindex>] ?

:Description:
    Configuration of Gaussian distribution.
    
    .. note::
    
        In case of ``_impairment_type_xindex != DELAY``: (1) mean plus 3 times standard deviation should be less than or equal to max allowed (4194288). (2) mean should always be at least 3 times the standard deviation, this to ensure that the impairment distance is always positive.
        
        In case of ``_impairment_type_xindex = DELAY``: (1) mean plus 3 times standard deviation should be less than or equal to the maximum latency. (2) mean minus 3 times the standard deviation should be greater than or equal to minimum latency.

:Actions:
    set, get

:Parameter:
    ``mean: <integer>``, specifies the Gaussian mean.

    ``std_deviation: <integer>``, specifies the Gaussian standard deviation.


:Example:
    .. code-block::

        # set
        input:  0/1 PED_GAUSS [0, 0] 1 1
        output: <OK>

        # get
        input:  0/1 PED_GAUSS [0, 0] ?
        output: 0/1 PED_GAUSS [0, 0] 1 1


``PED_POISSON``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PED_POISSON [<flow_xindex>, <impairment_type_xindex>] <mean>

    # get
    <module-index>/<port-index> PED_POISSON [<flow_xindex>, <impairment_type_xindex>] ?

:Description:
    Configuration of "Poisson" distribution.
    
    .. note:: 
    
        Standard deviation is derived from mean, i.e., standard deviation = SQRT(mean).
        
        In case of ``_impairment_type_xindex != DELAY``, mean plus 3 times standard deviation should be less than or equal to max allowed (4194288).
        
        In case of ``_impairment_type_xindex = DELAY``, mean plus 3 times standard deviation should be less than or equal to the maximum latency.

:Actions:
    set, get

:Parameter:
    ``mean: <integer>``, specifies the Poisson mean value.


:Example:
    .. code-block::

        # set
        input:  0/1 PED_POISSON [0, 0] 1
        output: <OK>

        # get
        input:  0/1 PED_POISSON [0, 0] ?
        output: 0/1 PED_POISSON [0, 0] 1


``PED_GAMMA``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PED_GAMMA [<flow_xindex>, <impairment_type_xindex>] <shape> <scale>

    # get
    <module-index>/<port-index> PED_GAMMA [<flow_xindex>, <impairment_type_xindex>] ?

:Description:
    Configuration of Gamma distribution.
    
    .. note::
    
        Mean and Standard deviation are calculated from Shape and Scale parameters and validation is performed using those. standard deviation = [SQRT(shape * scale * scale)]mean = [shape * scale].
        
        In case of ``_impairment_type_xindex != DELAY``, (1) mean plus 4 times standard deviation should be less than or equal to max allowed(4194288). (2)shape and scale should be greater than or equal to 0.
        
        In case of ``_impairment_type_xindex = DELAY``, mean plus 4 times standard deviation should be less than or equal to the maximum latency.

:Actions:
    set, get

:Parameter:
    ``shape: <integer>``, specifies the shape. Units: none. Default value: 0.

    ``scale: <integer>``, specifies the Gamma function scaleparameter.


:Example:
    .. code-block::

        # set
        input:  0/1 PED_GAMMA [0, 0] 1 1
        output: <OK>

        # get
        input:  0/1 PED_GAMMA [0, 0] ?
        output: 0/1 PED_GAMMA [0, 0] 1 1


``PED_CUST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PED_CUST [<flow_xindex>, <impairment_type_xindex>] <cust_id>

    # get
    <module-index>/<port-index> PED_CUST [<flow_xindex>, <impairment_type_xindex>] ?

:Description:
    Associate a custom distribution to a flow and impairment type.
    
    .. note:: 
    
        Before associating a custom distribution, the below validation checks are applied.
        
        In case of ``_impairment_type_xindex != DELAY``, (1) Custom values should be less than or equal to max allowed (4194288). (2) Custom distribution bust contain 512 values. 
        
        In case of ``_impairment_type_xindex = DELAY``, (1) Custom values should be less than or equal to the maximum latency. (2) Custom values should be greater than or equal to minimum latency. (3) Custom distribution should contain 1024 values.

:Actions:
    set, get

:Parameter:
    ``cust_id: <integer>``, custom distribution identifier


:Example:
    .. code-block::

        # set
        input:  0/1 PED_CUST [0, 0] 1
        output: <OK>

        # get
        input:  0/1 PED_CUST [0, 0] ?
        output: 0/1 PED_CUST [0, 0] 1


``PED_CONST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PED_CONST [<flow_xindex>, <impairment_type_xindex>] <delay>

    # get
    <module-index>/<port-index> PED_CONST [<flow_xindex>, <impairment_type_xindex>] ?

:Description:
    Configuration of Constant Delay distribution (DELAY only). Unit is ns (must be
    multiples of 100ns). Default value: Minimum supported per speed and FEC mode.

    .. note::
    
        If the latency is less than minimum latency, value is set to minimum latency. If the latency is greater than maximum latency, value is set to maximum latency.

:Actions:
    set, get

:Parameter:
    ``delay: <integer>``, specifies the constant delay/latency time. Unit is nanosecond (must be multiples of 100 ns). Default value: Minimum supported per speed and FEC mode.


:Example:
    .. code-block::

        # set
        input:  0/1 PED_CONST [0, 0] 1
        output: <OK>

        # get
        input:  0/1 PED_CONST [0, 0] ?
        output: 0/1 PED_CONST [0, 0] 1


``PED_ACCBURST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PED_ACCBURST [<flow_xindex>, <impairment_type_xindex>] <delay>

    # get
    <module-index>/<port-index> PED_ACCBURST [<flow_xindex>, <impairment_type_xindex>] ?

:Description:
    Configuration of Accumulate & Burst distribution (DELAY only).
    
    .. note:: 
        
        If the delay is less than minimum latency, value is set to minimum latency. If the delay is greater than maximum latency, value is set to maximum latency.

:Actions:
    set, get

:Parameter:
    ``delay: <integer>``, specifies the burst delay time. Units = nanosecond (must multiples of 100 ns). Default value: minimum latency.


:Example:
    .. code-block::

        # set
        input:  0/1 PED_ACCBURST [0, 0] 1
        output: <OK>

        # get
        input:  0/1 PED_ACCBURST [0, 0] ?
        output: 0/1 PED_ACCBURST [0, 0] 1


``PED_STEP``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PED_STEP [<flow_xindex>, <impairment_type_xindex>] <low> <high>

    # get
    <module-index>/<port-index> PED_STEP [<flow_xindex>, <impairment_type_xindex>] ?

:Description:
    Configuration of Step distribution (DELAY only).
    
    .. note:: 
        
        If the low/high is less than minimum latency, value is set to minimum latency. If the low/high is greater than maximum latency, value is set to maximum latency.

:Actions:
    set, get

:Parameter:
    ``low: <integer>``, specifies the packet delay in the 'low' state of the step. Units = nanosecond (must be multiples of 100 ns).

    ``high: <integer>``, specifies the packet delay in the 'high' state of the step. Units = nanosecond (must be multiples of 100 ns).


:Example:
    .. code-block::

        # set
        input:  0/1 PED_STEP [0, 0] 1 1
        output: <OK>

        # get
        input:  0/1 PED_STEP [0, 0] ?
        output: 0/1 PED_STEP [0, 0] 1 1


``PED_ENABLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PED_ENABLE [<flow_xindex>, <impairment_type_xindex>] ?

:Description:
    Control whether impairment is enabled of disabled.
    
    .. note:: 
    
        This command is not applicable for :class:`~xoa_driver.internals.core.commands.pe_commands.PE_BANDPOLICER` and :class:`~xoa_driver.internals.core.commands.pe_commands.PE_BANDSHAPER` because they have a separate ``ON / OFF`` parameter.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PED_ENABLE [0, 0] ?
        output: 0/1 PED_ENABLE [0, 0]



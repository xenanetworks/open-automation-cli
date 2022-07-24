Histogram Commands
---------------------

``PD_INDICES``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PD_INDICES <histogram_indices>

    # get
    <module-index>/<port-index> PD_INDICES ?

:Description:
    Obtain or configure histogram indices for each of N histograms.

:Actions:
    set, get

:Parameter:
    ``histogram_indices: <indices>``, histogram indices


:Example:
    .. code-block::

        # set
        input:  0/1 PD_INDICES 0 1
        output: <OK>

        # get
        input:  0/1 PD_INDICES ?
        output: 0/1 PD_INDICES 0 1


``PD_CREATE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PD_CREATE [<dataset_xindex>]


:Description:
    Creates a histogram definition with the specified sub-index value.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PD_CREATE [0]
        output: <OK>



``PD_DELETE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PD_DELETE [<dataset_xindex>]


:Description:
    Delete an existing histogram definition.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PD_DELETE [0]
        output: <OK>



``PD_ENABLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PD_ENABLE [<dataset_xindex>] <on_off>

    # get
    <module-index>/<port-index> PD_ENABLE [<dataset_xindex>] ?

:Description:
    Whether a histogram is currently active on a port. When turned on, all the bucket
    counts are cleared to zero. Subsequently each packet matching the histogram source
    criteria is counted into one of the buckets. While a histogram is enabled its
    parameters cannot be changed.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, whether the histogram is enabled

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PD_ENABLE [0] OFF
        output: <OK>

        # get
        input:  0/1 PD_ENABLE [0] ?
        output: 0/1 PD_ENABLE [0] OFF


``PD_SOURCE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PD_SOURCE [<dataset_xindex>] <source_type> <which_packets> <identity>

    # get
    <module-index>/<port-index> PD_SOURCE [<dataset_xindex>] ?

:Description:
    The source criteria specifying what is counted, and for which packets, by a
    histogram of a port.

:Actions:
    set, get

:Parameter:
    ``source_type: <SourceType>``, what is counted and for which packets

        * ``TXIFG = 0``
        * ``TXLEN = 1``
        * ``RXIFG = 2``
        * ``RXLEN = 3``
        * ``RXLAT = 4``
        * ``RXJIT = 5``

    ``which_packets: <PacketDetailSelection>``, a further detail on which packets to count

        * ``ALL = 0``
        * ``TPLD = 1``
        * ``FILTER = 2``
        
    ``identity: <integer>``, test payload id or filter id for the wanted packets


:Example:
    .. code-block::

        # set
        input:  0/1 PD_SOURCE [0] TXIFG ALL 1
        output: <OK>

        # get
        input:  0/1 PD_SOURCE [0] ?
        output: 0/1 PD_SOURCE [0] TXIFG ALL 1


``PD_RANGE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PD_RANGE [<dataset_xindex>] <start> <step> <bucket_count>

    # get
    <module-index>/<port-index> PD_RANGE [<dataset_xindex>] ?

:Description:
    The bucket ranges used for classifying the packets counted by a histogram of a
    port. The packets are either counted by length, measured in bytes, by inter-
    frame gap to the preceding packet,  also measured in bytes, or by latency in
    transmission measured in nanoseconds.  There are a fixed number of buckets, each
    middle bucket covering a fixed-size range of values which is a power of two.
    The first and last buckets count all the packets that do not fit within the
    ranges of the middel buckets. The buckets are placed at a certain offset by
    specifying the first value that should be counted by the first middle bucket.

:Actions:
    set, get

:Parameter:
    ``start: <integer>``, first value going into the second bucket

    ``step: <integer>``, the span of each middle bucket: (1) 1,2,4,8,16,32,64,128,256,512 (bytes, non-latency histograms). (2) 16,32,64,128,...,1048576,2097152 (nanoseconds, latency histograms)

    ``bucket_count: <integer>``, the total number of buckets


:Example:
    .. code-block::

        # set
        input:  0/1 PD_RANGE [0] 1 1 1
        output: <OK>

        # get
        input:  0/1 PD_RANGE [0] ?
        output: 0/1 PD_RANGE [0] 1 1 1


``PD_SAMPLES``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PD_SAMPLES [<dataset_xindex>] ?

:Description:
    The current set of counts collected by a histogram for a port. There is one value
    for each bucket, but any trailing zeros are left out. The list is empty if all
    counts are zero.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PD_SAMPLES [0] ?
        output: 0/1 PD_SAMPLES [0]



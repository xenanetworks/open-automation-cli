Impairment Custom Distribution Commands
----------------------------------------


``PEC_INDICES``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEC_INDICES <indices>

    # get
    <module-index>/<port-index> PEC_INDICES ?

:Description:
    The full list of which custom distributions which are defined for a port. These
    are the custom id values that are used for assigning the custom distributions to
    an impairment. Setting the value of this command creates a new custom
    distribution (default values) for each value that is not already in use, and
    deletes each custom distribution that is not mentioned in the list. The same can
    be accomplished one-custom-distribution-at-a-time using the PEC_VAL and
    PEC_DELETE commands.
    
    .. note::
        
        Custom distributions which are currently defined are not affected when mentioned in a PEC_INDICES set command. Custom distributions which are currently assigned to an impairment cannot be deleted and any attempt of deleting such a custom distribution using either :class:`~xoa_driver.internals.core.commands.pec_commands.PEC_DELETE` or :class:`~xoa_driver.internals.core.commands.pec_commands.PEC_INDICES` will result in an error.

:Actions:
    set, get

:Parameter:
    ``indices: <indices>``, a list of indices to create new custom distributions


:Example:
    .. code-block::

        # set
        input:  0/1 PEC_INDICES 0 1
        output: <OK>

        # get
        input:  0/1 PEC_INDICES ?
        output: 0/1 PEC_INDICES 0 1


``PEC_VAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEC_VAL [<custom_distribution_xindex>] <linear> <symmetric> <entry_count> <data_x>

    # get
    <module-index>/<port-index> PEC_VAL [<custom_distribution_xindex>] ?

:Description:
    Definition of custom distribution. Custom distributions can be defined for
    latency with 1024 entries and for non-latency impairments with 512 entries. Each
    port will maintain a list of defined custom distributions, identified by an
    CUST_ID. (Range: 1 - 40).

:Actions:
    set, get

:Parameter:
    ``linear: <OnOff>``, defines the way the FPGA RAM content is played out

        * ``OFF = 0``
        * ``ON = 1``

    ``symmetric: <OnOff>``, reserved for future use, must be set to 0.

        * ``OFF = 0``
        * ``ON = 1``
        
    ``entry_count: <integer>``, defines the number of entries in "dataX" (allowed value: 512,1024). For Latency, 1024 entries are used, and for rest, 512 entries are used)

    ``data_x: <integer list>``, array size="num_entries", holds values to be filled in the RAM memory.


:Example:
    .. code-block::

        # set
        input:  0/1 PEC_VAL [0] OFF OFF 1 0 1
        output: <OK>

        # get
        input:  0/1 PEC_VAL [0] ?
        output: 0/1 PEC_VAL [0] OFF OFF 1 0 1


``PEC_COMMENT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEC_COMMENT [<custom_distribution_xindex>] <comment>

    # get
    <module-index>/<port-index> PEC_COMMENT [<custom_distribution_xindex>] ?

:Description:
    Defines the user-defined description string of a custom distribution.

:Actions:
    set, get

:Parameter:
    ``comment: <string>``, the user-specified comment/description for the custom distribution.


:Example:
    .. code-block::

        # set
        input:  0/1 PEC_COMMENT [0] word
        output: <OK>

        # get
        input:  0/1 PEC_COMMENT [0] ?
        output: 0/1 PEC_COMMENT [0] word


``PEC_DELETE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PEC_DELETE [<custom_distribution_xindex>]


:Description:
    Deletes the custom distribution definition.
    
    .. note::
    
        Once a customer has defined a customer distribution using :class:`~xoa_driver.internals.core.commands.pec_commands.PEC_VAL`, it is defined until it is explicitly deleted.Only customer distributions which are not referenced by any impairments, can be deleted.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PEC_DELETE [0]
        output: <OK>



``PEC_DISTTYPE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index>/<port-index> PEC_DISTTYPE [<custom_distribution_xindex>] ?

:Description:
    Retrieves if a custom distribution is defined for latency or non-latency.
    
    .. note::
    
        Using :class:`~xoa_driver.internals.core.commands.pec_commands.PEC_DISTTYPE` as set has no effect. The disttype is determined upon custom distribution creation and cannot be modified later. However, it is legal to issue the :class:`~xoa_driver.internals.core.commands.pec_commands.PEC_DISTTYPE` set command with no effect.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0/1 PEC_DISTTYPE [0] ?
        output: 0/1 PEC_DISTTYPE [0]



Length Term Commands
---------------------

``PL_INDICES``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PL_INDICES <length_term_xindices>

    # get
    <module-index>/<port-index> PL_INDICES ?

:Description:
    The full list of which length terms are defined for a port. These are the sub-
    index values that are used for the parameters defining the length-based matching
    of packets received for the port. Setting the value of this parameter creates a
    new empty length term for each value that is not already in use, and deletes
    each length term that is not mentioned in the list. The same can be accomplished
    one- length-term-at-a-time using the PL_CREATE and PL_DELETE commands.

:Actions:
    set, get

:Parameter:
    ``length_term_xindices: <indices>``, the list of indices of length terms to be created on a port.


:Example:
    .. code-block::

        # set
        input:  0/1 PL_INDICES 0 1
        output: <OK>

        # get
        input:  0/1 PL_INDICES ?
        output: 0/1 PL_INDICES 0 1


``PL_CREATE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PL_CREATE [<length_term_xindex>]


:Description:
    Creates an empty length term definition with the specified sub-index value.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PL_CREATE [0]
        output: <OK>



``PL_DELETE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PL_DELETE [<length_term_xindex>]


:Description:
    Deletes the length term definition with the specified sub-index value. A length
    term cannot be deleted while it is used in the condition of any filter for the
    port.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PL_DELETE [0]
        output: <OK>



``PL_LENGTH``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PL_LENGTH [<length_term_xindex>] <length_check_type> <size>

    # get
    <module-index>/<port-index> PL_LENGTH [<length_term_xindex>] ?

:Description:
    The specification for a length-based check that is applied on the packets
    received on the port.

:Actions:
    set, get

:Parameter:
    ``length_check_type: <LengthCheckType>``, whether to test for shorter-than or longer-than

        * ``AT_MOST = 0``
        * ``AT_LEAST = 1``
        
    ``size: <integer>``, the value to compare the packet length against


:Example:
    .. code-block::

        # set
        input:  0/1 PL_LENGTH [0] AT_MOST 1
        output: <OK>

        # get
        input:  0/1 PL_LENGTH [0] ?
        output: 0/1 PL_LENGTH [0] AT_MOST 1



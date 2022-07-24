Match Term Commands
---------------------

``PM_INDICES``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PM_INDICES <match_term_xindices>

    # get
    <module-index>/<port-index> PM_INDICES ?

:Description:
    The full list of which match terms are defined for a port. These are the sub-
    index values that are used for the parameters defining the content-based
    matching of packets received for the port. Setting the value of this parameter
    creates a new empty match term for each value that is not already in use, and
    deletes each match term that is not mentioned in the list. The same can be
    accomplished one match-term-at-a-time using the PM_CREATE and PM_DELETE commands.

:Actions:
    set, get

:Parameter:
    ``match_term_xindices: <indices>``, the sub-index of a match term definition for the port


:Example:
    .. code-block::

        # set
        input:  0/1 PM_INDICES 0 1
        output: <OK>

        # get
        input:  0/1 PM_INDICES ?
        output: 0/1 PM_INDICES 0 1


``PM_CREATE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PM_CREATE [<match_term_xindex>]


:Description:
    Creates an empty match term definition with the specified sub-index value.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PM_CREATE [0]
        output: <OK>



``PM_DELETE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PM_DELETE [<match_term_xindex>]


:Description:
    Deletes the match term definition with the specified sub-index value. A match
    term cannot be deleted while it is used in the condition of any filter for the
    port.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PM_DELETE [0]
        output: <OK>



``PM_PROTOCOL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PM_PROTOCOL [<match_term_xindex>] <segments>

    # get
    <module-index>/<port-index> PM_PROTOCOL [<match_term_xindex>] ?

:Description:
    The protocol segments assumed on the packets received on the port. This is
    mainly for information purposes, and helps you identify which portion of the
    packet header is being matched. The actual value definition of the match
    position is specified with PM_POSITION.

:Actions:
    set, get

:Parameter:
    ``segments: <List[ProtocolOption]>``, a number specifying a built-in protocol segment: Uses the same coded values as the PS_HEADERPROTOCOL parameter


:Example:
    .. code-block::

        # set
        input:  0/1 PM_PROTOCOL [0] 0 1 2
        output: <OK>

        # get
        input:  0/1 PM_PROTOCOL [0] ?
        output: 0/1 PM_PROTOCOL [0] 0 1 2


``PM_POSITION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PM_POSITION [<match_term_xindex>] <byte_offset>

    # get
    <module-index>/<port-index> PM_POSITION [<match_term_xindex>] ?

:Description:
    The position within each received packet where content matching begins for the
    port.

:Actions:
    set, get

:Parameter:
    ``byte_offset: <integer>``, offset from the start of the packet bytes


:Example:
    .. code-block::

        # set
        input:  0/1 PM_POSITION [0] 1
        output: <OK>

        # get
        input:  0/1 PM_POSITION [0] ?
        output: 0/1 PM_POSITION [0] 1


``PM_MATCH``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PM_MATCH [<match_term_xindex>] <mask> <value>

    # get
    <module-index>/<port-index> PM_MATCH [<match_term_xindex>] ?

:Description:
    The value that must be found at the match term position for packets received on
    the port. The mask can make certain bit positions don't-care.

:Actions:
    set, get

:Parameter:
    ``mask: <string>``, which bits are significant in the match operation

    ``value: <string>``, the value that must be found for the match term to be true


:Example:
    .. code-block::

        # set
        input:  0/1 PM_MATCH [0] word word
        output: <OK>

        # get
        input:  0/1 PM_MATCH [0] ?
        output: 0/1 PM_MATCH [0] word word



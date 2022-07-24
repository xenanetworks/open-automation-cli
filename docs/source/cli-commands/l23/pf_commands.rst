Filter Commands
---------------------

``PF_INDICES``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PF_INDICES <filter_xindices>

    # get
    <module-index>/<port-index> PF_INDICES ?

:Description:
    The full list of which filters are defined for a port. These are the sub-index
    values that are used for the parameters defining the compound conditions on the
    match/length terms operating on the packets received for the port. Setting the
    value of this parameter creates a new empty filter for each value that is not
    already in use, and deletes each filter that is not mentioned in the list. The
    same can be accomplished one-filter-at-a-time using the PF_CREATE and PF_DELETE
    commands.

:Actions:
    set, get

:Parameter:
    ``filter_xindices: <indices>``, the list of indices of filters to be created on a port.


:Example:
    .. code-block::

        # set
        input:  0/1 PF_INDICES 0 1
        output: <OK>

        # get
        input:  0/1 PF_INDICES ?
        output: 0/1 PF_INDICES 0 1


``PF_CREATE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PF_CREATE [<filter_xindex>]


:Description:
    Creates an empty filter definition with the specified sub-index value.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PF_CREATE [0]
        output: <OK>



``PF_DELETE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PF_DELETE [<filter_xindex>]


:Description:
    Deletes the filter definition with the specified sub-index value.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0/1 PF_DELETE [0]
        output: <OK>



``PF_ENABLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PF_ENABLE [<filter_xindex>] <on_off>

    # get
    <module-index>/<port-index> PF_ENABLE [<filter_xindex>] ?

:Description:
    Whether a filter is currently active on a port. While a filter is enabled its
    condition cannot be changed, nor can any match term or length terms used by it.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, whether the filter is enabled

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  0/1 PF_ENABLE [0] OFF
        output: <OK>

        # get
        input:  0/1 PF_ENABLE [0] ?
        output: 0/1 PF_ENABLE [0] OFF


``PF_COMMENT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PF_COMMENT [<filter_xindex>] <comment>

    # get
    <module-index>/<port-index> PF_COMMENT [<filter_xindex>] ?

:Description:
    The description of a filter.

:Actions:
    set, get

:Parameter:
    ``comment: <string>``, the description of the filter.


:Example:
    .. code-block::

        # set
        input:  0/1 PF_COMMENT [0] word
        output: <OK>

        # get
        input:  0/1 PF_COMMENT [0] ?
        output: 0/1 PF_COMMENT [0] word


``PF_CONDITION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PF_CONDITION [<filter_xindex>] <and_expression_0> <and_not_expression_0> <and_expression_1> <and_not_expression_1> <and_expression_2> <and_expression_3>

    # get
    <module-index>/<port-index> PF_CONDITION [<filter_xindex>] ?

:Description:
    The boolean condition on the terms specifying when the filter is satisfied. The condition uses a canonical and-or-not expression on the match terms and length terms. The condition is specified using a number of compound terms, each encoded as an integer value specifying an arbitrary set of the match terms and length terms defined for the port. Each match or length term has a specific power-of-two value, and the set is encoded as the sum of the values for the contained terms:
        
        Value for match term ``[match_term_xindex] = 2^match_term_xindex``

        Value for length term ``[length_term_xindex] = 2^(length_term_xindex+16)``

        A compound term is true if all the match terms and length terms contained in it are true. This supports the and-part of the condition. If some compound term is satisfied, the condition as a whole is true.

        This is the or-part of the condition. The first few compound terms at the even positions (second, fourth, ...) are inverted, and all the contained match terms and length terms must be false at the same time that the those of the preceding compound term are true. This is the not-part of the condition.

        At the top level, a condition is a bunch of things or-ed together.

        ``<filter-condition> = <or-expr>`` 

        Two of the or-operands are *general*, two are 'simple'.

        ``<or-expr> =  <general-and-expr>  or  <general-and-expr>  or  <simple-and-expr>  or  <simple-and-expr>`` 

        A 'general' and-expression can include negated terms.

        ``<general-and-expr>  =  <term>  and  <term>  and ... and  not <term>  and ... and  not <term>`` 

        A 'simple' and-expression can only have non-negated terms.

        ``<simple-and-expr>   =  <term>  and  <term>  and ... and <term>``  

        ``<term>              =  <match-term>``
        
        ``<term>              =  <length-term>``  

        In practice, the simplest way to generate these encodings is to use the ValkyrieManager, which supports Boolean expressions using the operators ``&, |, and ~``, and simply query the chassis for the resulting script-level definition.

:Actions:
    set, get

:Parameter:
    ``and_expression_0: <integer>``, encoding a compound term which is a set of the match terms AND length terms.

    ``and_not_expression_0: <integer>``, encoding a compound term which is a set of the match NOT terms AND length NOT terms.

    ``and_expression_1: <integer>``, encoding a compound term which is a set of the match terms AND length terms.

    ``and_not_expression_1: <integer>``, encoding a compound term which is a set of the match NOT terms AND length NOT terms.

    ``and_expression_2: <integer>``, encoding a compound term which is a set of the match terms AND length terms.

    ``and_expression_3: <integer>``, encoding a compound term which is a set of the match terms AND length terms.


:Example:
    .. code-block::

        # set
        input:  0/1 PF_CONDITION [0] 1 1 1 1 1 1
        output: <OK>

        # get
        input:  0/1 PF_CONDITION [0] ?
        output: 0/1 PF_CONDITION [0] 1 1 1 1 1 1


``PF_STRING``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index>/<port-index> PF_STRING [<filter_xindex>] <string_name>

    # get
    <module-index>/<port-index> PF_STRING [<filter_xindex>] ?

:Description:
    The string representation of a filter.

:Actions:
    set, get

:Parameter:
    ``string_name: <string>``, the string representation of the filter


:Example:
    .. code-block::

        # set
        input:  0/1 PF_STRING [0] word
        output: <OK>

        # get
        input:  0/1 PF_STRING [0] ?
        output: 0/1 PF_STRING [0] word



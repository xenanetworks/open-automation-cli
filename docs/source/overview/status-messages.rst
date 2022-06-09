Status Messages
==========================================

The ``set`` commands themselves simply produce a reply from the chassis of:

``<OK>``

In case something is unacceptable to the chassis, it may return one of the following
status messages:

* ``<NOCONNECTIONS>`` Chassis has no available connection slots.
* ``<NOTLOGGEDON>`` You have not issued a ``C_LOGON`` providing the chassis password.
* ``<NOTRESERVED>`` You have not issued a ``x_RESERVATION`` for the resource you want to change.
* ``<NOTREADABLE>`` The command is write-only.
* ``<NOTWRITABLE>`` The command is read-only.

* ``<NOTVALID>`` The operation is not valid in the current chassis state, e.g. because traffic is on.
* ``<BADPARAMETER>`` Invalid command.
* ``<BADMODULE>`` The module index value is out of bounds.
* ``<BADPORT>`` The port index value is out of bounds.
* ``<BADINDEX>`` A command sub-index value is wrong.
* ``<BADSIZE>`` The size of a data value is not appropriate.
* ``<BADVALUE>`` A parameter is not appropriate.
* ``<FAILED>`` An operation failed to produce a result.

* ``<MEMORYFAILURE>`` Failed to allocate memory.
* ``<NOLICPE>`` No free PE license.
* ``<NOLICPORT>`` No free Port license.
* ``<NOTSUPPORTED>`` Not supported.

In case of a plain syntax error, misspelled command name, or inappropriate use of module/port/indices, the chassis will return a line pointing out the column where the error was detected, e.g.

.. code-block::
    :linenos:

    0/5 PS_RATEPPS [] 5q00
    —^
    #Syntax error in column 24


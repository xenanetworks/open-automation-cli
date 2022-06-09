Command Synopsis
=====================

The CLI have similar syntax for setting and getting parameters of individual commands of the chassis resources. Some commands, such as inter-frame gap, support both ``set`` and ``get`` actions; others, like physical port type, support only ``get``; and a few, like injecting errors, support only ``set``.

Set Synopsis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You change parameters or states of the test resources using:

.. code-block::
    
    [module-index/port-index] <command> [indices] [parameters]

* ``module-index`` and ``port-index`` are the numeric indices for a particular port (for chassis-level commands neither of these are present, and for module-level commands only module is present).
* ``command`` is one of the names specified later in this document in the reference sections
* ``indices`` are possible sub-indices of the command, for instance identifying a stream; and each specifies a parameter appropriate for the particular command. All indices start at zero.
* ``parameters`` are specified using one of the following formats:

    * ``Integer`` (``I``): decimal integer, in the 32-bit range, e.g. 1234567.
    * ``Long`` (``L``): decimal integer, in the 64-bit range, e.g. 123456789123.
    * ``Byte`` (``B``): decimal integer, in the 8-bit range, e.g. 123.
    * ``Hex`` (``H``): two hexadecimal digits prefixed by ``0x``, e.g. 0xF7.
    * ``String`` (``S``): printable 7-bit ASCII characters enclosed in ``''``, e.g. ''A string''. Characters with values outside the 32-126 range and the ``''`` character itself are specified by their decimal value, outside the quotation marks and separated by commas, e.g. ''A line'', 13, 10, ''and the next line''.
    * ``Owner`` (``O``): a short string used to identify an owner, used for the reservation.
    * ``Address`` (``A``): a dot-separated IP address, e.g. 192.168.1.200.

Some commands allow a variable number of parameters of a particular type (``I*, B*, H*``), and these are simply written with spaces in between. For hex parameters (``H*``), multiple bytes can be specified using a single ``0x`` prefix, e.g. 0xF700ABCD2233.

Finally, certain commands are actually integers, but use coded names for special numeric values to enhance readability, e.g. (``0=OFF,1=ON``).

Get Synopsis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can query the current parameters of test resources using:

.. code-block::
    
    [module-index/port-index] <command> [indices] ?

The chassis responds with a line using identical syntax to the change-command, containing the current parameters. These responses can, therefore, be *''replayed''* back to the chassis to re-establish the parameter from a previous query. This is actually the core of the load/save mechanism of the ValkyrieManager, as you can see by using an ordinary text editor to inspect the local files produced by saving. You can also change the content if you want to; it is not interpreted by the Manager applications.

.. note::
    
    Some queries, like ``P_INFO ?`` and ``P_CONFIG ?``, are special in that they do not refer to one particular command, but rather to a collection of commands. The response is multiple lines containing the current parameter of each of these commands.


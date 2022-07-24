Command Synopsis
=====================

The CLI have similar syntax for setting and getting parameters of individual commands of the chassis resources. Some commands, such as inter-frame gap, support both ``set`` and ``get`` actions; others, like physical port type, support only ``get``; and a few, like injecting errors, support only ``set``.


``set`` Synopsis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You change parameters or states of the test resources using:

.. code-block:: 
    
    [module-index/port-index] <command> [\[sub-indices\]] [parameters]

* ``module-index`` and ``port-index`` are the numeric sub-indices for a particular port (for chassis-level commands neither of these are present, and for module-level commands only module-index is present).
* ``command`` is one of the names specified later in this document in the reference sections
* ``sub-indices`` are possible sub-indices of the command. When there are multiple, separated by comma. Each sub-index specifies a parameter appropriate for the particular command. All sub-indices start at zero.
* ``parameters`` are possible parameters of the command. When there are multiple, separated by space. A parameter is specified using one of the following formats:

.. _data_types:

    * ``integer`` (``I``): decimal integer, in the 32-bit range, e.g. 1234567.
    * ``long`` (``L``): decimal integer, in the 64-bit range, e.g. 123456789123.
    * ``byte`` (``B``): decimal integer, in the 8-bit range, e.g. 123.
    * ``hex`` (``H``): two hexadecimal digits prefixed by ``0x``, e.g. 0xF7.
    * ``string`` (``S``): printable 7-bit ASCII characters enclosed in ``''``, e.g. ''A string''. Characters with values outside the 32-126 range and the ``''`` character itself are specified by their decimal value, outside the quotation marks and separated by commas, e.g. ''A line'', 13, 10, ''and the next line''.
    * ``owner`` (``O``): a short string used to identify an owner, used for the reservation.
    * ``address`` (``A``): a dot-separated IP address, e.g. 192.168.1.200.

Some commands allow a variable number of parameters of a particular type (``List[integer] I*, List[byte] B*, List[hex] H*``), and these are simply written with spaces in between. For hex parameters (``H*``), multiple bytes can be specified using a single ``0x`` prefix, e.g. 0xF700ABCD2233.

Finally, certain commands are actually integers, but use coded names for special numeric values to enhance readability, e.g. (``0=OFF,1=ON``).

``get`` Synopsis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can query the current parameters of test resources using:

.. code-block::
    
    [module-index\/port-index] <command> [sub-indices] ?

The chassis responds with a line using identical syntax to the change-command, containing the current parameters. These responses can, therefore, be *''replayed''* back to the chassis to re-establish the parameter from a previous query. This is actually the core of the load/save mechanism of the ValkyrieManager, as you can see by using an ordinary text editor to inspect the local files produced by saving. You can also change the content if you want to; it is not interpreted by the Manager applications.

.. note::
    
    Some queries, like ``P_INFO ?`` and ``P_CONFIG ?``, are special in that they do not refer to one particular command, but rather to a collection of commands. The response is multiple lines containing the current parameter of each of these commands.


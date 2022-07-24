L47 Module Commands
---------------------

``M4_SYSTEMID``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M4_SYSTEMID ?

:Description:
    Return the system identifier of a L47 module.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M4_SYSTEMID ?
        output: 0 M4_SYSTEMID


``M4_VERSIONNO``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M4_VERSIONNO ?

:Description:
    Returns a version string containing a combination of information regarding the
    software version and the build environment. The first part of the string is the
    software build version.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M4_VERSIONNO ?
        output: 0 M4_VERSIONNO


``M4_SYSTEM_STATUS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M4_SYSTEM_STATUS ?

:Description:
    Returns the L47 module system status in a text string.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M4_SYSTEM_STATUS ?
        output: 0 M4_SYSTEM_STATUS


``M4_COMPATIBLE_CLIENT_VERSION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M4_COMPATIBLE_CLIENT_VERSION ?

:Description:
    Returns the recommended and required VulcanMananger client version.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M4_COMPATIBLE_CLIENT_VERSION ?
        output: 0 M4_COMPATIBLE_CLIENT_VERSION


``M4_TIME``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M4_TIME ?

:Description:
    Returns the module time in millisecond.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M4_TIME ?
        output: 0 M4_TIME


``M4_SYSTEM_TIME``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M4_SYSTEM_TIME <year> <month> <day> <hour> <minute> <second>

    # get
    <module-index> M4_SYSTEM_TIME ?

:Description:
    Sets or returns the modules system time in UTC.

:Actions:
    set, get

:Parameter:
    ``year: <integer>``, the year

    ``month: <integer>``, the month

    ``day: <integer>``, the day of the month

    ``hour: <integer>``, the hour

    ``minute: <integer>``, the minute

    ``second: <integer>``, the second


:Example:
    .. code-block::

        # set
        input:  0 M4_SYSTEM_TIME 1 1 1 1 1 1
        output: <OK>

        # get
        input:  0 M4_SYSTEM_TIME ?
        output: 0 M4_SYSTEM_TIME 1 1 1 1 1 1


``M4_MEM_INFO``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M4_MEM_INFO ?

:Description:
    Return the system memory information.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M4_MEM_INFO ?
        output: 0 M4_MEM_INFO


``M4_CAPTURE_SIZE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M4_CAPTURE_SIZE <size>

    # get
    <module-index> M4_CAPTURE_SIZE ?

:Description:
    Specify whether to capture whole packets(large) or truncated packets. When
    truncated (small) is selected only the first 128 bytes of the packet are saved.

:Actions:
    set, get

:Parameter:
    ``size: <CaptureSize>``, specifying whether to capture whole packets or truncated packets.

        * ``FULL = 0``
        * ``SMALL = 1``

:Example:
    .. code-block::

        # set
        input:  0 M4_CAPTURE_SIZE FULL
        output: <OK>

        # get
        input:  0 M4_CAPTURE_SIZE ?
        output: 0 M4_CAPTURE_SIZE FULL


``M4_LICENSE_INFO``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M4_LICENSE_INFO ?

:Description:
    Returns the number of available and free PE licenses. Only 'available' number of PEs
    can simultaneously be assigned to reserved ports.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M4_LICENSE_INFO ?
        output: 0 M4_LICENSE_INFO


``M4_REPLAY_PARSE_START``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M4_REPLAY_PARSE_START <filename>


:Description:
    Command to start parsing an uploaded Capture File (in PCAP format) intended for
    use in a replay test scenario. The result of the parsing - if successful - is a
    Replay File (in BSON format) with the same name as the Capture File, which can
    be used as parameter to P4G_REPLAY_filename command. If parsing is unsuccessful,
    a Replay File is created containing the parse result. The
    M4_REPLAY_FILE_INFO_BSON command can be used to get information about a Replay
    File - including the parse result. PCAP Capture Files can be uploaded to the L47
    chassis using FTP. The 'root' location of Capture Files uploaded manually by the
    user is /var/ftp/pub/replay/pcap/. Three subdirectories exist: cache/, user/ and
    xena/. cache / and xena/ is used by Vulcan Manager, and user/ is intended for
    manual upload and parsing of Capture Files. A similar directory structure is
    present for Replay Files generated by the parsing, and the 'root' location is
    /var/ftp/pub/replay/bson/.

:Actions:
    set

:Parameter:
    ``filename: <string>``, filename (including relative path and excluding the '.pcap' extension).


:Example:
    .. code-block::

        # set
        input:  0 M4_REPLAY_PARSE_START word
        output: <OK>



``M4_REPLAY_PARSE_STOP``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M4_REPLAY_PARSE_STOP


:Description:
    Command to stop parsing a Capture File. Parsing of very large Capture Files may
    take several seconds, and may be aborted using this command. No parameters

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  0 M4_REPLAY_PARSE_STOP
        output: <OK>



``M4_REPLAY_PARSE_STATE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M4_REPLAY_PARSE_STATE ?

:Description:
    Only one Capture File can be parsed at a time. This command returns the state of
    the parser, which can be PARSING or OFF. M4_REPLAY_PARSE_START command is only
    accepted when the parser state is OFF.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M4_REPLAY_PARSE_STATE ?
        output: 0 M4_REPLAY_PARSE_STATE


``M4_REPLAY_PARSER_PARAMS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M4_REPLAY_PARSER_PARAMS <tcp_port>

    # get
    <module-index> M4_REPLAY_PARSER_PARAMS ?

:Description:
    Configuration of parameters for the parsing of pcap files.

:Actions:
    set, get

:Parameter:
    ``tcp_port: <integer>``, server-side TCP port of the dummy TCP connection inserted in UDP.


:Example:
    .. code-block::

        # set
        input:  0 M4_REPLAY_PARSER_PARAMS 1
        output: <OK>

        # get
        input:  0 M4_REPLAY_PARSER_PARAMS ?
        output: 0 M4_REPLAY_PARSER_PARAMS 1


``M4_REPLAY_FILE_LIST_BSON``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M4_REPLAY_FILE_LIST_BSON ?

:Description:
    Works as ``M4_REPLAY_FILE_LIST``, but returns the file list formatted as a BSON
    document.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M4_REPLAY_FILE_LIST_BSON ?
        output: 0 M4_REPLAY_FILE_LIST_BSON


``M4_REPLAY_FILE_LIST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M4_REPLAY_FILE_LIST ?

:Description:
    Returns a list of Replay Files (``.bson`` files) in the 'user' Replay File
    directory (``/var/ftp/pub/replay/bson/user/``).

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M4_REPLAY_FILE_LIST ?
        output: 0 M4_REPLAY_FILE_LIST


``M4_CAPTURE_FILE_LIST_BSON``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M4_CAPTURE_FILE_LIST_BSON ?

:Description:
    Works as ``M4_CAPTURE_FILE_LIST``, but returns the file list formatted as a BSON
    document.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M4_CAPTURE_FILE_LIST_BSON ?
        output: 0 M4_CAPTURE_FILE_LIST_BSON


``M4_CAPTURE_FILE_LIST``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M4_CAPTURE_FILE_LIST ?

:Description:
    Returns a list of Capture Files (``.pcap`` files) in the 'user' Capture File
    directory (``/var/ftp/pub/replay/pcap/user/``).

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M4_CAPTURE_FILE_LIST ?
        output: 0 M4_CAPTURE_FILE_LIST


``M4_REPLAY_FILE_DELETE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M4_REPLAY_FILE_DELETE <filename>


:Description:
    Command to delete a Replay File (``.bson`` file) in the Replay File directory
    (``/var/ftp/pub/replay/bson/``). For information about the location and directory
    structure for the Replay Files, see: M4_REPLAY_PARSE_START

:Actions:
    set

:Parameter:
    ``filename: <string>``, file name (including relative path and excluding the ``.bson`` extension).


:Example:
    .. code-block::

        # set
        input:  0 M4_REPLAY_FILE_DELETE word
        output: <OK>



``M4_CAPTURE_FILE_DELETE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    <module-index> M4_CAPTURE_FILE_DELETE <filename>


:Description:
    Command to delete a Capture File (``.pcap`` file) in the Capture File directory
    (``/var/ftp/pub/replay/pcap/``). For information about the location and directory
    structure for the Capture Files, see: M4_REPLAY_PARSE_START

:Actions:
    set

:Parameter:
    ``filename: <string>``, file name (including relative path and excluding the ``.pcap`` extension).


:Example:
    .. code-block::

        # set
        input:  0 M4_CAPTURE_FILE_DELETE word
        output: <OK>



``M4_TLS_CIPHER_SUITES``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    <module-index> M4_TLS_CIPHER_SUITES ?

:Description:
    Returns a list of supported TLS Cipher Suites.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  0 M4_TLS_CIPHER_SUITES ?
        output: 0 M4_TLS_CIPHER_SUITES



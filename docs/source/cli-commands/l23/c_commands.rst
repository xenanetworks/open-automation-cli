Chassis Commands
---------------------

``C_LOGON``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_LOGON <password>


:Description:
    You log on to the chassis by setting the value of this command to the correct
    password for the chassis. All other commands will fail if the session has not
    been logged on.

:Actions:
    set

:Parameter:
    ``password: <string>``, password for creating a tester management session and logging on to the tester.


:Example:
    .. code-block::

        # set
        input:  C_LOGON "xena"
        output: <OK>



``C_OWNER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_OWNER <username>

    # get
    C_OWNER ?

:Description:
    Identify the owner of the management session. The name can be any short quoted
    string up to eight characters long. This name will be used when reserving ports
    prior to updating their configuration. There is no authentication of the users,
    and the chassis does not have any actual user accounts. Multiple concurrent
    connections may use the same owner name, but only one connection can have any
    particular resource reserved at any given time. Until an owner is specified the
    chassis configuration can only be read. Once specified, the session can reserve
    ports for that owner, and will inherit any existing reservations for that owner
    retained at the chassis. Maximum 32 ASCII characters.

:Actions:
    set, get

:Parameter:
    ``username: <string>``, the username of this chassis management session.


:Example:
    .. code-block::

        # set
        input:  C_OWNER "spongebob"
        output: <OK>

        # get
        input:  C_OWNER ?
        output: C_OWNER "spongebob"


``C_KEEPALIVE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_KEEPALIVE ?

:Description:
    You can request this value from the chassis, simply to let it (as well as and
    any routers and proxies between you) know that the connection is still valid.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  C_KEEPALIVE ?
        output: C_KEEPALIVE 1234


``C_TIMEOUT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_TIMEOUT <second_count>

    # get
    C_TIMEOUT ?

:Description:
    The maximum number of idle seconds allowed before the connection is timed out by
    the tester.

:Actions:
    set, get

:Parameter:
    ``second_count: <integer>``, the maximum idle interval, default is 130 seconds.


:Example:
    .. code-block::

        # set
        input:  C_TIMEOUT 1
        output: <OK>

        # get
        input:  C_TIMEOUT ?
        output: C_TIMEOUT 1


``C_RESERVATION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_RESERVATION <operation>

    # get
    C_RESERVATION ?

:Description:
    You set this command to reserve, release, or relinquish the chassis itself.
    The chassis must be reserved before any of the chassis-level parameters can be
    changed. The owner of the session must already have been specified.
    Reservation will fail if any modules or ports are reserved for other users.
    
    NOTICE: Before reserve Tester need to reserve all the ports on it, otherwise 
    ``<STATUS_NOTVALID>``

:Actions:
    set, get

:Parameter:
    ``operation: <ReservedAction>``, reservation operation to be performed.

        * ``RELEASE = 0``
        * ``RESERVE = 1``
        * ``RELINQUISH = 2``

:Example:
    .. code-block::

        # set
        input:  C_RESERVATION RELEASE
        output: <OK>

        # get
        input:  C_RESERVATION ?
        output: C_RESERVATION RELEASE


``C_RESERVEDBY``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_RESERVEDBY ?

:Description:
    Identify the user who has the chassis reserved. The empty string if the chassis
    is not currently reserved.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  C_RESERVEDBY ?
        output: C_RESERVEDBY ""spongebob""


``C_LOGOFF``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_LOGOFF


:Description:
    Terminates the current scripting session. Courtesy only, the chassis will also
    handle disconnection at the TCP/IP level

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  C_LOGOFF
        output: <OK>



``C_DOWN``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_DOWN <operation>


:Description:
    Shuts down the chassis, and either restarts it in a clean state or leaves it
    powered off.

:Actions:
    set

:Parameter:
    ``operation: <ChassisShutdownAction>``, what to do after shutting chassis down.

        * ``RESTART = 1``
        * ``POWEROFF = 2``

:Example:
    .. code-block::

        # set
        input:  C_DOWN RESTART
        output: <OK>



``C_CAPABILITIES``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_CAPABILITIES ?

:Description:
    A series of integer values specifying various internal limits (aka.
    capabilities) of the chassis.

:Actions:
    get

:Parameter:
    ``version: <integer>``, chassis software build number.
    ``max_name_len: <integer>``, max ASCII characters in chassis name.
    ``max_comment_len: <integer>``, max ASCII characters in chassis comment.
    ``max_password_len: <integer>``, max ASCII characters in chassis password.
    ``max_ext_rate: <integer>``, maximum rate for external traffic.
    ``max_session_count: <integer>``, max number of management and scripting sessions.
    ``max_chain_depth: <integer>``, max chain index.
    ``max_module_count: <integer>``, maximum number of L23 modules.
    ``max_protocol_count: <integer>``, max protocol segments in a packet.
    ``can_stream_based_arp: <integer>``, does server support stream-based ARP/NDP?
    ``can_sync_traffic_start: <integer>``, does server support synchronous traffic start?
    ``can_read_log_files: <integer>``, can clients read debug log files from server?
    ``can_par_module_upgrade: <integer>``, can server handle parallel module upgrades?
    ``can_upgrade_timekeeper: <integer>``, is server capable of upgrading the TimeKeeper application?
    ``can_custom_defaults: <integer>``, can server handle custom default values for XMP parameters?
    ``can_latency_f2f: <integer>``, can server handle first-to-first latency mode?
    ``max_owner_name_length: <integer>``, max number of ASCII characters in C_OWNER name
    ``can_read_temperatures: <integer>``, can the server read out chassis and/or CPU temperatures? (C_TEMPERATURE ?)

:Example:
    .. code-block::

        # get
        input:  C_CAPABILITIES ?
        output: C_CAPABILITIES 1 50 50 127 10 100 3 12 30 1 1 1 1 1 1 1 32 1


``C_MODEL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_MODEL ?

:Description:
    Gets the specific model of this Xena chassis.

:Actions:
    get

:Parameter:
    ``model: <string>``, the model of the Xena tester.

:Example:
    .. code-block::

        # get
        input:  C_MODEL ?
        output: C_MODEL 


``C_SERIALNO``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_SERIALNO ?

:Description:
    Gets the unique serial number of this particular Xena chassis.

:Actions:
    get

:Parameter:
    ``serial_number: <integer>``, the serial number of the Xena tester.

:Example:
    .. code-block::

        # get
        input:  C_SERIALNO ?
        output: C_SERIALNO 123456


``C_VERSIONNO``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_VERSIONNO ?

:Description:
    Gets the major version numbers for the chassis firmware and the Xena PCI
    driver installed on the chassis.

:Actions:
    get

:Parameter:
    ``chassis_major_version: <integer>``, the chassis firmware major version number.
    ``pci_driver_version: <integer>``, the Xena PCI driver version.

:Example:
    .. code-block::

        # get
        input:  C_VERSIONNO ?
        output: C_VERSIONNO 423 30


``C_PORTCOUNTS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_PORTCOUNTS ?

:Description:
    Gets the number of ports in each module slot of the chassis, and indirectly
    the number of slots and modules.
    
    .. note::
    
        CFP modules return the number 8 which is the maximum number of 10G ports, but the actual number of ports can be configured dynamically using the :class:`~xoa_driver.internals.core.commands.m_commands.M_CFPCONFIG` command.

:Actions:
    get

:Parameter:
    ``port_counts: <List[integer]>``, the number of ports of each module slot of the tester, 0 for an empty slot.

:Example:
    .. code-block::

        # get
        input:  C_PORTCOUNTS ?
        output: C_PORTCOUNTS 6 6 6 6 0 0 0 0 2 2 2 2


``C_PORTERRORS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_PORTERRORS ?

:Description:
    Gets the number of errors detected across all streams on each port of each
    test module of the chassis. The counts are ordered in sequence with those of
    the module in the lowest numbered chassis slot first. Empty slots are skipped
    so that a chassis with a 6-port and a 2-port test module will return eight
    counts regardless of which slots they are in.
    
    .. note::
    
        CFP modules return eight error counts since they can be configured as up to eight 10G ports. When in 100G and 40G mode only the first one or two counts are significant.
    
    .. note::
        
        FCS errors are included, which leads to double-counting for streams detecting lost packets using the test payload mechanism.

:Actions:
    get

:Parameter:
    ``error_count: <integer>``, the total number of errors across all streams, and including FCS errors.

:Example:
    .. code-block::

        # get
        input:  C_PORTERRORS ?
        output: C_PORTERRORS 369


``C_REMOTEPORTCOUNTS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_REMOTEPORTCOUNTS ?

:Description:
    Gets the number of ports of each remote module. A remote module is a
    relative to the xenaserver, for example, xenal47server. The first integer in
    the returned list is always 0 because it represents the xenaserver, which is
    not a remote module.

:Actions:
    get

:Parameter:
    ``port_counts: <List[integer]>``, the number of ports of each module slot of the tester, 0 for an empty slot.

:Example:
    .. code-block::

        # get
        input:  C_REMOTEPORTCOUNTS ?
        output: C_REMOTEPORTCOUNTS 0 6


``C_BUILDSTRING``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_BUILDSTRING ?

:Description:
    Identify the hostname of the PC that builds the xenaserver. It uniquely
    identifies the build of a xenaserver.

:Actions:
    get

:Parameter:
    ``build_string: <string>``, build string that identifies the hostname of the PC that builds the xenaserver.

:Example:
    .. code-block::

        # get
        input:  C_BUILDSTRING ?
        output: C_BUILDSTRING "2022-06-20-092729[localhost.localdomai] 4dd4444", 0


``C_NAME``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_NAME <chassis_name>

    # get
    C_NAME ?

:Description:
    The name of the chassis, as it appears at various places in the user interface.
    The name is also used to distinguish the various chassis contained within a
    testbed  and in files containing the configuration for an entire test case.

:Actions:
    set, get

:Parameter:
    ``chassis_name: <string>``, the name of the tester


:Example:
    .. code-block::

        # set
        input:  C_NAME "Just a name"
        output: <OK>

        # get
        input:  C_NAME ?
        output: C_NAME "Just a name"


``C_COMMENT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_COMMENT <comment>

    # get
    C_COMMENT ?

:Description:
    The description of the chassis.

:Actions:
    set, get

:Parameter:
    ``comment: <string>``, the description of the tester


:Example:
    .. code-block::

        # set
        input:  C_COMMENT "just a comment"
        output: <OK>

        # get
        input:  C_COMMENT ?
        output: C_COMMENT "just a comment"


``C_PASSWORD``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_PASSWORD <password>

    # get
    C_PASSWORD ?

:Description:
    The password of the chassis, which must be provided when logging on to the chassis.

:Actions:
    set, get

:Parameter:
    ``password: <string>``, the password of the tester


:Example:
    .. code-block::

        # set
        input:  C_PASSWORD "new_password"
        output: <OK>

        # get
        input:  C_PASSWORD ?
        output: C_PASSWORD "new_password"


``C_IPADDRESS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_IPADDRESS <ipv4_address> <subnet_mask> <gateway>

    # get
    C_IPADDRESS ?

:Description:
    The network configuration parameters of the chassis management port.

:Actions:
    set, get

:Parameter:
    ``ipv4_address: <ipv4_address>``, the static IP address of the chassis

    ``subnet_mask: <ipv4_address>``, the subnet mask of the local network segment

    ``gateway: <ipv4_address>``, the gateway of the local network segment


:Example:
    .. code-block::

        # set
        input:  C_IPADDRESS 192.168.1.100 255.255.255.0 192.168.1.1
        output: <OK>

        # get
        input:  C_IPADDRESS ?
        output: C_IPADDRESS 192.168.1.100 255.255.255.0 192.168.1.1


``C_DHCP``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_DHCP <on_off>

    # get
    C_DHCP ?

:Description:
    Controls whether the chassis will use DHCP to get the management IP address.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, whether DHCP is enabled or disabled.

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  C_DHCP OFF
        output: <OK>

        # get
        input:  C_DHCP ?
        output: C_DHCP OFF


``C_MACADDRESS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_MACADDRESS ?

:Description:
    Get the MAC address for the chassis management port.

:Actions:
    get

:Parameter:
    ``mac_address: <mac_address>``, the MAC address for the chassis management port

:Example:
    .. code-block::

        # get
        input:  C_MACADDRESS ?
        output: C_MACADDRESS 0x00187DBA1111


``C_HOSTNAME``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_HOSTNAME <hostname>

    # get
    C_HOSTNAME ?

:Description:
    Get or set the chassis hostname used when DHCP is enabled.

:Actions:
    set, get

:Parameter:
    ``hostname: <string>``, the chassis hostname


:Example:
    .. code-block::

        # set
        input:  C_HOSTNAME "xena-12345"
        output: <OK>

        # get
        input:  C_HOSTNAME ?
        output: C_HOSTNAME "xena-12345"


``C_FLASH``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_FLASH <on_off>

    # get
    C_FLASH ?

:Description:
    Make all the test port LEDs flash on and off with a 1-second interval. This is
    helpful if you have multiple chassis mounted side by side and you need to
    identify a specific one.

    NOTICE: Require Tester to be reserved before change value.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, determines whether to blink all test port LEDs.

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  C_FLASH OFF
        output: <OK>

        # get
        input:  C_FLASH ?
        output: C_FLASH OFF


``C_DEBUGLOGS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_DEBUGLOGS ?

:Description:
    Allows to dump all the logs of a chassis.

:Actions:
    get

:Parameter:
    ``message_length: <integer>``, length of the message.
    ``data: <List[hex]>``, all the logs of a chassis

:Example:
    .. code-block::

        # get
        input:  C_DEBUGLOGS ?
        output: C_DEBUGLOGS 16 0x51525354515253545152535451525354


``C_TEMPERATURE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_TEMPERATURE ?

:Description:
    Get chassis temperature readings, if supported. Unit is millidegree Celsius.

:Actions:
    get

:Parameter:
    ``mb1_temperature: <integer>``, the temperature of motherboard 1 (millidegree Celsius).
    ``mb2_temperature: <integer>``, the temperature of motherboard 2 (millidegree Celsius).
    ``cpu_temperature: <integer>``, the temperature of CPU (millidegree Celsius).

:Example:
    .. code-block::

        # get
        input:  C_TEMPERATURE ?
        output: C_TEMPERATURE 0 0 52000


``C_RESTPORT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_RESTPORT <tcp_port>

    # get
    C_RESTPORT ?

:Description:
    The TCP port used by the REST API server.

:Actions:
    set, get

:Parameter:
    ``tcp_port: <integer>``, the TCP port number (default 57911)


:Example:
    .. code-block::

        # set
        input:  C_RESTPORT 8111
        output: <OK>

        # get
        input:  C_RESTPORT ?
        output: C_RESTPORT 8111


``C_RESTENABLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_RESTENABLE <on_off>

    # get
    C_RESTENABLE ?

:Description:
    Controls whether the chassis will run REST API server or not. The command takes
    affect only after chassis reset. To start/stop REST API server use ``C_RESTCONTROL`` command.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, determines whether REST API server should be enabled or disabled

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  C_RESTENABLE OFF
        output: <OK>

        # get
        input:  C_RESTENABLE ?
        output: C_RESTENABLE OFF


``C_RESTCONTROL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_RESTCONTROL <operation>


:Description:
    Controls REST API server. This command should be used with extra care as it can
    affect other users using the server.

:Actions:
    set

:Parameter:
    ``operation: <RESTControlAction>``, what to do with the REST API server

        * ``START = 0``
        * ``STOP = 1``
        * ``RESTART = 2``

:Example:
    .. code-block::

        # set
        input:  C_RESTCONTROL START
        output: <OK>



``C_RESTSTATUS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_RESTSTATUS ?

:Description:
    Gets the REST API server operation status - whether it is active (running) or
    not. To get the admin status (whether the server is enabled or disabled) use
    ``C_RESTCONTROL`` command.

:Actions:
    get

:Parameter:
    ``status: <ServiceStatus>``, the operation status of th REST API server

        * ``SERVICE_OFF = 0``
        * ``SERVICE_ON = 1``

:Example:
    .. code-block::

        # get
        input:  C_RESTSTATUS ?
        output: C_RESTSTATUS SERVICE_ON


``C_WATCHDOG``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_WATCHDOG <timer_value>

    # get
    C_WATCHDOG ?

:Description:
    If the chassis stalls for a long time, when the timer expires the chassis will
    be rebooted automatically.

:Actions:
    set, get

:Parameter:
    ``timer_value: <integer>``, the timer value that reboots the chassis


:Example:
    .. code-block::

        # set
        input:  C_WATCHDOG 1
        output: <OK>

        # get
        input:  C_WATCHDOG ?
        output: C_WATCHDOG 1


``C_INDICES``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_INDICES ?

:Description:
    Gets the session indices for all current sessions on the chassis.

:Actions:
    get

:Parameter:
    ``session_ids: <List[integer]>``, the session indices for all current sessions on the chassis

:Example:
    .. code-block::

        # get
        input:  C_INDICES ?
        output: C_INDICES 1 2 3


``C_STATSESSION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_STATSESSION [<ession_xindex>] ?

:Description:
    Gets information and statistics for a particular session on the chassis.

:Actions:
    get

:Parameter:
    ``session_type: <ChassisSessionType>``, type of session

        * ``MANAGER = 1``
        * ``SCRIPT = 2```

    ``ipv4_address: <ipv4_address>``, client IP address
    ``owner: <string>``, the name of the session owner
    ``operation_count: <long>``, number of operations done during the session
    ``requested_byte_count: <long>``, number of bytes received by the chassis
    ``responded_byte_count: <long>``, number of bytes sent by the chassis

:Example:
    .. code-block::

        # get
        input:  C_STATSESSION [0] ?
        output: C_STATSESSION [0] SCRIPT 10.10.10.10 "spongebob" 12 208 2736548


``C_TKLICFILE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_TKLICFILE <license_content>

    # get
    C_TKLICFILE ?

:Description:
    Get Xena TimeKeeper license file content.

:Actions:
    set, get

:Parameter:
    ``license_content: <List[byte]>``, Xena TimeKeeper license file content


:Example:
    .. code-block::

        # set
        input:  C_TKLICFILE 0x51525354515253545152535451525354
        output: <OK>

        # get
        input:  C_TKLICFILE ?
        output: C_TKLICFILE 0x51525354515253545152535451525354


``C_TKLICSTATE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_TKLICSTATE ?

:Description:
    Get the state of the Xena TimeKeeper license file content.

:Actions:
    get

:Parameter:
    ``license_file_state: <TimeKeeperLicenseFileState>``, Xena TimeKeeper license file content
        
        * ``NA = 0``
        * ``INV = 1``
        * ``VALID = 2``

    ``license_type: <TimeKeeperLicenseType>``, Xena TimeKeeper license file content

        * ``UNDEF = 0``
        * ``CLIENT = 1``
        * ``SERVER = 2``

:Example:
    .. code-block::

        # get
        input:  C_TKLICSTATE ?
        output: C_TKLICSTATE VALID CLIENT


``C_FILESTART``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_FILESTART <file_type> <size> <time> <mode> <checksum> <name>


:Description:
    Initiates upload of a file to the chassis. This command should be followed by
    a sequence og ``C_FILEDATA`` parameters to provide the file content, and finally a
    ``C_FILEFINISH`` to commit the new file to the chassis.

:Actions:
    set

:Parameter:
    ``file_type: <hex hex hex hex>``, the file type, should be 1

    ``size: <hex hex hex hex>``, the number of bytes in the file

    ``time: <hex hex hex hex>``, he Linux date+time of the file

    ``mode: <hex hex hex hex>``, the Linux permissions of the file

    ``checksum: <hex hex hex hex>``, the checksum of the file

    ``name: <string>``, the name and location of the file, as a full path


:Example:
    .. code-block::

        # set
        input:  C_FILESTART 0x01000000 0xF1B2C3E4 0x12341234 0x00000000 0x43ED5611 "/xbin/xenaserver"
        output: <OK>



``C_FILEDATA``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_FILEDATA <offset> <data_bytes>


:Description:
    Uploads a fragment of a file to the chassis.

:Actions:
    set

:Parameter:
    ``offset: <integer>``, the position within the file

    ``data_bytes: <List[hex]>``, the data content of a section of the file


:Example:
    .. code-block::

        # set
        input:  C_FILEDATA 1 0xABCDEFABCDEFABCDEFABCDEFABCDEFABCDEFABCDEF
        output: <OK>



``C_FILEFINISH``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_FILEFINISH


:Description:
    Completes upload of a file to the chassis. After validation it will replace any
    existing file with the same name.

:Actions:
    set

:Parameter:
    

:Example:
    .. code-block::

        # set
        input:  C_FILEFINISH
        output: <OK>



``C_TRAFFIC``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_TRAFFIC <on_off> <module_ports>


:Description:
    Starts or stops the traffic on a number of ports on the chassis simultaneously.
    The ports are identified by pairs of integers (module port).

:Actions:
    set

:Parameter:
    ``on_off: <OnOff>``, determines whether to start or stop traffic generation

        * ``OFF = 0``
        * ``ON = 1``

    ``module_ports: <>``, specifies ports on modules, which should stop or start generating traffic


:Example:
    .. code-block::

        # set
        input:  C_TRAFFIC OFF 0 0 0 1
        output: <OK>



``C_VERSIONNO_MINOR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_VERSIONNO_MINOR ?

:Description:
    Gets the minor version number for the chassis firmware. The full version of
    the chassis firmware is thus where the number is obtained  with the ``C_VERSIONNO``
    command and the number is obtained with the ``C_VERSIONNO_MINOR`` command.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  C_VERSIONNO_MINOR ?
        output: C_VERSIONNO_MINOR


``C_START``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_START <module_ports>


:Description:
    Start traffic on N ports and each port is described by (module index, port
    index).

:Actions:
    set

:Parameter:
    ``module_ports: <>``, specifies ports on modules, which should stop or start generating traffic


:Example:
    .. code-block::

        # set
        input:  C_START 0 0 0 1
        output: <OK>



``C_STOP``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_STOP <module_ports>


:Description:
    Stop traffic on N ports and each port is described by (module index, port index)

:Actions:
    set

:Parameter:
    ``module_ports: <>``, specifies ports on modules, which should stop or start generating traffic


:Example:
    .. code-block::

        # set
        input:  C_STOP 0 0 0 1
        output: <OK>



``C_MULTIUSER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_MULTIUSER <on_off>

    # get
    C_MULTIUSER ?

:Description:
    Enable or disable the ability to control one resource from several different TCP
    connections.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, enable or disable the ability to control one resource from several different TCP connections

        * ``OFF = 0``
        * ``ON = 1``

:Example:
    .. code-block::

        # set
        input:  C_MULTIUSER OFF
        output: <OK>

        # get
        input:  C_MULTIUSER ?
        output: C_MULTIUSER OFF


``C_SCRIPT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_SCRIPT <command_string>


:Description:
    To load and save CLI commands e.g. port configuration, through the binary XMP session.

:Actions:
    set

:Parameter:
    ``command_string: <string>``, text CLI command


:Example:
    .. code-block::

        # set
        input:  C_SCRIPT word
        output: <OK>



``C_TKSTATUS``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_TKSTATUS ?

:Description:
    Report TimeKeeper version and status.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  C_TKSTATUS ?
        output: C_TKSTATUS


``C_TKSVCSTATE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_TKSVCSTATE <state>

    # get
    C_TKSVCSTATE ?

:Description:
    Get and control TimeKeeper service state.

:Actions:
    set, get

:Parameter:
    ``state: <TimeKeeperServiceAction>``, TimeKeeper service state

        * ``STOP = 0``
        * ``START = 1``
        * ``RESTART = 2``

:Example:
    .. code-block::

        # set
        input:  C_TKSVCSTATE STOP
        output: <OK>

        # get
        input:  C_TKSVCSTATE ?
        output: C_TKSVCSTATE STOP


``C_TKCONFIG``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_TKCONFIG <config_file>

    # get
    C_TKCONFIG ?

:Description:
    TimeKeeper config file content.

:Actions:
    set, get

:Parameter:
    ``config_file: <string>``, TimeKeeper config file content


:Example:
    .. code-block::

        # set
        input:  C_TKCONFIG word
        output: <OK>

        # get
        input:  C_TKCONFIG ?
        output: C_TKCONFIG word


``C_TKGPSSTATE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_TKGPSSTATE ?

:Description:
    Get TimeKeeper GPS status.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  C_TKGPSSTATE ?
        output: C_TKGPSSTATE


``C_TIME``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_TIME ?

:Description:
    Get local chassis time in seconds.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  C_TIME ?
        output: C_TIME


``C_TRAFFICSYNC``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # set
    C_TRAFFICSYNC <on_off> <timestamp> <module_ports>

    # get
    C_TRAFFICSYNC ?

:Description:
    Works just as the ``C_TRAFFIC`` command described above with an additional option to
    specify  a point in time where traffic should be started. This can be used to
    start traffic simultaneously on multiple chassis. The ports are identified by
    pairs of integers (module port).
    
    .. note::
    
        This requires that the chassis in question all use the TimeKeeper option to keep their CPU clocks synchronized.

:Actions:
    set, get

:Parameter:
    ``on_off: <OnOff>``, determines whether to start or stop traffic generation

        * ``OFF = 0``
        * ``ON = 1``

    ``timestamp: <integer>``, the time where traffic should be started, expressed as the number of seconds since January 1 2010, 00

    ``module_ports: <>``, specifies ports on modules, which should stop or start traffic generation.


:Example:
    .. code-block::

        # set
        input:  C_TRAFFICSYNC OFF 2147483647 0 0 0 1
        output: <OK>

        # get
        input:  C_TRAFFICSYNC ?
        output: C_TRAFFICSYNC OFF 2147483647 0 0 0 1


``C_TKSTATUSEXT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_TKSTATUSEXT ?

:Description:
    Report TimeKeeper version and status (extended version).

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  C_TKSTATUSEXT ?
        output: C_TKSTATUSEXT


``C_EXTNAME``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # get
    C_EXTNAME ?

:Description:
    Get the chassis extension name.

:Actions:
    get

:Parameter:
    

:Example:
    .. code-block::

        # get
        input:  C_EXTNAME ?
        output: C_EXTNAME



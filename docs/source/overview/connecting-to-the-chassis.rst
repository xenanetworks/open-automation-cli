Connecting to the Chassis
==========================================

The chassis support multiple concurrent scripting sessions, just like they support multiple concurrent interactive Manager sessions. And like Manager sessions, scripting sessions interact with the chassis in its current state; establishing a scripting session does not in itself impact the chassis state.

In order to start a CLI scripting session, you establish a TCP/IP connection with the chassis using port ``22611``, on the same IP address as when using Manager applications.

You then send lines of ASCII text to the chassis, terminated by ``CR/LF``, and receive lines of ASCII text in response. The first command should be a logon with the valid password for the chassis, or the session will be terminated.

You can use any client platform that is able to establish a TCP/IP connection and send and receive lines of text through it. Typical client platforms include Tcl, Perl, Python, Java, Excel/VBA, and Telnet. You may use client-side functionality to execute script commands conditionally or repetitively.

.. important::
    
    All lines sent to the chassis must be terminated by ``CR/LF``. You will need to include these characters explicitly if the connection library of your platform does not do so automatically.

.. note::
    
    Also please make sure to read all the responses sent back to you from the chassis, so that the buffer is empty when the connection is eventually closed down.

Xena also provides a simple interactive scripting client application, *XenaScriptClient*, that runs on Windows and allows you to manually type commands to the chassis and see its responses.

.. figure:: /_static/xena_script_client.png
    :scale: 100 %
    :alt: XenaScriptClient
    :align: center

    XenaScriptClient

To keep the session alive the client must show some activity every minute or so; else the chassis will assume that the client has stopped, and there are also routers that will kill a TCP session that is inactive for more than a few minutes. The simplest way is to send an empty line, and the chassis will also respond with an empty line. The timeout interval can be changed with the ``C_TIMEOUT`` command so that for instance ``C_TIMEOUT 99999`` effectively disables the timeout.

Chassis resources must as always be reserved before they can be updated, whereas you can view any chassis, module, or port command as soon as the session is logged on. Reserving and releasing is done through the ``C/M/P_RESERVATION`` commands.

Before reservation, a user name must be provided for the scripting session using the ``C_OWNER`` command. If the chassis has resources reserved for this username they will automatically be granted to this session.

Any line starting with a semicolon is treated as a comment and ignored by the chassis, e.g.

.. code-block::
    :linenos:

    ;This this a comment

Commands to the chassis are not case-sensitive, and replies from the chassis are in uppercase.


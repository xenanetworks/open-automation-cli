XOA CLI Explained
==========================================

The XOA CLI commands are simple lines of text exchanged between a client and the chassis. An example command to the chassis could be:

.. code-block::
    :linenos:

    0/5 PS_RATEPPS [3] 500000

This goes to module 0, port 5, and sets stream 3's rate to 500000 packets per second. The chassis responds with:

.. code-block::
    :linenos:

    <OK>

You would query for the current parameter this way:

.. code-block::
    :linenos:

    0/5 PS_RATEPPS [3] ?

And the chassis would respond in exactly the same way that you set the parameter yourself:

.. code-block::
    :linenos:

    0/5 PS_RATEPPS [3] 500000

This document contains a general overview of the scripting mechanism, followed by reference sections describing each group of scriptable commands in detail. There are a few hundred commands in total, but only a handful is required for typical simple tasks.

To set up basic traffic patterns and obtain traffic statistics, use the port commands (starting with ``P_…``), the stream commands (starting with ``PS_…``), and the transmit/receive statistics commands (starting with ``PT_…`` and ``PR_…``).

At the end of the overview sections there is a complete example of how to use a collection of script commands to define and execute some simple operations on a chassis.

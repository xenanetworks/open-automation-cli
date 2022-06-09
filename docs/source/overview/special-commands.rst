Special Commands
==========================================

The CLI environment provides a few commands that do not directly interact with the chassis state, but rather support the CLI process itself.

* ``SYNC``. This command simply produces a reply of, which can be helpful when parsing and delimiting the lines returned from the chassis, in particular when using multi-command queries. You can also do ``SYNC ON``, which will subsequently cause an automatic ``SYNC`` after each command. ``SYNC OFF`` disables this.
* ``WAIT <n>``. This command waits for ``<n>`` number of seconds, up to 60, and then produces a reply of. This is a simple mechanism for inserting pauses into scripts that are contained in a file and simply sent to the chassis line-by-line. Longer waits and more sophisticated automation require client-side functionality, which must also handle the keep-alives.
* ``HELP ?``. This command gives you an overview of the built-in help function, useful when using the scripting environment interactively, as from the XenaScriptingClient.
* ``HELP ''<command>''``. Gives you a brief overview of the required indices and parameters for ``''<command>''``. You are allowed to specify only a prefix of the command name, which will then give you the overview for each matching command, e.g. ``HELP ''P_''`` for all port-level commands. The summary of the required parameters uses the abbreviations for the various types introduced in the command syntax above, e.g. ``B(0=OFF,1=ON)``, which means a single-byte parameter where the two relevant parameters can be specified using coded names.


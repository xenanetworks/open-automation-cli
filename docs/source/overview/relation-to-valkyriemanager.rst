Relation to ValkyrieManager
==========================================

Basically anything you can do with ValkyrieManager (and VulcanManager) applications you can also do via CLI commands, and the correspondence is quite straightforward. For example, just as the ValkyrieManager's **Port Properties** panel has a field for viewing and changing a port's minimum inter-frame gap, the CLI interface can view and change the ``P_INTERFRAMEGAP`` command for doing the same. The same applies to most of the other fields of the Manager's user interface.

.. figure:: /_static/inter_frame_gap.png
    :scale: 60 %
    :alt: Inter-Frame Gap
    :align: center

    Min. Average Inter-Frame Gap field in ValkyrieManager 

However, there are a few areas where the Manager has more advanced functionality, which is missing in the CLI commands. This does not limit what you can do, but the way you must do it is more primitive.

* **Stream rates and capping.** When you specify the rate of a stream using either a percentage, layer-2 Mbps, or packets per second, the Manager calculates the equivalent rates using the other two methods. It also checks that you do not exceed the available bandwidth for the port. This is not available through scripting: you just specify the rate using your method of choice, and you must take care not to exceed the available bandwidth.

* **Protocol field editing.** The Manager knows the field-by-field layout of various common protocols and allows you to inspect and edit packet data at the field level. With scripting, you just specify packet data as a sequence of hexadecimal bytes.

* **Filter conditions.** The Manager allows you to enter filter conditions as an easy-to-read Boolean expression on the various terms. With scripting, you need to encode the condition using a set of bitmasks.

* **Capture protocol decoding.** The Manager inspects the raw bytes of captured packets in order to identify the protocols at the header of the packet. With scripting, you must decode the packet data yourself if needed.

Also, the Manager will disable the user-interface whenever a particular operation is not currently allowed; for instance trying to update the configuration of a port that has not been reserved, changing a command for an enabled stream while traffic is on, or changing a filter term used in the condition of an enabled filter. Attempting such things in a scripting session will instead lead to error status messages.

At a more fundamental level, the Manager supports the notion of a testbed containing multiple chassis. This is not applicable through scripting since each scripting session runs through its own connection to a single chassis, and indeed the chassis are not aware of each other. Any cross-chassis control must be handled at the scripting client environment; in particular cross-chassis statistics such as packet loss.

In contrast, the CLI environment provides :ref:`wildcarding <Overview:Defaults and Wildcarding>` across modules and ports, which is not available through the Manager.

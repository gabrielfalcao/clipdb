clipdb
======

clipdb (aka "CLI pdb") is a drop-in replacement for `ipdb
<https://pypi.org/project/ipdb/>`_ which handles ``KeyboardInterrupt``
nicely, that is, when the user presses ``Control-C``, there is no
unnecesary output regarding the act of doing just so like that.

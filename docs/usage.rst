=====
Usage
=====
- Import codemelli
.. code-block:: python

    >>> import codemelli

- Validate a real codemelli

.. code-block:: python

    >>> codemelli.validator(2833411839)
    True

- Validate a fake codemelli

.. code-block:: python

    >>> codemelli.validator(3235632189)
    False

- Generate a random valid codemelli

.. code-block:: python

    >>> codemelli.generator()
    6615365987

- Generate a random codemelli with a defined city code

.. code-block:: python

    >>> codemelli.generator(223)
    2239832630

- Lookup city and state of a valid codemelli

.. code-block:: python

    >>> codemelli.lookup(2239832630)
    {'city': 'بندرترکمن', 'state': 'گلستان'}


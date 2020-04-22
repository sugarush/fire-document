About
=====

Sugar Document provides two classes for accessing `dictionaries` with the
dot syntax, `Document` and `Documents`.

Installation
------------

Suagr Document can be installed with `pip`.

``pip install git+https://github.com/sugarush/sugar-document@master``

Usage
-----

`dict` example:

.. code-block:: python

  from sugar_document import Document

  doc = Document({ 'some': { 'nested': 'value' } })

  assert doc.some.nested == 'value'

`list` example:

.. code-block:: python

  from sugar_document import Documents

  docs = Documents([
    { 'some': { 'nested': 'value' } },
    { 'another': { 'nested': 'value' } }
  ])

  assert docs[1].another.nested == 'value'

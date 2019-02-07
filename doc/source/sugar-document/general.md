# General

A Sugar Document transform a Python dictionary into something much more dynamic.

## Basic Usage

A __Document__ can be initialized with a dictionary.

```
from sugar_document import Document

doc = Document({ 'test': 'ing '})

doc.test # 'ing'
```

A __Document__ can be initialized with keywords.

```
from sugar_document import Document

doc = Document(test='ing')

doc.test # 'ing'
```
 A __Document__ can contain *Arrays*.

 ```
from sugar_document import Document

doc = Document({
  'items': [
    { 'field': 'value' }
  ]
})

doc.items[0].field # 'value'
```

A __Document__ cannot set values in *Arrays*.

```
from sugar_document import Document

doc = Document({
  'items': [
    { }
  ]
})

doc.items[0].field = 'value'
doc.items[0].field # None
```

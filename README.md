# ordered-set-stubs - stubs with type annotations for ordered-set Python library
## Usage
For example, you have the following code in `ordered_set_stubs_test.py` file:
```python
from ordered_set import OrderedSet


# noinspection PyPep8Naming
def receives_OrderedSet_int(ordered_set: 'OrderedSet[int]') -> 'OrderedSet[int]':
    return ordered_set


receives_OrderedSet_int(OrderedSet(['ololo']))
```

Run `mypy` to check the code and check that it returns an error:
```
$ mypy ordered_set_stubs_test.py
ordered_set_stubs_test.py:10: error: List item 0 has incompatible type "str"; expected "int"
```

In Python 3.7 you can even drop quotes:
```python
from __future__ import annotations
from ordered_set import OrderedSet


# noinspection PyPep8Naming
def receives_OrderedSet_int(ordered_set: OrderedSet[int]) -> OrderedSet[int]:
    return ordered_set


receives_OrderedSet_int(OrderedSet(['ololo']))
```

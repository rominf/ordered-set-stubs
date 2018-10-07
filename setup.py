# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['ordered_set-stubs']

package_data = \
{'': ['*']}

extras_require = \
{':(python_version >= "2.7" and python_version < "2.8") or (python_version >= "3.3" and python_version < "3.5")': ['typing>=3.6,<4.0']}

setup_kwargs = {
    'name': 'ordered-set-stubs',
    'version': '0.1.3',
    'description': 'Stubs with type annotations for ordered-set Python library',
    'long_description': '# ordered-set-stubs - stubs with type annotations for ordered-set Python library\n## Usage\nFor example, you have the following code in `ordered_set_stubs_test.py` file:\n```python\nfrom ordered_set import OrderedSet\n\n\n# noinspection PyPep8Naming\ndef receives_OrderedSet_int(ordered_set: \'OrderedSet[int]\') -> \'OrderedSet[int]\':\n    return ordered_set\n\n\nreceives_OrderedSet_int(OrderedSet([\'ololo\']))\n```\n\nRun `mypy` to check the code and check that it returns an error:\n```\n$ mypy ordered_set_stubs_test.py\nordered_set_stubs_test.py:10: error: List item 0 has incompatible type "str"; expected "int"\n```\n\nIn Python 3.7 you can even drop quotes:\n```python\nfrom __future__ import annotations\nfrom ordered_set import OrderedSet\n\n\n# noinspection PyPep8Naming\ndef receives_OrderedSet_int(ordered_set: OrderedSet[int]) -> OrderedSet[int]:\n    return ordered_set\n\n\nreceives_OrderedSet_int(OrderedSet([\'ololo\']))\n```\n',
    'author': 'Roman Inflianskas',
    'author_email': 'infroma@gmail.com',
    'url': 'https://github.com/rominf/ordered-set-stubs',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*',
}


setup(**setup_kwargs)

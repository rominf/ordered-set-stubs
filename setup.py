# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['ordered_set-stubs']

package_data = \
{'': ['*']}

install_requires = \
['typing>=3.6,<4.0']

setup_kwargs = {
    'name': 'ordered-set-stubs',
    'version': '0.1.0',
    'description': 'Stubs with type annotations for ordered-set Python library',
    'long_description': '# ordered_set-stubs\nStubs with type annotations for ordered-set Python library\n',
    'author': 'Roman Inflianskas',
    'author_email': 'infroma@gmail.com',
    'url': 'https://github.com/rominf/ordered_set-stubs',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
}


setup(**setup_kwargs)

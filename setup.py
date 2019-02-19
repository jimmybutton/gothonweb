from setuptools import find_packages, setup

config = {
    'name': 'game',
    'version': '0.1',
    'description': 'A very simple game with rooms and tests.',
    'author': 'Samuel Liedtke',
    'url': 'URL to get it at',
    'author_email': 'samu.liedtke@gmail.com',
    'install_requires': [
        'pytest',
    ],
    'packages': findpackages(),
    'scripts': []
}

setup(**config)

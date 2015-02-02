try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A program to solve sudoku for given input from a user! Or \
					really a demonstration project showing off python coding.',
    'author': 'Philip Castiglione',
    'url': 'PLACEHOLDER',
    'download_url': 'PLACEHOLDER',
    'author_email': 'philipcastiglione@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['sudokusolver'],
    'scripts': [],
    'name': 'sudokusolver'
}

setup(**config)
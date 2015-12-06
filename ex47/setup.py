try:
    from setuptools import setup
except ImportEroor:
    from distutils.core import setup

config = {
    'description': 'Exercise of 47',
    'author': 'Han'
    'url':  'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'hanfangyu12345@163.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': []
    'name': 'ex47'
}

setup(**config)

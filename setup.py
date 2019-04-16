from setuptools import setup

from domain_events import get_version

setup(
    name='domain-events',
    version=get_version(),
    license='GPLv3',
    author='Agroptima S.L.',
    author_email='developers@agroptima.com',
    description='A lightweight library with an implementation of Pub-Sub.',
    long_description=open('README.md').read(),
    url='https://github.com/agroptima/domain-events',
    download_url='https://github.com/agroptima/domain-events/releases',
    keywords=['python', 'ddd'],
    packages=['domain_events'],
    install_requires=[
        'pytz'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)

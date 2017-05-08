from setuptools import setup, find_packages

setup(
    name = 'negotiator',
    version = '1.0.0',
    packages = find_packages(),
    install_requires = [],
    url = '',
    author = 'Richard Jones',
    author_email = 'richard@cottagelabs.com',
    description = """
    Proper Content Negotiation for Python
    
    The Negotiator is a library for decision making over Content Negotiation requests.
    It takes the standard HTTP Accept headers (Accept, Accept-Language, Accept-Charset,
    Accept-Encoding) and rationalises them against the parameters acceptable by the
    server; it then makes a recommendation as to the appropriate response format.
    
    This version of the Negotiator also supports the SWORDv2 extensions to HTTP Accept
    in the form of Accept-Packaging.
    """,
    license = 'CC0',
    classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)


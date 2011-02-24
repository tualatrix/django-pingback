from setuptools import setup, find_packages

setup(
    name = 'django-pingback',
    version = __import__('pingback').__version__,
    description = 'Pingback client and server for Django web framework, extracted from Byteflow blog engine.',
    keywords = 'django apps',
    license = 'New BSD License',
    author = 'Alexander Solovyov',
    author_email = 'piranha@piranha.org.ua',
    url = 'http://hg.piranha.org.ua/django-pingback/',
    install_requires = ['django-xmlrpc>=0.1.0'],
    dependency_links = ['http://pypi.aartemenko.com'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = find_packages(),
    include_package_data = True,
)


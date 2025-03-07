"""setuptools setup module for oauth-dropins.

Docs:
https://packaging.python.org/en/latest/distributing.html
http://pythonhosted.org/setuptools/setuptools.html

Based on https://github.com/pypa/sampleproject/blob/master/setup.py
"""
from setuptools import setup, find_packages


setup(name='oauth-dropins',
      version='4.0',
      description='Drop-in OAuth Flask views for many popular sites.',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      url='https://github.com/snarfed/oauth-dropins',
      packages=find_packages(),
      include_package_data = True,
      author='Ryan Barrett',
      author_email='oauth-dropins@ryanb.org',
      license='Public domain',
      python_requires='>=3.6',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Topic :: System :: Systems Administration :: Authentication/Directory',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Environment :: Web Environment',
          'License :: OSI Approved :: MIT License',
          'License :: Public Domain',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
      ],
      keywords='oauth appengine',
      install_requires=[
          'beautifulsoup4~=4.8',
          'cachetools>=3.1,<5.0',
          'domain2idna~=1.12',
          'flask~=2.0.1',
          'flask-caching~=1.10.1',
          'gdata-python3~=3.0',
          'google-cloud-ndb>=1.10.1,<1.12.0',
          'humanize>=3.1.0,<4.0',
          'jinja2>=2.10,<4.0',
          'mf2py~=1.1,>=1.1.2',
          'mf2util>=0.5.0',
          'oauthlib~=3.1',
          'praw>=7.3.0,<8.0',
          'python-tumblpy~=1.1',
          'requests-oauthlib',
          'requests~=2.22',
          'tweepy<=4.4',
          'ujson>=5.1',
          'urllib3~=1.14',
          'webapp2>=3.0.0b1',
      ],
      tests_require=['mox3>=0.28,<2.0'],
)

from setuptools import setup, find_packages
import os

version = '2.0.3.dev0'

tests_require = [
    'ftw.builder',
    'ftw.testbrowser',
    'ftw.testing',
    'plone.app.testing',
]


setup(name='ftw.theming',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" + open(
          os.path.join("docs", "HISTORY.txt")).read(),

      classifiers=[
          "Environment :: Web Environment",
          'Framework :: Plone',
          'Framework :: Plone :: 4.3',
          'Framework :: Plone :: 5.1',
          "Intended Audience :: Developers",
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],

      keywords='ftw theming',
      author='4teamwork AG',
      author_email='mailto:info@4teamwork.ch',
      url='https://github.com/4teamwork/ftw.theming',
      license='GPL2',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
          'Plone',
          'cssselect',
          'ftw.upgrade',
          'ftw.profilehook',
          'lxml',
          'path.py',
          'pyScss >= 1.3',
          'six >= 1.4.0',  # six.unichr
          'setuptools',
          'tarjan',
      ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
)

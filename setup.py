from setuptools import setup, find_packages
import os

version = '1.2'

setup(name='cs.portlet.aemet',
      version=version,
      description="A portlet to show the weather via AEMET",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='weather portlet plone aemet',
      author='Dani Reguera',
      author_email='dreguera@codesyntax.com',
      url='http://code.codesyntax.com/private/cs.portlet.aemet',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cs', 'cs.portlet'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'lxml',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

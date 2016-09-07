Introduction
============

This products creates a portlet to show weather information
as provided by AEMET_ .

It parses an XML file and creates a data structure to create
a portlet based on a structure similar to the one provided by
the product Meteo_ . This product worked great, but due to
the constantly changing HTML of the AEMET_ site, it failed easily.

Now AEMET provides a fixed XML for each place, so you just have
to create a portlet and type the URL of the XML file you want
to show. The parsing results are cached in memory using
`plone.memoize`_'s RAMCache.

If you want to customize the look and feel of the portlet, use
`z3c.jbot`_ and look at the internals of the dict created after
parsing the XML at aemetparser.py file.

You can see examples of customization of this portlet at:

-  http://www.aretxabaleta.eus
-  http://www.eibar.eus
-  http://www.deba.eus

Compatibility
==============

Tested on Plone 4.0.x, 4.1, 4.2 and 4.3 Not tested on Plone 3.3.x but it should work.


Credits
========

- Idea: GMV_ for Meteo_
- AEMET_: for providing weather information freely available (always giving credit) in Spain.
- Parsing code and portlet implementation: Dani Reguera <dreguera@codesyntax.com>
- Plone goodies, doc and i18n: Mikel Larreategi <mlarreategi@codesyntax.com>

.. _AEMET: http://www.aemet.es
.. _Meteo: http://plone.org/products/meteo
.. _`z3c.jbot`: http://pypi.python.org/pypi/z3c.jbot
.. _GMV: http://www.gmv.com/en/
.. _`plone.memoize`: http://pypi.python.org/pypi/plone.memoize

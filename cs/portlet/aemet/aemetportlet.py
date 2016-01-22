from aemetparser import parseXML
from cs.portlet.aemet import AEMETPortletMessageFactory as _
from plone.app.portlets.portlets import base
from plone.memoize.ram import cache
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope import schema
from zope.formlib import form
from zope.interface import implements
from Acquisition import aq_inner
from time import time


class IAEMETPortlet(IPortletDataProvider):
    """A portlet

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """

    portlet_title = schema.TextLine(
        title=_(u"Title"),
        description=_(u"Enter the title of the portlet"),
        required=True,
    )

    url = schema.TextLine(
        title=_(u"URL"),
        description=_(u"Enter the URL of the XML file with the weather data"),
        required=True,
    )

    daynumber = schema.Int(
        title=_('Day number to show'),
        description=_('The number of days to show in the portlet'),
        required=True,
    )


class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IAEMETPortlet)

    def __init__(self, portlet_title=u"", url=u'', daynumber=0):
        self.portlet_title = portlet_title
        self.url = url
        self.daynumber = daynumber

    def title(self):
        return self.portlet_title


class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """

    render = ViewPageTemplateFile('aemetportlet.pt')

    def title(self):
        return self.data.portlet_title

    def _render_cache_key(func, item):
        context = aq_inner(item.context)
        return [context.absolute_url(), time() // (43200)]

    @cache(_render_cache_key)
    def get_weather(self):
        try:
            data = parseXML(self.data.url)
            return data[:self.data.daynumber]
        except:
            return []


class AddForm(base.AddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    form_fields = form.Fields(IAEMETPortlet)

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(IAEMETPortlet)

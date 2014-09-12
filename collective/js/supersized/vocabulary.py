from Products.CMFCore.utils import getToolByName
from zope.interface import directlyProvides
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory

try:
    from zope.app.component.hooks import getSite
except ImportError:
    from zope.component.hooks import getSite

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.js.supersized')

def format_size(size):
    return "".join(size).split(' ')[0]


def ImageSizeVocabulary(context):
    site = getSite()
   
    portal_properties = getToolByName(site, 'portal_properties', None)
    if 'imaging_properties' in portal_properties.objectIds():
        sizes = portal_properties.imaging_properties.getProperty('allowed_sizes')
        sizes += ('original',)
        terms = [ SimpleTerm(value=format_size(pair), token=format_size(pair), title=pair) for pair in sizes ]
        return SimpleVocabulary(terms)
    else:
        return SimpleVocabulary([
            SimpleTerm('preview', 'preview', u'Preview'),
            SimpleTerm('large', 'large', u'Large'),
        ])  
      
    return SimpleVocabulary(terms)

directlyProvides(ImageSizeVocabulary, IVocabularyFactory)

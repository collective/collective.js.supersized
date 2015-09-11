from Products.CMFCore.utils import getToolByName
from zope.interface import directlyProvides
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from plone import api

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
    #default vocabulary if everything else fails
    sizes = None
    terms = [
            SimpleTerm('mini', 'mini', u'Mini'),
            SimpleTerm('preview', 'preview', u'Preview'),
            SimpleTerm('large', 'large', u'Large'),
            SimpleTerm('original', 'original', u'Original'),
        ]
        
    try:
        #Plone 5
        sizes = api.portal.get_registry_record('plone.allowed_sizes')
    except: 
        #Plone 4
        portal_properties = api.portal.get_tool(name='portal_properties')
        if 'imaging_properties' in portal_properties.objectIds():
            sizes = portal_properties.imaging_properties.getProperty('allowed_sizes')

    if sizes:
        if not 'original' in sizes:
            sizes += ('original',)
        terms = [ SimpleTerm(value=format_size(pair), token=format_size(pair), title=pair) for pair in sizes ]
      
    return SimpleVocabulary(terms)
    
directlyProvides(ImageSizeVocabulary, IVocabularyFactory)
    
def TransitionVocabulary(context):
    return SimpleVocabulary([
            SimpleTerm(0, 0,
                _(u"label_transition0", default=u"None")),
            SimpleTerm(1, 1,
                _(u"label_transition1", default=u"Fade")),
            SimpleTerm(2, 2,
                _(u"label_transition2", default=u"Slide Top")),
            SimpleTerm(3, 3,
                _(u"label_transition3", default=u"Slide Right")),
            SimpleTerm(4, 4,
                _(u"label_transition4", default=u"Slide Bottom")),
            SimpleTerm(5, 5,
                _(u"label_transition5", default=u"Slide Left")),
            SimpleTerm(6, 6,
                _(u"label_transition6", default=u"Carousel Right")),
            SimpleTerm(7, 7,
                _(u"label_transition7", default=u"Carousel Left")
            )
     ])

directlyProvides(TransitionVocabulary, IVocabularyFactory)

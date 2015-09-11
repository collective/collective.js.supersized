from zope import schema
from zope.interface import Interface
from z3c.form import interfaces
from zope.interface import alsoProvides
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.js.supersized')


class ISupersizedSettings(form.Schema):
    """Adds supersized settings to medialog.controlpanel
        """
    form.fieldset(
        'supersized',
        label=_(u'supersized'),
            fields=[
              'min_width',
              'min_height',
              'vertical_center',
              'horizontal_center',
              'fit_always',
              'fit_portrait',
              'fit_landscape',
              'imagesize',
              'transition',
            ],
    )

    min_width = schema.Int(
        title=_(u"min_width", 
            default=u"min_width"),
        description=_(u"help_min_width",
            default="Minimum width in pixels")
    )

    min_height = schema.Int(
        title=_(u"min_height", 
            default=u"min_height"),
        description=_(u"help_min_height",
            default="Minimum height in pixels")
    )

    vertical_center = schema.Bool(
        title=_(u"vertical_center", 
            default=u"vertical_center"),
        description=_(u"help_vertical_center",
            default="Should the images center vertically")
    )
    
    horizontal_center = schema.Bool(
        title=_(u"horizontal_center", 
            default=u"horizontal_center"),
        description=_(u"help_horizontal_center",
            default="Should the images center horizontally")
    ) 


    fit_always = schema.Bool(
        title=_(u"fit_always", 
            default=u"fit_always"),
        description=_(u"help_fit_always",
            default="Should all images fit.")
    )   

    fit_portrait  = schema.Bool(
        title=_(u"fit_portrait", 
            default=u"fit_portrait"),
        description=_(u"help_fit_portrait",
            default="Should portrait images fit.")
    )    

    fit_landscape  = schema.Bool(
        title=_(u"fit_landscape", 
            default=u"fit_landscape"),
        description=_(u"help_fit_landscape",
            default="Should the landscape images fit")
    )
    
    imagesize = schema.Choice(
        title = _("label_imagesize", default=u"Size for image"),
        description = _("help_imagesize",
                      default="Choose Size"),
        vocabulary='collective.js.supersized.ImageSizeVocabulary',
    )
    
    transition = schema.Choice(
        title=_(u"label_transition",
            default=u"Transition"),
        vocabulary='collective.js.supersized.TransitionVocabulary',
    )
    
alsoProvides(ISupersizedSettings, IMedialogControlpanelSettingsProvider)

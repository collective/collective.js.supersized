# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from Products.CMFCore.utils import getToolByName
from plone import api
from collective.js.supersized.interfaces import ISupersizedSettings

from plone.dexterity.utils import iterSchemata
from zope.schema import getFields
from plone.dexterity.interfaces import IDexterityContent

from plone.namedfile.field import NamedBlobImage

class SupersizedViewlet(ViewletBase):
    """ A viewlet which renders the background image """
    
    render = ViewPageTemplateFile('viewlet.pt')
    
    @property
    def imagefields(self):
        size = api.portal.get_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.imagesize')
        image_url_end = ''
        if size != 'original':
            image_url_end += '/'
            image_url_end += size
        
        image_fields = []
        context=self.context
        if IDexterityContent.providedBy(context):
            for schemata in iterSchemata(context):
                for name, field in getFields(schemata).items():
                    #checking for image field
                    #must be a better way to do this
                    filetype = str(context.__dict__.get(name).__class__)
                    checkfor = "<class 'plone.namedfile.file.NamedBlobImage'>"
                    if  filetype == checkfor:
                        image = {'image': str(self.context.absolute_url() + '/@@images/' + name + image_url_end) }
                        image_fields.append(image)
            if image_fields != []: 
                return image_fields
            return [{'image' : (self.context.absolute_url() + '/@@images/image/' + image_url_end) }]
    def javascript(self):
        if self.context.image:
            images = self.imagefields
            
            return u"""
<script type="text/javascript" charset="utf-8">
$(document).ready(function(){
    $.supersized({
        // Size & Position                         
        min_width               :   %(min_width)i,          // Min width allowed (in pixels)
        min_height              :   %(min_height)i,         // Min height allowed (in pixels)
        vertical_center         :   %(vertical_center)i,    // Vertically center background
        horizontal_center       :   %(horizontal_center)i,  // Horizontally center background
        fit_always              :   %(fit_always)i,         // Image will never exceed browser width or height (Ignores min. dimensions)
        fit_portrait            :   %(fit_portrait)i,       // Portrait images will not exceed browser height
        fit_landscape           :   %(fit_landscape)i,      // Landscape images will not exceed browser width
        transition              :   %(transition)i,         // how images change
                                                   
        // Components                           
        slide_links             :   'blank',    // Individual links for each slide (Options: false, 'num', 'name', 'blank')
        thumb_links             :   1,          // Individual thumb links for each slide
        slides                  :   %(images)s,
                                    
        // Theme Options               
        mouse_scrub             :   0
    });
});
</script>
""" % {
        'images' : images, 
        'min_width' :       api.portal.get_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.min_width'),
        'min_height' :      api.portal.get_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.min_height'),
        'vertical_center' : api.portal.get_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.vertical_center'),
        'horizontal_center':api.portal.get_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.horizontal_center'),
        'fit_always' :      api.portal.get_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.fit_always'),
        'fit_portrait' :    api.portal.get_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.fit_portrait'),
        'fit_landscape' :   api.portal.get_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.fit_landscape'),
        'transition'    :   api.portal.get_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.transition')
    }
    
        return ""
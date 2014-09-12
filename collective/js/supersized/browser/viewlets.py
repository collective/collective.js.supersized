# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from Products.CMFCore.utils import getToolByName
from plone import api
from collective.js.supersized.interfaces import ISupersizedSettings

class SupersizedViewlet(ViewletBase):
    """ A viewlet which renders the background image """
    
    render = ViewPageTemplateFile('viewlet.pt')

    def javascript(self):
        if self.context.image:
            image_url = self.context.absolute_url() + '/@@images/image'
            size = api.portal.get_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.imagesize')
            if size != 'original':
                image_url += '/'
                image_url += size
        
            return u"""
<script type="text/javascript" charset="utf-8">
$(document).ready(function(){
    $.supersized({
        // Size & Position                         
        min_width               :   %(min_width)i,          // Min width allowed (in pixels)
        min_height              :   %(min_height)i,         // Min height allowed (in pixels)
        vertical_center         :   %(vertical_center)i,    // Vertically center background
        horizontal_center       :   %(horizontal_center)i,  // Horizontally center background
        fit_always              :   %(fit_always)i,     // Image will never exceed browser width or height (Ignores min. dimensions)
        fit_portrait            :   %(fit_portrait)i,       // Portrait images will not exceed browser height
        fit_landscape           :   %(fit_landscape)i,      // Landscape images will not exceed browser width
                                                   
        // Components                           
        slide_links             :   'blank',    // Individual links for each slide (Options: false, 'num', 'name', 'blank')
        thumb_links             :   1,          // Individual thumb links for each slide
        slides                  :   [{image : '%(image)s'},
                                    ],
                                    
        // Theme Options               
        mouse_scrub             :   0
    });
});
</script>
""" % {
        'image' : image_url, 
        'min_width' :       api.portal.get_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.min_width'),
        'min_height' :      api.portal.get_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.min_height'),
        'vertical_center' : api.portal.get_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.vertical_center'),
        'horizontal_center':api.portal.get_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.horizontal_center'),
        'fit_always' :      api.portal.get_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.fit_always'),
        'fit_portrait' :    api.portal.get_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.fit_portrait'),
        'fit_landscape' :   api.portal.get_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.fit_landscape') 
    }
    
        return ""
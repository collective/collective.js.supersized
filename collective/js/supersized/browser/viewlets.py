# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFCore.utils import getToolByName


class SupersizedViewlet(ViewletBase):
    """ A viewlet which renders the background image """
    
    render = ViewPageTemplateFile('viewlet.pt')

    def javascript(self):
        propertiestool = getToolByName(self, 'portal_properties')
        supersized_properties = propertiestool['supersized_properties']
        
        return u"""
<script type="text/javascript" charset="utf-8">
$(document).ready(function(){
    $.supersized({
        // Size & Position						   
        min_width		        :   %(min_width)i,			// Min width allowed (in pixels)
        min_height		        :   %(min_height)i,			// Min height allowed (in pixels)
        vertical_center         :   %(vertical_center)i,	// Vertically center background
        horizontal_center       :   %(horizontal_center)i,	// Horizontally center background
        fit_always				:	%(fit_always)i,		// Image will never exceed browser width or height (Ignores min. dimensions)
        fit_portrait         	:   %(fit_portrait)i,		// Portrait images will not exceed browser height
        fit_landscape			:   %(fit_landscape)i,		// Landscape images will not exceed browser width
                                                   
        // Components							
        slide_links				:	'blank',	// Individual links for each slide (Options: false, 'num', 'name', 'blank')
        thumb_links				:	1,			// Individual thumb links for each slide
        slides 					:  	[{image : 'http://localhost:8080/cccc/logo.png'},
                                    ],
                                    
        // Theme Options			   
        mouse_scrub				:	0
    });
});
</script>
""" % {
        'image' : self.context.absolute_url(),
        'min_width'	:       supersized_properties.min_width,
        'min_height' :      supersized_properties.min_height,
        'vertical_center' : supersized_properties.vertical_center,
        'horizontal_center':supersized_properties.horizontal_center,
        'fit_always' :      supersized_properties.fit_always,
        'fit_portrait' :    supersized_properties.fit_portrait,
        'fit_landscape'	:   supersized_properties.fit_landscape,
    }
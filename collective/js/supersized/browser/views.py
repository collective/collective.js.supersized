from Products.Five.browser import BrowserView
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.interface import implements, Interface
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
#from zope.component import getMultiAdapter



class SupersizedView(BrowserView):
    """
    A browser view to be used on news items. It will show the news image as background image as background
    """
    template = ViewPageTemplateFile('supersized.pt')

    def __init__(self, context, request):
        """ init view """
        self.context = context
        propertiestool = getToolByName(self, 'portal_properties')
        supersized_properties = getattr(propertiestool, 'supersized_properties', None)
        
    def javascript(self):
        return u"""
<script type="text/javascript" charset="utf-8">
$(document).ready(function(){
    $.supersized({
        // Size & Position						   
        min_width		        :   %(min_width)i,			// Min width allowed (in pixels)
        min_height		        :   %(min_heitgh)i,			// Min height allowed (in pixels)
        vertical_center         :   %(vertical_center)i,	// Vertically center background
        horizontal_center       :   %(horizontal_center)i,	// Horizontally center background
        fit_always				:	$%(fit_always)i,		// Image will never exceed browser width or height (Ignores min. dimensions)
        fit_portrait         	:   %(fit_portrait)i,		// Portrait images will not exceed browser height
        fit_landscape			:   %(fit_landscape)i,		// Landscape images will not exceed browser width
                                                   
        // Components							
        slide_links				:	'blank',	// Individual links for each slide (Options: false, 'num', 'name', 'blank')
        thumb_links				:	%(thumb_links),			// Individual thumb links for each slide
        slides 					:  	[{image : '%(image)s/image'},
                                    ],
                                    
        // Theme Options			   
        mouse_scrub				:	%(mouse_scrub)i,
    });
});
</script>
""" % {
        'image' : self.context.absolute_url(),
        'min_width'	: getattr(supersized_properties, 'min_width', 0),
        'min_height' : getattr(supersized_properties, 'min_height', 0),
        'vertical_center' : getattr(supersized_properties, 'vertical_center', 1),
        'horizontal_center' : getattr(supersized_properties, 'horizontal_center', 1),
        'fit_always' : getattr(supersized_properties, 'fit_always', 0),
        'fit_portrait' : getattr(supersized_properties, 'fit_portrait', 0),
        'fit_landscape'	: getattr(supersized_properties, 'fit_landscape', 0),
        'thumb_links' : getattr(supersized_properties, 'thumb_lins', 1),
        'mouse_scrub' : getattr(supersized_properties, 'mouse_scrub', 0),
    }

    def css(self):
        return u"""
""" 
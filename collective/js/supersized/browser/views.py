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

    def javascript(self):
        return u"""
<script type="text/javascript" charset="utf-8">
$(document).ready(function(){
    $.supersized({
        // Size & Position						   
        min_width		        :   0,			// Min width allowed (in pixels)
        min_height		        :   0,			// Min height allowed (in pixels)
        vertical_center         :   1,			// Vertically center background
        horizontal_center       :   1,			// Horizontally center background
        fit_always				:	0,			// Image will never exceed browser width or height (Ignores min. dimensions)
        fit_portrait         	:   1,			// Portrait images will not exceed browser height
        fit_landscape			:   0,			// Landscape images will not exceed browser width
                                                   
        // Components							
        slide_links				:	'blank',	// Individual links for each slide (Options: false, 'num', 'name', 'blank')
        thumb_links				:	1,			// Individual thumb links for each slide
        slides 					:  	[{image : '%(image)s/image'},
                                    ],
                                    
        // Theme Options			   
        mouse_scrub				:	0
    });
});
</script>
""" % {
         'image' : self.context.absolute_url(),  
    }


    def css(self):
        return u"""
""" 

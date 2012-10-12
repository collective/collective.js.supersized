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

    @property
    def supersized_properties(self):
        propertiestool = getToolByName(self, 'portal_properties')
        supersized_properties = getattr(propertiestool, 'supersized_properties', None)
        
    def javascript(self):
        return u"""
<script type="text/javascript" charset="utf-8">
$(document).ready(function(){
    $.supersized({
       
    });
});
</script>
""" % {
        'image' : self.context.absolute_url(),
        'min_width'	:       getattr(self.supersized_properties, 'min_width', 0),
        'min_height' :      getattr(self.supersized_properties, 'min_height', 0),
        'vertical_center' : getattr(self.supersized_properties, 'vertical_center', 1),
        'horizontal_center' : getattr(self.supersized_properties, 'horizontal_center', 1),
        'fit_always' :      getattr(self.supersized_properties, 'fit_always', 0),
        'fit_portrait' :    getattr(self.supersized_properties, 'fit_portrait', 0),
        'fit_landscape'	:   getattr(self.supersized_properties, 'fit_landscape', 0),
    }
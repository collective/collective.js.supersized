# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName
from plone import api


 
def to_11(context):
    "move settings from properties to registry and control panel and install new stuff"
    context.runAllImportStepsFromProfile('profile-collective.js.supersized:to_11')
    
    propertiestool = getToolByName(context, 'portal_properties')
    supersized_properties = propertiestool['supersized_properties']
              
    api.portal.set_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.min_width', supersized_properties.min_width)
    api.portal.set_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.min_height',  supersized_properties.min_height)
    api.portal.set_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.vertical_center',  supersized_properties.vertical_center)
    api.portal.set_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.horizontal_center', supersized_properties.horizontal_center)
    api.portal.set_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.fit_always', supersized_properties.fit_always)
    api.portal.set_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.fit_portrait', supersized_properties.fit_portrait)
    api.portal.set_registry_record('collective.js.supersized.interfaces.ISupersizedSettings.fit_landscape', supersized_properties.fit_landscape,)
 
Introduction
============

Integration of supersized in Plone4(tested) and Plone3 (untested).

This version include supersized v3.2.7.
There is a small change from the original supersized.shutter.js (the image path), and a few in the css files.
This product is no longer used for truegallery, use collective.ptg.supersized instead

News item view
==============
You can see the "single background image mode" by 
- installing the product
- go to http://mysite/mynewsitemwithimage/@@supersized_view


Dexterity behavior
==================
Version 0.4 added a dexterity behavior.
- Add one or more imagefields to your content type… or
- Add lead image behavior to your content type
- If you add several image fields, you will get a slideshow
- There is a separate view for plone.app.contenttypes Newsitem, so you can choose if you want to use the behavior or the view. 

Example on Using it on folders
===============================
- add a folderish content type (lets call it «Myfoldertype» with a image field named «Image» (or content lead image)
- Add a content type («mytype») with supersized behvaior
- Add a «Myfoldertype» to your site
- Add a «mytype» in «Myfoldertype» and you will get the image from «Myfoldertype» supersized 


Gallery effect
==============
If you add more than one image to your content type, you will get a slideshow effect.
It will only work for images on the same content, not its parent


The control panel
=================
In the (medialog) control panel, you can choose which size to use for the background image and a few other settings..


Authors
=======

- Espen Moe-Nilssen <espen atmedialog.no>


Contributors
============

.. _supersized: http://buildinternet.com/project/supersized

-- macagua


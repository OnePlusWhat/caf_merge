#!/usr/bin/env python3.5

import subprocess
from xml.etree import ElementTree
import os

manifest = subprocess.check_output(['repo', 'manifest'])
xml_root = ElementTree.fromstring(manifest)
projects = xml_root.findall('project')
for project in projects:
    path = project.get('path')
    name = project.get('name')
    groups = project.get('groups')
    revision = project.get('revision') # Just for the lulz, don't actually do anything with it - we wanna get rid of it
    if path is not None and groups is not None:
        print ('  <project groups="%s" name="%s" path="%s" />' % (groups, name, path))
    elif path is not None:
        print ('  <project name="%s" path="%s" />' % (name, path))
    elif groups is not None:
        print('  <project groups="%s" name="%s" />' % (groups, name))
    else:
        print('  <project name="%s"' % (name))

#!/usr/bin/env python3.5
#
# Copyright � 2017, Harsh Shandilya 'MSF-Jarvis' <msfjarvis@gmail.com>
#
# This software is licensed under the terms of the GNU General Public
# License version 2, as published by the Free Software Foundation, and
# may be copied, distributed, and modified under those terms.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# Please maintain this if you use this script or any part of it
#

import subprocess
from xml.etree import ElementTree
import os

projects_to_merge = []
caf_url = "https://source.codeaurora.org/platform/"
caf_tag = "LA.BR.1.2.9_rb1.14"
build_top = os.curdir
erring_repo = []
manifest = subprocess.check_output(['repo', 'manifest'])
xml_root = ElementTree.fromstring(manifest)
projects = xml_root.findall('project')
for project in projects:
    path = project.get('path')
    revision = project.get('revision')
    if revision is None:
        projects_to_merge.append(path)
for project in projects_to_merge:
    if project is not None:
        print(project)
        count = len(project.split("/"))
        os.chdir(project)
        subprocess.call(["git", "remote", "add", "caf", caf_url + project])
        subprocess.call(["git", "fetch", "caf", caf_tag])
        ret_code = subprocess.check_call(["git", "merge", 'FETCH_HEAD'], shell=True)
        if ret_code != 0:
            erring_repo.append(project)
        os.chdir("../" * count)

print(erring_repo)

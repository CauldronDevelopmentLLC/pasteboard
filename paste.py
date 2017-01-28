#!/usr/bin/python3

################################################################################
#                                                                              #
#                Copyright (c) 2017 Cauldron Development LLC                   #
#                            All rights reserved.                              #
#                                                                              #
#           This program is free software: you can redistribute it             #
#         and/or modify it under the terms of the GNU General Public           #
#        License as published by the Free Software Foundation, either          #
#          version 3 of the License, or (at your option) any later             #
#                                  version.                                    #
#                                                                              #
#          This program is distributed in the hope that it will be             #
#         useful, but WITHOUT ANY WARRANTY; without even the implied           #
#          warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR             #
#           PURPOSE.  See the GNU General Public License for more              #
#                                  details.                                    #
#                                                                              #
#         You should have received a copy of the GNU General Public            #
#               License along with this program.  If not, see                  #
#                      <http://www.gnu.org/licenses/>.                         #
#                                                                              #
#                For information regarding this software email:                #
#              "Joseph Coffland" <joseph@cauldrondevelopment.com>              #
#                                                                              #
################################################################################

import cgi
import os
import subprocess

max_paste = 102400          # Limit to 100KiB by default
filename = '/tmp/paste.txt' # This file must be writable by the Web server
content = ''

fs = cgi.FieldStorage()

if 'shred' in fs:
    if os.path.exists(filename):
        subprocess.run(['shred', filename])
        os.unlink(filename)

elif 'paste' in fs:
    content = fs.getfirst('paste')[0:max_paste]
    f = open(filename, 'w')
    f.write(content)
    f.close()

elif os.path.exists(filename):
    f = open(filename, 'r')
    content = f.read(max_paste)
    f.close()


print('''Content-type: text/html

<!DOCKTYPE html>
<html>
  <head>
    <style type="text/css">form {display: inline-block}</style>
  <head>
  <body>
    <h1>Pasteboard</h1>
    <form id="paste" method="post">
      <textarea rows="40" cols="120" name="paste">%s</textarea>
    </form>
    <br/>
    <button onclick="document.getElementById('paste').submit()">Save</button>
    <form method="post">
      <input type="hidden" name="shred" value="1"/>
      <input type="submit" value="Shred"/>
    </form>
    <form method="get"><input type="submit" value="Reload"/></form>
  </body>
</html>
''' % cgi.escape(content))

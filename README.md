Pasteboard
==========

Pasteboard is a *very* simple Web app similar to http://pastebin.com/ but it
only allows for one paste page.  However, it is extremely easy to deploy and can
be useful on private networks or for sharing stuff with VMs when cut and paste
is not available.

# Installation
Copy ``paste.py`` to your Web server and enable Python CGI support.  With Apache
with mod-python you can achieve this by creating a ``.htaccess`` file in the
same directory with the following contents:

    Options +ExecCGI
    AddHandler cgi-script .py

# Usage
Navigate to the page, for example, by going to http://localhost/paste.py.
Type some text and save it.  The text could then be accessed from a VM or, given
the Web server's external IP address, from other machines.

Clicking ``Shred`` attempts to run the program ``shred`` on the temporary paste
file and then deletes it.

Clicking ``Reload`` reloads the page content.  This is useful after it has been
updated elsewhere.

# Limitations
 * There is only ever one paste page.
 * The default max paste size is 100KiB.
 * If the Web server does not have ``shred`` it wont shred the paste data.

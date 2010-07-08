gorun
=====

(c) Peter Bengtsson, Fry-IT, peter@fry-it.com, 2009-2010
License: Python


Using (py)inotify to run commands when files change
---------------------------------------------------

Tired of switching console, arrow-up, Enter, switch console back for
every little change you make when you're writing code that has tests?
Running with `gorun.py` enables you to just save in your editor and
the tests are run automatically and immediately. 

`gorun.py` does not use a slow pulling process which keeps taps on
files modification time. Instead it uses the
[inotify](http://en.wikipedia.org/wiki/Inotify) which is...

> inotify is a Linux kernel subsystem that provides file system event
> notification


Installation
------------

This will only work on Linux which has the inotify module enabled in
the kernel. (Most modern kernels do)

First install [pyinotify](http://trac.dbzteam.org/pyinotify) the usual
way:

        $ easy_install pyinotify
	
Then download `gorun` and put `gorun.py` into your `~/bin` directory
and make it executable. Then, create a settings file, which is just a
python file that is expected to define a variable called
`DIRECTORIES`. Here's an example:

        DIRECTORIES = (
	  ('some/place/', './myframework test --dir some/place'),
	  ('some/place/unitests.py', 
	   './myframework test --dir some/place --testclass Unittests'),
	  ('/var/log/torrentsdownload.log',
	   'growl downloads --logfile /var/log/torrentsdownload.log'),
	)

Save that file as, for example, `gorun_settings.py` and then start it
like this:

        $ gorun.py gorun_settings

Configuration
-------------

Once you've set gorun to monitor a directory it will kick off on any
file that changes in that directory. By default things like autosave
files from certain editors are automatically created (e.g. #foo.py# or
foo.py~) and these are ignored. If there are other file extensions you
want gorun to ignore add this to your settings file:

        IGNORE_EXTENSIONS = ('log',)
        
This will add to the list of already ignored file extensions such as
`.pyc`. 

Similarly, if there are certain directories that you don't want the
inotify to notice, you can list them like this:

        IGNORE_DIRECTORIES = ('xapian_index', '.autosavefiles')
        
Disclaimer
----------

This code hasn't been extensively tested and relies on importing
python modules so don't let untrusted morons fiddle with your dev
environment.

Todo
----

When doing Django development I often run on single test method over
and over and over again till I get rid of all errors. When doing this
I have to change the settings so it just runs one single test and when
I'm done I go back to set it up so that it runs all tests when adjacent 
code works. 

This is a nuisance and I might try to solve that one day. If you have
any tips please let me know. 
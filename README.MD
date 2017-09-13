 MOVIE TRAILER PROJECT



 REQUIREMENTS :
 --------------

1. Windows, Linux, Mac or any other OS.
2. Python v2.7.13 or higher, sublime or any other text editor which can run python code.
3. Any Internet browser.

 FILES
=======

1. media.py:
 -----------
	This file has a class named Movie where the init function is defined to initialise the class variables passed to it.
It also has another function show_trailer() to show the trailer of the movie. 
This file imports webbrowser module since webbrowser.open() function is used.

2. entertainment_center.py:
 --------------------------
	This file imports both the media and fresh tomatoes files. 
This file contains the instances of the class Movie , a list with all the movie names, and a function call to open_movies_page to open and display the movie trailer website.

3. fresh_tomatoes.py:
 --------------------
	This file consists of the total designing and structure of the website.

4. To run the project:
======================

In Command Line:
----------------
This webiste can also be opened using command line. The corresponding steps are listed below:
1. Set the path of your command line to the working directory.
2. Then type the command : python entertainment_center.py.

In PYTHON Shell(IDLE):
======================
1. Open entertainment_center.py in editing mode(In IDLE).
2. Then press F5 (or) click Run module under run.

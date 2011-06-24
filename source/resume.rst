.. _resume:

.. include:: include/glossary.rst




KDr2's Resume
======================

:ref:`简体中文版 <resume_zh_cn>`

Personal Infomation
----------------------
* Birth : 1983.07.23
* Email : killy.draw\#gmail.com
* WebSite : http://kdr2.net

.. * CellPhone : +86 135****2633

Education
-------------

[2002-2006] `Xi'an Jiaotong University
<http://www.xjtu.edu.cn>`_, China. 


.. _it_skills_list:

IT Skills
-------------

 * **Be proficient in/Devoting myself to:** Linux, C, Erlang, Python, Common Lisp
 * **Good at/Can also do:**  Java, Perl, Ruby, JavaScript, Objective-, C++
 * **Know noting about/Can't do:** Almost every thing relevant to MS Windows

Tools I am familiar with and often use
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 (inculdes OS, Platform, FrameWork, Library, Product, DevTools and so
 on)

 * Linux(System progrmming, Kernel Dev), MacOSX
 * Erlang/otp, RabbitMQ
 * SBCL, ECL
 * Qt(C++ GUI lib),PyQt
 * CPAN
 * Pylons, WSGI
 * jQuery
 * apache/nginx/bind(named)/proftpd/subversion/git/trac
 * MySQL,MySQl-Proxy,SphinxSearch,SQLite
 * |emacs|_/|sphinx|_/|wordpress|_


Projects(by reverse chronological order)
---------------------------------------------

 * A telnetd Server under Linux and SCO: telnetd server with
   tty-binding feature.

 * A log analyzer [07/2009],Which is based on `Python
   <http://www.python.org>`_, `PyQt4
   <http://www.riverbankcomputing.co.uk/software/pyqt/intro>`_,
   and `matplotlib  <http://matplotlib.sourceforge.net/>`_. Its
   plug-ins mechanism allows us to write a plugin easily to analyze
   logs in diffrent formats. What you only need is to write an Python
   class(a subclass of a certain class in this application), then you
   will see the result as graphics after you analyze your log-data
   with the plugin you just write.

 * A webpage visit counter [10/2008-12/2008], which is a `nginx
   <http://nginx.net/>`_ module, using memcached and mysql as its
   cache and storage, supplying a pv-counter service in high
   performance.


 * An extension of AMQP(implemented on RabbitMQ) [02/2009-05/2009] : I
   designed an `message selector` as an extension of AMQP-Spec-0.8, to
   route a certain message in a certain queue to a certain
   subscriber. And I implemented this on RabbitMQ 1.5.x.

 * `Erlix <http://github.com/KDr2/erlix/>`_: the Ruby interface for
   Erlang [Began at 07/2009, and who can take this project over? mail
   me please].

 * `SB-FastCGI <http://github.com/KDr2/sb-fastcgi/>`_

 * `CL-FastCGI <http://github.com/KDr2/cl-fastcgi/>`_

 * A Banking Teller System which can run on kinds of platform [after
   09/2007, and now I'm still working on its Android version]. This
   System are used by lots of banks in China now. It's implemented on
   Eclipse RCP(both the server side and the standard client side). The
   server side of this system is a Java Application Server(just like
   tomcat/jboss but much simpler than them), but what is running in it
   is not html/jsp/servlet, it's xml files and java byte-code files in
   our private format. It has several kinds of client : standard
   client(based on Eclipse RCP), webpage client, wap cliant, mobile
   application client, terminal client(VT100) and so on.

 * A simple web spider [05/2007-07/2007] wrritten in perl, to fetch
   certain block on certain page and display the block to our
   users. The looks of the block who is fetched must be kept down as
   same as it is in the origin webpage.

 * Some MIS/GIS applicatons,based on Java EE [before 2007] : Sorry,
   I'm boring to count them now.


What kind of jobs I prefer?
----------------------------------

I like working with linux, python, erlang, javascript, c, c++. I also
like typing code in |emacs|_. I can do linux system programming, web
development, and some more things which are relevant to the
technologies listed on my :ref:`it skills list
<it_skills_list>`. After all, I prefer a job that can be done without
MicroSoft Windows(and without Microsoft Office, certainly).


.. include:: include/footer.rst
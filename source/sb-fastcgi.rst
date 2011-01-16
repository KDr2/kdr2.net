
.. include:: include/glossary.rst

.. _sb-fastcgi:

SB-FastCGI
=====================

Introduction
---------------------

sb-fastcgi is a |cl|_ |fcgi|_ API Toolkit for |sbcl|_, It contains a
group of low-level API's which like the c API of |fcgi|_, a group of
fcgi-server implementations, and a high-level |wsgi|_ style interface.

You can get it from https://github.com/KDr2/sb-fastcgi .

If you want use sb-fastcgi on some other Common Lisp implementations
rather than SBCL, you can refer to :ref:`CL-FastCGI <cl-fastcgi>`

Getting Start
----------------------

Frist, install |sbcl|_ and sb-fastcgi asdf-package. Then get a share
object of |fcgi|_ (usually named libfcgi.so*). You can get it by
installing the package **libfcgi-dev** in your box, or by exceuting
command **make** under the directory **sb-fastcgi/c_src**.

Now, you need load the asdf-package and the libfcgi.so:

.. code-block:: common-lisp

  ;;; A1. load sb-fascgi asdf
  (asdf:operate 'asdf:load-op 'sb-fastcgi)
  ;;; A2. load libfcgi.so
  (sb-fastcgi:load-libfcgi "/usr/lib/libfcgi.so.0.0.0")


Low-Level API's
------------------------

sb-fastcgi provides a group of low-level API's corresponding to the
c-API of |fcgi|_, see the list below:

 - fcgx-init
 - fcgx-init-request
 - fcgx-accept
 - fcgx-finish
 - fcgx-puts
 - fcgx-getparam
 - fcgx-getenv

Usually you need not use the first four functions (fcgx-init /
fcgx-init-request / fcgx-accept / fcgx-finish), there are some
fcgi-server implementations in sb-fastcgi(will be demonstrated in next
section), you can use these implementations rather than use the first
four functions in the list above.

The last three functions (fcgx-puts / fcgx-getparam / fcgx-getenv) is
very useful :

**fcgx-puts** is for writting content to a http-response, e.g. use
``(fcgx-puts req "CONETNT")`` to write the string "CONTENT" to the
http-response corresponding to http-request ``req``.

**fcgx-getparam**  is for getting parameter from the http-request
header, e.g. ``(fcgx-getparam req "QUERY_STRING")`` will return the
QUERY_STRING of the http-request ``req``.

**fcgx-getenv**  is like fcgx-getparam, ``(fcgx-getenv req)`` return
all the headers/parameters of the http-request ``req``, in a
assoc-list format.


Write a FCGI-APP
---------------------

In this section we will finish our first FCGI-APP with sb-fastcgi.

First we write a function called ``simple-app``, which has one
argument(the http-request), in this function, we use **fcgx-puts** to
write a simple string to the http-response:


.. code-block:: common-lisp

  (defun simple-app (req)
    (let ((c (format nil "Content-Type: text/plain

  Hello, I am a fcgi-program using Common-Lisp")))
      (sb-fastcgi:fcgx-puts req c)))


Then we can run this simple-app:

.. code-block:: common-lisp

  (sb-fastcgi:simple-server #'simple-app)


the simple-server runs the simple-app on stdin, so you can integrate
it with apache via mod_fastcgi, or use spawn-fcgi to run it on a
listening socket.

There are four fcgi-server implementations in sb-fastcgi now:

.. code-block:: common-lisp

  (sb-fastcgi:simple-server #'simple-app)
  (sb-fastcgi:simple-server-threaded #'simple-app)
  (sb-fastcgi:socket-server #'simple-app)
  (sb-fastcgi:socket-server-threaded #'simple-app)

* the implementations with the prefix "simple-" runs on stdin.
* the implementations with the prefix "socket-" runs on a inet-socket
  or a unix-domain-socket.
* the implementations with the postfix "-threaded" runs in
  multi-thread mode.

See ``sb-fastcgi/test.lisp`` for more examples.


The |wsgi|_ Style API
--------------------------

If you do not know |wsgi|_, get to know it first, and then see this
example:

.. code-block:: common-lisp

  ;;; C1. app using WSGI-style interface
  (defun wsgi-app (env start-response)
    (funcall start-response "200 OK" '(("X-author" . "Who?")
                                       ("Content-Type" . "text/html")))
    (list "ENV (show in alist format): <br>" env))

  ;;; C2. run app above on 0.0.0.0:9000 (by default)
  (defun run-app-1 ()
    (sb-fastcgi:socket-server-threaded
     (sb-fastcgi:make-serve-function #'wsgi-app)
     :inet-addr "0.0.0.0"
     :port 9000))

* the function ``wsgi-app`` defined a wsgi-style app
* the function call ``(sb-fastcgi:make-serve-function #'wsgi-app)``
  convert the ``wsgi-app`` to a fcgi-app-function in sb-fastcgi.
* use ``sb-fastcgi:socket-server-threaded`` to run the
  fcgi-app-function we just get in the last step.


The wsgi-app can be nested:

.. code-block:: common-lisp

  ;;; C4. a nested WSGI-style app example
  (defun wsgi-app2 (app)
    (lambda (env start-response)
      (let ((content-0 (funcall app env start-response))) ; call outter app
        ;;reset X-author in headers
        (funcall start-response nil '(("X-author" . "KDr2!")))
        (append '("Prefix <br/>")  content-0 '("<br/>Postfix")))))

  ;;; C5. run (test-app1 test-app2) nested app
  (defun run-app-2 ()
    (sb-fastcgi:socket-server-threaded
     (sb-fastcgi:make-serve-function (wsgi-app2 #'wsgi-app))
     :inet-addr "0.0.0.0"
     :port 9000))


* the function ``wsgi-app2`` accept a wsgi-style-app in its argument,
  and return a new wsgi-style-app. In ``wsgi-app2`` you can change the
  reponse headers, filter or translate the response body...
* run the nested wsgi-style-app.

Nested wsgi-style-app make you webapp like an onion, and you can
add/remove a layer from it conveniently, use sb-fastcgi's WSGI-Style
API you can build/run your webapp or webapp-framework easily.

See ``sb-fastcgi/test.lisp`` for more examples.


Bug Report
-----------------------------

 * on github : https://github.com/KDr2/sb-fastcgi
 * email me  : killy.draw<``@``>gmail.com

.. include:: include/footer.rst

.. include:: include/comments.rst
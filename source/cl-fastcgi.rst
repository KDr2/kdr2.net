.. include:: include/glossary.rst

.. _cl-fastcgi:

CL-FastCGI
=====================

Introduction
---------------------


CL-FastCGI is a generic version of :ref:`SB-FastCGI <sb-fastcgi>`,
target to running on mostly Common Lisp implementation.

You can get it from https://github.com/KDr2/cl-fastcgi .

CL-FastCGI's API is exactly the same as :ref:`SB-FastCGI <sb-fastcgi>`'s.

Differences between :Ref:`SB-FastCGI <sb-fastcgi>`
-----------------------------------------------------

**SB-FastCGI**
 - Supports SBCL only.
 - No third-party packages dependences.
 - Supports unix-domain-socket/inet-socket/stdin
 - Multithreaded fastcgi server.

**CL-FastCGI**
 - Targeting to running on all Common Lisp implementation. And now
   supports:

   - SBCL
   - CMUCL
   - CLISP
   - Clozure CL
   - LispWorks

 - Depends on **cffi** and **usocket**
 - Unix-domain-socket is unsupported.
 - Multithreaded fastcgi server is unsupported(You can run it in
   multi-processes mode).

Which to Use?
----------------------------

If you use SBCL, I recommand you select :ref:`SB-FastCGI
<sb-fastcgi>`, and package :ref:`SB-FastCGI <sb-fastcgi>` has a
nickname ``cl-fastcgi``, so you can change :ref:`SB-FastCGI
<sb-fastcgi>` to cl-fastcgi or change back easily, without code
modifications.


Bug Report
-----------------------------

 * on github : https://github.com/KDr2/cl-fastcgi
 * email me  : killy.draw<``@``>gmail.com

.. include:: include/footer.rst


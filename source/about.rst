.. about
.. date : 2011-11-28 22:17

.. include:: include/glossary.rst

About This Site
====================


It's built on Sphinx
---------------------

I built this site with |sphinx|_, and I had put its |rst|_ sources on
|kd@github|_, you can get it freely if you want.


Where is my old blog?
-----------------------

It's gone, because I hate writting things in an online editor. Since
now, I will write pages with my |emacs|_ in |rst|_ format, and compile
them using |sphinx|_.


Changelog of this site
-----------------------

You can subscribe the |rss|_ of this site to watch its content updates.

The Source Code updates:

- 2012-05, use disqus as comment services
- 2011-06-27 rewrite service using O'Caml/web.py

.. graphviz::

   digraph foo {
      //rankdir=LR;
      fontname="courier new"
      fontsize=12
      node [fontname="courier new"
            fontsize=10]
      "web.py(Python)"  -> "Pylons(Python)" [dir=back];
      "Ocamlnet(O'Caml)" -> "Pylons(Python)" [dir=back];
      "Pylons(Python)" -> "Django(Python)" [dir=back];
   }

- 2010-09-19 change django_ to pylons_
- 2010-02-28 add rss feed.
- 2010-02-04 add comments service based on django_ and Ajax.
- 2010-02-04 remove the blog based on |wordpress|_.
- 2010-01-31 built the first version with |sphinx|_.

.. .. include:: include/footer.rst

.. include:: include/comments.rst


.. include:: include/glossary.rst


Ocampickle - Pickle/unPickle simple Python object in OCaml
===============================================================

Introduction
---------------------

Ocampickle is a samll library to Pickle/unPickle simple
Python object in |ocaml|_, corresponding to the
**cPickle** module in |python|_.

You can get it from https://github.com/KDr2/ocampickle .

Install
---------------------

 - git clone git://github.com/KDr2/ocampickle.git
 - cd ocampickle
 - omake
 - omake install

 
Getting Start
---------------------

.. code-block:: ocaml

  $ocaml
         Objective Caml version 3.12.0

  # #use "topfind";;
  - : unit = ()
  Findlib has been successfully loaded. Additional directives:
    #require "package";;      to load a package
    #list;;                   to list the available packages
    #camlp4o;;                to load camlp4 (standard syntax)
    #camlp4r;;                to load camlp4 (revised syntax)
    #predicates "p,q,...";;   to set these predicates
    Topfind.reset();;         to force that packages will be reloaded
    #thread;;                 to enable threads

  - : unit = ()
  # #load "nums.cma";;
  # #require "ocampickle";;
  /opt/local/lib/ocaml/site-lib/ocampickle: added to search path
  /opt/local/lib/ocaml/site-lib/ocampickle/ocampickle.cma: loaded
  # Ocampickle.loads;;
  - : string -> Ocampickle_type.t = <fun>
  # let x=Ocampickle.loads "(lp1\nS'a'\naS'b'\na(dp2\nS'x'\nS'\\xe6\\xb5\\x8b\\xe8\\xaf\\x95'\np3\nsa.";;
  val x : Ocampickle_type.t =
    Ocampickle_type.List
     [Ocampickle_type.String "a"; Ocampickle_type.String "b";
      Ocampickle_type.Dict <abstr>]
  # Ocampickle_utils.pyprint x;;
  ["a","b",{"x":"测试",},]- : unit = ()
  #...

Simple API
----------------------

.. code-block:: ocaml

  (* TYPE : Ocampickle_type.t *)
  type t = 
    | Dict of (t, t) Hashtbl.t  (* dict    *)
    | List of t list            (* list    *)
    | Tuple of t list           (* tuple   *)
    | String of string          (* str     *)
    | Unicode of string         (* unicode *)
    | Int of int                (* int     *)
    | Long of Big_int.big_int   (* int     *)
    | Float of float            (* float   *) 
    | Bool of bool              (* bool    *)
    | Object of string          (* object  *)
    | Null                      (* None    *)
    | Ref of (t ref)            (* Ref     *);;

  (* pickle object *)
  val  Ocampickle.dumps : ?proto:int -> Ocampickle_type.t -> string = <fun>

  (* unpickle object *)
  val Ocampickle.loads : string -> Ocampickle_type.t = <fun>

  (* print python object *)
  val Ocampickle_utils.pyoutput : out_channel -> Ocampickle_type.t -> unit = <fun>
  val Ocampickle_utils.pyprint :  Ocampickle_type.t -> unit = <fun>

Data Type Supported
--------------------------

Unfortunately, not all kinds of python data type are supported now,
here is a table demonstrating this below, and it will support all kind
of the data types (actually, all of the pickle opcode) later. 


.. csv-table:: python data-type supported by ocampickle
  :header: "type", "proto 0", "proto 1", "proto 2"

  None,  pickle/unpickle, pickle/unpickle, pickle/unpickle
  bool,  pickle/unpickle, pickle/unpickle, pickle/unpickle
  int,   pickle/unpickle, pickle/unpickle, pickle/unpickle
  long,  pickle/unpickle, pickle/unpickle, -/-
  float, pickle/unpickle, pickle/unpickle, pickle/unpickle
  string,pickle/unpickle, pickle/unpickle, pickle/unpickle
  unicode,pickle/unpickle,pickle/unpickle, pickle/unpickle
  tuple, pickle/unpickle, pickle/unpickle, pickle/unpickle
  list,  pickle/unpickle, pickle/unpickle, pickle/unpickle
  dict,  pickle/unpickle, pickle/unpickle, pickle/unpickle
  reference,pickle/-, pickle/-, pickle/-
  instance, -/-, -/-, -/-


Bug Report
-----------------------------

 * on github : https://github.com/KDr2/ocampickle
 * email me  : killy.draw<``@``>gmail.com

.. include:: include/footer.rst

.. include:: include/comments.rst



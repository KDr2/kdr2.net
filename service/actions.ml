(*
 * file : actions.ml
 * author : KDr2
 *)

let abort404 (cgi:Netcgi.cgi) () =
  cgi#set_header
    ~status:`Not_found
    ~cache:`No_cache
    ~content_type:"text/html; charset=\"utf-8\""
    ();
  "404 Not Found";;




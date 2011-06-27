(*
 * file : actions.ml
 * author : KDr2
 *)


let echo (cgi:Netcgi.cgi) url_map () =
  cgi#set_header
    ~cache:`No_cache
    ~content_type:"text/html; charset=\"utf-8\""
    ();
  "URL : " ^ (cgi#environment#cgi_property "REQUEST_URI");;

let abort404 (cgi:Netcgi.cgi) () =
  cgi#set_header
    ~status:`Not_found
    ~cache:`No_cache
    ~content_type:"text/html; charset=\"utf-8\""
    ();
  "404 Not Found : " ^ (cgi#environment#cgi_path_info);;




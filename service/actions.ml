(*
 * file : actions.ml
 * author : KDr2
 *)


let echo (cgi:Netcgi.cgi) url_map () =
  cgi#set_header
    ~cache:`No_cache
    ~content_type:"text/html; charset=\"utf-8\""
    ();
  let ret = ref "env:" and
      env = Unix.environment () in
  for i=0 to Array.length env - 1 do
    ret := !ret ^ ";" ^ env.(i)
  done;
  !ret ^ (cgi#environment#cgi_path_info) ^ "!";;

let abort404 (cgi:Netcgi.cgi) () =
  cgi#set_header
    ~status:`Not_found
    ~cache:`No_cache
    ~content_type:"text/html; charset=\"utf-8\""
    ();
  "404 Not Found : " ^ (cgi#environment#cgi_path_info);;




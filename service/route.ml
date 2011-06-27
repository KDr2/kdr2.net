(*
 * file : route.ml
 * author : KDr2
 *)

let route_map :
    (string, Netcgi.cgi -> (string, string) Hashtbl.t -> unit -> string) Hashtbl.t
    = Hashtbl.create 0;;

let route_list = ref [];;

let map_of_pcre_subs rex subs =
  let n = Pcre.num_of_subs subs and
      names = Pcre.names rex in
  let ret = Hashtbl.create n in
  for i=0 to n-1 do
    Hashtbl.add ret
      (string_of_int i)
      (Pcre.get_substring subs i)
  done;
  Array.iter (fun name ->
    Hashtbl.add ret name (Pcre.get_named_substring rex name subs)
  ) names;
  ret;;

let request_uri (cgi : Netcgi.cgi) =
  try cgi#environment#cgi_property "REQUEST_URI" with
      Not_found -> cgi#environment#cgi_path_info;;

let route (cgi : Netcgi.cgi) =
  let url = request_uri cgi in
  (* Hashtbl.fold (fun k v f -> match f with
     | None -> let subs =
     try Some (Pcre.exec ~rex:k url) with
     Not_found -> None in begin match subs with
     | Some sbs ->
     Some (v cgi (map_of_pcre_subs k sbs))
     | None -> None
                    end
     | Some _ -> f
     ) route_map None;;*)
  let target = List.fold_left (fun a k ->
    match a with
      | Some _ -> a
      | None -> try Some (k,(Pcre.exec ~rex:(snd k) url)) with
          Not_found -> None
  ) None !route_list in
  match target with
    | Some ((url,reg),subs) ->
      let f = Hashtbl.find route_map url in
      f cgi (map_of_pcre_subs reg subs)
    | None -> Actions.abort404 cgi;;

let map url action = let reg = Pcre.regexp url in
                     route_list := (List.append !route_list [(url,reg)]);
                     Hashtbl.add route_map url action;;


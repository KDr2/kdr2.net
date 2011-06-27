(*
 * file : comments.ml
 * author : KDr2
 *)

let opt_str_nn v = match v with
  | Some s -> s
  | None -> "";;

let comments_callback ret row headers =
  let comment = ref [] in begin
    for i = 0 to Array.length headers - 1 do
      comment := (headers.(i),Json_type.String (opt_str_nn row.(i)))::!comment
    done;
    match !ret with
      | Json_type.Array l ->
        ret := Json_type.Array ((Json_type.Object !comment) :: l)
      | _ -> ()
  end;;


let get_comments (cgi:Netcgi.cgi) arg_map () =
  cgi#set_header
    ~cache:`No_cache
    ~content_type:"text/javascript; charset=\"utf-8\""
    ();
  let target = Hashtbl.find arg_map "target" and
      ret = ref (Json_type.Array []) in
  ignore(Database.DB.query
           ("select date,content,url,author from comments where target=\"" ^ target^ "\"order by id desc")
           (comments_callback ret));
  Json_io.string_of_json !ret;;
    
let post_comment (cgi:Netcgi.cgi) arg_map () =
  cgi#set_header
    ~cache:`No_cache
    ~content_type:"text/javascript; charset=\"utf-8\""
    ();
  let target = cgi#argument_value "target" and
      author = cgi#argument_value "name" and
      email = cgi#argument_value "email" and
      url = cgi#argument_value "url" and
      content = cgi#argument_value "content" in
  ignore(Database.DB.update_stmt
           "insert into comments (target,author,email,url,content,date) values (?,?,?,?,?,datetime('now'))"
           [`TEXT target; `TEXT author; `TEXT email; `TEXT url; `TEXT content]);
  let ret = Json_type.Object [
    ("status",Json_type.String "ok");
    ("author",Json_type.String author);
    ("url",Json_type.String url);
    ("content",Json_type.String content);
    ("date",Json_type.String "seconds ago");
  ] in Json_io.string_of_json ret;;

(*
 * file : feed.ml
 * author : KDr2
 *)

let rss_header children = Xml.Element ("rss",
                                       [("version","2.0");
                                        ("xmlns:content","http://purl.org/rss/1.0/modules/content/");
                                        ("xmlns:wfw","http://wellformedweb.org/CommentAPI/");
                                        ("xmlns:dc","http://purl.org/dc/elements/1.1/");
                                        ("xmlns:atom","http://www.w3.org/2005/Atom");
                                        ("xmlns:sy","http://purl.org/rss/1.0/modules/syndication/");
                                        ("xmlns:slash","http://purl.org/rss/1.0/modules/slash/");
                                       ],children);;

let rss_channel items =
  let channel =
    Xml.Element ("channel",[],[
      Xml.Element("title",[],[Xml.PCData "KDr2"]);
      Xml.Element("atom:link",[
        ("href","http://kdr2.net/service/feed/rss");
        ("rel","self");
        ("type","application/rss+xml");
      ],[]);
      Xml.Element("link",[],[Xml.PCData "http://kdr2.net"]);
      Xml.Element("description",[],[Xml.PCData "KDr2's Personal Site"]);
      Xml.Element("generator",[],[Xml.PCData "OCaml/XML-LIGHT"]);
      Xml.Element("language",[],[Xml.PCData "en"]);
      Xml.Element("sy:updatePeriod",[],[Xml.PCData "hourly"]);
      Xml.Element("sy:updateFrequency",[],[Xml.PCData "1"]);
    ] @ items)
  in rss_header [channel]

let tag key = match key with
  | "date" -> "pubDate"
  | "title" -> "title"
  | "link" -> "link"
  | "author" -> "dc:creator"
  | "cats" -> "category"
  | "desc" -> "description"
  | "content" -> "content:encoded"
  | _ -> "unkonwn-tag";;
  

let obj_to_ele obj = match obj with
  | Json_type.Object jo ->
    let tbl = Json_type.Browse.make_table jo and
        tags = ref [] in
    Hashtbl.iter (fun k v -> match v with
      | Json_type.String s ->
        tags := (Xml.Element (tag k,[],[Xml.PCData s]))::!tags
      | _ -> ()) tbl;
    Xml.Element ("item",[],!tags);
  | _ -> Xml.Element ("unknown-tag",[],[]);;
    
let items_from_file file =
  let json = Json_io.load_json file and
      items = ref [] in begin
  match json with
    | Json_type.Array list ->
      List.iter (fun o ->
        items := !items @ [obj_to_ele o]
      ) list
    | _ -> ()
      end;
  !items;;


let feed_rss (cgi:Netcgi.cgi) url_map () =
  cgi#set_header
    ~cache:`No_cache
    ~content_type:"application/rss+xml; charset=\"utf-8\""
    ();
  let items = items_from_file Config.changelog  in
  Xml.to_string_fmt (rss_channel items);;

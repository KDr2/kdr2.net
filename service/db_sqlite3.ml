(*
 * file : db_sqlite3.ml
 * author : KDr2
 *)


let conn = ref None;;

let data_convertor d =
  match d with
    | `TEXT str -> Sqlite3.Data.TEXT str
    | `BLOB str -> Sqlite3.Data.BLOB str
    | `FLOAT f -> Sqlite3.Data.FLOAT f
    | `INT i64 -> Sqlite3.Data.INT i64
    | _ -> Sqlite3.Data.NULL;;


let init ?(pool_size=5) db_url =
  let db = Sqlite3.db_open db_url in
  conn := Some db;;

let destroy () = match !conn with
  | None -> true; 
  | Some db -> Sqlite3.db_close db;;

let query sql cb = match !conn with
  | None -> raise (Sqlite3.Error "no connection")
  | Some db -> Sqlite3.exec db ~cb:cb sql;;

let update sql = match !conn with
  | None -> raise (Sqlite3.Error "no connection")
  | Some db -> Sqlite3.exec db sql;;

let update_stmt sql data = match !conn with
  | None -> raise (Sqlite3.Error "no connection")
  | Some db -> let stmt = Sqlite3.prepare db sql and
               sdata = List.map data_convertor data in
               for i = 1 to List.length sdata do
                 match Sqlite3.bind stmt i (List.nth sdata (i-1)) with
                   | Sqlite3.Rc.ERROR -> raise (Sqlite3.Error "stmt error")
                   | _ -> ()
               done;
               ignore(Sqlite3.step stmt);
               Sqlite3.finalize stmt;;


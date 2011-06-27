


Database.DB.init Config.db_url;;

let map_init () =
  Route.map "/service/feed/rss" Feed.feed_rss;
  Route.map "/service/comments/get/(?<target>.*)" Comments.get_comments ;
  Route.map "/service/comments/post" Comments.post_comment ;;

map_init ();;

(* Server.run_on_port_threaded 9000;; *)

Server.run_on_fd Unix.stdin;;

Database.DB.destroy();;

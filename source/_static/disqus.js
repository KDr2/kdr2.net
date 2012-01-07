function _url(){
    var tmp=window.location+"";
    ret=tmp.replace(/^\w+:\/\/.*?\//i,"").replace(/#.*$/gi,"");
    if(ret!="")return ret;
    return "index.html";
}


function setup_block(){
    var comments_parent_div=$(".bodywrapper");
    var comments_div='<div id="comments" class="body">'+
        '<h2>Comments</h2>'+
        '<div id="disqus_thread"></div>'+
        '</div>';
    comments_parent_div.append($(comments_div));
    //var comments_ul=$("#comments");
    var toc_comment_link='<li><a class="reference external" href="#comments">Comments</a></li>';
    $(".sphinxsidebarwrapper > ul > li > ul").append($(toc_comment_link));
}


var disqus_shortname = 'kdr2'; 
var disqus_url = 'http://kdr2.net/'+_url();

function setup_disqus(){
    setup_block();
    var dsq = document.createElement('script'); dsq.type = 'text/javascript';
    dsq.async = true;
    dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
    (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
}

if(true){
    $(document).ready(setup_disqus);
}


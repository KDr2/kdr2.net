/*
 * tumblr.js by KDr2
 */



function setup_tumblr(){
    ul=$('#recently-updates ul');
    tumblr_container='<li class="toctree-l1">'+
        '<span class="reference internal">Recently Updates on This Site'+
        '</span><ul id="tumblr_feeds"></ul></li>';
    ul.append($(tumblr_container));

    $.get('/service/tumblr/feed.json', function(data) {
        var feeds=eval(data);
        for(var i=0;i<feeds.length;i++){
            item='<li class="toctree-l2">'+
                '<a class="reference internal" href="'+
                feeds[i]['link']+'">'+
                feeds[i]['title']+'</a></li>';
            comments_ul.append($(item));
        }
    });
}
    
/*

*/
$(document).ready(setup_tumblr);




/*
 * tumblr.js by KDr2
 */



function setup_tumblr(){

    $.get('/service/tumblr/feed.json', function(data) {
        ul=$('#recently-updates ul')[0];
        tumblr_container='<li class="toctree-l1">'+
            '<span class="reference internal">'+
            'Recently Updates on Tumblr'+
            '</span><ul id="tumblr_feeds"></ul></li>';
        
        $(ul).append($(tumblr_container));
        
        var feeds=eval(data);
        for(var i=0;i<feeds.length;i++){
            item='<li class="toctree-l2">'+
                '<a class="reference internal" href="'+
                feeds[i]['link']+'" target="_blank">'+
                feeds[i]['title']+'</a></li>';
            $("#tumblr_feeds").append($(item));
        }
    });
}
    
/*

*/
$(document).ready(setup_tumblr);




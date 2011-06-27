/*
 * comments.js by KDr2
 */

function need_show_comments(){
    return /^https?:\/\//.test(window.location);
}

function _url(){
    var tmp=window.location+"";
    ret=tmp.replace(/^\w+:\/\/.*?\//i,"").replace(/#.*$/gi,"");
    if(ret!="")return ret;
    return "index.html";
}

function format_comment(cmt){
    return '<a href="'+cmt['url']+'" target="_blank"><strong>'+cmt['author']+
        '</strong></a> ( '+cmt['date']+' )'+
        ' said:<br/> &nbsp;&nbsp;'+cmt['content'];
}

function validate_comment(cmt){
    if(/^\s*$/gi.test($("#c_name").attr("value"))){
        alert("fill your name please!");
        $("#c_name").focus();
        return false;
    }
    var email=$("#c_email").attr("value");

    if(/^\s*$/gi.test($("#c_content").attr("value"))){
        alert("fill the comment content please!");
        $("#c_content").focus();
        return false;
    }
    return true;
}

function fill_comments(comments){
    $("#cmt_progress").text("Loading Comments...");
    $("#cmt_progress").addClass("waiting");
    var comments_ul=$("#comments_ul");
    $.get('/service/comments/get/'+_url(), function(data) {
        var comments=eval(data);
        for(var i=0;i<comments.length;i++){
            comments_ul.append($("<li>"+format_comment(comments[i])+"</li>"));
        }
        $("#cmt_progress").addClass("load_succeed");
        $("#cmt_progress").text("All comments are Loaded");
        $("#cmt_progress").fadeOut(1500);
    });
}

function append_comment(comment){
    var comments_ul=$("#comments_ul");
    comments_ul.append($("<li>"+format_comment(comment)+"</li>"));
}

function store_cookies(comment){
    var days = 180;
    var exp  = new Date();
    exp.setTime(exp.getTime() + days*24*60*60*1000);
    document.cookie="user_name="+escape(comment.name)+
        "; expires=" + exp.toGMTString();;
    document.cookie="user_email="+escape(comment.email)+
        "; expires=" + exp.toGMTString();;
    document.cookie="user_url="+escape(comment.url)+
        "; expires=" + exp.toGMTString();;
}

function get_cookie(key){
    var arr_cookie=document.cookie.split("; ");
    for(var i=0;i<arr_cookie.length;i++){
        var arr=arr_cookie[i].split("=");
        if(key==arr[0]){
            return unescape(arr[1]);
        }
    }
    return "";
}

function post_comment(){
    cmt_data={ target: _url(), name:$("#c_name").attr("value"),
               email:$("#c_email").attr("value"),url:$("#c_url").attr("value"),
               content:$("#c_content").attr("value")};
    if(!validate_comment(cmt_data))return;
    store_cookies(cmt_data);
    $("#cmt_progress").addClass("waiting");
    $("#cmt_progress").text("Posting Comments...");
    $("#cmt_progress").show();
    $.post("/service/comments/post", cmt_data,
           function(data){
               if(/^ERR.*/gi.test(data)){
                   $("#cmt_progress").addClass("load_failed");
                   $("#cmt_progress").text("Comment post failed!");
               }else{
                   append_comment(eval(data));
                   clear_inputs();
                   $("#cmt_progress").addClass("load_succeed");
                   $("#cmt_progress").text("Comment post succeeded");
               }
               $("#cmt_progress").fadeOut(1500);
           });
}

function clear_inputs(){
    $("#c_name").attr("value",get_cookie("user_name"));
    $("#c_url").attr("value",get_cookie("user_url"));
    $("#c_email").attr("value",get_cookie("user_email"));
    $("#c_content").attr("value","");
}

function setup_block(){
    var comments_parent_div=$(".bodywrapper");
    var comments_div='<div id="comments" class="body">'+
        '<h2>Comments</h2>'+
        '<ul id="comments_ul" class="simple">'+
        '</ul><div id="cmt_progress"></div><div style="clear:both;"></div><h3>Leave a comment:</h3>'+
        //comment form:
        '<p><input name="c_name" value="" type="text" id="c_name" class="cmt_field" /><label for="name" class="label">NAME(required)</label></p>'+
        '<p><input name="c_url" value="" type="text" id="c_url" class="cmt_field" /><label for="url" class="label">SITE</label></p>'+
        '<p><input name="c_email" value="" type="text" id="c_email" class="cmt_field" /><label for="email" class="label">EMAIL</label></p>'+
        '<p><label for="comment_content">CONTENT:</label><br /><textarea name="c_content" rows="4" cols="60" id="c_content"'+
        ' class="cmt_area"></textarea></p> <p><input value="Submit Comment" type="button" id="submit_comment" class="cmt_field"/></p>'+
        '</div>';
    comments_parent_div.append($(comments_div));
    var comments_ul=$("#comments");
    var toc_comment_link='<li><a class="reference external" href="#comments">Comments</a></li>';
    $(".sphinxsidebarwrapper > ul > li > ul").append($(toc_comment_link));
    $("#submit_comment").click(post_comment);
    fill_comments();
    clear_inputs();
}

if(need_show_comments()){
    $(document).ready(setup_block);
}
/**
 * Created by 0701052m on 02/03/2015.
 */

$(document).ready(function(){

    $('.like').click(function(){
        var postid;
        postid = $(this).attr("data-postid");
        $.get('/logoBox/like_post/',{post_id: postid}, function(data){
            $($('strong[id="' + postid + '"]')).html(data);
            $($('button[id="' + postid + '"]')).attr("disabled", true);
        });
    });

});
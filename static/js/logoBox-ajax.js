/**
 * Created by 0701052m on 02/03/2015.
 */

$(document).ready(function(){

    $('#likes').click(function(){
        var postid;
        postid = $(this).attr("data-postid");
        $.get('/logoBox/like_post/',{post_id: postid}, function(data){
            $($('strong[class="count"]').attr('id', postid)).html(data);
            $(postid).attr("disabled", true);
        });
    });

});
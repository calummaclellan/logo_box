/**
 * Created by 0701052m on 02/03/2015.
 */

$(document).ready(function() {

    $('.like').click(function () {
        var postid;
        var btn = $(this);
        postid = btn.attr("data-postid");
        $.get('/logoBox/like_post/', {post_id: postid}, function (data) {
            btn.prev().html(data);
            btn.attr("disabled", true);
            $($('button[id="' + postid + '"]')).attr("disabled", true);
        });
    });
    $('.dislike').click(function () {
        var postid;
        var btn = $(this);
        postid = $(this).attr("data-postid");
        $.get('/logoBox/dislike_post/', {post_id: postid}, function (data) {
            btn.prev().html(data);
            btn.attr("disabled", true);
            $($('button[id="' + postid + '"]')).attr("disabled", true);
        });
    });
});
/**
 * Created by 0701052m on 02/03/2015.
 */

$(document).ready(function() {

    //like button event handler
    $('.like').click(function () {
        var postid;
        var btn = $(this);
        postid = btn.attr("data-postid");
        //make an ajax request to like_post view passing the postid attribute
        $.get('/logoBox/like_post/', {post_id: postid}, function (data) {
            btn.prev().html(data); //attach the result, i.e. incremented number of likes
            btn.attr("disabled", true); //disables the like button button
            $($('button[id="' + postid + '_dislikebutton"]')).attr("disabled", true); //disables the dislike button
        });
    });
    //dislike button event handler
    $('.dislike').click(function () {
        var postid;
        var btn = $(this);
        postid = $(this).attr("data-postid");
        //make an ajax request to dislike_post view passing the postid attribute
        $.get('/logoBox/dislike_post/', {post_id: postid}, function (data) {
            btn.prev().html(data); //attach the result, i.e. incremented number of dislikes
            btn.attr("disabled", true); //disables the dislike button button
            $($('button[id="' + postid + '_likebutton"]')).attr("disabled", true); //disables the like button
        });
    });
});
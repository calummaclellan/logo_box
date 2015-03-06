/**
 * Created by 0701052m on 02/03/2015.
 */

$(document).ready( function(){

    $('#likes').click(function(){
         var catid;
        catid = $(this).attr("data-catid");
        $.get('/rango/like_category/',{category_id:catid}, function(data){
            $('#like_count').html(data);
            $('#likes').hide();
        });
    });

});
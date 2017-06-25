/**
 * Created by osboxes on 27/04/17.
 */


function get_next_word() {

    $.get('/ajax/next_word/', {}, function (data) {
        if (data.end){
            alert(data.end);
        }
        else{
            $('#expression_id').html(data.expression);
        }

    });

}
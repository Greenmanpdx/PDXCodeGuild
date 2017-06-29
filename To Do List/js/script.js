/**
 * Created by greenman on 6/28/17.
 */

$('#add').click(function () {
    var check = "<input type='checkbox'>";
    var txt = $('#toAdd').val();
    var stuff = '<div>'+ check + txt +'<div>'
    $('#list').append(stuff)
});


